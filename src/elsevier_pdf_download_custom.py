# -*- coding: utf-8 -*-
import requests

#path="D:/glass/pdf_list/"
#path="D:/glass1419/pdf_list_1419/"
path="D:/glass-total-results/els_pdf7/"
f=open(path+"els_pdf.txt")
doi=[]
for tmp in f.readlines():
    if '/' in tmp:
        tmp1=tmp.replace("\n","")
        tmp1=tmp1.replace(" ","")
        doi.append(tmp1)
f.close()

for i in range(3000,len(doi)):
    try:
        response=requests.get("https://api.elsevier.com/content/article/doi/"+doi[i]+"?apiKey='your API key'&httpAccept=application%2Fpdf")
        print(doi[i]+"  status: "+str(response.status_code)+"\n")

    except:
        print(doi[i]+" ERROR\n")
    
    file=doi[i].replace('/','_')
    f=open(path+file+".pdf",'wb')
    f.write(response.content)
    f.close()

