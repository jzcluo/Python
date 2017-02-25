#imaplib gmail


import imaplib
import getpass
import email

mail = imaplib.IMAP4_SSL('imap.gmail.com')
mail.login(getpass.getusername(), getpass.getpass())
mail.select()
typ, data = mail.search(None, '(From "Uber Receipts")','(SINCE "13-Jan-2017")')

uberFee=0
for num in data[0].split():
    alright, msgdata = mail.fetch(num,"(RFC822)")
    currentList=email.message_from_string(msgdata[0][1].decode())
    if currentList.is_multipart():
        for payload in currentList.get_payload():
            curMsg=payload.get_payload(decode=True)
            decodedMsg=str(curMsg)
            where=decodedMsg.find("$")
            if where != -1:
                splitStr=decodedMsg[where+1:where+7].split()
                uberFee+=eval(splitStr[0].strip("n").strip("\\"))
                break
        
print(uberFee)

mail.close()
mail.logout()
