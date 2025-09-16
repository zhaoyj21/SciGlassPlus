# -*- coding: utf-8 -*-
import requests
import json
import time
import random

def pdf_download(path,doi):
    global fout
    base_url = 'http://api.crossref.org/works/'
    name=doi.replace('/','_')
    
    f=open(path+name+'.pdf','wb')
    
    api_url = base_url + doi
    
    headers = {
        'Accept': 'application/json'
    }
    
    response = json.loads(requests.get(api_url, headers=headers).text)
    
    pdf_url = response['message']['link'][0]['URL']
    
    app_type = str(response['message']['link'][0]['content-type'])
    
    if app_type in ['application/pdf', 'unspecified']:
        headers = {
            'Accept': 'application/pdf'
        }
        r = requests.get(pdf_url, stream=True, headers=headers)
        if r.status_code == 200:
            for chunk in r.iter_content(2048):
                f.write(chunk)
            print('DOWNLOADED: '+doi)
            fout.write('DOWNLOADED: '+doi+'\n')
        else:
            print('ERROR: '+doi)
            fout.write('ERROR: '+doi+'\n')
    
    f.close()


#path="D:/glass1419/pdf_list3_1419/"
#path="F:/glass0013/pdf_list_0013/"
path="D:/glass-total-results/pdf8/"
f=open(path+"other_pdf.txt")
#f=open(path+"doi3.txt")
doi=[]
for tmp in f.readlines():
    if '/' in tmp:
        tmp1=tmp.replace("\n","")
        tmp1=tmp1.replace(" ","")
        doi.append(tmp1)
f.close()

fout=open(path+"other_doi.log","w")
for i in range(220,len(doi)):
    #if (i>0)and(len(doi[i])>7)and(len(doi[i-1])>7)and(doi[i-1][0:7]==doi[i][0:7]):
    lag=random.uniform(3,6)
    time.sleep(lag+1) 
    try:
        pdf_download(path,doi[i])
    except:
        print('ERROR0: '+doi[i])
        fout.write('ERROR0: '+doi[i]+'\n')

f.close()

# # TEST
# base_url = 'http://api.crossref.org/works/'
# doi='10.1111/ffe.13598'
# name=doi.replace('/','_')

# f=open('D:/'+name+'.pdf','wb')

# api_url = base_url + doi

# headers = {
#     'Accept': 'application/json'
# }

# proxies={
#     "https":None,
#     "http":None,
# }

# response = json.loads(requests.get(api_url, headers=headers).text)

# pdf_url = response['message']['link'][0]['URL']

# app_type = str(response['message']['link'][0]['content-type'])

# if app_type in ['application/pdf', 'unspecified']:
#     headers = {
#         'Accept': 'application/pdf',
#         'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36 Edg/97.0.1072.55'
#     }
#     r = requests.get(pdf_url, proxies=proxies, stream=True, headers=headers)
#     if r.status_code == 200:
#         for chunk in r.iter_content(2048):
#             f.write(chunk)
#     else:
#         print('ERROR')

# f.close()