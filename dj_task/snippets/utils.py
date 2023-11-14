def save_file(obj,filename:str):
    with open(filename,"wb+")as writer:
        for chunk in obj.chunks():
            writer.write(chunk)