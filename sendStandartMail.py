import smtplib

sender = "9292mmu@gmail.com"
recipient = "mirko_@bluewin.ch"
password = "606c6cgm"  # Your SMTP password for Gmail
subject = "Test email from Python"
text = "Hello from Python"
headersMessageid = "014906859904830.1571067673.025117635726929-openerp-1-purchase.order@euedu5a.odoo.com"

smtp_server = smtplib.SMTP_SSL("smtp.gmail.com", 465)
smtp_server.login(sender, password)
message = "Subject: {}\n\n{}".format(subject, text)
smtp_server.sendmail(sender, recipient, message, headersMessageid)
smtp_server.close()
