import subprocess
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


driver = webdriver.Chrome(executable_path=r"ADD PATH")
driver.maximize_window()
driver.get("https://WEBSITE.com/")
time.sleep(10)
elem = driver.find_element_by_xpath('/html/body/div/div/div/div[2]/div/p[3]/a')
time.sleep(10)


#login
elem.send_keys(Keys.RETURN)
time.sleep(20)
elem = driver.find_element_by_xpath('//*[@id="EmailID"]')
elem.click()
elem.send_keys("isltest2019@gmail.com")
elem = driver.find_element_by_xpath('//*[@id="Password"]')
elem.click()
elem.send_keys("prafful123")
elem = driver.find_element_by_xpath('/html/body/div/div/div/div[2]/div/form/p/input')
elem.send_keys(Keys.RETURN)

try:
    elemtest = driver.find_element_by_xpath('//*[@id="India"]/p')
    test_login='Pass'
except:
    test_login='Fail'
    pass

#instance creation
elem = driver.find_element_by_xpath('//*[@id="wrapper"]/ul/li[2]/a')
elem.click()
#elem.send_keys(Keys.RETURN)
time.sleep(15)
elem = driver.find_element_by_xpath('//*[@id="2,Finland,Europe"]')
time.sleep(10)
elem.click()
elem = driver.find_element_by_xpath('//*[@id="35,CentOS,7,1,2"]')
elem.click()
elem = driver.find_element_by_xpath('//*[@id="15,425"]')
elem.click()
elem = driver.find_element_by_xpath('//*[@id="my_key"]')
elem.click()
elem = driver.find_element_by_xpath('//*[@id="txt_server_name"]')
elem.send_keys("test_instance")
elem = driver.find_element_by_xpath('//*[@id="content-wrapper"]/div/div[1]/div/div/form/div/p[2]/input')
elem.click()
time.sleep(15)
try:
    elemtest = driver.find_element_by_xpath('//*[@id="content-wrapper"]/div/div/div[2]/div/p')
    test_instance_creation='Pass'
except:
    test_instance_creation='Fail'
    pass

#enviornment
elem = driver.find_element_by_xpath('//*[@id="environmentDropdown"]/span')
elem.click()
time.sleep(10)
elem = driver.find_element_by_xpath('//*[@id="wrapper"]/ul/li[3]/div/a[1]/span')
elem.click()
time.sleep(20)


#instance stop
elem = driver.find_element_by_xpath('//*[@id="btn_instance_action"]')
elem.click()
time.sleep(15)
elem = driver.find_element_by_xpath('//*[@id="DataTables_Table_0"]/tbody/tr/td[9]/div/div/form/input[5]')
elem.click()

try:
    elemtest = driver.find_element_by_xpath('//*[@id="div_page_success"]/span[2]')
    test_instance_stop='Pass'
except:
    test_instance_stop='Fail'
    pass
time.sleep(90)


#instance start
elem = driver.find_element_by_xpath('//*[@id="btn_instance_action"]')
elem.click()
time.sleep(10)
elem = driver.find_element_by_xpath('//*[@id="DataTables_Table_0"]/tbody/tr/td[9]/div/div/form/input[5]')
elem.click()

try:
    elemtest = driver.find_element_by_xpath('//*[@id="div_page_success"]/span[2]')
    test_instance_start='Pass'
except:
    test_instance_start='Fail'
    pass
time.sleep(20)


#instance reboot
elem = driver.find_element_by_xpath('//*[@id="btn_instance_action"]')
elem.click()
time.sleep(10)
elem = driver.find_element_by_xpath('//*[@id="DataTables_Table_0"]/tbody/tr/td[9]/div/div/form/input[6]')
elem.click()

try:
    elemtest = driver.find_element_by_xpath('//*[@id="div_page_success"]/span[2]')
    test_instance_reboot='Pass'
except:
    test_instance_reboot='Fail'
    pass
time.sleep(20)


#instance launch
elem = driver.find_element_by_xpath('//*[@id="btn_instance_action"]')
elem.click()
time.sleep(10)
elem = driver.find_element_by_xpath('//*[@id="DataTables_Table_0"]/tbody/tr/td[9]/div/div/form/input[8]')
elem.click()

try:
    elemtest = driver.find_element_by_xpath('//*[@id="btn_back"]')
    test_instance_launch='Pass'
except:
    test_instance_launch='Fail'
    pass
time.sleep(15)


#instance deletion
elem = driver.find_element_by_xpath('//*[@id="btn_back"]')
elem.click()
time.sleep(15)

elem = driver.find_element_by_xpath('//*[@id="btn_instance_action"]')
elem.click()

elem = driver.find_element_by_xpath('//*[@id="DataTables_Table_0"]/tbody/tr/td[9]/div/div/form/input[7]')
elem.click()

try:
    elemtest = driver.find_element_by_xpath('//*[@id="div_page_success"]/span[2]')
    test_instance_deletion='Pass'
except:
    test_instance_deletion='Fail'
    pass
time.sleep(15)


#INSTANCE QUOTA
elem = driver.find_element_by_xpath('//*[@id="environmentDropdown"]')
elem.click()
elem = driver.find_element_by_xpath('//*[@id="wrapper"]/ul/li[3]/div/a[2]/span')
elem.click()
time.sleep(15)

elem = driver.find_element_by_xpath('//*[@id="instancequotarequest"]')
elem.send_keys("2")

elem = driver.find_element_by_xpath('//*[@id="instancequotarequestdesc"]')
elem.send_keys("for testing")

elem = driver.find_element_by_xpath('//*[@id="content-wrapper"]/div/div/div[2]/div/form/table/tbody/tr[3]/td/input')
elem.click()

try:
    elemtest = driver.find_element_by_xpath('//*[@id="div_page_success"]/span[2]')
    test_instance_quota='Pass'
except:
    test_instance_quota='Fail'
    pass
time.sleep(20)


#Billing
#Current Billing
elem = driver.find_element_by_xpath('//*[@id="billingDropdown"]')
elem.click()
elem = driver.find_element_by_xpath('//*[@id="wrapper"]/ul/li[4]/div/a[1]/span')
elem.click()
time.sleep(15)
try:
    elemtest = driver.find_element_by_xpath('//*[@id="content-wrapper"]/div/div/div[2]/p')
    test_billing='Pass'
except:
    test_billing='Fail'
    pass
time.sleep(20)


#Billing Invoice
elem = driver.find_element_by_xpath('//*[@id="billingDropdown"]')
elem.click()
elem = driver.find_element_by_xpath('//*[@id="wrapper"]/ul/li[4]/div/a[2]/span')
elem.click()
time.sleep(15)
try:
    elemtest = driver.find_element_by_xpath('//*[@id="content-wrapper"]/div/div/div/p')
    test_billing_invoice='Pass'
except:
    test_billing_invoice='Fail'
    pass
time.sleep(20)


#Billing History
elem = driver.find_element_by_xpath('//*[@id="billingDropdown"]')
elem.click()
elem = driver.find_element_by_xpath('//*[@id="wrapper"]/ul/li[4]/div/a[3]/span')
elem.click()
time.sleep(15)
try:
    elemtest = driver.find_element_by_xpath('//*[@id="content-wrapper"]/div/div/div[2]/p')
    test_billing_history='Pass'
except:
    test_billing_history='Fail'
    pass
time.sleep(20)


#Billing setup
elem = driver.find_element_by_xpath('//*[@id="billingDropdown"]')
elem.click()
elem = driver.find_element_by_xpath('//*[@id="wrapper"]/ul/li[4]/div/a[4]/span')
elem.click()
time.sleep(15)

elem = driver.find_element_by_xpath('//*[@id="billingname"]')
elem.send_keys("tester_Master")
elem = driver.find_element_by_xpath('//*[@id="billingaddress"]')
elem.send_keys("Infrastacklabs_HQ")
elem = driver.find_element_by_xpath('//*[@id="billingcity"]')
elem.send_keys("Bengaluru")
elem = driver.find_element_by_xpath('//*[@id="billingstate"]')
elem.send_keys("Karnataka")
elem = driver.find_element_by_xpath('//*[@id="billingpostcode"]')
elem.send_keys("560068")
elem = driver.find_element_by_xpath('//*[@id="billingcountry"]')
elem.send_keys("India")

elem = driver.find_element_by_xpath('//*[@id="frm_billing_address"]/p/input')
elem.click()
time.sleep(15)

try:
    elemtest = driver.find_element_by_xpath('//*[@id="div_page_success"]/span[2]')
    test_billing_address='Pass'
except:
    test_billing_address='Fail'
    pass
time.sleep(20)




#Creating instance for further testing
elem = driver.find_element_by_xpath('//*[@id="wrapper"]/ul/li[2]/a/span')
elem.click()
"""
elem = driver.find_element_by_xpath('//*[@id="wrapper"]/ul/li[2]/a')
elem.send_keys(Keys.RETURN)
time.sleep(15)
"""
elem = driver.find_element_by_xpath('//*[@id="2,Finland,Europe"]')
elem.click()

elem = driver.find_element_by_xpath('//*[@id="35,CentOS,7,1,2"]')
elem.click()
elem = driver.find_element_by_xpath('//*[@id="15,425"]')
elem.click()
elem = driver.find_element_by_xpath('//*[@id="my_key"]')
elem.click()

elem = driver.find_element_by_xpath('//*[@id="txt_server_name"]')
elem.send_keys("1_test_instance")

elem = driver.find_element_by_xpath('//*[@id="content-wrapper"]/div/div[1]/div/div/form/div/p[2]/input')
elem.click()
time.sleep(15)


#Volume
#Volume Creation
elem = driver.find_element_by_xpath('//*[@id="volumeDropdown"]/span')
elem.click()
elem = driver.find_element_by_xpath('//*[@id="wrapper"]/ul/li[5]/div/a[1]/span')
elem.click()

elem = driver.find_element_by_xpath('//*[@id="volumename"]')
elem.send_keys("Volume_Creation_testing")
elem = driver.find_element_by_xpath('//*[@id="content-wrapper"]/div/div/div[2]/div/form/p/input')
elem.click()

try:
    elemtest = driver.find_element_by_xpath('//*[@id="div_page_success"]/span[2]')
    test_volume_creation='Pass'
except:
    test_volume_creation='Fail'
    pass
time.sleep(20)




#Snapshot
elem = driver.find_element_by_xpath('//*[@id="snapshotDropdown"]')
elem.click()
elem = driver.find_element_by_xpath('//*[@id="wrapper"]/ul/li[6]/div/a[1]/span')
elem.click()
time.sleep(20)
#Instance Snapshot

elem = driver.find_element_by_xpath('//*[@id="snapshotname"]')
elem.send_keys("Instance_Screenshot")
elem = driver.find_element_by_xpath('//*[@id="content-wrapper"]/div/div/div[1]/div/form/p/input')
elem.click()

try:
    elemtest = driver.find_element_by_xpath('//*[@id="div_page_success"]/span[2]')
    ss_instance='Pass'
except:
    ss_instance='Fail'
    pass
time.sleep(20)


#Creation of Instance using Snapshot
elem = driver.find_element_by_xpath('//*[@id="btn_tag"]')
elem.click()
elem = driver.find_element_by_xpath('//*[@id="instancename"]')
elem.send_keys("Instance_Using_Screenshot")
elem = driver.find_element_by_xpath('//*[@id="DataTables_Table_0"]/tbody/tr/td[5]/div/form/div/input[2]')
elem.click()

try:
    elemtest = driver.find_element_by_xpath('//*[@id="div_page_success"]/span[2]')
    ss_instance_creation='Pass'
except:
    ss_instance_creation='Fail'
    pass
time.sleep(20)


#Deletion of Snapshot
elem = driver.find_element_by_xpath('//*[@id="snapshotDropdown"]')
elem.click()
elem = driver.find_element_by_xpath('//*[@id="wrapper"]/ul/li[6]/div/a[1]/span')
elem.click()

time.sleep(15)

elem = driver.find_element_by_xpath('//*[@id="DataTables_Table_0"]/tbody/tr/td[6]/form/input[6]')
elem.click()

try:
    elemtest = driver.find_element_by_xpath('//*[@id="div_page_success"]/span[2]')
    ss_deletion='Pass'
except:
    ss_deletion='Fail'
    pass
time.sleep(20)


#Volume Snapshot
elem = driver.find_element_by_xpath('//*[@id="snapshotDropdown"]')
elem.click()
elem = driver.find_element_by_xpath('//*[@id="wrapper"]/ul/li[6]/div/a[2]/span')
elem.click()
time.sleep(20)

elem = driver.find_element_by_xpath('//*[@id="snapshotname"]')
elem.send_keys("Volume_Screenshot")
elem = driver.find_element_by_xpath('//*[@id="content-wrapper"]/div/div/div[1]/div/form/p/input')
elem.click()

try:
    elemtest = driver.find_element_by_xpath('//*[@id="div_page_success"]/span[2]')
    ss_volume='Pass'
except:
    ss_volume='Fail'
    pass
time.sleep(20)


#Creation of Volume Using Snapshot
elem = driver.find_element_by_xpath('//*[@id="btn_tag"]')
elem.click()
elem = driver.find_element_by_xpath('//*[@id="volumename"]')
elem.send_keys("Volume_Using_Screenshot")
elem = driver.find_element_by_xpath('//*[@id="DataTables_Table_0"]/tbody/tr[1]/td[5]/div/div/input')
elem.click()

try:
    elemtest = driver.find_element_by_xpath('//*[@id="div_page_success"]/span[2]')
    ss_volume_creation='Pass'
except:
    ss_volume_creation='Fail'
    pass
time.sleep(20)


#Deletion of Volume Snapshot
elem = driver.find_element_by_xpath('//*[@id="snapshotDropdown"]')
elem.click()
elem = driver.find_element_by_xpath('//*[@id="wrapper"]/ul/li[6]/div/a[2]/span')
elem.click()
time.sleep(15)
elem = driver.find_element_by_xpath('//*[@id="DataTables_Table_0"]/tbody/tr[1]/td[6]/input[3]')
elem.click()
time.sleep(10)

try:
    elemtest = driver.find_element_by_xpath('//*[@id="div_page_success"]/span[2]')
    ss_volume_deletion='Pass'
except:
    ss_volume_deletion='Fail'
    pass
time.sleep(20)

#IP allocation
elem = driver.find_element_by_xpath('//*[@id="networkDropdown"]')
elem.click()
elem = driver.find_element_by_xpath('//*[@id="wrapper"]/ul/li[7]/div/a[1]/span')
elem.click()

time.sleep(15)
elem = driver.find_element_by_xpath('//*[@id="content-wrapper"]/div/div/div[1]/div/form/p/input')
elem.click()

try:
    elemtest = driver.find_element_by_xpath('//*[@id="div_page_success"]/span[2]')
    IP_allocation='Pass'
except:
    IP_allocation='No IP available'
    pass
time.sleep(20)

#Terminating all Tested Instances
elem = driver.find_element_by_xpath('//*[@id="environmentDropdown"]/span')
elem.click()
elem = driver.find_element_by_xpath('//*[@id="wrapper"]/ul/li[3]/div/a[1]/span')
elem.click()

time.sleep(10)

elem = driver.find_element_by_xpath('//*[@id="btn_instance_action"]')
elem.click()
elem = driver.find_element_by_xpath('//*[@id="DataTables_Table_0"]/tbody/tr[1]/td[9]/div/div/form/input[7]')
elem.click()

time.sleep(20)

elem = driver.find_element_by_xpath('//*[@id="btn_instance_action"]')
elem.click()
elem = driver.find_element_by_xpath('//*[@id="DataTables_Table_0"]/tbody/tr[1]/td[9]/div/div/form/input[7]')
elem.click()

time.sleep(20)

try:
    elemtest = driver.find_element_by_xpath('//*[@id="div_page_success"]/span[2]')
    deletion_of_tested_instances='Pass'
except:
    deletion_of_tested_instances='Fail'
    pass
time.sleep(15)

#Deallocating IP from Project
elem = driver.find_element_by_xpath('//*[@id="networkDropdown"]/span')
elem.click()
elem = driver.find_element_by_xpath('//*[@id="wrapper"]/ul/li[7]/div/a[1]/span')
elem.click()

time.sleep(10)

try:
    elemtest = driver.find_element_by_xpath('/html/body/div[2]/div[2]/div/div/div[2]/div/table/tbody/tr[1]/td[7]/div/a')
    elemtest.click()
except:
    pass

try:
    elemtest = driver.find_element_by_xpath('/html/body/div[2]/div[2]/div/div/div[2]/div/table/tbody/tr[1]/td[7]/div/div/form/p/input')
    elemtest.click()
except:
    pass

try:
    elemtest = driver.find_element_by_xpath('//*[@id="div_page_success"]/span[2]')
    Deallocation_of_IP_after_Testing='Pass'
except:
    Deallocation_of_IP_after_Testing='Fail'
    pass

time.sleep(20)
"""
#Terminating Tested Volumes
elem = driver.find_element_by_xpath('//*[@id="volumeDropdown"]/span')
elem.click()
elem = driver.find_element_by_xpath('//*[@id="wrapper"]/ul/li[5]/div/a[2]/span')
elem.click()

def expand_shadow_element(element):
    shadow_root = driver.execute_script('return arguments[0].shadowRoot', element)
    return shadow_root

"""
driver.execute_script("window.open('');")
driver.switch_to.window(driver.window_handles[1])
driver.get('chrome://settings/')

root=driver.find_element_by_xpath("*//settings-ui")
shadow_root = expand_shadow_element(root)
container= shadow_root.find_element_by_id("container")

root= container.find_element_by_css_selector("settings-main")
shadow_root = expand_shadow_element(root)

root=shadow_root.find_element_by_css_selector("settings-basic-page")

shadow_root = expand_shadow_element(root)
basic_page = shadow_root.find_element_by_id("basicPage")

settings_section= basic_page.find_element_by_xpath(".//settings-section[@section='appearance']")

root= settings_section.find_element_by_css_selector("settings-appearance-page")
shadow_root=expand_shadow_element(root)

settings_animated_pages= shadow_root.find_element_by_id("pages")


zoomLevel= settings_animated_pages.find_element_by_xpath(".//select[@id='zoomLevel']/option[@value='0.5']")
zoomLevel.click()

driver.switch_to.window(driver.window_handles[0])

time.sleep(10)


elem = driver.find_element_by_xpath('//*[@id="DataTables_Table_0"]/tbody/tr/td[8]/form/input[2]')
driver.execute_script("arguments[0].click();", elem)

try:
    elemtest = driver.find_element_by_xpath('//*[@id="div_page_success"]/span[2]')
    Deletion_of_tested_volume='Pass'
except:
    Deletion_of_tested_volume='Fail'
    pass

time.sleep(30)
"""
driver.get('chrome://settings/')

root=driver.find_element_by_xpath("*//settings-ui")
shadow_root = expand_shadow_element(root)
container= shadow_root.find_element_by_id("container")

root= container.find_element_by_css_selector("settings-main")
shadow_root = expand_shadow_element(root)

root=shadow_root.find_element_by_css_selector("settings-basic-page")

shadow_root = expand_shadow_element(root)
basic_page = shadow_root.find_element_by_id("basicPage")

settings_section= basic_page.find_element_by_xpath(".//settings-section[@section='appearance']")

root= settings_section.find_element_by_css_selector("settings-appearance-page")
shadow_root=expand_shadow_element(root)

settings_animated_pages= shadow_root.find_element_by_id("pages")


zoomLevel= settings_animated_pages.find_element_by_xpath(".//select[@id='zoomLevel']/option[@value='1']")
zoomLevel.click()
"""
#Closing Settings Tab
driver.close()

date = datetime.datetime.now()

# Email Notification
# Email Notification
emailfrom = ""
recipients = ['','']
username = ""
password = ""

html="""<table cellspacing="0" cellpadding="0" dir="ltr" border="1" style="table-layout:fixed;font-size:10pt;font-family:Arial;width:0px;border-collapse:collapse;border:none">
<colgroup><col width="48"><col width="58"><col width="124"><col width="520"><col width="69"></colgroup>
<tbody>
	<tr style="height:21px">
		<td style="border:1px solid rgb(0,0,0);overflow:hidden;padding:2px 3px;vertical-align:bottom;font-size:11pt;font-weight:bold;text-align:center">S.No.</td>
		<td style="border-width:1px;border-style:solid;border-color:rgb(0,0,0) rgb(0,0,0) rgb(0,0,0) rgb(204,204,204);overflow:hidden;padding:2px 3px;vertical-align:bottom;font-size:11pt;font-weight:bold;text-align:center">Priority</td>
		<td style="border-width:1px;border-style:solid;border-color:rgb(0,0,0) rgb(0,0,0) rgb(0,0,0) rgb(204,204,204);overflow:hidden;padding:2px 3px;vertical-align:bottom;font-size:11pt;font-weight:bold;text-align:center">Module</td>
		<td style="border-width:1px;border-style:solid;border-color:rgb(0,0,0) rgb(0,0,0) rgb(0,0,0) rgb(204,204,204);overflow:hidden;padding:2px 3px;vertical-align:bottom;font-size:11pt;font-weight:bold;text-align:center">To be tested</td>
		<td style="border-width:1px;border-style:solid;border-color:rgb(0,0,0) rgb(0,0,0) rgb(0,0,0) rgb(204,204,204);overflow:hidden;padding:2px 3px;vertical-align:bottom;font-size:11pt;font-weight:bold;text-align:center">Pass/Fail</td>
	</tr>
	<tr style="height:21px">
		<td style="border-width:1px;border-style:solid;border-color:rgb(204,204,204) rgb(0,0,0) rgb(0,0,0);overflow:hidden;padding:2px 3px;vertical-align:bottom;font-size:11pt;text-align:center">1</td>
		<td style="border-width:1px;border-style:solid;border-color:rgb(204,204,204) rgb(0,0,0) rgb(0,0,0) rgb(204,204,204);overflow:hidden;padding:2px 3px;vertical-align:bottom;font-size:11pt;text-align:center">High</td>
		<td style="border-width:1px;border-style:solid;border-color:rgb(204,204,204) rgb(0,0,0) rgb(0,0,0) rgb(204,204,204);overflow:hidden;padding:2px 3px;vertical-align:bottom;font-size:11pt">Login</td>
		<td style="border-width:1px;border-style:solid;border-color:rgb(204,204,204) rgb(0,0,0) rgb(0,0,0) rgb(204,204,204);overflow:hidden;padding:2px 3px;vertical-align:bottom;font-size:11pt">Login with email id and password,
		should direct to dashboard.</td>
		<td style="border-width:1px;border-style:solid;border-color:rgb(204,204,204) rgb(0,0,0) rgb(0,0,0) rgb(204,204,204);overflow:hidden;padding:2px 3px;vertical-align:bottom;font-size:11pt;"><center>"""+ str(test_login) +"""</center></td>
    </tr>
    <tr style="height:21px">
        <td style="border-width:1px;border-style:solid;border-color:rgb(204,204,204) rgb(0,0,0) rgb(0,0,0);overflow:hidden;padding:2px 3px;vertical-align:bottom;font-size:11pt;text-align:center">2</td>
        <td style="border-width:1px;border-style:solid;border-color:rgb(204,204,204) rgb(0,0,0) rgb(0,0,0) rgb(204,204,204);overflow:hidden;padding:2px 3px;vertical-align:bottom;font-size:11pt;text-align:center">High</td>
        <td style="border-width:1px;border-style:solid;border-color:rgb(204,204,204) rgb(0,0,0) rgb(0,0,0) rgb(204,204,204);overflow:hidden;padding:2px 3px;vertical-align:bottom;font-size:11pt">Wizard</td>
        <td style="border-width:1px;border-style:solid;border-color:rgb(204,204,204) rgb(0,0,0) rgb(0,0,0) rgb(204,204,204);overflow:hidden;padding:2px 3px;vertical-align:bottom;font-size:11pt">Create an Instances,
        and should show success page </td>
        <td style="border-width:1px;border-style:solid;border-color:rgb(204,204,204) rgb(0,0,0) rgb(0,0,0) rgb(204,204,204);overflow:hidden;padding:2px 3px;vertical-align:bottom;font-size:11pt"><center>"""+ str(test_instance_creation) +"""</center></td>
    </tr>
    <tr style="height:21px">
        <td style="border-width:1px;border-style:solid;border-color:rgb(204,204,204) rgb(0,0,0) rgb(0,0,0);overflow:hidden;padding:2px 3px;vertical-align:bottom;font-size:11pt;text-align:center">3</td>
        <td style="border-width:1px;border-style:solid;border-color:rgb(204,204,204) rgb(0,0,0) rgb(0,0,0) rgb(204,204,204);overflow:hidden;padding:2px 3px;vertical-align:bottom;font-size:11pt;text-align:center">High</td>
        <td style="border-width:1px;border-style:solid;border-color:rgb(204,204,204) rgb(0,0,0) rgb(0,0,0) rgb(204,204,204);overflow:hidden;padding:2px 3px;vertical-align:bottom;font-size:11pt">Environment</td>
        <td style="border-width:1px;border-style:solid;border-color:rgb(204,204,204) rgb(0,0,0) rgb(0,0,0) rgb(204,204,204);overflow:hidden;padding:2px 3px;vertical-align:bottom;font-size:11pt">Check for stoping of instance </td>
        <td style="border-width:1px;border-style:solid;border-color:rgb(204,204,204) rgb(0,0,0) rgb(0,0,0) rgb(204,204,204);overflow:hidden;padding:2px 3px;vertical-align:bottom;font-size:11pt"><center>"""+ str(test_instance_stop) +"""</center></td>
    </tr>
    <tr style="height:21px">
        <td style="border-width:1px;border-style:solid;border-color:rgb(204,204,204) rgb(0,0,0) rgb(0,0,0);overflow:hidden;padding:2px 3px;vertical-align:bottom;font-size:11pt;text-align:center">4</td>
        <td style="border-width:1px;border-style:solid;border-color:rgb(204,204,204) rgb(0,0,0) rgb(0,0,0) rgb(204,204,204);overflow:hidden;padding:2px 3px;vertical-align:bottom;font-size:11pt;text-align:center">High</td>
        <td style="border-width:1px;border-style:solid;border-color:rgb(204,204,204) rgb(0,0,0) rgb(0,0,0) rgb(204,204,204);overflow:hidden;padding:2px 3px;vertical-align:bottom;font-size:11pt">Environment</td>
        <td style="border-width:1px;border-style:solid;border-color:rgb(204,204,204) rgb(0,0,0) rgb(0,0,0) rgb(204,204,204);overflow:hidden;padding:2px 3px;vertical-align:bottom;font-size:11pt">Check for starting of instance </td>
        <td style="border-width:1px;border-style:solid;border-color:rgb(204,204,204) rgb(0,0,0) rgb(0,0,0) rgb(204,204,204);overflow:hidden;padding:2px 3px;vertical-align:bottom;font-size:11pt"><center>"""+ str(test_instance_start) +"""</center></td>
    </tr>
    <tr style="height:21px">
        <td style="border-width:1px;border-style:solid;border-color:rgb(204,204,204) rgb(0,0,0) rgb(0,0,0);overflow:hidden;padding:2px 3px;vertical-align:bottom;font-size:11pt;text-align:center">5</td>
        <td style="border-width:1px;border-style:solid;border-color:rgb(204,204,204) rgb(0,0,0) rgb(0,0,0) rgb(204,204,204);overflow:hidden;padding:2px 3px;vertical-align:bottom;font-size:11pt;text-align:center">High</td>
        <td style="border-width:1px;border-style:solid;border-color:rgb(204,204,204) rgb(0,0,0) rgb(0,0,0) rgb(204,204,204);overflow:hidden;padding:2px 3px;vertical-align:bottom;font-size:11pt">Environment</td>
        <td style="border-width:1px;border-style:solid;border-color:rgb(204,204,204) rgb(0,0,0) rgb(0,0,0) rgb(204,204,204);overflow:hidden;padding:2px 3px;vertical-align:bottom;font-size:11pt">Check for reboot of instance </td>
        <td style="border-width:1px;border-style:solid;border-color:rgb(204,204,204) rgb(0,0,0) rgb(0,0,0) rgb(204,204,204);overflow:hidden;padding:2px 3px;vertical-align:bottom;font-size:11pt"><center>"""+ str(test_instance_reboot) +"""</center></td>
    </tr>
    <tr style="height:21px">
        <td style="border-width:1px;border-style:solid;border-color:rgb(204,204,204) rgb(0,0,0) rgb(0,0,0);overflow:hidden;padding:2px 3px;vertical-align:bottom;font-size:11pt;text-align:center">6</td>
        <td style="border-width:1px;border-style:solid;border-color:rgb(204,204,204) rgb(0,0,0) rgb(0,0,0) rgb(204,204,204);overflow:hidden;padding:2px 3px;vertical-align:bottom;font-size:11pt;text-align:center">High</td>
        <td style="border-width:1px;border-style:solid;border-color:rgb(204,204,204) rgb(0,0,0) rgb(0,0,0) rgb(204,204,204);overflow:hidden;padding:2px 3px;vertical-align:bottom;font-size:11pt">Environment</td>
        <td style="border-width:1px;border-style:solid;border-color:rgb(204,204,204) rgb(0,0,0) rgb(0,0,0) rgb(204,204,204);overflow:hidden;padding:2px 3px;vertical-align:bottom;font-size:11pt">Check for Deletion of instance </td>
        <td style="border-width:1px;border-style:solid;border-color:rgb(204,204,204) rgb(0,0,0) rgb(0,0,0) rgb(204,204,204);overflow:hidden;padding:2px 3px;vertical-align:bottom;font-size:11pt"><center>"""+ str(test_instance_launch) +"""</center></td>
    </tr>
    <tr style="height:21px">
        <td style="border-width:1px;border-style:solid;border-color:rgb(204,204,204) rgb(0,0,0) rgb(0,0,0);overflow:hidden;padding:2px 3px;vertical-align:bottom;font-size:11pt;text-align:center">7</td>
        <td style="border-width:1px;border-style:solid;border-color:rgb(204,204,204) rgb(0,0,0) rgb(0,0,0) rgb(204,204,204);overflow:hidden;padding:2px 3px;vertical-align:bottom;font-size:11pt;text-align:center">High</td>
        <td style="border-width:1px;border-style:solid;border-color:rgb(204,204,204) rgb(0,0,0) rgb(0,0,0) rgb(204,204,204);overflow:hidden;padding:2px 3px;vertical-align:bottom;font-size:11pt">Environment</td>
        <td style="border-width:1px;border-style:solid;border-color:rgb(204,204,204) rgb(0,0,0) rgb(0,0,0) rgb(204,204,204);overflow:hidden;padding:2px 3px;vertical-align:bottom;font-size:11pt">Check for Deletion of instance </td>
        <td style="border-width:1px;border-style:solid;border-color:rgb(204,204,204) rgb(0,0,0) rgb(0,0,0) rgb(204,204,204);overflow:hidden;padding:2px 3px;vertical-align:bottom;font-size:11pt"><center>"""+ str(test_instance_deletion) +"""</center></td>
    </tr>
    <tr style="height:21px">
        <td style="border-width:1px;border-style:solid;border-color:rgb(204,204,204) rgb(0,0,0) rgb(0,0,0);overflow:hidden;padding:2px 3px;vertical-align:bottom;font-size:11pt;text-align:center">8</td>
        <td style="border-width:1px;border-style:solid;border-color:rgb(204,204,204) rgb(0,0,0) rgb(0,0,0) rgb(204,204,204);overflow:hidden;padding:2px 3px;vertical-align:bottom;font-size:11pt;text-align:center">Normal</td>
        <td style="border-width:1px;border-style:solid;border-color:rgb(204,204,204) rgb(0,0,0) rgb(0,0,0) rgb(204,204,204);overflow:hidden;padding:2px 3px;vertical-align:bottom;font-size:11pt">Environment</td>
        <td style="border-width:1px;border-style:solid;border-color:rgb(204,204,204) rgb(0,0,0) rgb(0,0,0) rgb(204,204,204);overflow:hidden;padding:2px 3px;vertical-align:bottom;font-size:11pt">Quota,
        Raise and request and check</td>
        <td style="border-width:1px;border-style:solid;border-color:rgb(204,204,204) rgb(0,0,0) rgb(0,0,0) rgb(204,204,204);overflow:hidden;padding:2px 3px;vertical-align:bottom;font-size:11pt"><center>"""+ str(test_instance_quota) +"""</center></td>
    </tr>
    <tr style="height:21px">
        <td style="border-width:1px;border-style:solid;border-color:rgb(204,204,204) rgb(0,0,0) rgb(0,0,0);overflow:hidden;padding:2px 3px;vertical-align:bottom;font-size:11pt;text-align:center">9</td>
        <td style="border-width:1px;border-style:solid;border-color:rgb(204,204,204) rgb(0,0,0) rgb(0,0,0) rgb(204,204,204);overflow:hidden;padding:2px 3px;vertical-align:bottom;font-size:11pt;text-align:center">Normal</td>
        <td style="border-width:1px;border-style:solid;border-color:rgb(204,204,204) rgb(0,0,0) rgb(0,0,0) rgb(204,204,204);overflow:hidden;padding:2px 3px;vertical-align:bottom;font-size:11pt">Billing</td>
        <td style="border-width:1px;border-style:solid;border-color:rgb(204,204,204) rgb(0,0,0) rgb(0,0,0) rgb(204,204,204);overflow:hidden;padding:2px 3px;vertical-align:bottom;font-size:11pt">Current Billing,
        should show the current usage value.</td>
        <td style="border-width:1px;border-style:solid;border-color:rgb(204,204,204) rgb(0,0,0) rgb(0,0,0) rgb(204,204,204);overflow:hidden;padding:2px 3px;vertical-align:bottom;font-size:11pt"><center>"""+ str(test_billing) +"""</center></td>
    </tr>
    <tr style="height:21px">
        <td style="border-width:1px;border-style:solid;border-color:rgb(204,204,204) rgb(0,0,0) rgb(0,0,0);overflow:hidden;padding:2px 3px;vertical-align:bottom;font-size:11pt;text-align:center">10</td>
        <td style="border-width:1px;border-style:solid;border-color:rgb(204,204,204) rgb(0,0,0) rgb(0,0,0) rgb(204,204,204);overflow:hidden;padding:2px 3px;vertical-align:bottom;font-size:11pt;text-align:center">High</td>
        <td style="border-width:1px;border-style:solid;border-color:rgb(204,204,204) rgb(0,0,0) rgb(0,0,0) rgb(204,204,204);overflow:hidden;padding:2px 3px;vertical-align:bottom;font-size:11pt">Billing</td>
        <td style="border-width:1px;border-style:solid;border-color:rgb(204,204,204) rgb(0,0,0) rgb(0,0,0) rgb(204,204,204);overflow:hidden;padding:2px 3px;vertical-align:bottom;font-size:11pt">Invoice schedule,check view invoice &amp;Pay
        </td>
        <td style="border-width:1px;border-style:solid;border-color:rgb(204,204,204) rgb(0,0,0) rgb(0,0,0) rgb(204,204,204);overflow:hidden;padding:2px 3px;vertical-align:bottom;font-size:11pt"><center>"""+ str(test_billing_invoice) +"""</center></td>
    </tr>
    <tr style="height:21px">
        <td style="border-width:1px;border-style:solid;border-color:rgb(204,204,204) rgb(0,0,0) rgb(0,0,0);overflow:hidden;padding:2px 3px;vertical-align:bottom;font-size:11pt;text-align:center">11</td>
        <td style="border-width:1px;border-style:solid;border-color:rgb(204,204,204) rgb(0,0,0) rgb(0,0,0) rgb(204,204,204);overflow:hidden;padding:2px 3px;vertical-align:bottom;font-size:11pt;text-align:center">Normal</td>
        <td style="border-width:1px;border-style:solid;border-color:rgb(204,204,204) rgb(0,0,0) rgb(0,0,0) rgb(204,204,204);overflow:hidden;padding:2px 3px;vertical-align:bottom;font-size:11pt">Billing</td>
        <td style="border-width:1px;border-style:solid;border-color:rgb(204,204,204) rgb(0,0,0) rgb(0,0,0) rgb(204,204,204);overflow:hidden;padding:2px 3px;vertical-align:bottom;font-size:11pt">Payment history,should show if any payments is done</td>
        <td style="border-width:1px;border-style:solid;border-color:rgb(204,204,204) rgb(0,0,0) rgb(0,0,0) rgb(204,204,204);overflow:hidden;padding:2px 3px;vertical-align:bottom;font-size:11pt"><center>"""+ str(test_billing_history) +"""</center></td>
    </tr>
    <tr style="height:21px">
        <td style="border-width:1px;border-style:solid;border-color:rgb(204,204,204) rgb(0,0,0) rgb(0,0,0);overflow:hidden;padding:2px 3px;vertical-align:bottom;font-size:11pt;text-align:center">12</td>
        <td style="border-width:1px;border-style:solid;border-color:rgb(204,204,204) rgb(0,0,0) rgb(0,0,0) rgb(204,204,204);overflow:hidden;padding:2px 3px;vertical-align:bottom;font-size:11pt;text-align:center">Normal</td>
        <td style="border-width:1px;border-style:solid;border-color:rgb(204,204,204) rgb(0,0,0) rgb(0,0,0) rgb(204,204,204);overflow:hidden;padding:2px 3px;vertical-align:bottom;font-size:11pt">Billing</td>
        <td style="border-width:1px;border-style:solid;border-color:rgb(204,204,204) rgb(0,0,0) rgb(0,0,0) rgb(204,204,204);overflow:hidden;padding:2px 3px;vertical-align:bottom;font-size:11pt">Billing address,
        Update billing address</td>
        <td style="border-width:1px;border-style:solid;border-color:rgb(204,204,204) rgb(0,0,0) rgb(0,0,0) rgb(204,204,204);overflow:hidden;padding:2px 3px;vertical-align:bottom;font-size:11pt"><center>"""+ str(test_billing_address) +"""</center></td>
    </tr>
    <tr style="height:21px">
        <td style="border-width:1px;border-style:solid;border-color:rgb(204,204,204) rgb(0,0,0) rgb(0,0,0);overflow:hidden;padding:2px 3px;vertical-align:bottom;font-size:11pt;text-align:center">14</td>
        <td style="border-width:1px;border-style:solid;border-color:rgb(204,204,204) rgb(0,0,0) rgb(0,0,0) rgb(204,204,204);overflow:hidden;padding:2px 3px;vertical-align:bottom;font-size:11pt;text-align:center">High</td>
        <td style="border-width:1px;border-style:solid;border-color:rgb(204,204,204) rgb(0,0,0) rgb(0,0,0) rgb(204,204,204);overflow:hidden;padding:2px 3px;vertical-align:bottom;font-size:11pt">Volumes</td>
        <td style="border-width:1px;border-style:solid;border-color:rgb(204,204,204) rgb(0,0,0) rgb(0,0,0) rgb(204,204,204);overflow:hidden;padding:2px 3px;vertical-align:bottom;font-size:11pt">Volume creation and attach to a selected instance.</td>
        <td style="border-width:1px;border-style:solid;border-color:rgb(204,204,204) rgb(0,0,0) rgb(0,0,0) rgb(204,204,204);overflow:hidden;padding:2px 3px;vertical-align:bottom;font-size:11pt"><center>"""+ str(test_volume_creation) +"""</center></td>
    </tr>
    <tr style="height:21px">
        <td style="border-width:1px;border-style:solid;border-color:rgb(204,204,204) rgb(0,0,0) rgb(0,0,0);overflow:hidden;padding:2px 3px;vertical-align:bottom;font-size:11pt;text-align:center">15</td>
        <td style="border-width:1px;border-style:solid;border-color:rgb(204,204,204) rgb(0,0,0) rgb(0,0,0) rgb(204,204,204);overflow:hidden;padding:2px 3px;vertical-align:bottom;font-size:11pt;text-align:center">Normal</td>
        <td style="border-width:1px;border-style:solid;border-color:rgb(204,204,204) rgb(0,0,0) rgb(0,0,0) rgb(204,204,204);overflow:hidden;padding:2px 3px;vertical-align:bottom;font-size:11pt">Snapshot</td>
        <td style="border-width:1px;border-style:solid;border-color:rgb(204,204,204) rgb(0,0,0) rgb(0,0,0) rgb(204,204,204);overflow:hidden;padding:2px 3px;vertical-align:bottom;font-size:11pt">Instance Snapshot</td>
        <td style="border-width:1px;border-style:solid;border-color:rgb(204,204,204) rgb(0,0,0) rgb(0,0,0) rgb(204,204,204);overflow:hidden;padding:2px 3px;vertical-align:bottom;font-size:11pt"><center>"""+ str(ss_instance_creation) +"""</center></td>
    </tr>
    <tr style="height:21px">
        <td style="border-width:1px;border-style:solid;border-color:rgb(204,204,204) rgb(0,0,0) rgb(0,0,0);overflow:hidden;padding:2px 3px;vertical-align:bottom;font-size:11pt;text-align:center">16</td>
        <td style="border-width:1px;border-style:solid;border-color:rgb(204,204,204) rgb(0,0,0) rgb(0,0,0) rgb(204,204,204);overflow:hidden;padding:2px 3px;vertical-align:bottom;font-size:11pt;text-align:center">Normal</td>
        <td style="border-width:1px;border-style:solid;border-color:rgb(204,204,204) rgb(0,0,0) rgb(0,0,0) rgb(204,204,204);overflow:hidden;padding:2px 3px;vertical-align:bottom;font-size:11pt">Snapshot</td>
        <td style="border-width:1px;border-style:solid;border-color:rgb(204,204,204) rgb(0,0,0) rgb(0,0,0) rgb(204,204,204);overflow:hidden;padding:2px 3px;vertical-align:bottom;font-size:11pt">Instance creation using Snapshot</td>
        <td style="border-width:1px;border-style:solid;border-color:rgb(204,204,204) rgb(0,0,0) rgb(0,0,0) rgb(204,204,204);overflow:hidden;padding:2px 3px;vertical-align:bottom;font-size:11pt"><center>"""+ str(ss_instance) +"""</center></td>
    </tr>
    <tr style="height:21px">
        <td style="border-width:1px;border-style:solid;border-color:rgb(204,204,204) rgb(0,0,0) rgb(0,0,0);overflow:hidden;padding:2px 3px;vertical-align:bottom;font-size:11pt;text-align:center">17</td>
        <td style="border-width:1px;border-style:solid;border-color:rgb(204,204,204) rgb(0,0,0) rgb(0,0,0) rgb(204,204,204);overflow:hidden;padding:2px 3px;vertical-align:bottom;font-size:11pt;text-align:center">Normal</td>
        <td style="border-width:1px;border-style:solid;border-color:rgb(204,204,204) rgb(0,0,0) rgb(0,0,0) rgb(204,204,204);overflow:hidden;padding:2px 3px;vertical-align:bottom;font-size:11pt">Snapshot</td>
        <td style="border-width:1px;border-style:solid;border-color:rgb(204,204,204) rgb(0,0,0) rgb(0,0,0) rgb(204,204,204);overflow:hidden;padding:2px 3px;vertical-align:bottom;font-size:11pt">Instance Snapshot deletion</td>
        <td style="border-width:1px;border-style:solid;border-color:rgb(204,204,204) rgb(0,0,0) rgb(0,0,0) rgb(204,204,204);overflow:hidden;padding:2px 3px;vertical-align:bottom;font-size:11pt"><center>"""+ str(ss_deletion) +"""</center></td>
    </tr>
    <tr style="height:21px">
        <td style="border-width:1px;border-style:solid;border-color:rgb(204,204,204) rgb(0,0,0) rgb(0,0,0);overflow:hidden;padding:2px 3px;vertical-align:bottom;font-size:11pt;text-align:center">18</td>
        <td style="border-width:1px;border-style:solid;border-color:rgb(204,204,204) rgb(0,0,0) rgb(0,0,0) rgb(204,204,204);overflow:hidden;padding:2px 3px;vertical-align:bottom;font-size:11pt;text-align:center">Normal</td>
        <td style="border-width:1px;border-style:solid;border-color:rgb(204,204,204) rgb(0,0,0) rgb(0,0,0) rgb(204,204,204);overflow:hidden;padding:2px 3px;vertical-align:bottom;font-size:11pt">Snapshot</td>
        <td style="border-width:1px;border-style:solid;border-color:rgb(204,204,204) rgb(0,0,0) rgb(0,0,0) rgb(204,204,204);overflow:hidden;padding:2px 3px;vertical-align:bottom;font-size:11pt">Volume Snapshot</td>
        <td style="border-width:1px;border-style:solid;border-color:rgb(204,204,204) rgb(0,0,0) rgb(0,0,0) rgb(204,204,204);overflow:hidden;padding:2px 3px;vertical-align:bottom;font-size:11pt"><center>"""+ str(ss_volume) +"""</center></td>
    </tr>
    <tr style="height:21px">
        <td style="border-width:1px;border-style:solid;border-color:rgb(204,204,204) rgb(0,0,0) rgb(0,0,0);overflow:hidden;padding:2px 3px;vertical-align:bottom;font-size:11pt;text-align:center">19</td>
        <td style="border-width:1px;border-style:solid;border-color:rgb(204,204,204) rgb(0,0,0) rgb(0,0,0) rgb(204,204,204);overflow:hidden;padding:2px 3px;vertical-align:bottom;font-size:11pt;text-align:center">Normal</td>
        <td style="border-width:1px;border-style:solid;border-color:rgb(204,204,204) rgb(0,0,0) rgb(0,0,0) rgb(204,204,204);overflow:hidden;padding:2px 3px;vertical-align:bottom;font-size:11pt">Snapshot</td>
        <td style="border-width:1px;border-style:solid;border-color:rgb(204,204,204) rgb(0,0,0) rgb(0,0,0) rgb(204,204,204);overflow:hidden;padding:2px 3px;vertical-align:bottom;font-size:11pt">Volume creation Snapshot</td>
        <td style="border-width:1px;border-style:solid;border-color:rgb(204,204,204) rgb(0,0,0) rgb(0,0,0) rgb(204,204,204);overflow:hidden;padding:2px 3px;vertical-align:bottom;font-size:11pt"><center>"""+ str(ss_volume_creation) +"""</center></td>
    </tr>
    <tr style="height:21px">
        <td style="border-width:1px;border-style:solid;border-color:rgb(204,204,204) rgb(0,0,0) rgb(0,0,0);overflow:hidden;padding:2px 3px;vertical-align:bottom;font-size:11pt;text-align:center">20</td>
        <td style="border-width:1px;border-style:solid;border-color:rgb(204,204,204) rgb(0,0,0) rgb(0,0,0) rgb(204,204,204);overflow:hidden;padding:2px 3px;vertical-align:bottom;font-size:11pt;text-align:center">Normal</td>
        <td style="border-width:1px;border-style:solid;border-color:rgb(204,204,204) rgb(0,0,0) rgb(0,0,0) rgb(204,204,204);overflow:hidden;padding:2px 3px;vertical-align:bottom;font-size:11pt">Snapshot</td>
        <td style="border-width:1px;border-style:solid;border-color:rgb(204,204,204) rgb(0,0,0) rgb(0,0,0) rgb(204,204,204);overflow:hidden;padding:2px 3px;vertical-align:bottom;font-size:11pt">Volume Snapshot deletion</td>
        <td style="border-width:1px;border-style:solid;border-color:rgb(204,204,204) rgb(0,0,0) rgb(0,0,0) rgb(204,204,204);overflow:hidden;padding:2px 3px;vertical-align:bottom;font-size:11pt"><center>"""+ str(ss_volume_deletion) +"""</center></td>
    </tr>
    <tr style="height:21px">
        <td style="border-width:1px;border-style:solid;border-color:rgb(204,204,204) rgb(0,0,0) rgb(0,0,0);overflow:hidden;padding:2px 3px;vertical-align:bottom;font-size:11pt;text-align:center">21</td>
        <td style="border-width:1px;border-style:solid;border-color:rgb(204,204,204) rgb(0,0,0) rgb(0,0,0) rgb(204,204,204);overflow:hidden;padding:2px 3px;vertical-align:bottom;font-size:11pt;text-align:center">High</td>
        <td style="border-width:1px;border-style:solid;border-color:rgb(204,204,204) rgb(0,0,0) rgb(0,0,0) rgb(204,204,204);overflow:hidden;padding:2px 3px;vertical-align:bottom;font-size:11pt">Network and Security</td>
        <td style="border-width:1px;border-style:solid;border-color:rgb(204,204,204) rgb(0,0,0) rgb(0,0,0) rgb(204,204,204);overflow:hidden;padding:2px 3px;vertical-align:bottom;font-size:11pt">IP Allocation to Project</td>
        <td style="border-width:1px;border-style:solid;border-color:rgb(204,204,204) rgb(0,0,0) rgb(0,0,0) rgb(204,204,204);overflow:hidden;padding:2px 3px;vertical-align:bottom;font-size:11pt"><center>"""+ str(IP_allocation) +"""</center></td>
    </tr>
       <tr style="height:21px">
        <td style="border-width:1px;border-style:solid;border-color:rgb(204,204,204) rgb(0,0,0) rgb(0,0,0);overflow:hidden;padding:2px 3px;vertical-align:bottom;font-size:11pt;text-align:center">22</td>
        <td style="border-width:1px;border-style:solid;border-color:rgb(204,204,204) rgb(0,0,0) rgb(0,0,0) rgb(204,204,204);overflow:hidden;padding:2px 3px;vertical-align:bottom;font-size:11pt;text-align:center">High</td>
        <td style="border-width:1px;border-style:solid;border-color:rgb(204,204,204) rgb(0,0,0) rgb(0,0,0) rgb(204,204,204);overflow:hidden;padding:2px 3px;vertical-align:bottom;font-size:11pt">Environment</td>
        <td style="border-width:1px;border-style:solid;border-color:rgb(204,204,204) rgb(0,0,0) rgb(0,0,0) rgb(204,204,204);overflow:hidden;padding:2px 3px;vertical-align:bottom;font-size:11pt">Deletion of tested instances </td>
        <td style="border-width:1px;border-style:solid;border-color:rgb(204,204,204) rgb(0,0,0) rgb(0,0,0) rgb(204,204,204);overflow:hidden;padding:2px 3px;vertical-align:bottom;font-size:11pt"><center>"""+ str(deletion_of_tested_instances) +"""</center></td>
   </tr>
   <tr style="height:21px">
        <td style="border-width:1px;border-style:solid;border-color:rgb(204,204,204) rgb(0,0,0) rgb(0,0,0);overflow:hidden;padding:2px 3px;vertical-align:bottom;font-size:11pt;text-align:center">23</td>
        <td style="border-width:1px;border-style:solid;border-color:rgb(204,204,204) rgb(0,0,0) rgb(0,0,0) rgb(204,204,204);overflow:hidden;padding:2px 3px;vertical-align:bottom;font-size:11pt;text-align:center">High</td>
        <td style="border-width:1px;border-style:solid;border-color:rgb(204,204,204) rgb(0,0,0) rgb(0,0,0) rgb(204,204,204);overflow:hidden;padding:2px 3px;vertical-align:bottom;font-size:11pt">Network and Security</td>
        <td style="border-width:1px;border-style:solid;border-color:rgb(204,204,204) rgb(0,0,0) rgb(0,0,0) rgb(204,204,204);overflow:hidden;padding:2px 3px;vertical-align:bottom;font-size:11pt">IP Deallocation after Testing</td>
        <td style="border-width:1px;border-style:solid;border-color:rgb(204,204,204) rgb(0,0,0) rgb(0,0,0) rgb(204,204,204);overflow:hidden;padding:2px 3px;vertical-align:bottom;font-size:11pt"><center>"""+ str(Deallocation_of_IP_after_Testing) +"""</center></td>
    </tr>
     <tr style="height:21px">
        <td style="border-width:1px;border-style:solid;border-color:rgb(204,204,204) rgb(0,0,0) rgb(0,0,0);overflow:hidden;padding:2px 3px;vertical-align:bottom;font-size:11pt;text-align:center">24</td>
        <td style="border-width:1px;border-style:solid;border-color:rgb(204,204,204) rgb(0,0,0) rgb(0,0,0) rgb(204,204,204);overflow:hidden;padding:2px 3px;vertical-align:bottom;font-size:11pt;text-align:center">High</td>
        <td style="border-width:1px;border-style:solid;border-color:rgb(204,204,204) rgb(0,0,0) rgb(0,0,0) rgb(204,204,204);overflow:hidden;padding:2px 3px;vertical-align:bottom;font-size:11pt">Volumes</td>
        <td style="border-width:1px;border-style:solid;border-color:rgb(204,204,204) rgb(0,0,0) rgb(0,0,0) rgb(204,204,204);overflow:hidden;padding:2px 3px;vertical-align:bottom;font-size:11pt">Deletion of tested Volume</td>
        <td style="border-width:1px;border-style:solid;border-color:rgb(204,204,204) rgb(0,0,0) rgb(0,0,0) rgb(204,204,204);overflow:hidden;padding:2px 3px;vertical-align:bottom;font-size:11pt"><center>"""+ str(Deletion_of_tested_volume) +"""</center></td>
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
server.login('Username','Password')
server.sendmail(emailfrom, recipients, msg.as_string())
server.quit()
