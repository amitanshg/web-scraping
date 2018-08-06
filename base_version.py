from BeautifulSoup import BeautifulSoup
import urllib2
import re

html_page = urllib2.urlopen("http://www.imd.gov.in/Welcome%20To%20IMD/Welcome.php")
soup = BeautifulSoup(html_page)
b = soup.findAll('a', attrs={'href': re.compile("^http://hydro.imd.gov.in/hydrometweb/")})
c = b[0]['href']
d = c[0:len(c)-12]

e = d + "PRODUCTS/Rainfall_Statistics/Cumulative/District_RF_Distribution/DISTRICT_RAINFALL_DISTRIBUTION_COUNTRY_INDIA_cd.PDF"

def download_file(download_url):
    response = urllib2.urlopen(download_url)
    file = open("document.pdf", 'wb')
    file.write(response.read())
    file.close()
    print("Completed")
    
download_file(e) 
