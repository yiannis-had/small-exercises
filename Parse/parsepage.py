import requests, bs4
    
req = requests.get('https://www.onixs.biz/fix-dictionary/4.2/tagNum_1.html')
soup = bs4.BeautifulSoup(req.text,features="html.parser")
elems = soup.select('h3')
for elem in elems:
    if elem.get_text() == 'Used In':
        for sibling in elem.find_next_siblings():
            print(sibling.get_text())
    else:
        pass
