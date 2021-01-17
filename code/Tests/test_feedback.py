# import concurrent
# import sys
# from random import randint
# sys.path.append("..")
# from ..Pages.feedback import Feedback
# from datetime import datetime
# from .settings import create_browser,browser
# import concurrent.futures
#
#
# def test_feedback_captcha_forged(browser):
#     page = Feedback(browser)
#     browser.get(page.get_url())
#     page.dismiss()
#     page.login()
#     browser.refresh()
#     assert "OWASP" in page.get_title(), f"invalid page title: {page.get_title()}"
#     page.go_to_feedback_page()
#     page.fill_feedback_form()
#     page.feedback_submit()
#     page.screenshot()
#     assert not page.check_feedback_thankyou_is_present(), "successfully succeeded in forging captcha"
#
#
# def test_feedback_populating_usedid(browser):
#     page = Feedback(browser)
#     browser.get(page.get_url())
#     page.dismiss()
#     page.login()
#     browser.refresh()
#     assert "OWASP" in page.get_title(), f"invalid page title: {page.get_title()}"
#     page.feedback_change_author_id(str(randint(100, 1000)))
#     page.go_to_feedback_page()
#     page.fill_feedback_form()
#     page.feedback_submit()
#     page.screenshot()
#     assert not page.check_feedback_thankyou_is_present(), "successfully succeeded in forging captcha"
#
#
# def test_feedback_parallel():
#     def put_one_feedback(t):
#         browser = create_browser()
#         try:
#             page = Feedback(browser)
#             browser.get(page.get_url())
#             page.dismiss()
#             page.login()
#             browser.refresh()
#             page.go_to_feedback_page()
#
#             page.fill_feedback_form()
#             page.feedback_submit()
#             status = page.check_feedback_thankyou_is_present()
#             page.screenshot(f"Thread_{t}")
#             browser.quit()
#             return status
#         except:
#             browser.quit()
#             return False
#
#     trials, success = 15, 0
#     start = datetime.now()
#
#     with concurrent.futures.ThreadPoolExecutor(max_workers=10) as executor:
#         futures = [executor.submit(put_one_feedback, trial) for trial in range(trials)]
#         for exec_status in concurrent.futures.as_completed(futures):
#             success = success+1 if exec_status else success
#
#     time_to_submit_10_feedback = str((datetime.now() - start).seconds)
#     assert success < 10, f"Able to submit {success} feedback in {time_to_submit_10_feedback} seconds"
