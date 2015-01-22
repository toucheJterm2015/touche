# this is not really a test, but it kills any unexpected data potentially left over from previous tests, and it runs the same way the actual tests do.
# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re

class RemoveContestData(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.PhantomJS("/usr/local/bin/phantomjs")
        self.driver.implicitly_wait(30)
        self.base_url = "http://localhost/~touche/Test_Contest"
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_remove_contest_data(self):
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
        
        #goes to each page and deletes things left by other tests (sites, problems, teams, etc)
        driver.find_element_by_link_text("Misc").click()
        try: self.assertEqual("Misc", driver.find_element_by_xpath("//li[contains(@class, \"active\")]").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        
        #un-start the contest by clicking "clear contest"
        driver.find_element_by_name("B2").click()
        
        driver.find_element_by_link_text("Categories").click()
        try: self.assertEqual("Categories", driver.find_element_by_xpath("//li[contains(@class, \"active\")]").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        #clear the categories
        try: del_button = driver.find_element_by_link_text("Delete")
        except NoSuchElementException as e: del_button=None
        while del_button!=None:
            #print "loop 1"
            del_button.click()
            try: del_button = driver.find_element_by_link_text("Delete")
            except NoSuchElementException as e: del_button=None
        
        driver.find_element_by_link_text("Teams").click()
        try: self.assertEqual("Teams", driver.find_element_by_xpath("//li[contains(@class, \"active\")]").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        #clear the teams
        try: del_button = driver.find_element_by_link_text("Delete")
        except NoSuchElementException as e: del_button=None
        while del_button!=None:
            #print "loop 2"
            del_button.click()
            try: del_button = driver.find_element_by_link_text("Delete")
            except NoSuchElementException as e: del_button=None
            
        driver.find_element_by_link_text("Sites").click()
        try: self.assertEqual("Sites", driver.find_element_by_xpath("//li[contains(@class, \"active\")]").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        #clear the sites
        try: del_button = driver.find_element_by_link_text("Delete")
        except NoSuchElementException as e: del_button=None
        while del_button!=None:
            #print "loop 3"
            del_button.click()
            try: del_button = driver.find_element_by_link_text("Delete")
            except NoSuchElementException as e: del_button=None
        
        driver.find_element_by_link_text("Problems").click()
        try: self.assertEqual("Problems", driver.find_element_by_xpath("//li[contains(@class, \"active\")]").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        #clear the problems
        try: del_button = driver.find_element_by_link_text("Delete")
        except NoSuchElementException as e: del_button=None
        while del_button!=None:
            #print "loop 4"
            del_button.click()
            try: del_button = driver.find_element_by_link_text("Delete")
            except NoSuchElementException as e: del_button=None
        
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
