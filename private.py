class Test:
    __variavel_static = '__variavel_static'

    def __init__(self):
        self.__variavel = 'variavel'
    
    def __method(self):
        print('__method private')

    @staticmethod
    def __method_static():
        print('__method static private')