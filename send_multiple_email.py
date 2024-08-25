import smtplib as s

ob = s.SMTP('smtp.gmail.com', 587)
ob.ehlo()
ob.starttls()
# write your email id and password here 
ob.login('daniyalakhtar1996@gmail.com', '')
subject="Testing mail"
body="I love Python"
massage="subject:{}\n\n{}".format(subject, body)
# need to write all email addresses where you want to send email 
listadd=['cloudseavy@gmail.com', 'info@seavycloudinc.com']
ob.sendmail('daniyalakhtar1996@gmail.com', listadd, massage)
print("Email send successfully")
ob.quit()