##############################################################################
# IMPORTS
##############################################################################

import subprocess
import requests
import wget
import zipfile
import os

##############################################################################
# SCRIPTS
##############################################################################



# Entry point to retrieve either the local or latest version of
# chromedriver. Our test script will try to run without downloading. If
# that fails, it will try with the latest version of chromedriver.
# Failing that it will try with the local version.
class UpdateChromeDriver(object):
    # Get the latest version of chromedriver directly from Google.
    def get_latest_version():
        version = get_latest_chromedriver_version()
        download_chromedriver(version)

    # Get chromedriver based on the currently installed version of
    # Chrome.
    def get_local_version():
        chrome_version = get_pc_chrome_version
        version = get_specific_chromedriver_version(chrome_version)
        download_chromedriver(version)


# Retrieve the currently installed version of Chrome
def get_pc_chrome_version():
    # Get the PC's chromedriver version.
    path = (
        r'wmic datafile where name="C:'
        r'\\Program Files (x86)\\Google'
        r'\\Chrome\\Application\\'
        r'chrome.exe" get Version /value')
    output = subprocess.check_output(
        path,
        shell=True
    )
    return output.decode('utf-8').strip()


# Given the installed version of Chrome, get the equivalent version of
# chromedriver.
def get_specific_chromedriver_version(chrome_version):
    print('Chrome Version: ', chrome_version)
    version = chrome_version.split('=')[1].split('.')[0]
    url = (
        'https://chromedriver.storage.googleapis.com/'
        'LATEST_RELEASE_' + version + ''
        )
    # Get the version and return it
    response = requests.get(url)
    return response.text


# Get the latest version of chromedriver from Google
def get_latest_chromedriver_version():
    # Grab the url
    url = 'https://chromedriver.storage.googleapis.com/LATEST_RELEASE'
    # Get the version and return it
    response = requests.get(url)
    print('Latest Release: ', response.text)
    return response.text


# Given the desired version number of chromedriver, go download it and
# unzip it into the current directory.
def download_chromedriver(version_number):
    # Set our download url based on version.
    download_url = (
        "https://chromedriver.storage.googleapis.com/" 
        + version_number +"/chromedriver_win32.zip"
        )
    # Download the zip file using the url built above.
    latest_driver_zip = wget.download(download_url,'chromedriver.zip')

    # Extract the zip file.
    with zipfile.ZipFile(latest_driver_zip, 'r') as zip_ref:
        # Specify destination path as needed.
        zip_ref.extractall()
    # Clean out the zip file after extracting the needed file.
    os.remove(latest_driver_zip)


##############################################################################
# END
##############################################################################
