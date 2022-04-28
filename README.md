# Test-Form-Script
This is a repository for my web form testing scripts using Selenium.

# Background
Let's create scripts for automating testing of all functionality of a live site. We'll test all links and forms, as well as check if buttons and other elements can be successfully clicked. The project is split into data, housing the ids and classes of HTML elements we want to test, and tests, housing scripts for testing sites piecemeal or in their entirety. The Python file selenium_driver.py stores the main logic for testing and tabulating the test results to the terminal. update_driver.py stores the logic for automatically updating chromedriver before tests. Our local version of chromedriver will become outdated quickly and render our scripts useless.

We'll use code from https://towardsdatascience.com/automating-submission-forms-with-python-94459353b03e as a starting point.

# Build Status
Script works for testing all links and forms for the portfolio site. Currently, debugging an error with testing the Hope Medical contact form. Expanding to include tests for the Hope Medical site and Issue Tracker.
