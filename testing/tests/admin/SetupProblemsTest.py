#! usr/bin/python

# this is just the presence-of (buttons, text fields...) tests, not the functionality tests
# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re

class SetupProblemsTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.PhantomJS("/usr/local/bin/phantomjs")
        self.driver.implicitly_wait(15)
        self.base_url = "http://localhost/~touche/Test_Contest"
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_setup_problems(self):
        driver = self.driver
        
        #should be moved to separate function, but for now when I try to do so, it breaks.
        driver.get(self.base_url + "/admin/index.php")
        user = driver.find_element_by_name("user")
        user.clear()
        user.send_keys("admin")
        driver.find_element_by_name("password").clear()
        driver.find_element_by_name("password").send_keys("password")
        driver.find_element_by_name("submit").click()
        #end of what should be the login function
        
        driver.get(self.base_url + "/admin/setup_problems.php")
        try: self.assertTrue(self.is_element_present(By.CSS_SELECTOR, "div.col-md-6"))
        except AssertionError as e: self.verificationErrors.append(str(e)+" test 1")
        try: self.assertEqual("Add or Edit Problems", driver.find_element_by_css_selector("div.table-responsive > table.table > tbody > tr > td > h3").text)
        except AssertionError as e: self.verificationErrors.append(str(e)+" test 2")
        try: self.assertTrue(self.is_element_present(By.CSS_SELECTOR, "div.col-md-5"))
        except AssertionError as e: self.verificationErrors.append(str(e)+" test 3")
        try: self.assertEqual("Edit Current Problems", driver.find_element_by_css_selector("div.col-md-5 > div.table-responsive > table.table > tbody > tr > td").text)
        except AssertionError as e: self.verificationErrors.append(str(e)+" test 4")
        try: self.assertTrue(self.is_element_present(By.NAME, "problem_name"))
        except AssertionError as e: self.verificationErrors.append(str(e)+" test 5")
        try: self.assertTrue(self.is_element_present(By.NAME, "problem_short_name"))
        except AssertionError as e: self.verificationErrors.append(str(e)+" test 6")
        try: self.assertTrue(self.is_element_present(By.NAME, "problem_loc"))
        except AssertionError as e: self.verificationErrors.append(str(e)+" test 7")
        try: self.assertTrue(self.is_element_present(By.NAME, "problem_note"))
        except AssertionError as e: self.verificationErrors.append(str(e)+" test 8")
        try: self.assertTrue(self.is_element_present(By.NAME, "submit"))
        except AssertionError as e: self.verificationErrors.append(str(e)+" test 9")
    
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
