# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re

class Clarifications(unittest.TestCase):
    def __init__(self, url):
        self.setUp(url)

    def setUp(self, url):
        self.driver = webdriver.PhantomJS("/usr/local/bin/phantomjs")
        self.driver.implicitly_wait(30)
        self.base_url = url
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_clarifications(self):
        driver = self.driver
        driver.get(self.base_url + "/index.php")
        driver.find_element_by_name("user").clear()
        driver.find_element_by_name("user").send_keys("team1")
        driver.find_element_by_name("password").clear()
        driver.find_element_by_name("password").send_keys("password")
        driver.find_element_by_name("submit").click()
        driver.find_element_by_link_text("Clarifications").click()
        try: self.assertEqual("problem1", driver.find_element_by_link_text("problem1").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertEqual("problem2", driver.find_element_by_link_text("problem2").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        driver.find_element_by_css_selector("button.btn.btn-default").click()
        Select(driver.find_element_by_name("problem_id")).select_by_visible_text("problem1")
        driver.find_element_by_name("question").clear()
        driver.find_element_by_name("question").send_keys("Do clarifications work?")
        driver.find_element_by_name("submit").click()
        driver.get(self.base_url + "/judge/index.php")
        driver.find_element_by_name("user").clear()
        driver.find_element_by_name("user").send_keys("judge")
        driver.find_element_by_name("password").clear()
        driver.find_element_by_name("password").send_keys("password")
        driver.find_element_by_name("submit").click()
        driver.find_element_by_link_text("Clarifications").click()
        driver.find_element_by_link_text("Respond to Clarification").click()
        driver.find_element_by_name("response").clear()
        driver.find_element_by_name("response").send_keys("Ummmm yeah! They sure do.")
        driver.find_element_by_name("submit").click()
        driver.get(self.base_url + "/index.php")
        driver.find_element_by_name("user").clear()
        driver.find_element_by_name("user").send_keys("team1")
        driver.find_element_by_name("password").clear()
        driver.find_element_by_name("password").send_keys("password")
        driver.find_element_by_name("submit").click()
        driver.find_element_by_link_text("Clarifications").click()
        driver.find_element_by_link_text("problem1").click()
        try: self.assertRegexpMatches(driver.find_element_by_xpath("//tr[5]/td[2]").text, r"^[\s\S]*clarification[\s\S]*$")
        except AssertionError as e: self.verificationErrors.append(str(e))
        driver.find_element_by_css_selector("button.btn.btn-default").click()
        driver.find_element_by_name("question").clear()
        driver.find_element_by_name("question").send_keys("Special characters?  ~`!@#$%^&*()_+09><?/;:'\"\\|,.<> {}[] \"asdf\" 'asdf'")
        driver.find_element_by_name("submit").click()
        driver.get(self.base_url + "/judge/index.php")
        driver.find_element_by_name("user").clear()
        driver.find_element_by_name("user").send_keys("judge")
        driver.find_element_by_name("password").clear()
        driver.find_element_by_name("password").send_keys("password")
        driver.find_element_by_name("submit").click()
        driver.find_element_by_link_text("Clarifications").click()
        driver.find_element_by_link_text("Respond to Clarification").click()
        driver.find_element_by_name("response").clear()
        driver.find_element_by_name("response").send_keys("Special character response - \n~`\n!1\n@2\n#3\n$4\n%5\n^6\n&7\n888*?/><,.")
        Select(driver.find_element_by_name("broadcast")).select_by_visible_text("Respond to All")
        driver.find_element_by_name("submit").click()
        driver.get(self.base_url + "/index.php")
        driver.find_element_by_name("user").clear()
        driver.find_element_by_name("user").send_keys("team1")
        driver.find_element_by_name("password").clear()
        driver.find_element_by_name("password").send_keys("password")
        driver.find_element_by_name("submit").click()
        driver.find_element_by_link_text("Clarifications").click()
        try: self.assertRegexpMatches(driver.find_element_by_xpath("//tr[6]/td[2]").text, r"^[\s\S]*response[\s\S]*$")
        except AssertionError as e: self.verificationErrors.append(str(e))
        driver.get(self.base_url + "/index.php")
        driver.find_element_by_name("user").clear()
        driver.find_element_by_name("user").send_keys("team2")
        driver.find_element_by_name("password").clear()
        driver.find_element_by_name("password").send_keys("password")
        driver.find_element_by_name("submit").click()
        driver.find_element_by_link_text("Clarifications").click()
        try: self.assertRegexpMatches(driver.find_element_by_xpath("//tr[6]/td[2]").text, r"^[\s\S]*response[\s\S]*$")
        except AssertionError as e: self.verificationErrors.append(str(e))
        driver.find_element_by_link_text("problem1").click()
        try: self.assertNotRegexpMatches(driver.find_element_by_xpath("//tr[5]/td[2]").text, r"^[\s\S]*$")
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
