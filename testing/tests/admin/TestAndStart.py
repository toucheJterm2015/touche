# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re

class TestAndStart(unittest.TestCase):
    def __init__(self, url):
        self.setUp(url)

    def setUp(self, url):
        self.driver = webdriver.PhantomJS("/usr/local/bin/phantomjs")
        self.driver.implicitly_wait(30)
        self.base_url = url
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_and_start(self):
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
        
        #clears the contest in case it has been started before, so all of the sites are listed as not-yet started.
        driver.get(self.base_url + "/admin/misc.php")
        driver.find_element_by_name("B2").click()#this is the "clear contest" button
        
        driver.get(self.base_url + "/admin/start.php")
        
        #presence of expected objects
        try: self.assertTrue(self.is_element_present(By.CSS_SELECTOR, "div.innerglow"))
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertRegexpMatches(driver.find_element_by_xpath("//form/div/table/tbody/tr[2]/td").text, r"^[\s\S]*PrimarySite[\s\S]*$")
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertRegexpMatches(driver.find_element_by_xpath("//form/div/table/tbody/tr[3]/td").text, r"^[\s\S]*SecondarySite[\s\S]*$")
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertTrue(self.is_element_present(By.NAME, "chksite[2]"))#if there's a second one, then the first one is also there.
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertTrue(self.is_element_present(By.NAME, "submit"))
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertTrue(self.is_element_present(By.XPATH, "(//button[@name='submit'])[2]"))
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertRegexpMatches(driver.find_element_by_css_selector("div.innerglow").text, r"^[\s\S]*Start Contest[\s\S]*$")
        except AssertionError as e: self.verificationErrors.append(str(e))
        
        #functionality of said objects
        driver.find_element_by_name("chksite[]").click()
        driver.find_element_by_xpath("(//input[@name='chksite[]'])[2]").click()
        driver.find_element_by_xpath("(//button[@name='submit'])[2]").click()
        try: self.assertRegexpMatches(driver.find_element_by_css_selector("div.innerglow").text, r"^[\s\S]*Running Test[\s\S]*Running Test[\s\S]*$")
        except AssertionError as e: self.verificationErrors.append(str(e))
        driver.find_element_by_name("chksite[]").click()
        driver.find_element_by_name("submit").click()
        try: self.assertRegexpMatches(driver.find_element_by_css_selector("div.innerglow").text, r"^[\s\S]*Running Test[\s\S]*$")
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertRegexpMatches(driver.find_element_by_css_selector("div.innerglow").text, r"^[\s\S]*Contest Started[\s\S]*$")
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertFalse(self.is_element_present(By.XPATH, "(//input[@name='chksite[]'])[2]"))
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
