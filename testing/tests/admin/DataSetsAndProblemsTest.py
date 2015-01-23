# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re

class DataSetsAndProblemsTest(unittest.TestCase):
    def __init__(self, url):
        self.setUp(url)

    def setUp(self, url):
        self.driver = webdriver.PhantomJS("/usr/local/bin/phantomjs")
        self.driver.implicitly_wait(15)
        self.base_url = url
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
        driver.find_element_by_name("problem_name").send_keys("problem1")
        driver.find_element_by_name("problem_short_name").clear()
        driver.find_element_by_name("problem_short_name").send_keys("prob1")
        driver.find_element_by_name("problem_note").clear()
        driver.find_element_by_name("problem_note").send_keys("it is a description")#apostrophes currently break things (sql injection)
        driver.find_element_by_name("submit").click()
        driver.find_element_by_name("problem_name").clear()
        driver.find_element_by_name("problem_name").send_keys("problem2")
        driver.find_element_by_name("problem_short_name").clear()
        driver.find_element_by_name("problem_short_name").send_keys("prob2")
        driver.find_element_by_name("problem_note").clear()
        driver.find_element_by_name("problem_note").send_keys("it is a description yay")#apostrophes currently break things (sql injection)
        driver.find_element_by_name("submit").click()
        
        #this will currently break due to issues with uploading through text/PhantomJS. See documentation/aNoteAboutTheStateOfTheTests.txt
        #driver.find_element_by_link_text("Edit").click()
        #driver.find_element_by_name("html_file").clear()
        #driver.find_element_by_name("html_file").send_keys(self.base_url + "placeholder")#replace with the proper path to the html
        #driver.find_element_by_name("pdf_file").clear()
        #driver.find_element_by_name("pdf_file").send_keys(self.base_url + "placeholder")#replace with the proper path to the pdf
        #driver.find_element_by_name("submit").click()
        #if you want to comment out these lines, the only actual issue is that there is no problem visible that contestants can see. We need to test it, but for now, it isn't essential for testing admin things.
        
        #back to useful, functional code.
        driver.find_element_by_link_text("Data").click()
        try: self.assertTrue(self.is_element_present(By.LINK_TEXT, "Add new data set"))
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertNotRegexpMatches(driver.find_element_by_css_selector("div.col-md-6").text, r"^[\s\S]*Adding data[\s\S]*$")
        except AssertionError as e: self.verificationErrors.append(str(e))
        driver.find_element_by_link_text("Add new data set").click()
        
        #more uploading issues. These are currently essential to starting the contest.
        driver.find_element_by_name("data_set_in").clear()
        driver.find_element_by_name("data_set_in").send_keys(self.base_url + "placeholder")#replace with the proper path to input
        driver.find_element_by_name("data_set_out").clear()
        driver.find_element_by_name("data_set_out").send_keys(self.base_url + "placeholder")#replace with the proper path to a matching output file
        #end file upload
        
        driver.find_element_by_name("submit").click()
        try: self.assertNotRegexpMatches(driver.find_element_by_css_selector("div.col-md-6").text, r"^[\s\S]*Adding data[\s\S]*$")
        except AssertionError as e: self.verificationErrors.append(str(e))#the form to add data should not be visible once the data is added.
        driver.find_element_by_xpath("//a[contains(text(), 'Add new data set')][2]").click()#add data to the second problem. Repeat as necessary for how many data sets you want to use.
        
        #more uploading problems...
        driver.find_element_by_name("data_set_in").clear()
        driver.find_element_by_name("data_set_in").send_keys(self.base_url + "placeholder")#replace with the proper path to input
        driver.find_element_by_name("data_set_out").clear()
        driver.find_element_by_name("data_set_out").send_keys(self.base_url + "placeholder")#replace with the proper path to a matching output file
        #end upload
        
        driver.find_element_by_name("submit").click()
        try: self.assertTrue(self.is_element_present(By.XPATH, "//tr[4]"))#there are two problems names and two data sets taking up four rows in the table.
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertRegexpMatches(driver.find_element_by_css_selector("div.col-md-5").text, r"^[\s\S]*placeholder[\s\S]*$")#change this when you change the placeholder strings. This should be one of the input file names.
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
