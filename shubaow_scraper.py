import requests
from bs4 import BeautifulSoup
import time
import os

def scrape_page(url,file_name):
    time.sleep(5)
    page = requests.get(url)
    soup = BeautifulSoup(page.content,'html.parser')
    title_div = soup.find('div',{'class':'nr_function'})
    title = title_div.find('h1').text
    text_div = soup.find(id='nr1')
    paragraphs = text_div.text.split('\xa0\xa0\xa0\xa0')
    nav_div = soup.find('div',{'class':'page_chapter'})
    next_chap = nav_div.find('a',{'class':'p4'})
    next_link = 'https://m.shubaow.net'+next_chap['href']
    
    with open(file_name, 'a') as file:
        file.write(title+'\n')
        for p in paragraphs:
            file.write(p+'\n')

    print('successfully scraped chapter',title)

    return next_link

def scrape_novel(prefix,link):
    """
    prefix: novel file will be saved under this name + .txt
    link: first chapter link
    """
    file_name = prefix+'.txt'
    while True:
        link = scrape_page(link,file_name)
        if link[-4:] != 'html':
            print('complete')
            return True
        
def find_c1_link(link):
    """
    link: novel page link
    returns: link to chapter 1
    """
    time.sleep(5)
    page = requests.get(link)
    soup = BeautifulSoup(page.content,'html.parser')
    lists = soup.find_all('ul',{'class':'p2'})
    c1_a = lists[1].find('a')
    return 'https://m.shubaow.net'+c1_a['href']
    
def scrape_author(author,link,exclude=None):
    """
    author: author name, will be first part of file name
    link: author page link
    exclude: do not download novels in this list
    """
    if exclude is None:
        exclude = []
    
    if not os.path.exists(author):
        os.makedirs(author)
    
    page = requests.get(link)
    soup = BeautifulSoup(page.content,'html.parser')
    novels = soup.find_all('div',{'class':'content_link'})
    # match file prefix: first chapter link (input to scrape_novel)
    link_dict = {}

    for novel in novels:
        title_p = novel.find('p',{'class':'p2'})
        title_a = title_p.find('a')
        title = title_a.text
        if title in exclude:
            continue
        prefix = author+'/'+title
        print('found novel',title)
        nov_link = find_c1_link('https://m.shubaow.net'+title_a['href'])
        link_dict[prefix] = nov_link

    for prefix,nov_link in link_dict.items():
        print('scraping novel',prefix)
        scrape_novel(prefix,nov_link)

    return True
