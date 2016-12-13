import RPi.GPIO as GPIO
import time
import pycurl
import serial
import json
import StringIO

GPIO.setmode(GPIO.BOARD)
GPIO.setup(11,GPIO.OUT)

serial0=serial.Serial("/dev/ttyS0",2400)

Vout_H=0
Vout_L=0
Vret_H=0
Vret_L=0
check=0
A=1000

username='zhangsheng377'
password='bz292929'

response = StringIO.StringIO()
mycurl=pycurl.Curl()
mycurl.setopt(mycurl.URL,'http://api.yeelink.net/v1.0/user/apikey?username='+username+'&pass='+password)
mycurl.setopt(mycurl.WRITEFUNCTION, response.write)
mycurl.perform()
#response=mycurl.getinfo(mycurl.RESPONSE_CODE)
myresp=json.loads(response.getvalue())
if myresp['errcode']=='0':
     apikey=myresp['apikey']
     print apikey
mycurl.close()

device_id='353097'
sensor_id='397985'

while True:
     waitlen=serial0.inWaiting()
     if waitlen!=0:
          recv=serial0.read(waitlen)
          listhex=[ord(i) for i in recv]
          count=0
          for i in range(len(listhex)):
               if count==0:
                    if listhex[i]==170:
                         count+=1
                         Vout_H=0
                         Vout_L=0
                         Vret_H=0
                         Vret_L=0
                         check=0
               else:
                    count+=1
                    if count==2:
                         Vout_H=listhex[i]
                    elif count==3:
                         Vout_L=listhex[i]
                    elif count==4:
                         Vret_H=listhex[i]
                    elif count==5:
                         Vret_L=listhex[i]
                    elif count==6:
                         check=listhex[i] 
                    elif count==7:
                         count=0
                         if listhex[i] == 255:
                              if check==(Vout_H+Vout_L+Vret_H+Vret_L)%256:
                                   Vout=(Vout_H*256+Vout_L)*1.0/1024*8;
                                   Ud=1.0*A*Vout
                                   if Ud>0:
                                        print "pm2.5 :",Ud
                                        mycurl=pycurl.Curl()
                                        mycurl.setopt(mycurl.URL,'http://api.yeelink.net/v1.0/device/'+device_id+'/sensor/'+sensor_id+'/datapoints')
                                        mycurl.setopt(mycurl.HTTPHEADER,["U-ApiKey:"+apikey])
                                        mycurl.setopt(mycurl.POSTFIELDS,json.dumps({"value":Ud}))
                                        try:
                                             mycurl.perform()
                                        except Exception,e:
                                             print Exception,":",e
                                        mycurl.close()
                                        break
          #serial0.flushInput()
          #print "sleep"
          time.sleep(15)
          
               
 
     #GPIO.output(11,True)
     #time.sleep(1)
     #GPIO.output(11,False)
     #time.sleep(1)