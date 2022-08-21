# step01 > its > Cllct_it.py
import os
import sys
from typing import final

FILE_ABS_PATH = os.path.abspath(os.path.dirname(__file__))
for _ in range(2):
    FILE_ABS_PATH = os.path.dirname(FILE_ABS_PATH)

PROJ_ROOT_DIR = FILE_ABS_PATH
sys.path.append(PROJ_ROOT_DIR)

print(f"project-root-dir : {PROJ_ROOT_DIR}")

try:
    import requests 
    import urllib3
    from urllib.request import urlopen
    import ssl
    from bs4 import BeautifulSoup
except ImportError as err:
    print(err)

try:

    from step01.its.Model_its import Model_its
    from step01.common.Url import Url 
    from step01.util.TimeUtil import TimeUtil
    from customexcep.TException import DirectoryExcep
except ImportError as err:
    print(err)

##
# @category naver-news-it
# @author JunHyeon.Kim
# @date 20220820
## ----------------------------
class Cllct_its(Model_its, Url):
    
    def __init__(self) -> None:
        Model_its.__init__(self)
        Url.__init__(self)    
        self._crrt_time = TimeUtil.get_crrt_time() 
        self._news_category_dir = Cllct_its.set_json_dir()
        
        self._url_list = [] 
         
    def req_data(self):
        '''
        :param:
        :return:
        '''        
        context = ssl._create_unverified_context() 
        urllib3.disable_warnings()
        for page in range(1): # pagination 
            print(f"{page} 페이지 처리 중...")
            for sid2 in self._sid2_list: # sid2
                req_url = self.make_url(
                            sid1= self._sid1,
                            sid2= sid2,
                            page= page,
                            crrt_time= self._crrt_time)

                result = urlopen(req_url, context= context)
                status_code = result.status
                
                if status_code == 200:
                    try:
                        
                        bs_obj = BeautifulSoup(result.read(), "html.parser")
                        ul_type_headline = bs_obj.select_one("ul.type06_headline")
                        li_list = ul_type_headline.select("li")
                        
                        for l in li_list:
                            a_tag = l.select_one("dl > dt > a")
                            href = a_tag.attrs["href"]
                            self._url_list.append(href)
                        
                    except:
                        print("err")
                         
                result.close()
        
        self.url_file_write()     
         
    def url_file_write(self):
        '''
        :param:
        :return:
        '''
        if len(self._url_list) != 0:
            try:
                with open(self._news_category_dir + f"/{self._category}_{TimeUtil.insrt_crrt_time()}.log", 
                            "w", 
                            encoding="utf-8") as url_w:
                    
                    for u in self._url_list:
                        url_w.write(u + "\n")
            except:
                print("file write error !!")
            finally:
                url_w.close()
        else:
            print("list 에 데이터가 비어 있습니다.")
         
    @classmethod 
    def set_json_dir(cls)-> str:
        '''
        :param:
        :return:
        '''
        global PROJ_ROOT_DIR
        f_name, _ = os.path.splitext(os.path.basename(__file__))
        news_category = str(f_name).split("_")[1] 
        
        url_log_dir = os.path.join(
            PROJ_ROOT_DIR,
            f"json_file_dir/{news_category}"
        )
        is_true = os.path.isdir(url_log_dir)
        if is_true:
            return url_log_dir
        else:
            raise DirectoryExcep(dir = url_log_dir)
         
if __name__ == "__main__":
    o = Cllct_its()
    o.req_data()