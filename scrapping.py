from bs4 import BeautifulSoup #pip install beautifulsoup4
import urllib3 #pip install urllib3
import requests
import re
import urllib.request
import fitz #pip install PyMuPDF
import io 
import os

def bersihsub(expr):
    cleanr = re.compile('<.*?>')
    expr = str(expr)
    hsl = re.sub(cleanr,"",expr)
    hsl = re.sub("\n"," ",hsl)
    hsl = re.sub("  ","\n",hsl)
    return hsl

#Download PDF
def download_pdf(url,name_file):
    urllib.request.urlretrieve(url, name_file)

#Get content from MKRI website
def get_pdf(get_content):
    get_content= re.sub('<a href="','https://mkri.id/',get_content)
    get_content= re.sub('" style="color:#009900; text-decoration:none">','',get_content)
    get_content= re.sub('&amp;','&',get_content)
    get_content= re.sub("\n",'',get_content)
    get_content= re.sub("Klik Disini</a>",'',get_content)
    get_content= re.sub(' ','',get_content)
    return get_content

#Extract the PDF file
def extractText(file): 
    doc = fitz.open(file) 
    text = ""
    for page in doc: 
        text += str(page.getText())#.encode("utf8"))
    doc.close()
    return text
	
#Main program for scrapping PDF from MKRI website
for i in range (1,122): #Set page range that we want to scrap
    page = requests.get('https://mkri.id/index.php?page=web.Putusan&id='+str(i)+'&kat=1&menu=5') #Set spesific page type
    soup = BeautifulSoup(page.text,'html.parser')
    namelist = soup.find('div',class_ = 'isi-konten')
    namelist_item = namelist.find_all('div',class_ = 'content-persidangan')
    j=0
    for website in namelist_item:
        get_content= get_pdf(str(website.find('a')))       
        hasil_bersih = bersihsub(website)
        j+=1
        nama_pdf =str(i)+"_"+str(j)+".pdf" #Define PDF name
        nama_txt = "PUU_"+str(i)+"_"+str(j)+".txt" #Define extracted file name
        download_pdf(get_content, nama_pdf)
        txt = extractText(nama_pdf)
        with io.open(nama_txt, "w", encoding="utf-8") as text_file:
            text_file.write(txt)
        if os.path.exists(nama_pdf): #Comment this statement if we want to keep the PDF file
            os.remove(nama_pdf)
        print(nama_pdf) #Just print free name to make sure that our program still running