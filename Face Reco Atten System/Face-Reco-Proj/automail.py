import os
import yagmail

receiver = "reviever@gmail.com"  # receiver email address
body = "Attendence File"  # email body
filename = "Attendance"+os.sep+"Attendance_2021-04-28_11-30-16.csv"  # attach the file

# mail information
yag = yagmail.SMTP("your_gamail@gmail.com", "your_password")

# sent the mail
yag.send(
    to=receiver,
    subject="Attendance Report",  # email subject
    contents=body,  # email body
    attachments=filename,  # file attached
)
