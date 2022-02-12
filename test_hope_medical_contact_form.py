from test_form import HMSiteData, TestDriver


testDriver = TestDriver()
testDriver.getURL(HMSiteData)
testDriver.test_live_contact_form(HMSiteData)

