from requests import get
from typing import Dict, List, Optional, overload
from bs4 import BeautifulSoup
from filetypes.pdf import Pdf
from helpers.parser import parse_html


class Details(Pdf):
    def __init__(self) -> None:
        self.__url = f'https://github.com/'
        self._profile_data = {}

    def __call__(self, **kwargs: Dict) -> None:
        try:

            data = get(self.__url+kwargs.get("user_name"))
            soup_data = BeautifulSoup(data.content, "html.parser")
            self._profile_data = parse_html(soup_data)
        except Exception as e:
            print("network error")

        self._create_pdf__()
    def _create_pdf__(self):
        pdf=super()._create_pdf__(self._profile_data)
        pdf.output("something.pdf","f")
        
        
        
        #// will write save method here


