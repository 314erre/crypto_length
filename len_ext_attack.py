from pymd5 import md5, padding
import httplib, urlparse, sys
import urllib

url = sys.argv[1]

length_of_m = 52
m_bits = (length_of_m + len(padding(length_of_m * 8)))* 8

h = md5(state="402a574d265dc212ee64970f159575d0".decode("hex"), count=m_bits)

parsedUrl = urlparse.urlparse(url)

parsedstring = urllib.quote(parsedUrl)

x = "&command3=UnlockAllSafes"
h.update(x)
print h.hexdigest()

conn = httplib.HTTPSConnection(parsedUrl.hostname,parsedUrl.port)
conn.request("GET", parsedUrl.path + "?" + parsedUrl.query)
print conn.getresponse().read()
