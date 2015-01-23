# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re

class AddEditDeleteSites(unittest.TestCase):
    def __init__(self, url):
        self.setUp(url)

    def setUp(self, url):
        self.driver = webdriver.PhantomJS("/usr/local/bin/phantomjs")
        self.driver.implicitly_wait(30)
        self.base_url = url
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_add_edit_delete_sites(self):
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
        
        driver.get(self.base_url + "/~mschmock/Contest/admin/setup_site.php")
        driver.find_element_by_name("site_name").clear()
        driver.find_element_by_name("site_name").send_keys("My New Site")
        driver.find_element_by_name("submit").click()
        try: self.assertRegexpMatches(driver.find_element_by_css_selector("div.col-md-6").text, r"^[\s\S]*My New Site[\s\S]*$")
        except AssertionError as e: self.verificationErrors.append(str(e))
        driver.find_element_by_xpath("//td[contains(text(), \"My New Site\")]/../td[2]/a").click()
        driver.find_element_by_name("site_name").clear()
        driver.find_element_by_name("site_name").send_keys("Site Renamed")
        driver.find_element_by_name("submit").click()
        try: self.assertNotRegexpMatches(driver.find_element_by_css_selector("div.col-md-6").text, r"^[\s\S]*My New Site[\s\S]*$")
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertRegexpMatches(driver.find_element_by_css_selector("div.col-md-6").text, r"^[\s\S]*Site Renamed[\s\S]*$")
        except AssertionError as e: self.verificationErrors.append(str(e))
        driver.find_element_by_xpath("//td[contains(text(), \"Site Renamed\")]/../td[3]/a").click()
        try: self.assertNotRegexpMatches(driver.find_element_by_css_selector("div.col-md-6").text, r"^[\s\S]*Site Renamed[\s\S]*$")
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
