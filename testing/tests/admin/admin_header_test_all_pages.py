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

class AdminHeaderTestAllPages(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.PhantomJS("/usr/local/bin/phantomjs")
        self.driver.implicitly_wait(30)
        self.base_url = "http://localhost/~mschmock/Contest"
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_admin_header_test_all_pages(self):
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
        
        #this test goes to each main admin page in turn and checks that they are on the expected page, and all of the navbar and related things that should be on all the admin pages are actually there.
        try: self.assertEqual("Details", driver.find_element_by_xpath("//li[contains(@class, \"active\")]").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        self.check_each_page
        
        driver.find_element_by_link_text("Problems").click()
        try: self.assertEqual("Problems", driver.find_element_by_xpath("//li[contains(@class, \"active\")]").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        self.check_each_page
        
        driver.find_element_by_link_text("Data").click()
        try: self.assertEqual("Data", driver.find_element_by_xpath("//li[contains(@class, \"active\")]").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        self.check_each_page
        
        driver.find_element_by_link_text("Sites").click()
        try: self.assertEqual("Sites", driver.find_element_by_xpath("//li[contains(@class, \"active\")]").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        self.check_each_page
        
        driver.find_element_by_link_text("Teams").click()
        try: self.assertEqual("Teams", driver.find_element_by_xpath("//li[contains(@class, \"active\")]").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        self.check_each_page
        
        driver.find_element_by_link_text("Categories").click()
        try: self.assertEqual("Categories", driver.find_element_by_xpath("//li[contains(@class, \"active\")]").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        self.check_each_page
        
        driver.find_element_by_link_text("Headers").click()
        try: self.assertEqual("Headers", driver.find_element_by_xpath("//li[contains(@class, \"active\")]").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        self.check_each_page
        
        driver.find_element_by_link_text("Forbidden").click()
        try: self.assertEqual("Forbidden", driver.find_element_by_xpath("//li[contains(@class, \"active\")]").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        self.check_each_page
        
        driver.find_element_by_link_text("Misc").click()
        try: self.assertEqual("Misc", driver.find_element_by_xpath("//li[contains(@class, \"active\")]").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        self.check_each_page
        
        driver.find_element_by_link_text("Start").click()
        try: self.assertEqual("Start", driver.find_element_by_xpath("//li[contains(@class, \"active\")]").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        self.check_each_page
        
    
	#this batch of presence-of tests was so repetitive, I cut the commands out and pasted them into a separate function to give future developers half a chance of understanding what's going on.
    def check_each_page():
        try: self.assertTrue(self.is_element_present(By.CSS_SELECTOR, "div.panel-body"))
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertRegexpMatches(driver.find_element_by_css_selector("div.panel-body").text, r"^[\s\S]*Contest[\s\S]*$")
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertTrue(self.is_element_present(By.CSS_SELECTOR, "body > div.container"))
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertTrue(self.is_element_present(By.LINK_TEXT, "Details"))
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertTrue(self.is_element_present(By.LINK_TEXT, "Problems"))
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertTrue(self.is_element_present(By.LINK_TEXT, "Data"))
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertTrue(self.is_element_present(By.LINK_TEXT, "Sites"))
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertTrue(self.is_element_present(By.LINK_TEXT, "Teams"))
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertTrue(self.is_element_present(By.LINK_TEXT, "Categories"))
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertTrue(self.is_element_present(By.LINK_TEXT, "Headers"))
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertTrue(self.is_element_present(By.LINK_TEXT, "Forbidden"))
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertTrue(self.is_element_present(By.LINK_TEXT, "Misc"))
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertTrue(self.is_element_present(By.LINK_TEXT, "Start"))
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertTrue(self.is_element_present(By.CSS_SELECTOR, "h3"))
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertTrue(self.is_element_present(By.CSS_SELECTOR, "img[alt=\"Logo\"]"))
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertEqual("ADMIN", driver.find_element_by_css_selector("h3").text)
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
