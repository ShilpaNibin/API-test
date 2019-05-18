
import urllib.request
import re

urls=["https://www.atg.world/#"]
pattern="<title>(.+?)</title>"
result=re.compile(pattern)


for url in urls:
        htmlsource=urllib.request.urlopen(url)
        htmltext=htmlsource.read().decode('utf-8')
        titles=re.findall(result,htmltext)
        print (titles)
        
