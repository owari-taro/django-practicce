from unittest.mock import patch
import unittest
from hoge import Something, Hoge, URL
from hogehoge import HogeHoge

# https://stackoverflow.com/questions/38579535/how-to-supply-a-mock-class-method-for-python-unit-test
# https://auth0.com/blog/mocking-api-calls-in-python/


class Test(unittest.TestCase):

    @patch.object(Something, "post")
    @patch.object(Something, "get")
    #decorate are applied from bottom-up
    def test_something(self,  fake_get, fake_post):
        fake_get.return_value = 1234
        fake_post.return_value = 321
        sth = Something()
        print(sth)
        self.assertEqual(sth.get(), 1234)
        self.assertEqual(sth.post(), 321)

    @patch.object(Hoge, "get")
    def test_Hoge(self, fake_get):
        fake_get.return_value = {"status_code": 200}
        hoge = Hoge()
        self.assertEqual(hoge.get(), {"status_code": 200})

    @patch.object(Hoge, "get")
    def test_HogeHoge(self, fake_get):
        fake_get.return_value = "test"
        res = HogeHoge().tmp()
        self.assertEqual("test?", res)

    @patch("hoge.requests.get")
    def test_hoge_with_patch(self, mock_get):
        mock_get.return_value = {"fake-request!"}
        hoge = Hoge()
        res = hoge.get()
        mock_get.assert_called_with(URL)
        self.assertEqual(res, {"fake-request!"})


try:
    1/0
except Exception as err:
    print(str(err))
