# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re

class ContestantSubmissionsTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "http://touche.cse.taylor.edu/"
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_contestant_submissions(self):
        driver = self.driver
        # Each page is tested, and is marked below. This test assumes a contest 
        # has been started with two teams ("team1" and "team2", both passwords =
        # "password") and two problems ("problem1" and "problem2") to submit
        # answers to. Known issues are tagged with "!!!".
        # Don't forget - you'll have to change the file locations throughout this test for other contests/testers

# Begin test.
# !!! How do we test the time display?
# Open team sign-in page: username = "team1", password = "password"
driver.get(self.base_url + "/index.php")
driver.find_element_by_name("user").clear()
driver.find_element_by_name("user").send_keys("team1")
driver.find_element_by_name("password").clear()
driver.find_element_by_name("password").send_keys("password")
driver.find_element_by_name("submit").click()
self.assertRegexpMatches(driver.find_element_by_css_selector("h3").text, r"^[\s\S]*team1$")
# Verifying Alternate Teammate page (team1)
#     This will only happen upon a team's first sign-in. Why is this comment yellow?
#         (!!! Empty! Do something about this!)

# Verifying Problems Page Data (team1)
driver.find_element_by_link_text("Problems").click()
#     Checking that problem numbers and names display correctly
try: self.assertEqual("1 - problem1", driver.find_element_by_xpath("//tr[3]/td").text)
except AssertionError as e: self.verificationErrors.append(str(e))
try: self.assertEqual("2 - problem2", driver.find_element_by_xpath("//tr[4]/td").text)
except AssertionError as e: self.verificationErrors.append(str(e))
#     Checking that HTML and pdf display properly
#         (!!! Something is wrong with adding pdf's in admin.)
#         (!!! Not entirely sure how to check that these display faithfully.)

#     Checking that documents are not viewable for inactive contests
#         (!!! There are no inactive contests to check against at this time. Need to add that to test setup.)

# Verifying Submissions Page Data and Function Tests (team1)
driver.find_element_by_link_text("Submissions").click()
try: self.assertEqual("Problem #1: problem1", driver.find_element_by_css_selector("b").text)
except AssertionError as e: self.verificationErrors.append(str(e))
try: self.assertEqual("Problem #2: problem2", driver.find_element_by_xpath("//table[3]/tbody/tr/td/b").text)
except AssertionError as e: self.verificationErrors.append(str(e))
#     (Not terribly certain why the selectWindow command is necessary, nor how the type command works with the "Browse..." button
# ERROR: Caught exception [ERROR: Unsupported command [selectWindow | null | ]]
driver.find_element_by_name("source_file").clear()
driver.find_element_by_name("source_file").send_keys("X:\\08_2015_Jterm\\Project\\ContestProblems\\Submissions\\Answer1.cpp")
driver.find_element_by_css_selector("input[type=\"submit\"]").click()
self.assertEqual("Queued for judging", driver.find_element_by_xpath("//td[3]/font").text)
Select(driver.find_element_by_name("problem_id")).select_by_visible_text("2 - problem2")
#     ...because the selectWindow command isn't necessary here for some reason. And how do you "type" into a button?
driver.find_element_by_name("source_file").clear()
driver.find_element_by_name("source_file").send_keys("X:\\08_2015_Jterm\\Project\\ContestProblems\\Submissions\\Answer2.cpp")
driver.find_element_by_css_selector("input[type=\"submit\"]").click()
self.assertEqual("Queued for judging", driver.find_element_by_xpath("//table[3]/tbody/tr[3]/td[3]/font").text)

# Runing through the same set of instructions for team2
driver.get(self.base_url + "/index.php")
driver.find_element_by_name("user").clear()
driver.find_element_by_name("user").send_keys("team2")
driver.find_element_by_name("password").clear()
driver.find_element_by_name("password").send_keys("password")
driver.find_element_by_name("submit").click()
self.assertRegexpMatches(driver.find_element_by_css_selector("h3").text, r"^[\s\S]*team2$")
# Verifying Alternate Teammate page (team2)
#     This will only happen upon a team's first sign-in. Why is this comment yellow?
#         (!!! Empty! Do something about this!)

# Verifying Problems Page Data (team2)
driver.find_element_by_link_text("Problems").click()
#     Checking that problem numbers and names display correctly
try: self.assertEqual("1 - problem1", driver.find_element_by_xpath("//tr[3]/td").text)
except AssertionError as e: self.verificationErrors.append(str(e))
try: self.assertEqual("2 - problem2", driver.find_element_by_xpath("//tr[4]/td").text)
except AssertionError as e: self.verificationErrors.append(str(e))
#     Checking that HTML and pdf display properly
#         (!!! Something is wrong with adding pdf's in admin.)
#         (!!! Not entirely sure how to check that these display faithfully.)

#     Checking that documents are not viewable for inactive contests
#         (!!! There are no inactive contests to check against at this time. Need to add that to test setup.)

# Verifying Submissions Page Data and Function Tests (team2)
driver.find_element_by_link_text("Submissions").click()
try: self.assertEqual("Problem #1: problem1", driver.find_element_by_css_selector("b").text)
except AssertionError as e: self.verificationErrors.append(str(e))
try: self.assertEqual("Problem #2: problem2", driver.find_element_by_xpath("//table[3]/tbody/tr/td/b").text)
except AssertionError as e: self.verificationErrors.append(str(e))
#     (Not terribly certain why the selectWindow command is necessary, nor how the type command works with the "Browse..." button
# ERROR: Caught exception [ERROR: Unsupported command [selectWindow | null | ]]
driver.find_element_by_name("source_file").clear()
driver.find_element_by_name("source_file").send_keys("X:\\08_2015_Jterm\\Project\\ContestProblems\\Submissions\\Answer1.cpp")
driver.find_element_by_css_selector("input[type=\"submit\"]").click()
self.assertEqual("Queued for judging", driver.find_element_by_xpath("//td[3]/font").text)
Select(driver.find_element_by_name("problem_id")).select_by_visible_text("2 - problem2")
#     ...because the selectWindow command isn't necessary here for some reason. And how do you "type" into a button?
driver.find_element_by_name("source_file").clear()
driver.find_element_by_name("source_file").send_keys("X:\\08_2015_Jterm\\Project\\ContestProblems\\Submissions\\Answer2.cpp")
driver.find_element_by_css_selector("input[type=\"submit\"]").click()
self.assertEqual("Queued for judging", driver.find_element_by_xpath("//table[3]/tbody/tr[3]/td[3]/font").text)


# Moving to judge's page to generate feedback to display for the teams
#     !!! Need to add tests to check submissions for corruptions
#     !!! Need to add tests to check submissions remain paired with corresponding problems
driver.get(self.base_url + "/judge/index.php")
driver.find_element_by_name("user").clear()
driver.find_element_by_name("user").send_keys("judge")
driver.find_element_by_name("password").clear()
driver.find_element_by_name("password").send_keys("password")
driver.find_element_by_name("submit").click()
#     I think there's a better way to wait so that it will move on as soon as it "sees" the page is done loading. Figure it out later...
driver.refresh()
driver.find_element_by_link_text("judge submission").click()
Select(driver.find_element_by_name("result")).select_by_visible_text("Format Error")
driver.find_element_by_name("submit").click()
driver.find_element_by_link_text("judge submission").click()
Select(driver.find_element_by_name("result")).select_by_visible_text("Runtime Error")
driver.find_element_by_name("submit").click()
#     (Seriously, why do these "selectWindow" commands keep showing up?)
# ERROR: Caught exception [ERROR: Unsupported command [selectWindow | null | ]]
driver.find_element_by_link_text("judge submission").click()
Select(driver.find_element_by_name("result")).select_by_visible_text("Forbidden Word in Source")
driver.find_element_by_name("submit").click()
driver.find_element_by_link_text("judge submission").click()
Select(driver.find_element_by_name("result")).select_by_visible_text("Incorrect Output")
driver.find_element_by_name("submit").click()



# Moving back to team1 page to resubmit "corrected" submissions
driver.get(self.base_url + "/index.php")
driver.find_element_by_name("user").clear()
driver.find_element_by_name("user").send_keys("team1")
driver.find_element_by_name("password").clear()
driver.find_element_by_name("password").send_keys("password")
driver.find_element_by_name("submit").click()
driver.find_element_by_link_text("Submissions").click()
driver.find_element_by_name("source_file").clear()
driver.find_element_by_name("source_file").send_keys("X:\\08_2015_Jterm\\Project\\ContestProblems\\Submissions\\Answer1.cpp")
driver.find_element_by_css_selector("input[type=\"submit\"]").click()
Select(driver.find_element_by_name("problem_id")).select_by_visible_text("2 - problem2")
driver.find_element_by_name("source_file").clear()
driver.find_element_by_name("source_file").send_keys("X:\\08_2015_Jterm\\Project\\ContestProblems\\Submissions\\Answer2.cpp")
driver.find_element_by_css_selector("input[type=\"submit\"]").click()


# Back to judge... to accept team1's resubmissions
driver.get(self.base_url + "/judge/index.php")
driver.find_element_by_name("user").clear()
driver.find_element_by_name("user").send_keys("judge")
driver.find_element_by_name("password").clear()
driver.find_element_by_name("password").send_keys("password")
driver.find_element_by_name("submit").click()
driver.refresh()
driver.find_element_by_link_text("judge submission").click()
Select(driver.find_element_by_name("result")).select_by_visible_text("Accepted")
driver.find_element_by_name("submit").click()
driver.find_element_by_link_text("judge submission").click()
Select(driver.find_element_by_name("result")).select_by_visible_text("Accepted")
driver.find_element_by_name("submit").click()


# Back to team1... Checking the scoring displays
driver.get(self.base_url + "/index.php")
driver.find_element_by_name("user").clear()
driver.find_element_by_name("user").send_keys("team1")
driver.find_element_by_name("password").clear()
driver.find_element_by_name("password").send_keys("password")
driver.find_element_by_name("submit").click()
driver.find_element_by_link_text("Standings").click()
#     Checks that the number of submission attempts is accurate for each problem
#     !!! There should probably be a test to make sure the hours adding up, too (there isn't right now)
try: self.assertRegexpMatches(driver.find_element_by_xpath("//td[3]/font").text, r"^[\s\S]*/2$")
except AssertionError as e: self.verificationErrors.append(str(e))
sliceMeProb1 = driver.find_element_by_xpath("//td[3]/font").text

# ERROR: Caught exception [ERROR: Unsupported command [getEval | String(storedVars['sliceMeProb1']).slice(3,5) | ]]
prob1minutes = int(sliceMeProb1[3:5])

try: self.assertRegexpMatches(driver.find_element_by_xpath("//td[4]/font").text, r"^[\s\S]*/2$")
except AssertionError as e: self.verificationErrors.append(str(e))
sliceMeProb2 = driver.find_element_by_xpath("//td[4]/font").text

# ERROR: Caught exception [ERROR: Unsupported command [getEval | String(storedVars['sliceMeProb2']).slice(3,5) | ]]
prob2minutes = int(string(sliceMeProb2)[3:5])

# ERROR: Caught exception [ERROR: Unsupported command [getEval | parseInt(storedVars['prob1minutes']) + parseInt(storedVars['prob2minutes']) | ]]
combinedMinutes = prob1Minutes + prob2Mintues

sliceMeTotalScore = driver.find_element_by_xpath("//tr[3]/td[5]").text

# ERROR: Caught exception [ERROR: Unsupported command [getEval | String(storedVars['sliceMeTotalScore']).slice(5,7) | ]]
displayedScore = int(string(sliceMeTotalScore)[5:7])

#     We're adding 40 because we know there were 2 incorrect submission, costing 20 minutes each

# ERROR: Caught exception [ERROR: Unsupported command [getEval | ${combinedMinutes} + 40 | ]]
calculatedScore = combinedMinutes + 40

# ERROR: Caught exception [ERROR: Unsupported command [getEval | storedVars['displayedScore'] == storedVars['calculatedScore'] | ]]
try: self.eq(calculatedScore, displayedScore)
except AssertionError as e: self.verificationErrors.append(str(e))

#     !!! Should check for team2 submissions, too

    
    def is_element_present(self, how, what):
        try: self.driver.find_element(by=how, value=what)
        except NoSuchElementException, e: return False
        return True
    
    def is_alert_present(self):
        try: self.driver.switch_to_alert()
        except NoAlertPresentException, e: return False
        return True
    
    def close_alert_and_get_its_text(self):
        try:
            alert = self.driver.switch_to_alert()
            alert_text = alert.text
            if self.accept_next_alert:
                alert.accept()
            else:
                alert.dismiss()
            return alert_text
        finally: self.accept_next_alert = True
    
    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
