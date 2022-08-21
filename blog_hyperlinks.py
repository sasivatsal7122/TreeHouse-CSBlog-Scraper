def get_blogs_links_for(page_soup,blog_heading_ls):
    blog_hyperlinks = page_soup.find_all('article',{'class':'excerpt'})
    blog_hyperlinks_ls = []
    for text in blog_hyperlinks:
        links = text.find_all('a')
        for text in links:
            hrefText = (text['href'])
            blog_hyperlinks_ls.append(hrefText)
    blog_title_hyperlink = dict(zip(blog_heading_ls,blog_hyperlinks_ls))
    
    return blog_title_hyperlink