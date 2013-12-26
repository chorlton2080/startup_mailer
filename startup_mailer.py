# Credit to http://elinux.org/RPi_Email_IP_On_Boot_Debian
# Modified to include external IP

import urllib2
import subprocess
import smtplib
import socket
import string
from email.mime.text import MIMEText
import datetime
#import RPi.GPIO as GPIO

# leave an LED lit to show we have an IP address
#GPIO.setmode(GPIO.BCM)
#GPIO.setup(22, GPIO.OUT)
#GPIO.output(22, GPIO.HIGH)

# Change to your own account information
to = '????????@gmail.com' # enter your receiving email account here
gmail_user = '???????@gmail.com' # enter your gmail acc here to send
gmail_password = '???????????' # enter your gmail password here
smtpserver = smtplib.SMTP('smtp.gmail.com', 587)
smtpserver.ehlo()
smtpserver.starttls()
smtpserver.ehlo
smtpserver.login(gmail_user, gmail_password)
today = datetime.date.today()
ext_ip = urllib2.urlopen('http://checkip.dyndns.org').read()

# Very Linux Specific
arg='ip route list'
p=subprocess.Popen(arg,shell=True,stdout=subprocess.PIPE)
data = p.communicate()
split_data = data[0].split()
ipaddr = split_data[split_data.index('src')+1]
my_ip = 'RPiA IP: LAN  Address: %s' % ipaddr + (' External '+ ext_ip[56:91])
msg = MIMEText(my_ip)
msg['Subject'] = 'IP For RPiA on %s' % today.strftime('%b %d %Y')
msg['From'] = gmail_user
msg['To'] = to
smtpserver.sendmail(gmail_user, [to], msg.as_string())
smtpserver.quit()
