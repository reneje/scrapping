url = 'https://mkri.id/index.php?page=download.Putusan&id=2962'
 
# downloading with urllib
 
# import the urllib package
import urllib.request
 
# Copy a network object to a local file
urllib.request.urlretrieve(url, "tutorial.pdf")
 
 
# downloading with requests
 
# import the requests library
import requests
 
# download the file contents in binary format
r = requests.get(url)
 
# open method to open a file on your system and write the contents
with open("tutorial1.pdf", "wb") as code:
    code.write(r.content)
