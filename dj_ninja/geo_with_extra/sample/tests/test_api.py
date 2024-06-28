import pytest
from sample.schema import Store

@pytest.mark.django_db
class Test:
    #clinentはdjango-pytestで提供されてる
    def test_hello_with_no_content_in_db(self,client):
        #通常のdjango-pytestと同じようにtest可能
        print(client)
        res=client.get("/api/hello")
        assert len (res.json())==0
    #@pytest.mark.parametrize("test_input,expected", [("3+5", 8), ("2+4", 6), ("6*9", 42)])    
    @pytest.mark.parametrize("num",[1,3])
    def test_hello_with_content(self,client,store_factory,num):
        store_factory.create_batch(num)
        res=client.get("/api/hello")
        assert len(res.json())==num
        
    @pytest.mark.smoke
    def test_hello_with_specific_id(self,client):
        res=client.get("/api/hello/412")
        breakpoint()