'''To-do - scrape all data to CSV file
Goal - grab all links from rithm school website
Data - store URL, anchor tag text and date
https://www.rithmschool.com/blog/
'''
import requests 
from bs4 import BeautifulSoup
from csv import writer
'''
request HTML data through requests, get response; parse that response throguh BeautSoup ' extract needed info and pass it to csv
'''
response = requests.get("https://www.rithmschool.com/blog/")
#print(type(response.text))-string
#print(response.text)
soup = BeautifulSoup(response.text, "html.parser")
articles = soup.find_all("article")

with open("rithm_blog_data.csv","w") as csv_file:
    csv_writer = writer(csv_file)
    csv_writer.writerow(['title','link','date'])
    
    for i in articles:
        
        titles = i.find("a").get_text()
        link = i.find("a")["href"]
        date_time = i.find("time")["datetime"]
        csv_writer.writerow([title,link,date])

    
    


