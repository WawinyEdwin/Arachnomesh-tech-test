# Required imports
from email.mime.multipart import MIMEMultipart
import smtplib



s = smtplib.SMTP(host='sample_address', port=537)
s.starttls()
s.login('defineanyaddresshere', 'yourpass')

# Initialize the sample email data
emails = [ 'ghi@hotmail.com', 'def@yahoo.com', 'ghi@gmail.com', 'abc@channelier.com', 'abc@hotmail.com', 'def@hotmail.com', 'abc@gmail.com', 'abc@yahoo.com', 'def@channelier.com', 'jkl@hotmail.com', 'ghi@yahoo.com', 'def@gmail.com']


# Our Function to send emails
def send_mail(emails):

    # Sort the addresses alphabetically
    emails.sort()

    #  Send sample email
    for email in emails:
        msg = MIMEMultipart()

        msg['From'] = 'given address'
        msg['To'] = email
        msg['Subject'] = "A sample Mail"

        s.send_message(msg)

    s.quit()
    


send_mail(emails)