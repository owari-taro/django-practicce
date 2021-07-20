## fixture
テストで使うモデルをjson,ymlに書いてすます方法。  
setupメソッドが長くなって読みにくくなるとかを防ぐのに使える。


'''
[
    {
        "pk": "1",
        "model": "auth.user",
        "fields": {
            "username": "hogehoge",
            "email": "hoge@gmail.com",
            "password": "hoge1234"
        }
    },
    {
        "pk": "1",
        "model": "books.book",
        "fields": {
            "author": "saaaa",
            "title": "hoga"
        }
    },
    {
        "pk": "1",
        "model": "books.comment",
        "fields": {
            "comment": "hoge",
            #ForienKeyの指定はPKで行える
            "book":"1",
            #auto_nowの場合も指定する必要あり
            "created_at": "2021-07-16T17:41:28+00:00",
            "updated_at": "2021-07-16T17:41:28+00:00",
            "author": "1"
        }
    }
]

'''