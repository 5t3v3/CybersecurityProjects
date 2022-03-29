#Python script for finding redirections

import requests

txt=input('Enter the file containing list of URLS as TXT : ') #"Enter the url in correct format"
f = open(str(txt), 'r+')          # Open file from system
f_data=f.read().splitlines()      # Reading the file 
pay=input("\nEnter the payload file: ")
p=open(str(pay),'r+')
p_data=p.read().splitlines()
print ("\nStarting Test Module")
for i in f_data:
    for j in p_data:
        
        xy=str(j) # payload loop
        urll='https://'+i #adding http request
        xx=str(urll)   #url loop
        r=xx+'/'+xy # concatenating url with payload
        req=requests.get(r) #http request (GET) with the combined string
        print ("\nThe request is ",r)
        out=req.status_code         # http response code of the request
        print ("Http Response code is : ",out)

p.close()
f.close()
