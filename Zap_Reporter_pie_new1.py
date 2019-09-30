import re
import requests
import sys

url = "http://127.0.0.1:8095/JSON/alert/view/alertsSummary/?apikey=pbjh2cv3qv6u03ib3llfnpcq5c&baseurl=" + sys.argv[1]
print(url)
r = requests.get(url)
print(r.text)
highval = re.search('"High":(.+?),', r.text)
if highval:
	value_high = highval.group(1)
print("High",value_high)
value_high = int(value_high)

mediumval = re.search('"Medium":(.+?),', r.text)
if mediumval:
	value_medium = mediumval.group(1)
print("Medium:",value_medium)
value_medium = int(value_medium)
lowval = re.search('"Low":(.+?),', r.text)
if lowval:
	value_low = lowval.group(1)
print("Low",value_low)
value_low = int(value_low)
infoval = re.search('"Informational":(.+?)}',r.text)
if infoval:
    value_info = infoval.group(1)
print("Informational:",value_info)
value_info = int(value_info)

Total = value_info+value_low+value_medium+value_high
print ("Total:" , Total)

with open("C:/Users/Cv/Desktop/new1.html") as inf:
    txt = inf.read()
    txt = str(txt)
print(txt)
datah = str(value_high)
datam = str(value_medium)
datal = str(value_low)
datai = str(value_info)
# datah = str(datah)
# datam = str(datam)
# datal = str(datal)
# datai = str(datai)
html = re.sub(r"300878", datah, txt)
html1 = re.sub(r"266455", datam, html)
html2 = re.sub(r"169709", datal, html1)
html3 = re.sub(r"158400", datai, html2)
print (html3)
Html_file= open("C:/Users/Cv/Desktop/new2.html","w")
Html_file.write(html3)
Html_file.close()
