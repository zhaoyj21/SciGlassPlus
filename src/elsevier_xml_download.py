# -*- coding: utf-8 -*-
import requests
import time
import random
import os


apikey1='YOUR_KEY'

#opath="D:/glass/xml_els/"
#opath="D:/glass1419/xml_els/"
#opath="D:/glass0013/xml_els/"
opath="D:/glass-total-results/xml_els/"
#f=open("D:/glass/Elsevier.txt")
#f=open("D:/glass1419/Elsevier.txt")
#f=open("D:/glass0013/els2.txt")
f=open("D:/glass-total-results/Elsevier.txt")
#fout=open("D:/glass/xml_els/elsevier_xml_download_log.txt","a")
#fout=open("D:/glass1419/xml_els/elsevier_xml_download_log.txt","a")
fout=open("D:/glass0013/xml_els/elsevier_xml_download_log.txt","a")
doi=[]
doiname=[]
for tmp in f.readlines():
    tmp1=tmp.replace("\n","")
    tmp1=tmp1.replace(" ","")
    doi.append(tmp1)
    doiname.append(tmp1.replace("/","_"))
f.close()

for i in range(0,len(doi)):
    try:
        response=requests.get("https://api.elsevier.com/content/article/doi/"+doi[i],headers={'Accept':'application/xml','X-ELS-APIKey': apikey1, 'X-ELS-Insttoken': apikey2})
        print(doi[i]+"  status: "+str(response.status_code))
    except:
        print(doi[i]+" ERROR")
        fout.write(doi[i]+" ERROR\n")
        
    f=open(opath+doiname[i]+".xml",'w',encoding='utf-8')
    f.write(response.text)
    f.close()
    lag=random.uniform(1,3)
    time.sleep(lag)      
    
fout.close()