#Importing Library
import smtplib 

#SMTP Server Address of GMAIL
sm = smtplib.SMTP('smtp.gmail.com',587)

#Starting Serivce
sm.starttls()	

#Login To Your Mail Id.
sm.login("Sender Id","Password")

#Sending Mail.
sm.sendmail("Sender Id","Recivers Id","Message")

#Stoping Serivce
sm.quit()	