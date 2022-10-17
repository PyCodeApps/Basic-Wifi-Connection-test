import subprocess,os
import urllib.request
#welcome to my demo of an internet test
#today i'll be showing a simple internet test
#if you want to see the code go to the link in the description below
#without further ado lets start
print("Loading Wifi Test")
def connect(host='http://google.com'):
    try:
        urllib.request.urlopen(host) #Python 3.x
        return True
    except:
        return False
# test
print( '''         Wifi Connected
           (( :|:  ))
              |||
             |||||
            -------
''' if connect() else '''
No Internet
              :X:
              |||
             |||||
            -------
''' )

