import urllib2
import urllib
from time import gmtime, strftime
import ctypes

URL = "http://apod.nasa.gov/apod/astropix.html"
URL_FOLDER = "http://apod.nasa.gov/apod/"

checkString = "<a href=\"image/"
pageData = urllib2.urlopen(URL)
line = pageData.readline()
while(line!=''):
	if checkString in  line: 
		break
	line = pageData.readline()
NEW_URL = URL_FOLDER + line[9:-3]

postUrl = strftime("%d%m%Y",gmtime());
if(urllib.urlretrieve(NEW_URL,'newWallPaper'+postUrl+'.jpg')):
	SPI_SETDESKWALLPAPER = 20
	ctypes.windll.user32.SystemParametersInfoA(SPI_SETDESKWALLPAPER, 0, 'newWallPaper'+postUrl+'.jpg' , 0)	


