def scrape_head_desc_for(page_soup):
    blog_heading = page_soup.find_all('h3')
    blog_heading_ls = []
    for heading in blog_heading:
        blog_heading_ls.append(heading.text.strip())
    blog_desc = page_soup.find_all('div',{'class':'excerpt'})
    blog_desc_ls = []
    for text in blog_desc:
        desc = text.find_all('p')
        blog_desc_ls.append(desc[0].text.strip())
    blog_heading_desc = dict(zip(blog_heading_ls,blog_desc_ls))

    return blog_heading_desc,blog_heading_ls