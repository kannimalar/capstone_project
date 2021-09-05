import requests
from bs4 import BeautifulSoup
from datetime import datetime
startTime = datetime.now()
def jobdesc(givenUrl):
    details=""
    nexturl = "https://internshala.com"+givenUrl
    nextpage = requests.get(nexturl)
    soupnext = BeautifulSoup(nextpage.content, "html.parser")
    for p in soupnext.find_all(lambda tag: tag.name == 'div' and 
                                   tag.get('class') == ['text-container']):
        details= details+" "+p.text
    return details
    

URL = "https://internshala.com/fresher-jobs/job"
page = requests.get(URL)
soup = BeautifulSoup(page.content, "html.parser")
jobs = []
job_title =[]
jobdetails =[]

for div in soup.find_all(name="div",attrs={"class":"heading_4_5 profile"}):
    job_title.append(div.text)

for div0 in soup.find_all(name="div",attrs={"class":"heading_6 company_name"}):
    for a in div0.find_all(name="a" , attrs={"class":"link_display_like_text"}):
        jobs.append(a.text)
for a in soup.find_all(name="a" , attrs={"class":"view_detail_button"}):
        # print(a['href']+" end")
        jobdetails.append(jobdesc(a['href']))        
import pandas as pd
data_frame= pd.DataFrame({'Job title':job_title,'Company Name':jobs,'Job Details': jobdetails})

print(datetime.now()-startTime)
