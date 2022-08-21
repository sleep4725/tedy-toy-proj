from pexpect import ExceptionPexpect


class DirectoryExcep(ExceptionPexpect):
    
    def __init__(self, dir: str):
        super().__init__(f'{dir} 은 디렉토리가 아닙니다.')