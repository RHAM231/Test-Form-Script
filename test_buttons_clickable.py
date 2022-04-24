from test_form import TestDriver

# THIS FILE IS IN DEVELOPMENT AND DOES NOT REPRESENT A FINISHED PRODUCT

testDriver = TestDriver()
testDriver.getURL({'url': 'https://rexhmitchell.com/'})
testDriver.test_buttons_clickable()
testDriver.driver.quit()
