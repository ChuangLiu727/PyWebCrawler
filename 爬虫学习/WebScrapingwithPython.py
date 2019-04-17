#%% Change working directory from the workspace root to the ipynb file location. Turn this addition off with the DataScience.changeDirOnImportExport setting
import os
try:
	os.chdir(os.path.join(os.getcwd(), '爬虫学习'))
	print(os.getcwd())
except:
	pass

#%%
from urllib.request import urlretrieve 
from urllib.request import urlopen
from bs4 import BeautifulSoup
import re

#%% [markdown]
# # 第1章

#%%
html = urlopen("http://www.pythonscraping.com/pages/page1.html") 
bsObj = BeautifulSoup(html.read())
print(bsObj.h1)

#%% [markdown]
# # 第2章

#%%
html = urlopen("http://www.pythonscraping.com/pages/warandpeace.html") 
bsObj = BeautifulSoup(html)
nameList = bsObj.findAll("span", {"class":"green"}) 
#for name in nameList:
    #print(name.get_text())
    #get_text不保留标签


#%%
#正则表达式筛选商品图片
html = urlopen("http://www.pythonscraping.com/pages/page3.html")
bsObj = BeautifulSoup(html)
images = bsObj.findAll("img",{"src":re.compile("\.\.\/img\/gifts/img.*\.jpg")}) 
for image in images:
    print(image["src"])

#%% [markdown]
# # 第5章

#%%
html = urlopen("http://www.pythonscraping.com")
bsObj = BeautifulSoup(html)
imageLocation = bsObj.find("a", {"id": "logo"}).find("img")["src"]
urlretrieve (imageLocation, "logo.jpg")


#%%



