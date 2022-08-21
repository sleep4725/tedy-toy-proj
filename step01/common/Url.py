# https://news.naver.com/main/list.naver?mode=LS2D&mid=shm&sid2=226&sid1=105&date=20220819
from urllib.parse import urlencode

'''
@author JunHyeon.Kim
'''
class Url:
    
    def __init__(self) -> None:
        self._base_url = "https://news.naver.com/main/list.naver"
        self._params = urlencode({
            "mode": "LS2D"
            ,"mid": "shm" 
        })
        
    def make_url(self, sid1: int, sid2: int, page: int, crrt_time: str):
        '''
        :param: sid1
        :param: sid2
        :param: page
        :param: crrt_time
        :return:
        '''
        sid_param = "sid1=" + f"{sid1}" + \
                    "&" +\
                    "sid2=" + f"{sid2}"
        date_param = "date=" + f"{crrt_time}"
        page_param = "page=" + f"{page}"
        
        req_url = f"{self._base_url}?{self._params}&{sid_param}&{date_param}&{page_param}"
        
        return req_url