import pandas as pd
import csv
import json

with open ('D:\Users\u0162794\Desktop\Doc\Python\sample.csv','rb') as f:
    readers=csv.reader(f)
    for row in readers:
        print(row)

with open ('D:\Users\u0162794\Desktop\Doc\Python\samj.json','w', encoding="utf8") as jsonfile:
    json.dumps(readers,jsonfile)
    
    

    
