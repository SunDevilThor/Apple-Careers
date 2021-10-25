# Offline file from Apple-Careers.py

from bs4 import BeautifulSoup

file = open('Apple-Careers-OFFLINE.html')

soup = BeautifulSoup(file, 'html.parser')

jobs = soup.find_all('tbody')

for job in jobs:
    title = job.find('a').text
    link = 'https://jobs.apple.com' + str(job.a['href'])
    location = job.find('td', class_= 'table-col-2').text
    department = job.find('span', class_= 'table--advanced-search__role').text
    date_added = job.find('span', class_= 'table--advanced-search__date').text
    print(date_added)    


# Create a list at the top
# Create a dictionary at the bottom
# Append items from the dictionary to the list at the top
# Output data to Pandas DF
# Create For loop for pagination
# Create f strings for custom searches

# Remove git and start over. 

# git add .
# git commit -m 'Initial commit. Completed Title, Location, Department, and Date-Created'
# git remote add origin https://github.com/SunDevilThor/Apple-Careers.git
# git push --set-upstream origin master

file.close()