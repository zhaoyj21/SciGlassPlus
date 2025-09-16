# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver import ChromeOptions
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time
import random

def html_download(doi):
    if len(doi)<7:
        return
    if (doi[0:7]=='10.1111')or(doi[0:7]=='10.1002'): #wiley':
        base_url = 'http://onlinelibrary.wiley.com/doi/'
        api_url = base_url + doi
    elif doi[0:7]=='10.1088': 
        base_url='https://iopscience.iop.org/article/'
        api_url = base_url + doi
    elif (doi[0:7]=='10.1007')or(doi[0:7]=='10.1557'): #'springer':
        base_url = 'http://link.springer.com/'
        api_url = base_url + doi + '.html'
    else:  
        return
    option=ChromeOptions()
    option.add_experimental_option('excludeSwitches',['enable-automation'])
    option.add_argument("--no-sandbox")
    option.add_argument("--lang=zh-CN")
    # option.add_argument("--window-size=500,300")
    #service=Service(executable_path='D:/Tsinghua/Project/Fatigue Data Framework/code/python/chromedriver.exe')
    option.add_argument("-window-size=1000,800")
    driver=webdriver.Chrome('C:/Users/dell/anaconda3/pkgs/python-3.8.19-h1aa4202_0/Scripts/chromedriver.exe',options=option)
    driver.get(api_url)
    # windows=driver.window_handles
    # if len(windows)>1:
    #     driver.close()
    #     driver.switch_to.window(windows[-1])    
    lag=random.uniform(5,10)
    time.sleep(lag+1)     
    name=doi.replace('/','_')
    #f=open('D:/glass/html_wiley/'+name+'.html',"w",encoding='utf-8')
    f=open('D:/glass-total-results/html_wiley/'+name+'.html',"w",encoding='utf-8')
    #f=open('D:/glass1419/html_springer/'+name+'.html',"w",encoding='utf-8')
    f.write(driver.page_source)
    f.close()
    driver.close()
       

    
    
#f=open("D:/glass/Wiley.txt")
#f=open("D:/glass1419/Wiley.txt")
f=open("D:/glass-total-results/Wiley.txt")
#f=open("D:/glass1419/Springer.txt")
doi=[]
doiname=[]
for tmp in f.readlines():
    tmp1=tmp.replace("\n","")
    tmp1=tmp1.replace(" ","")
    doi.append(tmp1)
    doiname.append(tmp1.replace("/","_"))
f.close()

for i in range(0,len(doi)):
    #if (i>0)and(len(doi[i])>7)and(len(doi[i-1])>7)and(doi[i-1][0:7]==doi[i][0:7]):
    # lag=random.uniform(0,10)
    # time.sleep(lag+1) 
    # print(doi[i])
    try:
        html_download(doi[i])
        print('COMPLETED')
    except:
        print('ERROR')