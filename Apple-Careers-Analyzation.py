# Apple Careers Analyzation
# Find keywords in titles of careers
# Common keywords: 'Junior', 'Early Career'

import pandas as pd

file1 = pd.read_csv('Apple-Careers-Developer.csv')
file2 = pd.read_csv('Apple-Careers-Junior.csv')
file3 = pd.read_csv('Apple-Careers-EarlyCareer.csv')

df = pd.DataFrame(file3)

keywords = ['Junior', 'Early Career', 'Engineer', 'Developer']

title = df['title']

keyword = title.str.contains('Early Career')

main_df = df[keyword]

main_df.to_csv('Main-Keyword.csv')
print('File saved to CSV.')

'''




'''