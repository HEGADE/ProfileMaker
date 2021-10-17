from typing import Any, Dict

from requests.models import requote_uri
from .html_attributes import ATTRIBUTES, TAGNAME
from click import echo
from pprint import PrettyPrinter

   


def null_safety(single_ele):
    if single_ele:
        return single_ele.text.strip()
    return None



def parse_html(html_data) -> Dict:
    profile_data = {
        "name": None,
        "location": None,
        "bio": None,
        "twiter": None,
        "site": None,
        "repo": [],
        "rep_des": [],
        "img":None
    }
    try:
        if html_data:
           profile_data["name"]=null_safety(html_data.find(TAGNAME[0],attrs={"class":ATTRIBUTES[0]})) 
           profile_data["bio"]=null_safety(html_data.find("div",attrs={"class":"p-note"}).find("div"))
           profile_data["location"]=null_safety(html_data.find("span",attrs={"class":"p-label"}))
           profile_data["repo"]=[repo_name.text.strip() for repo_name in html_data.find_all("span",attrs={"class":"repo"})[:3]] 
           profile_data["rep_des"]=[repo_des.text.strip() for  repo_des in html_data.find_all("p",attrs={"class":"pinned-item-desc"})[:3]] 
           profile_data["img"]=html_data.find("img",attrs={"class":"avatar-user"})["src"]
           for rel_data in html_data.find_all("a",attrs={"rel":"nofollow"}):
               if  "twitter" in rel_data["href"]:
                 
                   profile_data["twiter"]=rel_data["href"]
               elif "http" or "https" in rel_data["href"]:
                   profile_data["site"]=rel_data["href"]
        else:
            raise Exception("Page not found please enter valid user name")
    except Exception as e:
        echo(e)
        print("Xfsdf")
    
    # print(profile_data)
    pp=PrettyPrinter(indent=5)
    pp.pprint(profile_data)
    return profile_data
