Response to ANZ challenge, applicaiton for Senior QA role
13/Jan/2021, By Adel Fazel
Answering to Challenges.

Answer to challenges. 
1) How to get things up and running.
Ans) Docker pull bkimminich/juice-shop which pulls image to docker repository.
This process is automated and  can be performed by:
-> make init
2) To use the test suite, you can either test it against a local docker or against the actual webapp.
-> make testlocal
-> make testweb
3) Please note that this suite case is designed to fail for all the test cases. The test artifacts, which are .png files
are brought back this machine after test is done in 'artefacts'
4) There are two test cases related to feedback as part of my answer. 
a) Putting too many feedbacks in short amount of time. This is achieved by creating multiple instaces of a browser in parallel 
and each creating a feedback. test_feedback_parallel
b) Prendting to be a another user test_feedback_captcha_forged_usedid, this test exploits existance of a field 'userid'
which shouldn't have been there fills it as part of providing a feedback.  
c) SQL injection. This is a rather simple test, by adding '-- to a known username, one can login, 
as '-- comments out the test that password provided by the user needs to match saved password. Automation test is in
test_sql_injection.py
d) Upload invalid file type, see the test_invalid_complaint, this is a trivial test that uses xml file instead of a approved files