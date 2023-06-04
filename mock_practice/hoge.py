import requests
URL = "http://google.com"


class Hoge:
    def get(self):
        res = requests.get(URL)
        return res

    def post(self):
        res = requests.post(URL)
        return res

class Something:
    def get(self):
        return 1



if __name__ == "__main__":
    hoge = Hoge()
    print(hoge.get().content)
