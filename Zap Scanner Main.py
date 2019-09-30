import time
from pprint import pprint
from zapv2 import ZAPv2

target = 'https://test.com'
apikey = 'pbjh2cv3qv6u03ib3llfnpcq5c' # Change to match the API key set in ZAP, or use None if the API key is disabled

# By default ZAP API client will connect to port 8080
zap = ZAPv2(apikey=apikey)
# Use the line below if ZAP is not listening on port 8080, for example, if listening on port 8090
zap = ZAPv2(apikey=apikey, proxies={'http': 'http://192.168.0.27:8095', 'https': 'http://192.168.0.27:8095'})

# do stuff
print ('Welcome to ------ Tool\n\n\n\n!!!NAME!!!')
print ('Accessing target %s' % target)
# try have a unique enough session...
zap.urlopen(target)
# Give the sites tree a chance to get updated
time.sleep(2)

print ('Spidering target %s' % target)
scanid = zap.spider.scan(target)
# Give the Spider a chance to start
print(zap.httpsessions.sites)
time.sleep(2)

while (int(zap.spider.status(scanid)) < 100):
    print ('Spider progress %: ' + zap.spider.status(scanid)+'\n\n\n\n')
    print(*zap.spider.results(scanid), sep = "\n")
    time.sleep(2)
print(*zap.spider.results(scanid), sep = "\n")
print ('Spider completed')
# Give the passive scanner a chance to finish
time.sleep(5)

print ('Scanning target %s' % target)
scanid = zap.ascan.scan(target)
while (int(zap.ascan.status(scanid)) < 100):
    print ('Scan progress %: ' + zap.ascan.status(scanid))
    print (*zap.ascan.scan_progress(scanid=scanid), sep = "\n")
    time.sleep(5)

print ('Scan completed')
time.sleep(1)

# Report the results
zap.core.htmlreport(apikey='pbjh2cv3qv6u03ib3llfnpcq5c')
print('Generating Report\n\n')
print ('Hosts: ' + ', '.join(zap.core.hosts))
print ('Alerts: ')
pprint (zap.core.alerts())
