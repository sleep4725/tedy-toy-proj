# https://news.naver.com/main/list.naver?mode=LS2D&mid=shm&sid1=105&sid2=731
# https://news.naver.com/main/list.naver?mode=LS2D&mid=shm&sid1=105&sid2=226
# https://news.naver.com/main/list.naver?mode=LS2D&mid=shm&sid1=105&sid2=227
# https://news.naver.com/main/list.naver?mode=LS2D&mid=shm&sid1=105&sid2=732

##
# @author JunHyeon.Kim
# @date 20220820
## ----------------------------
class Model_its:
    
    def __init__(self) -> None:
        self._category = "naver-news-its"
        self._sid1 = 105
        self._sid2_list = [731, 226, 227, 732]