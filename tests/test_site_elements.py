


# THIS FILE IS IN DEVELOPMENT AND DOES NOT REPRESENT A FINISHED PRODUCT

def check_elements(data, testDriver):
    tabulation = []
    for page, url in data.urls.items():
        testDriver.getURL({'url': url})
        if hasattr(data, 'classes'):
            elems_lkup = data.classes.get(page)
            results = testDriver.test_links(page, elems_lkup)
        elif hasattr(data, 'ids'):
            elems_lkup = data.ids.get(page)
            results = testDriver.test_buttons_clickable(page, elems_lkup)
        tabulation = tabulation + results

    return (tabulation, testDriver)
