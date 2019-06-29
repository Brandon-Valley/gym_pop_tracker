
import requests
import csv    
import io



def download_google_sheet_as_csv(shareable_link_id, output_csv_path):
    
    headers={}
    headers["User-Agent"]= "Mozilla/5.0 (Windows NT 6.2; WOW64; rv:22.0) Gecko/20100101 Firefox/22.0"
    headers["DNT"]= "1"
    headers["Accept"] = "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8"
    headers["Accept-Encoding"] = "deflate"
    headers["Accept-Language"]= "en-US,en;q=0.5"
    lines = []
    
    file_id=shareable_link_id
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
        rownum = rownum + 1
        
    with open(output_csv_path, 'wt', encoding='utf8') as writeFile:
        writer = csv.writer(writeFile, lineterminator = '\n')
        writer.writerows(lines)
        
    writeFile.close()
    
#     https://drive.google.com/open?id=1o3qlhQPgk_VM2i48y2DPBhsI6fGFeCtsXyTmU31RWAs
download_google_sheet_as_csv("1o3qlhQPgk_VM2i48y2DPBhsI6fGFeCtsXyTmU31RWAs", 'gym_pop.csv')
