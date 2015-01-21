# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re

class DataSetsAndProblemsTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.PhantomJS("/usr/local/bin/phantomjs")
        self.driver.implicitly_wait(15)
        self.base_url = "http://localhost/~mschmock/Contest"
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_data_sets_and_problems(self):
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
        
        driver.get(self.base_url + "/admin/setup_data_sets.php")
        try: self.assertRegexpMatches(driver.find_element_by_css_selector("div.col-md-5").text, r"^[\s\S]*No[\s\S]*Problems[\s\S]*$")
        except AssertionError as e: self.verificationErrors.append(str(e))
        driver.get(self.base_url + "/admin/setup_problems.php")
        driver.find_element_by_name("problem_name").clear()
        driver.find_element_by_name("problem_name").send_keys("Guess the number three")
        driver.find_element_by_name("problem_short_name").clear()
        driver.find_element_by_name("problem_short_name").send_keys("guess3")
        driver.find_element_by_name("problem_note").clear()
        driver.find_element_by_name("problem_note").send_keys("asdgdasgghkasdgjh asdgkhasdgdkjasghs dagasdgj ssdg")
        driver.find_element_by_name("submit").click()
        driver.find_element_by_link_text("Edit").click()
        driver.find_element_by_name("html_file").clear()
        driver.find_element_by_name("html_file").send_keys(self.base_url + "/../touche_mel/testing/placeholder.txt")#replace with the proper path to the html
        driver.find_element_by_name("pdf_file").clear()
        driver.find_element_by_name("pdf_file").send_keys(self.base_url + "/../touche_mel/testing/placeholder.txt")#replace with the proper path to the pdf
        driver.find_element_by_name("submit").click()
        driver.find_element_by_link_text("Data").click()
        try: self.assertTrue(self.is_element_present(By.LINK_TEXT, "Add new data set"))
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertNotRegexpMatches(driver.find_element_by_css_selector("div.col-md-6").text, r"^[\s\S]*Adding data[\s\S]*$")
        except AssertionError as e: self.verificationErrors.append(str(e))
        driver.find_element_by_link_text("Add new data set").click()
        driver.find_element_by_name("data_set_in").clear()
        driver.find_element_by_name("data_set_in").send_keys(self.base_url + "/../touche_mel/testing/placeholder.txt")#replace with the proper path to input
        driver.find_element_by_name("data_set_out").clear()
        driver.find_element_by_name("data_set_out").send_keys(self.base_url + "/../touche_mel/testing/placeholder.txt")#replace with the proper path to a matching output file
        driver.find_element_by_name("submit").click()
        try: self.assertNotRegexpMatches(driver.find_element_by_css_selector("div.col-md-6").text, r"^[\s\S]*Adding data[\s\S]*$")
        except AssertionError as e: self.verificationErrors.append(str(e))#the form to add data should not be visible once the data is added.
        driver.find_element_by_link_text("Add new data set").click()#repeat as many times as necessary depending on how many I/O pairs you have.
        driver.find_element_by_name("data_set_in").send_keys(self.base_url + "/../touche_mel/testing/placeholder.txt")#replace with the proper path to input
        driver.find_element_by_name("data_set_out").clear()
        driver.find_element_by_name("data_set_out").send_keys(self.base_url + "/../touche_mel/testing/placeholder.txt")#replace with the proper path to a matching output file
        driver.find_element_by_name("submit").click()
        try: self.assertTrue(self.is_element_present(By.XPATH, "//tr[4]"))
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertRegexpMatches(driver.find_element_by_css_selector("div.col-md-5").text, r"^[\s\S]*placeholder[\s\S]*$")
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
