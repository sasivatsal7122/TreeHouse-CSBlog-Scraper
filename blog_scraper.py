from bs4 import BeautifulSoup as soup
from urllib.request import Request, urlopen
import os

def scrape_and_save(choosen_blog_link,Title,save_in_folders=False,page_no=None):
    req = Request(choosen_blog_link, 
    headers={'User-Agent': 'Mozilla/5.0'}
    )
    webpage = urlopen(req).read()
    blog_soup = soup(webpage,'html.parser')
    blog_content_div = blog_soup.find_all('div',{'class':'content-cta'})
    for text in blog_content_div:
        blog_content = text.find('div')
        break
    blog_content_string  = ""
    blog_content_string+="Title: "+Title+ "\n\n\n"+blog_content.text
    
    unwanted = "!@#$;:!*%)(&^~}{:,.?/><=+][\|_"
    for char in unwanted:
        Title = Title.replace(char," -")
    try:
        os.mkdir("scraped blogs/") 
    except:
        pass
    if save_in_folders==False and page_no==None:
        with open(f"scraped blogs/{Title}.doc",'w',encoding="utf-8") as fp:
            fp.writelines(blog_content_string)
    else:
        try:
            os.mkdir(f"scraped blogs/Page-{page_no}") 
        except:
            pass
        with open(f"scraped blogs/Page-{page_no}/{Title}.doc",'w',encoding="utf-8") as fp:
            fp.writelines(blog_content_string)

    return