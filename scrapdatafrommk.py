from bs4 import BeautifulSoup
import urllib3
import requests
import re
import urllib.request
 

def bersihsub(expr):

    cleanr = re.compile('<.*?>')
    expr = str(expr)
    hsl = re.sub(cleanr,"",expr)
    hsl = re.sub("\n"," ",hsl)
    hsl = re.sub("  ","\n",hsl)
    return hsl
 
def download_pdf(url,name_file):
    urllib.request.urlretrieve(url, name_file)

def get_pdf(get_content):
    get_content= re.sub('<a href="','https://mkri.id/',get_content)
    get_content= re.sub('" style="color:#009900; text-decoration:none">','',get_content)
    get_content = re.sub('&amp;','&',get_content)
    get_content= re.sub("\n",'',get_content)
    get_content= re.sub("Klik Disini</a>",'',get_content)
    get_content= re.sub(' ','',get_content)
    return get_content

#collect first page of artists's list
for i in range (1,2):
    page = requests.get('https://mkri.id/index.php?page=web.Putusan&id='+str(i)+'&kat=1&cari=&menu=5')

    #create a beautifu;soup object
    soup = BeautifulSoup(page.text,'html.parser')

    # print (type(soup))

    # print(soup.prettify())
    namelist = soup.find('div',class_ = 'isi-konten')

    namelist_item = namelist.find_all('div',class_ = 'content-persidangan')
    # print(namelist_item)
    #simpan
    # fileopen = open("filekompas.txt","w")
    j=0
    print("halaman: ",i)
    for website in namelist_item:
        print("nomor ", j)
        get_content= get_pdf(str(website.find('a')))
        
        print(get_content)
        hasil_bersih = bersihsub(website)
        print("hasil ",hasil_bersih)
        j+=1
        nama=str(i)+"_"+str(j)+".pdf" 
        download_pdf(get_content, nama)
        # data = re.sub(r'<.*?>', '', website)
        # fileopen.write(website.prettify())

    # fileopen.close()