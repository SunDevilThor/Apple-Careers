# Apple Careers Analyzation
# Find keywords in titles of careers
# Common keywords: 'Junior', 'Early Career'

import pandas as pd

file1 = pd.read_csv('Apple-Careers-Developer.csv')
file2 = pd.read_csv('Apple-Careers-Junior.csv')

df = pd.DataFrame(file1)
df2 = pd.DataFrame(file2)

keywords = ['Junior', 'Early Career']

title = df['title']

# BELOW DOWN - NOT WORKING

main = title.str.contains('Junior')

junior = df2[df2['title'].str.contains('Junior')]

print(junior)

'''




'''