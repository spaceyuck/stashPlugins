import sys
import urllib.request

external_ip = urllib.request.urlopen('https://v4.ident.me/').read().decode('utf8')
print("\x01{}\x02".format("i"), f"Current IP : {external_ip}", file=sys.stderr, flush=True)
