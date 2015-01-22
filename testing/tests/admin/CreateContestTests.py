# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re

class CreateContestTests(unittest.TestCase):
    def __init__(self):
        self.setUp()

    def setUp(self):
        self.driver = webdriver.PhantomJS("/usr/local/bin/phantomjs")
        self.driver.implicitly_wait(30)
        self.base_url = "http://touche.cse.taylor.edu/"
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_create_contest_tests(self):
        driver = self.driver
        driver.get(self.base_url + "/~touche/index.php")
        try: self.assertRegexpMatches(driver.find_element_by_css_selector("h2").text, r"^[\s\S]*Welcome to Touche[\s\S]*$")
        except AssertionError as e: self.verificationErrors.append(str(e))
        driver.find_element_by_name("user").clear()
        driver.find_element_by_name("user").send_keys("admin")
        driver.find_element_by_name("password").clear()
        driver.find_element_by_name("password").send_keys("password")
        driver.find_element_by_name("submit").click()
        try: self.assertRegexpMatches(driver.find_element_by_css_selector("h2").text, r"^[\s\S]*Welcome to Touche[\s\S]*$")
        except AssertionError as e: self.verificationErrors.append(str(e))
        driver.find_element_by_name("user").clear()
        driver.find_element_by_name("user").send_keys("create")
        driver.find_element_by_name("password").clear()
        driver.find_element_by_name("password").send_keys("contest")
        driver.find_element_by_name("submit").click()
        driver.find_element_by_name("contest_host").clear()
        driver.find_element_by_name("contest_host").send_keys("The Organization")
        driver.find_element_by_name("contest_name").clear()
        driver.find_element_by_name("contest_name").send_keys("Test_Contest")
        driver.find_element_by_name("dbhost").clear()
        driver.find_element_by_name("dbhost").send_keys("localhost")
        driver.find_element_by_name("dbpassword").clear()
        driver.find_element_by_name("dbpassword").send_keys("password")
        # ERROR: Caught exception [unknown command [clickandWait]]
        for i in range(60):
            try:
                if r"^[\s\S]*Finished[\s\S]*$" == driver.find_element_by_tag_name("BODY").text: break
            except: pass
            time.sleep(10)#this takes for-freaking-ever, so make the loop longer. What's really important is the content of the next page.
        else: self.fail("time out")
        try: self.assertNotEqual(r"^[\s\S]*Unable[\s\S]*$", driver.find_element_by_tag_name("BODY").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertNotEqual(r"^[\s\S]*Something happened[\s\S]*$", driver.find_element_by_tag_name("BODY").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        driver.find_element_by_link_text("Administration setup").click()
        try: self.assertEqual(r"^[\s\S]*Admin Login[\s\S]*$", driver.find_element_by_tag_name("BODY").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        driver.find_element_by_name("user").clear()
        driver.find_element_by_name("user").send_keys("admin")
        driver.find_element_by_name("password").clear()
        driver.find_element_by_name("password").send_keys("password")
        driver.find_element_by_name("submit").click()
        try: self.assertEqual(r"^[\s\S]*Admin Login[\s\S]*$", driver.find_element_by_tag_name("BODY").text)#the original password for a new admin is admin
        except AssertionError as e: self.verificationErrors.append(str(e))
        driver.find_element_by_name("user").clear()
        driver.find_element_by_name("user").send_keys("admin")
        driver.find_element_by_name("password").clear()
        driver.find_element_by_name("password").send_keys("admin")
        driver.find_element_by_name("submit").click()
        try: self.assertEqual(r"^[\s\S]*Login Information[\s\S]*$", driver.find_element_by_tag_name("BODY").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertTrue(self.is_element_present(By.NAME, "user"))
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertTrue(self.is_element_present(By.NAME, "password"))
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertTrue(self.is_element_present(By.NAME, "password2"))
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertTrue(self.is_element_present(By.NAME, "submit"))
        except AssertionError as e: self.verificationErrors.append(str(e))
        driver.find_element_by_name("user").clear()
        driver.find_element_by_name("user").send_keys("admin")
        driver.find_element_by_name("password").clear()
        driver.find_element_by_name("password").send_keys("admin")
        driver.find_element_by_name("password2").clear()
        driver.find_element_by_name("password2").send_keys("password")#the passwords don't match, so the user gets redirected to this page
        driver.find_element_by_name("submit").click()
        try: self.assertEqual(r"^[\s\S]*Please change[\s\S]*$", driver.find_element_by_tag_name("BODY").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        driver.find_element_by_name("user").clear()
        driver.find_element_by_name("user").send_keys("admin")
        driver.find_element_by_name("password").clear()
        driver.find_element_by_name("password").send_keys("admin")
        driver.find_element_by_name("password2").clear()
        driver.find_element_by_name("password2").send_keys("admin")
        driver.find_element_by_name("submit").click()
        try: self.assertEqual(r"^[\s\S]*Please change[\s\S]*$", driver.find_element_by_tag_name("BODY").text)#should come back to this page, and enforce that the admin change their password.
        except AssertionError as e: self.verificationErrors.append(str(e))
        driver.find_element_by_name("user").clear()
        driver.find_element_by_name("user").send_keys("admin")
        driver.find_element_by_name("password").clear()
        driver.find_element_by_name("password").send_keys("password")
        driver.find_element_by_name("password2").clear()
        driver.find_element_by_name("password2").send_keys("password")
        driver.find_element_by_name("submit").click()
        try: self.assertTrue(self.is_element_present(By.LINK_TEXT, "Details"))
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
