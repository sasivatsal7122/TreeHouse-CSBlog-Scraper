from bs4 import BeautifulSoup as soup
from urllib.request import Request, urlopen
import re
from random import randint
import shutil

#local imports
from get_heading_desc import scrape_head_desc_for
from blog_hyperlinks import get_blogs_links_for
from blog_scraper import scrape_and_save

def driver(page=None,blog=None,scrape_all=False,random=False,multipage=False):
    
    if isinstance(page,list)==True:
        for i in range(page[0],page[1]+1):
            driver(page=str(i),blog=1,scrape_all=True,multipage=True)
            print(f"Completed Scraping Page-{i}")
    
    else:  
        if blog==None and scrape_all==True:
            blog=1
            
        base_url = "https://blog.teamtreehouse.com/page/"

        treq = Request(base_url+'2', 
            headers={'User-Agent': 'Mozilla/5.0'}
        )
        twebpage = urlopen(treq).read()
        tpage_soup = soup(twebpage,'html.parser')

        no_of_pages = tpage_soup.find('p',{'class':'header-back-link'})
        temp = re.findall(r'\d+', no_of_pages.text)
        pages_range = list(map(int, temp))
            
        if page==None and random==True:
            page_no = str(randint(pages_range[0],pages_range[1]))
        elif page==None:
            page_no = str(input(f"Enter page number to scrape from {pages_range[0]} to {pages_range[1]}: "))
        else:
            page_no = str(page)
            
        base_url+=page_no
        req = Request(base_url, 
            headers={'User-Agent': 'Mozilla/5.0'}
        )
        webpage = urlopen(req).read()
        page_soup = soup(webpage,'html.parser')
        
        head_desc_dict,heading_ls = scrape_head_desc_for(page_soup)
        title_hyperlinks = get_blogs_links_for(page_soup,heading_ls)
        
        if page==None and random==False:
            heading_with_desc_str = ""
            for i,j in enumerate(heading_ls):
                heading_with_desc_str+=f"{i+1}. {j}"
                heading_with_desc_str+=f"\n{head_desc_dict[j]}\n\n"
            print(heading_with_desc_str)
            
        if blog==None and random==True:
            choose_blog = randint(1,len(heading_ls))
        elif blog==None:
            choose_blog = int(input("Enter Blog Number to scrape: "))
        else:
            choose_blog = int(blog)
        choosen_blog_link = title_hyperlinks[heading_ls[choose_blog-1]]
        
        if multipage==True:
            scrape_and_save(choosen_blog_link,heading_ls[choose_blog-1],save_in_folders=True,page_no=str(page))
        else:
            scrape_and_save(choosen_blog_link,heading_ls[choose_blog-1])
        
        if scrape_all==True and multipage==True:
            blog+=1
            if blog == len(heading_ls)+1:
                return 
            driver(page=page,blog=blog,scrape_all=True,multipage=True)
        
        elif scrape_all==True:
            blog+=1
            if blog == len(heading_ls)+1:
                return 
            driver(page=page,blog=blog,scrape_all=True)
        
if __name__=='__main__':
    try:
        shutil.rmtree("scraped blogs/")
    except:
        pass
    driver(page=[5,9],scrape_all=True)