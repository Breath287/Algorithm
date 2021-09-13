import sys
print(sys.getsizeof(12))
print(sys.getsizeof(False))
print(sys.getsizeof(True))

import time
print(time.time())

import urllib.request
print(urllib.request.urlopen('http://www.google.com').read())

import schedule
def job():
    print('Hello!')

schedule.every(3).seconds.do(job)
while True:
    schedule.run_pending()
    time.sleep(1)