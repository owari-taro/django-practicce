import pytest
import os
def test_hoge(tmp_path):
    
    with open(tmp_path/"hoge.txt","w")as writer:
        writer.write("adsfasdfasdfasdf")
    print(os.listdir(tmp_path))
    assert 1==1