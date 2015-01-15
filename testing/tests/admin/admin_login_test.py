#! usr/bin/python

# this is specifically designed to test the login page AFTER the admin has logged in the first time and changed their password. The tests will not behave as expected if this is used on the admin's first login after creating a contest.
# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re

class AdminLoginTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.PhantomJS("/usr/local/bin/phantomjs")
        self.driver.implicitly_wait(30)
        self.base_url = "http://localhost/~mschmock/Contest"
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_admin_login(self):
        #log in with the right password
        driver = self.driver
        driver.get(self.base_url + "/admin/index.php")
        user = driver.find_element_by_name("user")
        user.clear()
        user.send_keys("admin")
        driver.find_element_by_name("password").clear()
        driver.find_element_by_name("password").send_keys("password")
        driver.find_element_by_name("submit").click()
        try: self.assertEqual("Edit Contest Info", driver.find_element_by_css_selector("div.table-responsive > table.table > tbody > tr").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        
        #back to the login page and try with an old password; should not log in
        driver.get(self.base_url + "/admin/index.php")
        driver.find_element_by_name("user").clear()
        driver.find_element_by_name("user").send_keys("admin")
        driver.find_element_by_name("password").clear()
        driver.find_element_by_name("password").send_keys("admin")
        driver.find_element_by_name("submit").click()
        try: self.assertRegexpMatches(driver.find_element_by_css_selector("div.row").text, r"^Admin Login[\s\S]*$")
        except AssertionError as e: self.verificationErrors.append(str(e))
        
        #make sure empty username and someone's good password do not log in
        driver.get(self.base_url + "/admin/index.php")
        driver.find_element_by_name("user").clear()
        driver.find_element_by_name("user").send_keys("")
        driver.find_element_by_name("password").clear()
        driver.find_element_by_name("password").send_keys("password")
        driver.find_element_by_name("submit").click()
        try: self.assertRegexpMatches(driver.find_element_by_css_selector("div.row").text, r"^Admin Login[\s\S]*$")
        except AssertionError as e: self.verificationErrors.append(str(e))
        
        #make sure empty password and someone's username do not log in
        driver.get(self.base_url + "/admin/index.php")
        driver.find_element_by_name("user").clear()
        driver.find_element_by_name("user").send_keys("admin")
        driver.find_element_by_name("password").clear()
        driver.find_element_by_name("password").send_keys("")
        driver.find_element_by_name("submit").click()
        try: self.assertRegexpMatches(driver.find_element_by_css_selector("div.row").text, r"^Admin Login[\s\S]*$")
        except AssertionError as e: self.verificationErrors.append(str(e))
        
        #blank user and password do not log in
        driver.get(self.base_url + "/admin/index.php")
        driver.find_element_by_name("user").clear()
        driver.find_element_by_name("user").send_keys("")
        driver.find_element_by_name("password").clear()
        driver.find_element_by_name("password").send_keys("")
        driver.find_element_by_name("submit").click()
        try: self.assertRegexpMatches(driver.find_element_by_css_selector("div.row").text, r"^Admin Login[\s\S]*$")
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
