SCRAPER INSTRUCTIONS

Requirements:
- have Python (3) installed
- install requests and beautifulsoup4
in terminal:
pip3 install requests
pip3 install beautifulsoup4

How to use scraper script:
1. run in python shell
2. in python shell, use the scrape_novel(title,url) function to scrape a novel
	the novel text will be saved to title.txt in the same folder as the script
	url is the url of CHAPTER 1 of the novel, NOT the index page (use the mobile site m.shubaow.net!)
3. scraper is set to take 1 page every 5 seconds to not spam the site with requests,
	wait for it to finish - it will go through the whole novel automatically,
	no need to scrape chapter by chapter
4. (NEW) to scrape ALL novels by a certain author, use the scrape_author(author, url) function
	the novel text will be saved to author/title.txt
	url is the url of the page listing all of that author's novels (use m.shubaow.net!)
	to exclude certain novels, use scrape_author(author,url,list) where list contains titles of all novels NOT to scrape (eg. ['title1','title2','title3'])