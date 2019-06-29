print('jo')

# id:       866939479966-ukmpi6vp1vdh0ghe1lj3h56upvjfpbg0.apps.googleusercontent.com 
# secret:       rjGB_bLvJlZS1fUrIe0u83ku 



# import requests
# response = requests.get('https://drive.google.com/open?id=1SjFm7bhtiirm7miEhdPhFPGMJUdH51xDgZI4df7ix2o&output=csv')
# assert response.status_code == 200, 'Wrong status code'
# print (response.content)




import requests
import csv    
import io

headers={}
headers["User-Agent"]= "Mozilla/5.0 (Windows NT 6.2; WOW64; rv:22.0) Gecko/20100101 Firefox/22.0"
headers["DNT"]= "1"
headers["Accept"] = "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8"
headers["Accept-Encoding"] = "deflate"
headers["Accept-Language"]= "en-US,en;q=0.5"
lines = []

file_id="1SjFm7bhtiirm7miEhdPhFPGMJUdH51xDgZI4df7ix2o"
url = "https://docs.google.com/spreadsheets/d/{0}/export?format=csv".format(file_id)

r = requests.get(url)

data = {}
cols = []

sio = io.StringIO( r.text, newline=None)
reader = csv.reader(sio, dialect=csv.excel)
rownum = 0

lines = []
for row in reader:
    print(row)
    lines.append(row)
    if rownum == 0:
        for col in row:
            data[col] = ''
            cols.append(col)

    else:
        i = 0
        for col in row:
            data[cols[i]] = col
            i = i +1

#         print( data)
    rownum = rownum + 1
    
print(reader)
with open('test.csv', 'wt', encoding='utf8') as writeFile:
    writer = csv.writer(writeFile, lineterminator = '\n')
    writer.writerows(lines)
    
# readFile.close()
writeFile.close()

