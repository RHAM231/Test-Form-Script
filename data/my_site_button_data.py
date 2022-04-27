import sys
sys.path.append('')

from initialize_driver import call_driver


# THIS FILE IS IN DEVELOPMENT AND DOES NOT REPRESENT A FINISHED PRODUCT

class MySiteButtonData(object):
    def __init__(self):
        self.urls = {
                    'home': 'https://rexhmitchell.com/', 
                    'portfolio': \
                        'https://rexhmitchell.com/portfolio-project/',
                    'contact': 'https://rexhmitchell.com/contact/',
                    'about': 'https://rexhmitchell.com/about_me/'
                    }
        self.ids = {
                    'home': [
                        'box-gh-id', 'box-ht5-id', 'box-git-id', 'box-aws-id',
                        'box-c3-id', 'box-ubt-id', 'box-js-id', 'box-dr-id',
                        'box-bst-id', 'box-pyt-id', 'box-dj-id',
                        'HM-btn-id', 'IT-btn-id', 'MS-btn-id'
                        ],
                    'portfolio': [
                        'github-btn-id', 'checklist-btn-id', 
                        'contact-btn-id'
                        ],
                    'contact': [
                        'id_name', 'id_sender', 'id_subject', 'id_message', 
                        'id_cc_myself', 'submit-btn-id'
                        ],
                    'about': ['contact-btn-id']
                    }

if __name__ == '__main__':
    data = MySiteButtonData()
    call_driver(data)
