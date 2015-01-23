# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re

class SubmitAndJudgeManyProblems(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = url
        self.verificationErrors = []
        self.accept_next_alert = True
        self.driver.set_file_detector(LocalFileDetector())
    
    def test_submit_and_judge_many_problems(self):
        driver = self.driver
        driver.get(self.base_url + "/index.php")
        driver.find_element_by_name("user").clear()
        driver.find_element_by_name("user").send_keys("team1")
        driver.find_element_by_name("password").clear()
        driver.find_element_by_name("password").send_keys("password")
        driver.find_element_by_name("submit").click()
        self.assertRegexpMatches(driver.find_element_by_css_selector("h3").text, r"^[\s\S]*team1$")
        driver.find_element_by_link_text("Submissions").click()
        self.assertRegexpMatches(driver.find_element_by_css_selector("b").text, r"^[\s\S]*problem1$")
        
        # ERROR: Caught exception [ERROR: Unsupported command [selectWindow | null | ]]
        
        try: self.assertRegexpMatches(driver.find_element_by_xpath("//table[3]/tbody/tr/td/b").text, r"^[\s\S]*problem2$")
        except AssertionError as e: self.verificationErrors.append(str(e))
        driver.find_element_by_name("source_file").clear()
        driver.find_element_by_name("source_file").send_keys("../../uploadableFiles/empty.java")
        driver.find_element_by_css_selector("input[type=\"submit\"]").click()
        self.assertEqual("Queued for judging", driver.find_element_by_xpath("//td[3]/font").text)
        Select(driver.find_element_by_name("problem_id")).select_by_visible_text("2 - problem2")
        driver.find_element_by_name("source_file").clear()
        driver.find_element_by_name("source_file").send_keys("../../uploadableFiles/empty.java")
        driver.find_element_by_css_selector("input[type=\"submit\"]").click()
        self.assertEqual("Queued for judging", driver.find_element_by_xpath("//table[3]/tbody/tr[3]/td[3]/font").text)
        driver.get(self.base_url + "/index.php")
        driver.find_element_by_name("user").clear()
        driver.find_element_by_name("user").send_keys("team2")
        driver.find_element_by_name("password").clear()
        driver.find_element_by_name("password").send_keys("password")
        driver.find_element_by_name("submit").click()
        self.assertRegexpMatches(driver.find_element_by_css_selector("h3").text, r"^[\s\S]*team2$")
        driver.find_element_by_link_text("Submissions").click()
        self.assertRegexpMatches(driver.find_element_by_css_selector("b").text, r"^[\s\S]*problem1$")
        
        # ERROR: Caught exception [ERROR: Unsupported command [selectWindow | null | ]]
        
        try: self.assertRegexpMatches(driver.find_element_by_xpath("//table[3]/tbody/tr/td/b").text, r"^[\s\S]*problem2$")
        except AssertionError as e: self.verificationErrors.append(str(e))
        driver.find_element_by_name("source_file").clear()
        driver.find_element_by_name("source_file").send_keys("../../uploadableFiles/empty..java")
        driver.find_element_by_css_selector("input[type=\"submit\"]").click()
        self.assertEqual("Queued for judging", driver.find_element_by_xpath("//td[3]/font").text)
        Select(driver.find_element_by_name("problem_id")).select_by_visible_text("2 - problem2")
        driver.find_element_by_name("source_file").clear()
        driver.find_element_by_name("source_file").send_keys("../../uploadableFiles/empty.java")
        driver.find_element_by_css_selector("input[type=\"submit\"]").click()
        self.assertEqual("Queued for judging", driver.find_element_by_xpath("//table[3]/tbody/tr[3]/td[3]/font").text)
        driver.get(self.base_url + "/judge/index.php")
        driver.find_element_by_name("user").clear()
        driver.find_element_by_name("user").send_keys("judge")
        driver.find_element_by_name("password").clear()
        driver.find_element_by_name("password").send_keys("password")
        driver.find_element_by_name("submit").click()
        driver.refresh()
        driver.find_element_by_link_text("judge submission").click()
        Select(driver.find_element_by_name("result")).select_by_visible_text("Format Error")
        driver.find_element_by_name("submit").click()
        driver.find_element_by_link_text("judge submission").click()
        Select(driver.find_element_by_name("result")).select_by_visible_text("Runtime Error")
        driver.find_element_by_name("submit").click()
        
        # ERROR: Caught exception [ERROR: Unsupported command [selectWindow | null | ]]
        
        driver.find_element_by_link_text("judge submission").click()
        Select(driver.find_element_by_name("result")).select_by_visible_text("Forbidden Word in Source")
        driver.find_element_by_name("submit").click()
        driver.find_element_by_link_text("judge submission").click()
        Select(driver.find_element_by_name("result")).select_by_visible_text("Incorrect Output")
        driver.find_element_by_name("submit").click()
        driver.get(self.base_url + "/index.php")
        driver.find_element_by_name("user").clear()
        driver.find_element_by_name("user").send_keys("team1")
        driver.find_element_by_name("password").clear()
        driver.find_element_by_name("password").send_keys("password")
        driver.find_element_by_name("submit").click()
        driver.find_element_by_link_text("Submissions").click()
        driver.find_element_by_name("source_file").clear()
        driver.find_element_by_name("source_file").send_keys("../../uploadableFiles/empty.java")
        driver.find_element_by_css_selector("input[type=\"submit\"]").click()
        Select(driver.find_element_by_name("problem_id")).select_by_visible_text("2 - problem2")
        driver.find_element_by_name("source_file").clear()
        driver.find_element_by_name("source_file").send_keys("../../uploadableFiles/empty.java")
        driver.find_element_by_css_selector("input[type=\"submit\"]").click()
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
        driver.get(self.base_url + "/index.php")
        driver.find_element_by_name("user").clear()
        driver.find_element_by_name("user").send_keys("team1")
        driver.find_element_by_name("password").clear()
        driver.find_element_by_name("password").send_keys("password")
        driver.find_element_by_name("submit").click()
        driver.find_element_by_link_text("Submissions").click()
        driver.find_element_by_link_text("Standings").click()
        try: self.assertRegexpMatches(driver.find_element_by_xpath("//td[3]/font").text, r"^[\s\S]*/2$")
        except AssertionError as e: self.verificationErrors.append(str(e))
        sliceMeProb1 = driver.find_element_by_xpath("//td[3]/font").text
        
        # ERROR: Caught exception [ERROR: Unsupported command 
        #[getEval | String(storedVars['sliceMeProb1']).slice(3,5) | ]]
        minutes = int(sliceMeProb1[3:5])
        
        sliceMeProb2 = driver.find_element_by_xpath("//td[4]/font").text
        
        # ERROR: Caught exception [ERROR: Unsupported command 
        #[getEval | parseInt(String(storedVars['sliceMeProb2']).slice(3,5)) + ${minutes} | ]]
        minutes = int(string(sliceMeProb2)[3:5]) + minutes
        
        sliceMeTotalScore = driver.find_element_by_xpath("//tr[3]/td[5]").text
        
        # ERROR: Caught exception [ERROR: Unsupported command 
        #[getEval | String(storedVars['sliceMeTotalScore']).slice(5,7) | ]]
        displayedScore = string(sliceMeTotalScore)[5:7]
        
        # ERROR: Caught exception [ERROR: Unsupported command 
        #[getEval | parseInt(storedVars['minutes']) + 40 | ]]
        calculatedScore = minutes + 40

        # ERROR: Caught exception [ERROR: Unsupported command 
        #[getEval | storedVars['displayedScore'] == storedVars['calculatedScore'] | ]]
        try: self.eq(calculatedScore, displayedScore)
        except AssertionError as e: self.verificationErrors.append(str(e))
    
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
