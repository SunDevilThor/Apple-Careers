# Apple Careers

import requests
from bs4 import BeautifulSoup
import pandas as pd

careers_list = []

def request(x):
    search_term = 'Early'
    url = (f'https://jobs.apple.com/en-us/search?search={search_term}&sort=relevance&location=united-states-USA&page={x}&team=apps-and-frameworks-SFTWR-AF+cloud-and-infrastructure-SFTWR-CLD+core-operating-systems-SFTWR-COS+devops-and-site-reliability-SFTWR-DSR+engineering-project-management-SFTWR-EPM+information-systems-and-technology-SFTWR-ISTECH+machine-learning-and-ai-SFTWR-MCHLN+security-and-privacy-SFTWR-SEC+software-quality-automation-and-tools-SFTWR-SQAT+wireless-software-SFTWR-WSFT')
    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.1.1 Safari/605.1.15'}
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, 'html.parser')
    return soup.find_all('tbody')


# Comment out after first run of script and file is successfully created. 
# with open('Apple-Careers-OFFLINE.html', 'w') as file: 
#    file.write(str(soup))
#    print('Offline file saved.')

def parse(jobs):
    for job in jobs:
        title = job.find('a').text
        link = 'https://jobs.apple.com' + str(job.a['href'])
        location = job.find('td', class_= 'table-col-2').text
        department = job.find('span', class_= 'table--advanced-search__role').text
        date_added = job.find('span', class_= 'table--advanced-search__date').text

        career = {
            'title': title, 
            'department': department, 
            'location': location, 
            'date_added': date_added, 
            'link': link, 
        }

        careers_list.append(career)

def output():
    df = pd.DataFrame(careers_list)
    df.to_csv('Apple-Careers-EarlyCareer.csv')
    print('Saved items to CSV file.')

x = 1 
while True: 
    print(f'Getting page: {x}')
    jobs = request(x)
    x += 1
    if len(jobs) != 0:
        parse(jobs)
    else: 
        break

print('Completed. Total available job listings:', len(careers_list))
output()



# NOTES:
# https://jobs.apple.com/en-us/search?location=united-states-USA
# https://jobs.apple.com/en-us/search?location=united-states-USA&page=2
# https://jobs.apple.com/en-us/search?search=developer&sort=relevance&location=united-states-USA
# https://jobs.apple.com/en-us/search?search=early%20career&sort=relevance&location=united-states-USA