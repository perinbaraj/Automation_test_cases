import json
import os
import smtplib
import mimetypes
from email.mime.multipart import MIMEMultipart
from email import encoders
from email.message import Message
from email.mime.text import MIMEText
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import datetime

driver = webdriver.Chrome(executable_path=r'ADD PATH OF CHROMEDRIVER')
driver.maximize_window()
driver.get("https://www.WEBSITE.com/")
main_page = driver.current_window_handle

#Home
elem = driver.find_element_by_xpath('/html/body/header/nav/div/div/ul/li[1]/a')
elem.click()
try:
    elemtest = driver.find_element_by_xpath('/html/body/div[1]/main/div/div/div[1]/div[1]/div[1]')
    home='Pass'
except:
    home='Fail'
    pass

#Omegha link
elem = driver.find_element_by_xpath('/html/body/div[1]/main/div/div/div[1]/div[1]/p[2]/a[1]')
elem.click()
try:
    elemtest = driver.find_element_by_xpath('/html/body/div/div/div/div[2]/div')
    omegha_link='Pass'
except:
    omegha_link='Fail'
    pass
time.sleep(15)
driver.switch_to.window(main_page)
time.sleep(10)

#Free credits
elem = driver.find_element_by_xpath('/html/body/div[1]/main/div/div/div[1]/div[1]/p[2]/a[2]')
elem.click()
try:
    elemtest = driver.find_element_by_xpath('/html/body/div/div/div/div/div[1]/div[1]/div[1]')
    free_credits='Pass'
except:
    free_credits='Fail'
    pass
time.sleep(15)
driver.switch_to.window(main_page)
time.sleep(10)

#Products
#Omegha
elem = driver.find_element_by_xpath('/html/body/header/nav/div/div/ul/li[2]/a')
elem.click()
elem = driver.find_element_by_xpath('/html/body/header/nav/div/div/ul/li[2]/div/div/div[1]/table/tbody/tr[1]/td[2]/div[1]/a')
elem.click()
try:
    elemtest = driver.find_element_by_xpath('//*[@id="iaas"]/div/div/h3')
    Omegha='Pass'
except:
    Omegha='Fail'
    pass
time.sleep(15)

#Consulting
elem = driver.find_element_by_xpath('/html/body/header/nav/div/div/ul/li[3]/a')
elem.click()
try:
    elemtest = driver.find_element_by_xpath('/html/body/div[1]/main/div/p[1]')
    Consulting='Pass'
except:
    Consulting='Fail'
    pass
time.sleep(15)

#Omegha Bridge
elem = driver.find_element_by_xpath('/html/body/header/nav/div/div/ul/li[4]/a')
elem.click()
try:
    elemtest = driver.find_element_by_xpath('/html/body/div[1]/main/form/div/p[1]')
    Bridge='Pass'
except:
    Bridge='Fail'
    pass
time.sleep(15)

#About Us
elem = driver.find_element_by_xpath('/html/body/header/nav/div/div/ul/li[5]/a')
elem.click()
try:
    elemtest = driver.find_element_by_xpath('//*[@id="section_about_us"]/div/div/h4[1]')
    About_Us='Pass'
except:
    About_Us='Fail'
    pass
time.sleep(15)

#Contact Us
elem = driver.find_element_by_xpath('/html/body/header/nav/div/div/ul/li[6]/a')
elem.click()
try:
    elemtest = driver.find_element_by_xpath('//*[@id="contact_us"]/div/div[1]/div/div[1]/h2')
    Contact_Us='Pass'
except:
    Contact_Us='Fail'
    pass
time.sleep(15)

#Privacy Policy
elem = driver.find_element_by_xpath('/html/body/footer/div/a[1]')
elem.click()
try:
    elemtest = driver.find_element_by_xpath('/html/body/div[1]/main/div/h2')
    Privacy_Policy='Pass'
except:
    Privacy_Policy='Fail'
    pass
time.sleep(15)


#terms and conditions
elem = driver.find_element_by_xpath('/html/body/footer/div/a[2]')
elem.click()
try:
    elemtest = driver.find_element_by_xpath('/html/body/div[1]/main/div/h2')
    terms_conditions='Pass'
except:
    terms_conditions='Fail'
    pass
time.sleep(15)

#closeing_driver
driver.close()

date = datetime.datetime.now()

# Email Notification
emailfrom = ""
recipients = ['']
username = ""
password = ""
html="""<table cellspacing="0" cellpadding="0" dir="ltr" border="1" style="table-layout:fixed;font-size:10pt;font-family:Arial;width:0px;border-collapse:collapse;border:none">
<colgroup><col width="58"><col width="520"><col width="69"></colgroup>
<tbody>
<tr style="height:21px">
		<td style="border:1px solid rgb(0,0,0);overflow:hidden;padding:2px 3px;vertical-align:bottom;font-size:11pt;font-weight:bold;text-align:center">S.No.</td>
		<td style="border-width:1px;border-style:solid;border-color:rgb(0,0,0) rgb(0,0,0) rgb(0,0,0) rgb(204,204,204);overflow:hidden;padding:2px 3px;vertical-align:bottom;font-size:11pt;font-weight:bold;text-align:center">Module                           </td>
		<td style="border-width:1px;border-style:solid;border-color:rgb(0,0,0) rgb(0,0,0) rgb(0,0,0) rgb(204,204,204);overflow:hidden;padding:2px 3px;vertical-align:bottom;font-size:11pt;font-weight:bold;text-align:center">Pass/Fail</td>
	</tr>
	<tr style="height:21px">
		<td style="border-width:1px;border-style:solid;border-color:rgb(204,204,204) rgb(0,0,0) rgb(0,0,0);overflow:hidden;padding:2px 3px;vertical-align:bottom;font-size:11pt;text-align:center">1</td>
		<td style="border-width:1px;border-style:solid;border-color:rgb(204,204,204) rgb(0,0,0) rgb(0,0,0) rgb(204,204,204);overflow:hidden;padding:2px 3px;vertical-align:bottom;font-size:11pt">Login</td>
		<td style="border-width:1px;border-style:solid;border-color:rgb(204,204,204) rgb(0,0,0) rgb(0,0,0) rgb(204,204,204);overflow:hidden;padding:2px 3px;vertical-align:bottom;font-size:11pt;"><center>"""+ str(home) +"""</center></td>
    </tr>
    <tr style="height:21px">
		<td style="border-width:1px;border-style:solid;border-color:rgb(204,204,204) rgb(0,0,0) rgb(0,0,0);overflow:hidden;padding:2px 3px;vertical-align:bottom;font-size:11pt;text-align:center">2</td>
		<td style="border-width:1px;border-style:solid;border-color:rgb(204,204,204) rgb(0,0,0) rgb(0,0,0) rgb(204,204,204);overflow:hidden;padding:2px 3px;vertical-align:bottom;font-size:11pt">Know more about Omegha</td>
		<td style="border-width:1px;border-style:solid;border-color:rgb(204,204,204) rgb(0,0,0) rgb(0,0,0) rgb(204,204,204);overflow:hidden;padding:2px 3px;vertical-align:bottom;font-size:11pt;"><center>"""+ str(home) +"""</center></td>
    </tr>
    <tr style="height:21px">
		<td style="border-width:1px;border-style:solid;border-color:rgb(204,204,204) rgb(0,0,0) rgb(0,0,0);overflow:hidden;padding:2px 3px;vertical-align:bottom;font-size:11pt;text-align:center">3</td>
		<td style="border-width:1px;border-style:solid;border-color:rgb(204,204,204) rgb(0,0,0) rgb(0,0,0) rgb(204,204,204);overflow:hidden;padding:2px 3px;vertical-align:bottom;font-size:11pt">Register with free credits</td>
		<td style="border-width:1px;border-style:solid;border-color:rgb(204,204,204) rgb(0,0,0) rgb(0,0,0) rgb(204,204,204);overflow:hidden;padding:2px 3px;vertical-align:bottom;font-size:11pt;"><center>"""+ str(home) +"""</center></td>
    </tr>
    <tr style="height:21px">
		<td style="border-width:1px;border-style:solid;border-color:rgb(204,204,204) rgb(0,0,0) rgb(0,0,0);overflow:hidden;padding:2px 3px;vertical-align:bottom;font-size:11pt;text-align:center">4</td>
		<td style="border-width:1px;border-style:solid;border-color:rgb(204,204,204) rgb(0,0,0) rgb(0,0,0) rgb(204,204,204);overflow:hidden;padding:2px 3px;vertical-align:bottom;font-size:11pt">Omegha Iaas</td>
		<td style="border-width:1px;border-style:solid;border-color:rgb(204,204,204) rgb(0,0,0) rgb(0,0,0) rgb(204,204,204);overflow:hidden;padding:2px 3px;vertical-align:bottom;font-size:11pt;"><center>"""+ str(Omegha) +"""</center></td>
    </tr>
    <tr style="height:21px">
		<td style="border-width:1px;border-style:solid;border-color:rgb(204,204,204) rgb(0,0,0) rgb(0,0,0);overflow:hidden;padding:2px 3px;vertical-align:bottom;font-size:11pt;text-align:center">5</td>
		<td style="border-width:1px;border-style:solid;border-color:rgb(204,204,204) rgb(0,0,0) rgb(0,0,0) rgb(204,204,204);overflow:hidden;padding:2px 3px;vertical-align:bottom;font-size:11pt">Omegha Cumulus</td>
		<td style="border-width:1px;border-style:solid;border-color:rgb(204,204,204) rgb(0,0,0) rgb(0,0,0) rgb(204,204,204);overflow:hidden;padding:2px 3px;vertical-align:bottom;font-size:11pt;"><center>"""+ str(Omegha) +"""</center></td>
    </tr>
    <tr style="height:21px">
		<td style="border-width:1px;border-style:solid;border-color:rgb(204,204,204) rgb(0,0,0) rgb(0,0,0);overflow:hidden;padding:2px 3px;vertical-align:bottom;font-size:11pt;text-align:center">6</td>
		<td style="border-width:1px;border-style:solid;border-color:rgb(204,204,204) rgb(0,0,0) rgb(0,0,0) rgb(204,204,204);overflow:hidden;padding:2px 3px;vertical-align:bottom;font-size:11pt">Vinayak</td>
		<td style="border-width:1px;border-style:solid;border-color:rgb(204,204,204) rgb(0,0,0) rgb(0,0,0) rgb(204,204,204);overflow:hidden;padding:2px 3px;vertical-align:bottom;font-size:11pt;"><center>"""+ str(Omegha) +"""</center></td>
    </tr>
    <tr style="height:21px">
		<td style="border-width:1px;border-style:solid;border-color:rgb(204,204,204) rgb(0,0,0) rgb(0,0,0);overflow:hidden;padding:2px 3px;vertical-align:bottom;font-size:11pt;text-align:center">7</td>
		<td style="border-width:1px;border-style:solid;border-color:rgb(204,204,204) rgb(0,0,0) rgb(0,0,0) rgb(204,204,204);overflow:hidden;padding:2px 3px;vertical-align:bottom;font-size:11pt">Consulting</td>
		<td style="border-width:1px;border-style:solid;border-color:rgb(204,204,204) rgb(0,0,0) rgb(0,0,0) rgb(204,204,204);overflow:hidden;padding:2px 3px;vertical-align:bottom;font-size:11pt;"><center>"""+ str(Consulting) +"""</center></td>
    </tr>
    <tr style="height:21px">
		<td style="border-width:1px;border-style:solid;border-color:rgb(204,204,204) rgb(0,0,0) rgb(0,0,0);overflow:hidden;padding:2px 3px;vertical-align:bottom;font-size:11pt;text-align:center">8</td>
		<td style="border-width:1px;border-style:solid;border-color:rgb(204,204,204) rgb(0,0,0) rgb(0,0,0) rgb(204,204,204);overflow:hidden;padding:2px 3px;vertical-align:bottom;font-size:11pt">Omegha Bridge</td>
		<td style="border-width:1px;border-style:solid;border-color:rgb(204,204,204) rgb(0,0,0) rgb(0,0,0) rgb(204,204,204);overflow:hidden;padding:2px 3px;vertical-align:bottom;font-size:11pt;"><center>"""+ str(Bridge) +"""</center></td>
    </tr>
    <tr style="height:21px">
		<td style="border-width:1px;border-style:solid;border-color:rgb(204,204,204) rgb(0,0,0) rgb(0,0,0);overflow:hidden;padding:2px 3px;vertical-align:bottom;font-size:11pt;text-align:center">9</td>
		<td style="border-width:1px;border-style:solid;border-color:rgb(204,204,204) rgb(0,0,0) rgb(0,0,0) rgb(204,204,204);overflow:hidden;padding:2px 3px;vertical-align:bottom;font-size:11pt">About Us</td>
		<td style="border-width:1px;border-style:solid;border-color:rgb(204,204,204) rgb(0,0,0) rgb(0,0,0) rgb(204,204,204);overflow:hidden;padding:2px 3px;vertical-align:bottom;font-size:11pt;"><center>"""+ str(About_Us) +"""</center></td>
    </tr>
    <tr style="height:21px">
		<td style="border-width:1px;border-style:solid;border-color:rgb(204,204,204) rgb(0,0,0) rgb(0,0,0);overflow:hidden;padding:2px 3px;vertical-align:bottom;font-size:11pt;text-align:center">10</td>
		<td style="border-width:1px;border-style:solid;border-color:rgb(204,204,204) rgb(0,0,0) rgb(0,0,0) rgb(204,204,204);overflow:hidden;padding:2px 3px;vertical-align:bottom;font-size:11pt">Contact Us</td>
		<td style="border-width:1px;border-style:solid;border-color:rgb(204,204,204) rgb(0,0,0) rgb(0,0,0) rgb(204,204,204);overflow:hidden;padding:2px 3px;vertical-align:bottom;font-size:11pt;"><center>"""+ str(Contact_Us) +"""</center></td>
    </tr>
    <tr style="height:21px">
		<td style="border-width:1px;border-style:solid;border-color:rgb(204,204,204) rgb(0,0,0) rgb(0,0,0);overflow:hidden;padding:2px 3px;vertical-align:bottom;font-size:11pt;text-align:center">11</td>
		<td style="border-width:1px;border-style:solid;border-color:rgb(204,204,204) rgb(0,0,0) rgb(0,0,0) rgb(204,204,204);overflow:hidden;padding:2px 3px;vertical-align:bottom;font-size:11pt">Privacy Polacy</td>
		<td style="border-width:1px;border-style:solid;border-color:rgb(204,204,204) rgb(0,0,0) rgb(0,0,0) rgb(204,204,204);overflow:hidden;padding:2px 3px;vertical-align:bottom;font-size:11pt;"><center>"""+ str(Privacy_Policy) +"""</center></td>
    </tr>
    <tr style="height:21px">
		<td style="border-width:1px;border-style:solid;border-color:rgb(204,204,204) rgb(0,0,0) rgb(0,0,0);overflow:hidden;padding:2px 3px;vertical-align:bottom;font-size:11pt;text-align:center">12</td>
		<td style="border-width:1px;border-style:solid;border-color:rgb(204,204,204) rgb(0,0,0) rgb(0,0,0) rgb(204,204,204);overflow:hidden;padding:2px 3px;vertical-align:bottom;font-size:11pt">Terms Conditions</td>
		<td style="border-width:1px;border-style:solid;border-color:rgb(204,204,204) rgb(0,0,0) rgb(0,0,0) rgb(204,204,204);overflow:hidden;padding:2px 3px;vertical-align:bottom;font-size:11pt;"><center>"""+ str(terms_conditions) +"""</center></td>
    </tr>
 </tbody>
 </table>"""
f = open('mail.html','w')
f.write(html)
f.close()



msg = MIMEMultipart()
msg["From"] = emailfrom
msg["To"] = ", ".join(recipients[:-1])
msg["cc"] = recipients[-1]
msg["Subject"] = "Testing Automation - """+ date.strftime("%x") +""
part2 = MIMEText(html, 'html')
msg.attach(part2)
server = smtplib.SMTP("smtp.gmail.com:587")
server.starttls()
server.login('username','password')
server.sendmail(emailfrom, recipients, msg.as_string())
server.quit()
