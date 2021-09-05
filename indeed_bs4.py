import requests
from bs4 import BeautifulSoup
from datetime import datetime
startTime = datetime.now()
def jobdesc(givenUrl,session):
    details=""
    nexturl = "https://in.indeed.com"+givenUrl
    nextpage = session.get(nexturl)
    soupnext = BeautifulSoup(nextpage.content, "html.parser")
    for p in soupnext.find_all(name="div",attrs={"class":"jobsearch-jobDescriptionText"}):
        details= details+" "+p.text
    return details.strip()
    

URL = "https://in.indeed.com/jobs?q&l=india&sort=date&vjk=38f72defe4a4fef1"
page = requests.get(URL)

# print(page.text)
soup = BeautifulSoup(page.content, "html.parser")
session = requests.Session()
# print(soup.prettify())
jobs = []
jobdetails =[]
for div0 in soup.find_all(name="div",attrs={"class":"mosaic-zone"}):
 for a in div0.find_all(name="a" , attrs={"data-hide-spinner":"true"}):
      if(a['href']!=''):
       jobdetails.append(jobdesc(a['href'],session)) 
       # print(a['href']+" "+"end"+"\n")
 for div in div0.find_all(name="div", attrs={"class":"job_seen_beacon"}):
    for div1 in div.find_all(name="div", attrs={"class":"heading6 company_location tapItem-gutter"}):
        for pre in div1.find_all(name="pre"):
            for span in pre.find_all(name="span",attrs={"class":"companyName"}):
                jobs.append(span.text)
                # print(span.text)
import pandas as pd
data_frame= pd.DataFrame({'Company Name':jobs,'Job Details': jobdetails})


print(datetime.now()-startTime)
