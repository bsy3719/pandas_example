class UserDefinedFunction():
    def add(one:str=1, two:int=2):
        """두개의 인자 값을 더해주는 함수!
            꼭 2개의 인자를 넣어주세요."""
        return one+two

    def substr(one:str):
        """문자를 자르는 함수
            꼭 1개의 인자를 넣어주세요."""
        return one.str[:-2]