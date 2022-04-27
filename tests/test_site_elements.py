##############################################################################
# NO IMPORTS, BEGIN SCRIPT
##############################################################################


# THIS FILE IS IN DEVELOPMENT AND DOES NOT REPRESENT A FINISHED PRODUCT

# Let's create a function to iteratively call our test driver for every
# page. We'll gather test results and return them, along with our
# driver, to the calling method. We'll keep this as a seperate file to
# make script entry points more accessible.
def check_elements(data, testDriver):
    # Initialize our resulsts
    tabulation = []
    # For every page name and corresponding url ...
    for page, url in data.urls.items():
        # Pass our url to driver.
        testDriver.getURL({'url': url})
        # Check what kind of lookup data we're given. We'll test links
        # with HTML classes and button clicks with HTML ids.
        if hasattr(data, 'classes'):
            elems_lkup = data.classes.get(page)
            results = testDriver.test_links(page, elems_lkup)
        elif hasattr(data, 'ids'):
            elems_lkup = data.ids.get(page)
            results = testDriver.test_buttons_clickable(page, elems_lkup)
        # At the end of each iteration, add our page results list to
        # our tabulation.
        tabulation = tabulation + results

    # Return our final tabulation and our driver.
    return (tabulation, testDriver)


##############################################################################
# END
##############################################################################
