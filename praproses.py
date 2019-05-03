import re
import pandas as pd 

def deleteTag(expr):
    cleanr = re.compile('<.*?>')
    expr = str(expr)
    hsl = re.sub(cleanr," ",expr)
    hsl = re.sub("\n"," ",hsl)
    hsl = re.sub(". ,",".",hsl)
    # hsl = re.sub(r"[\[\]]","",hsl)
    return hsl

def deleteTag2(expr):
    cleanr = re.compile('<.*?>')
    expr = str(expr)
    hsl = re.sub(cleanr," ",expr)
    hsl = re.sub("\n"," ",hsl)
    return hsl

def cleaning(dokumen):
    dokumen = re.sub(r"\[caption.*?\[/caption\]","",dokumen)
    dokumen = re.sub("sumber.*?,","",dokumen)
    dokumen = re.sub("http.*?,","",dokumen)
    dokumen = re.sub("http.*?=en","",dokumen)
    dokumen = re.sub("Sumber.*?.,","",dokumen)
    return dokumen

def changeSmtg(expr):
    expr = re.sub("&nbsp;"," ",expr)
    expr = re.sub("&amp;","&",expr)
    expr = re.sub("$quot;","\"",expr)
    expr = re.sub("&lt;","<",expr)
    expr = re.sub("&gt;",">",expr)
    expr = re.sub("&emsp;"," ",expr)
    expr = re.sub('¬†','',expr)
    # expr = re.sub("\\xa0  ","",expr)
    # expr re.sub(r'[^\x00-\x7F]+','',expr).decode('utf-8','ignore').strip()
    # expr = expr.replace(u'\xa0', u'')
    return expr

def deletehref(expr):
    expr = re.sub('href','',expr)
    expr = re.sub('\"','',expr)
    expr = re.sub('=','',expr)
    return expr

def saveToCSV(link,title, author, date, time,contain,tag,namafile):
    raw_data={"link":link,"title":title,"author":author,"date":date,"time":time,"news":contain,"tags":tag}
    dataf = pd.DataFrame(raw_data,columns=["link","title","author","date","time","news","tags"])
    dataf.to_csv(namafile)

def saveToCSV2(link,title, date, time,contain,tag,namafile):
    raw_data={"link":link,"title":title,"date":date,"time":time,"news":contain,"tags":tag}
    dataf = pd.DataFrame(raw_data,columns=["link","title","date","time","news","tags"])
    dataf.to_csv(namafile)