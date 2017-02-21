#imaplib gmail


import imaplib
import getpass
import email


'''
mail = imaplib.IMAP4_SSL('imap.gmail.com')
mail.login("jeffreyzcluo@gmail.com", getpass.getpass())
mail.select()
typ, data = mail.search(None, '(From "Uber Receipts")')
file=open("C:\\Users\\Jeff\\Desktop\\Spring 2017\\gmailheaders.txt","r")

#for num in data[0].split():
 #   alright, msgdata = mail.fetch(num,"(RFC822)")
  #  file.write(msgdata[0][1].decode()+"\n")


currentIndex=0
wholeFile=file.read()
splittedFile=wholeFile.split("Delivered-To")
uberFee=0
for e in splittedFile:
    curIndex=e.find("$")
    if curIndex != -1:
        splitStr=e[curIndex+1:curIndex+7].split()
        uberFee+=eval(splitStr[0])
        
print(uberFee)

mail.close()
mail.logout()
'''


mail = imaplib.IMAP4_SSL('imap.gmail.com')
mail.login("jeffreyzcluo@gmail.com", getpass.getpass())
mail.select()
typ, data = mail.search(None, '(From "Uber Receipts")','(SINCE "13-Jan-2017")')

#file=open("C:\\Users\\Jeff\\Desktop\\Spring 2017\\gmailheaders.txt","w")

uberFee=0
for num in data[0].split():
    alright, msgdata = mail.fetch(num,"(RFC822)")
    currentList=email.message_from_string(msgdata[0][1].decode())
    if currentList.is_multipart():
        for payload in currentList.get_payload():
            curMsg=payload.get_payload(decode=True)
            decodedMsg=str(curMsg)
            #file.write(decodedMsg)
            where=decodedMsg.find("$")
            if where != -1:
                splitStr=decodedMsg[where+1:where+7].split()
                uberFee+=eval(splitStr[0].strip("n").strip("\\"))
                break
        
print(uberFee)

mail.close()
mail.logout()
#file.close()

'''
mail = imaplib.IMAP4_SSL('imap.gmail.com')
mail.login("jeffreyzcluo@gmail.com", getpass.getpass())
mail.select()
typ, data = mail.search(None, '(From "Uber Receipts")')

uberFee=0
for num in data[0].split():
    alright, msgdata = mail.fetch(num,"(RFC822)")
    currentList=codecs.decode(msgdata[0][1])
    where=currentList.find("$")
    if where != -1:
        splitStr=currentList[where+1:where+7].split()
        uberFee+=eval(splitStr[0])
        
print(uberFee)

mail.close()
mail.logout()

'''
