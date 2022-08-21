import time 

##
# @author JunHyeon.Kim
# @date 20220820
## ----------------------------
class TimeUtil:
    
    @classmethod 
    def get_crrt_time(cls):
        '''
        :param:
        :return: yyyyMMdd (ex: 20220820)
        '''
        return time.strftime("%Y%m%d", time.localtime())
    
    @classmethod 
    def insrt_crrt_time(cls):
        '''
        :param:
        :return: yyyyMMdd HHmmSS ()
        '''
        return time.strftime("%Y%m%d%H%M%S", time.localtime())