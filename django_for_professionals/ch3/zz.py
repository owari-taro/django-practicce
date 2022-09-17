from functools import wraps

class arg_path_exist:
    def __init__(self,index:int):
        self.index=index
    
    def __call__(self,func):
        @wraps(func)
        def wrapped(*args,**kwargs):
            print(*args)

            return func(*args,**kwargs)

        return wrapped
class Hoge:
    @arg_path_exist(index=12)
    def hoge(self,x,y,z):
        print("asdlfkjalkdfjlaskdjf")

if __name__=="__main__":
    Hoge().hoge(1,2,4212)