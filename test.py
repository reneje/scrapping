from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

#System.setProperty("webdriver.chrome.driver", "/Users/rinijannati/Documents/Coding/python/crawling");
#WebDriver driver = new ChromeDriver();
driverPath = "/Users/rinijannati/anaconda/selenium"
driver = webdriver.Chrome(executable_path=r"chromedriver")
driver.get("https://kompasiana.com")

searchBox = driver.find_element_by_id ('text_search')
searchBox.send_keys ('ahy')
searchBox.send_keys(u'\ue007')

ctr = 0
while True :
    print (ctr)
    ctr += 1
    try : 
        buttonLoadMore = driver.find_element_by_id ("load-more-search")
        buttonLoadMore.click ()
        time.sleep (5)
    except Exception as e :
        print (e.args)
        break
    
    if ctr == 15:
        print ("HERE 2") 
        break


filename = 'hrefahy_.txt'
fileopen = open(filename,'w')
contents = driver.find_elements_by_class_name ('artikel--content')

for content in contents : 
    # print (dir (content))
    h2 = content.find_element_by_tag_name ("h2").find_element_by_tag_name ('a')
    fileopen.writelines(h2.get_attribute('href'))
    fileopen.writelines('\n')
print ("HERE")
fileopen.close()