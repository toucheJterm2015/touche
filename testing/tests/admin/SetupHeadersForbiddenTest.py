# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re

class SetupHeadersForbiddenTest(unittest.TestCase):
    def __init__(self, url):
        self.setUp(url)

    def setUp(self, url):
        self.driver = webdriver.PhantomJS("/usr/local/bin/phantomjs")
        self.driver.implicitly_wait(30)
        self.base_url = url
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_setup_headers_forbidden(self):
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
        
        #headers tests
        driver.get(self.base_url + "/admin/setup_headers.php")
        try: self.assertTrue(self.is_element_present(By.CSS_SELECTOR, "div.col-md-5"))
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertRegexpMatches(driver.find_element_by_css_selector("div.col-md-5").text, r"^[\s\S]*C[\s][\s\S]*$")
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertRegexpMatches(driver.find_element_by_css_selector("div.col-md-5").text, r"^[\s\S]*CXX[\s\S]*$")
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertRegexpMatches(driver.find_element_by_css_selector("div.col-md-5").text, r"^[\s\S]*JAVA[\s\S]*$")
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertRegexpMatches(driver.find_element_by_css_selector("div.col-md-5").text, r"^[\s\S]*Edit[\s\S]*$")
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertRegexpMatches(driver.find_element_by_css_selector("div.col-md-6 > div.table-responsive > table.table > tbody > tr > td").text, r"^[\s\S]*Please select[\s\S]*$")
        except AssertionError as e: self.verificationErrors.append(str(e))
        driver.find_element_by_link_text("Edit").click()
        try: self.assertNotRegexpMatches(driver.find_element_by_css_selector("div.col-md-6 > div.table-responsive > table.table > tbody > tr > td").text, r"^[\s\S]*Please select[\s\S]*$")
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertRegexpMatches(driver.find_element_by_css_selector("div.col-md-6").text, r"^[\s\S]*Editing[\s\S]*$")
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertTrue(self.is_element_present(By.NAME, "submit"))
        except AssertionError as e: self.verificationErrors.append(str(e))
        driver.find_element_by_name("submit").click()
        try: self.assertFalse(self.is_element_present(By.NAME, "submit"))
        except AssertionError as e: self.verificationErrors.append(str(e))
        
        #forbidden tests start here and continue until the end of the def
        
        #first, making every language have forbidden words
        driver.get(self.base_url + "/admin/setup_contest.php")
        if not driver.find_element_by_name("forbidden_c").is_selected():
            driver.find_element_by_name("forbidden_c").click()
        if not driver.find_element_by_name("forbidden_cpp").is_selected():
            driver.find_element_by_name("forbidden_cpp").click()
        if not driver.find_element_by_name("forbidden_java").is_selected():
            driver.find_element_by_name("forbidden_java").click()
        driver.find_element_by_name("submit").click()
        
        #now all of the lists of forbidden words should be accessible.
        driver.get(self.base_url + "/admin/setup_forbidden.php")
        try: self.assertTrue(self.is_element_present(By.CSS_SELECTOR, "div.col-md-5"))
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertRegexpMatches(driver.find_element_by_css_selector("div.col-md-5").text, r"^[\s\S]*C[\s][\s\S]*$")
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertRegexpMatches(driver.find_element_by_css_selector("div.col-md-5").text, r"^[\s\S]*CXX[\s\S]*$")
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertRegexpMatches(driver.find_element_by_css_selector("div.col-md-5").text, r"^[\s\S]*JAVA[\s\S]*$")
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertRegexpMatches(driver.find_element_by_css_selector("div.col-md-5").text, r"^[\s\S]*Edit[\s\S]*$")
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertRegexpMatches(driver.find_element_by_css_selector("div.col-md-6 > div.table-responsive > table.table > tbody > tr > td").text, r"^[\s\S]*Please select[\s\S]*$")
        except AssertionError as e: self.verificationErrors.append(str(e))
        driver.find_element_by_link_text("Edit").click()
        try: self.assertNotRegexpMatches(driver.find_element_by_css_selector("div.col-md-6 > div.table-responsive > table.table > tbody > tr > td").text, r"^[\s\S]*Please select[\s\S]*$")
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertRegexpMatches(driver.find_element_by_css_selector("div.col-md-6").text, r"^[\s\S]*Editing[\s\S]*$")
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertTrue(self.is_element_present(By.NAME, "submit"))
        except AssertionError as e: self.verificationErrors.append(str(e))
        driver.find_element_by_name("submit").click()
        try: self.assertFalse(self.is_element_present(By.NAME, "submit"))
        except AssertionError as e: self.verificationErrors.append(str(e))
        
        #turn off the java forbidden words (the most common to omit)
        driver.get(self.base_url + "/admin/setup_contest.php")
        if driver.find_element_by_name("forbidden_java").is_selected():
            driver.find_element_by_name("forbidden_java").click()
            driver.find_element_by_name("submit").click()
        
        #now make sure that java is not listed as an option
        driver.get(self.base_url + "/admin/setup_forbidden.php")
        try: self.assertRegexpMatches(driver.find_element_by_css_selector("div.col-md-5").text, r"^[\s\S]*CXX[\s\S]*$")
        except AssertionError as e: self.verificationErrors.append(str(e))#C++ should still be represented there, but Java should not.
        try: self.assertNotRegexpMatches(driver.find_element_by_css_selector("div.col-md-5").text, r"^[\s\S]*JAVA[\s\S]*$")
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
