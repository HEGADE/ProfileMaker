from typing import Any, Dict
from .html_attributes import ATTRIBUTES, TAGNAME
from click import echo

def null_safety(single_ele):
    if single_ele:
        return single_ele.text.strip()
    return None

fetch=lambda *args:null_safety(args[0].find(args[1],attrs={args[2]:args[3]})) 

def help(profile_data,html_data):
    profile_data["name"]=fetch(html_data,TAGNAME[0],"class",ATTRIBUTES[0]) 
    profile_data["bio"]=null_safety(html_data.find("div",attrs={"class":"p-note"}).find("div"))
    profile_data["location"]=fetch(html_data,"span","class","p-label")
    profile_data["img"]=html_data.find("img",attrs={"class":"avatar-user"})["src"]
    for rel_data in html_data.find_all("a",attrs={"rel":"nofollow"}):
      if  "twitter" in rel_data["href"]:
          profile_data["twiter"]=rel_data["href"]
      elif "http" or "https" in rel_data["href"]:
          profile_data["site"]=rel_data["href"]
    
    profile_data["repo"]=[repo_name.text.strip() for repo_name in html_data.find_all("span",attrs={"class":"repo"})[:3]] 
    profile_data["rep_des"]=[repo_des.text.strip() for  repo_des in html_data.find_all("p",attrs={"class":"pinned-item-desc"})[:3]] 
 
    return profile_data

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
       
        if html_data.string!="Not Found":
            profile_data=help(profile_data,html_data)
        else:
            raise Exception("Page not found please enter valid user name")
    except Exception as e:
        echo(e)
        exit(0)
 
    return profile_data
