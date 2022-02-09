from test_form import mySiteData, TestDriver


testDriver = TestDriver()
testDriver.getURL(mySiteData)
testDriver.test_live_contact_form(mySiteData)
