##############################################################################
# PYTHON IMPORTS
##############################################################################

import sys
sys.path.append('')

##############################################################################
# PROJECT IMPORTS
##############################################################################

from data.ms.my_site_button_data import MySiteButtonData
from initialize_driver import call_driver

##############################################################################
# BEGIN SCRIPT
##############################################################################


# Test just the button data for my site. Check if the elements can be
# clicked.
if __name__ == '__main__':
    data = MySiteButtonData()
    call_driver(data)


##############################################################################
# END
##############################################################################
