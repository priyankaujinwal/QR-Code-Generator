from pyqrcode import pyqrcode
reg_url = "https://docs.google.com/forms/d/e/1FAIpQLSejXNtpgKYUyX5XtNS4jrNbpmr8TJ-ShABYQ6CpGqPjxnCLhA/viewform"
url = pyqrcode.create(reg_url)
url.svg("WCSC.svg",scale=8)
print("QR Code generated successfully")
