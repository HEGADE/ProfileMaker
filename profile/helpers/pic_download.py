from sys import path
from requests import get
from pathlib import Path
def pic_download(url:str)->str:
    save_path= Path.joinpath(Path.home(),"user.jpg")
    try:
        image_buffer=get(url)
        with open(save_path,"wb") as f:
            f.write(image_buffer.content)
    except Exception as e:
        print(e)
        exit(0)
    return save_path
        
