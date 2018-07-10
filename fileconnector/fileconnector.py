import os
import time

strg=["open smb://pun-corpstrg-01","smb://isilon2.pun.stereodstaff.com","smb://isilon2.pun.stereodstaff.com/data_attachments","smb://support.pun.stereodstaff.com/data","smb://isilon2.pun.stereodstaff.com/bullpen","smb://isilon2.pun.stereodstaff.com/jobpen/projects","smb://support.tor.stereodstaff.com"]

for i in strg:
  os.system(i)
  time.sleep(5)
  print i,"-Done"
  

  