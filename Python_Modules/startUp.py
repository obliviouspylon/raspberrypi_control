from SendGrid import sendEmail
from time import sleep, time, strftime, localtime

recipient_email =  ""
recipient_name = ""
sleep(20)
sendEmail(recipient_email,
          "RaspberryPi Restarted",
          "RaspberryPi Restarted on " + strftime('%Y-%m-%d %H:%M:%S %Z',localtime(time())),
          name)
