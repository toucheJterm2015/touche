# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re

class AddEditDeleteProblems(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.PhantomJS("/usr/local/bin/phantomjs")
        self.driver.implicitly_wait(30)
        self.base_url = "http://localhost"
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_add_edit_delete_problems(self):
        driver = self.driver
        
        #should be moved to separate function, but for now when I try to do so, it breaks.
        driver.get(self.base_url + "/~mschmock/Contest/admin/index.php")
        user = driver.find_element_by_name("user")
        user.clear()
        user.send_keys("admin")
        driver.find_element_by_name("password").clear()
        driver.find_element_by_name("password").send_keys("password")
        driver.find_element_by_name("submit").click()
        #end of what should be the login function
        
        driver.get(self.base_url + "/~mschmock/Contest/admin/setup_problems.php")
        driver.find_element_by_name("problem_name").clear()
        driver.find_element_by_name("problem_name").send_keys("NewProblem")
        driver.find_element_by_name("problem_short_name").clear()
        driver.find_element_by_name("problem_short_name").send_keys("Noob")
        driver.find_element_by_name("problem_loc").clear()
        driver.find_element_by_name("problem_loc").send_keys("place")
        driver.find_element_by_name("problem_note").clear()
        driver.find_element_by_name("problem_note").send_keys("it is a problem being added for this test.")
        #do we want the long text box to be able to handle apostrophes? It currently breaks, and I don't know if we want that, or if we want to handle them intelligently and escape them so that admins can type whatever they want.
        driver.find_element_by_name("submit").click()
        try: self.assertRegexpMatches(driver.find_element_by_css_selector("div.col-md-5").text, r"^[\s\S]*NewProblem[\s\S]*$")
        except AssertionError as e: self.verificationErrors.append(str(e))
        driver.find_element_by_link_text("Edit").click()
        driver.find_element_by_name("problem_name").clear()
        driver.find_element_by_name("problem_name").send_keys("NewNameProb")
        try: self.assertTrue(self.is_element_present(By.NAME, "html_file"))
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertTrue(self.is_element_present(By.NAME, "pdf_file"))
        except AssertionError as e: self.verificationErrors.append(str(e))
        driver.find_element_by_name("submit").click()
        try: self.assertNotRegexpMatches(driver.find_element_by_css_selector("div.col-md-5").text, r"^[\s\S]*NewProblem[\s\S]*$")
        except AssertionError as e: self.verificationErrors.append(str(e))
        driver.find_element_by_xpath("//td[ contains( text(),'NewNameProb' ) ]/../td[3]/a").click()
        try: self.assertNotRegexpMatches(driver.find_element_by_css_selector("div.col-md-5").text, r"^[\s\S]*NewNameProb[\s\S]*$")
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
