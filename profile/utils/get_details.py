from requests import get
from typing import Dict,List,Optional
from bs4 import BeautifulSoup
from helpers.parser import parse_html
class Details():
    def __init__(self) -> None:
        self.__url=f'https://github.com/'
        self._profile_data={}

    def __call__(self,**kwargs:Dict) -> None:
        
        data=get(self.__url+kwargs.get("user_name"))
        soup_data=BeautifulSoup(data.content,"html.parser")
        self._profile_data=parse_html(soup_data)
        
      

     