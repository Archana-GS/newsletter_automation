"""

API EXAMPLE TEST
1. Add new car - POST request(without url_params)

"""

import os
import sys
import pytest
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from endpoints.API_Player import API_Player
from conf import api_example_conf as conf
from conftest import interactivemode_flag
import time

@pytest.mark.API
def test_api_example(test_api_obj):
    "Run api test"
    try:
        expected_pass = 0
        actual_pass = -1

        # set authentication details
        headers = conf.headers
        editor_list = conf.article_editors

        # add articles
        for counter,editor in enumerate(editor_list):
            current_timestamp =str(int(time.time())+counter)
            counter += 1
            StrCounter = str(counter)
            article_detail = {'url':conf.article_url +current_timestamp,'title':conf.article_title+StrCounter,'description':conf.article_description+StrCounter,'category_id':StrCounter,'article_editor':editor}
            test_api_obj.add_article(article_details=article_detail,headers=headers)
            result_flag = article_detail
        
        test_api_obj.log_result(result_flag,
                                positive='Successfully added new article with details %s' % article_detail,
                                negative='Could not add new article with details %s' % article_detail)
        
        # write out test summary
        expected_pass = test_api_obj.total
        actual_pass = test_api_obj.passed
        test_api_obj.write_test_summary()

    except Exception as e:
        print(e)
        if conf.api_url == 'http://127.0.0.1:5000':
            test_api_obj.write("Clone the repo 'git@github.com:qxf2/newsletter_automation.git' and run the newsletter app inorder to run the test against your system")

        else:
            test_api_obj.write("Exception when trying to run test:%s" % __file__)
            test_api_obj.write("Python says:%s" % str(e))

    # Assertion
    assert expected_pass == actual_pass,"Test failed: %s"%__file__

if __name__ == '__main__':
    test_api_example()