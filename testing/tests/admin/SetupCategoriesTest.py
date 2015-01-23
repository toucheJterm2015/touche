# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re

class SetupCategoriesTest(unittest.TestCase):
    def __init__(self, url):
        self.setUp(url)

    def setUp(self, url):
        self.driver = webdriver.PhantomJS("/usr/local/bin/phantomjs")
        self.driver.implicitly_wait(30)
        self.base_url = url
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_setup_categories(self):
        driver = self.driver
        
        #should be moved to separate function, but for now when I try to do so, it breaks.
        driver.get(self.base_url + "/admin/index.php")
        user = driver.find_element_by_name("user")
        user.clear()
        user.send_keys("admin")
        driver.find_element_by_name("password").clear()
        driver.find_element_by_name("password").send_keys("password")
        driver.find_element_by_name("submit").click()
        #end of what should be the login function0
        
        driver.get(self.base_url + "/admin/setup_categories.php")
        
        #check that everything shows up the way it should
        try: self.assertTrue(self.is_element_present(By.CSS_SELECTOR, "div.col-md-5"))
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertRegexpMatches(driver.find_element_by_css_selector("div.col-md-6").text, r"^[\s\S]*No current categories[\s\S]*$")
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertTrue(self.is_element_present(By.CSS_SELECTOR, "div.col-md-11"))
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertTrue(self.is_element_present(By.NAME, "category_name"))
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertTrue(self.is_element_present(By.NAME, "submit"))
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertTrue(self.is_element_present(By.NAME, "makechanges"))
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertRegexpMatches(driver.find_element_by_css_selector("div.col-md-5").text, r"^[\s\S]*Add[\s\S]*new[\s\S]*$")
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertRegexpMatches(driver.find_element_by_css_selector("div.col-md-11 > table.table > tbody > tr > td").text, r"^[\s\S]*Teams[\s\S]*$")
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertRegexpMatches(driver.find_element_by_xpath("//form/div/table/tbody/tr[2]/td").text, r"^[\s\S]*Team Name[\s\S]*$")
        except AssertionError as e: self.verificationErrors.append(str(e))
        driver.find_element_by_name("category_name").clear()
        driver.find_element_by_name("category_name").send_keys("cat5e")
        driver.find_element_by_name("submit").click()
        try: self.assertRegexpMatches(driver.find_element_by_css_selector("div.col-md-6 > div.table-responsive > table.table > tbody > tr > td > h3").text, r"^[\s\S]*Edit[\s\S]*$")
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertRegexpMatches(driver.find_element_by_css_selector("div.col-md-6").text, r"^[\s\S]*cat5e[\s\S]*$")
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertTrue(self.is_element_present(By.XPATH, "//td[contains(text(), \"cat5e\")]"))
        except AssertionError as e: self.verificationErrors.append(str(e))
        driver.find_element_by_link_text("Delete").click()
        
        #makes sure that everything works as expected
        try: self.assertFalse(self.is_element_present(By.LINK_TEXT, "Delete"))#the table should currently be empty of categories.
        except AssertionError as e: self.verificationErrors.append(str(e))
        driver.find_element_by_name("category_name").clear()
        driver.find_element_by_name("category_name").send_keys("cat1")
        driver.find_element_by_name("submit").click()
        
        #a brief interruption to make sure the edit function works and looks as expected.
        driver.find_element_by_xpath("//td[contains(text(), \"cat1\")]/../td[2]/a").click()
        try: self.assertRegexpMatches(driver.find_element_by_css_selector("div.table-responsive > table.table > tbody > tr > td").text, r"^[\s\S]*Editing[\s\S]*$")
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertEqual("Edit Category", driver.find_element_by_name("submit").text)#this should currently fail but it is not for some reason
        except AssertionError as e: self.verificationErrors.append(str(e))
        driver.find_element_by_name("category_name").clear()
        driver.find_element_by_name("category_name").send_keys("newName")
        driver.find_element_by_name("submit").click()
        try: self.assertNotRegexpMatches(driver.find_element_by_css_selector("div.col-md-6").text, r"^[\s\S]*cat1[\s\S]*$")
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertEqual("Add Category", driver.find_element_by_name("submit").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertRegexpMatches(driver.find_element_by_css_selector("div.table-responsive > table.table > tbody > tr > td").text, r"^[\s\S]*Add[\s\S]*new[\s\S]*$")
        except AssertionError as e: self.verificationErrors.append(str(e))
        
        driver.find_element_by_name("category_name").clear()
        driver.find_element_by_name("category_name").send_keys("cat2")
        driver.find_element_by_name("submit").click()
        driver.find_element_by_name("category_name").clear()
        driver.find_element_by_name("category_name").send_keys("cat3")
        driver.find_element_by_name("submit").click()
        driver.find_element_by_name("category_name").clear()
        driver.find_element_by_name("category_name").send_keys("cat4")
        driver.find_element_by_name("submit").click()
        try: self.assertTrue(self.is_element_present(By.XPATH, "(//a[contains(text(),'Edit')])[4]"))#after making four categories, there should be four Edit links in the table.
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertTrue(self.is_element_present(By.XPATH, "(//a[contains(text(),'Delete')])[4]"))#after making four categories, there should be four Delete links in the table.
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertEqual("cat4", driver.find_element_by_xpath("//td[5]").text)
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
