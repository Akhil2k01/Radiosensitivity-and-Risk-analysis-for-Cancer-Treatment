import end as e
import smtplib
from email.message import EmailMessage

#EMAIL_ADDRESS = os.environ.get('RRCT_MAIL')
#EMAIL_PASSWORD = os.environ.get('RRCT_PASS')

print("\nRunning mail.py")

EMAIL_ADDRESS = 'rrctresearchteam@gmail.com'
EMAIL_PASSWORD = 'lzpgrrxmlvnjsipv'

msg = EmailMessage()
msg['Subject'] = 'Your Final Report is Ready'
msg['From'] = EMAIL_ADDRESS
msg['To'] = e.patient_email
msg['Bcc'] = e.a.t.r.clinic_mail
id = e.id
name = e.name

msg.add_alternative(
'<h4>Dear Sir/Madam,<br><br>Patient ID : '+id+'<br>Patient Name : '+name+"""\
<!DOCTYPE html>
<html>
    <body>
        <h4>
            The report for the medical exam taken is attached herewith.<br> 
            Kindly consult the doctor for further treatment procedure. 
            We advise you to not take any medication unless its prescribed by the doctor/specialist.
            Furthermore, take care of your health and diet for recovery as per the suggestion in the report.<br><br> 
            We thank you for using our service and hope for your speedy recovery.<br>
            Wishing you good health and wellness.<br><br>Regards,<br>RRCT Team<br><br>
        </h4>
        <h5 style="color:SlateGray;">
            This is a system generated mail so please do not reply to this mail.<br>
            © RRCT Team 2023
        </h5>
    </body>
</html>
""", subtype='html')

with open('C:/Users/Dell/Desktop/final_proj/results/reports/'+e.id+'.pdf', 'rb') as attach:
    file_data = attach.read()
    file_name = e.id+'.pdf'

msg.add_attachment(file_data, maintype='application', subtype='octet-stream', filename=file_name)

with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
    smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
    smtp.send_message(msg)

print("Report has been successfully sent...\n")