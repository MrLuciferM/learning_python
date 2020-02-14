from bs4 import BeautifulSoup as soup
from urllib.request import urlopen as uReq

sear=str(input("Enter search data: "))

#myurl = 'https://www.flipkart.com/search?q=pixel&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=off&as=off'

#to combine the string replacing the white spaces 
def combine(sear):
    a='https://www.flipkart.com/search?q='
    b='&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=off&as=off'
    if " " in sear:
        sear=sear.strip()
        search_list=sear.split(" ")
        sear="%20".join(search_list)
        myurl=a+sear+b
        return myurl
myurl= combine(sear)
uClient = uReq(myurl)
page_html = uClient.read()
uClient.close()

page_soup = soup(page_html,"html.parser")

containers = page_soup.findAll("div",{"class":"col col-5-12 _2o7WAb"})
#print(len(containers))
#print(soup.prettify(containers[0])) # THIS PRINTS THE IDF STRUCTURE OF THAT CLASS
for i in range(len(containers)):
    container=containers[i]
    #print(container)
    price = container.findAll("div",{"class":"_1vC4OE _2rQ-NK"})
    container1 = page_soup.findAll("div",{"class":"col col-7-12"})
    rating = container1[i].findAll("div",{"class":"hGSR34"})
    Model = container1[i].findAll("div",{"class":"_3wU53n"})
    print(Model[0].text)
    print("Price: ",price[0].text)
    print("Rating: ",rating[0].text)
    print("\n")