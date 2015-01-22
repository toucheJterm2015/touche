# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re

class AddEditDeleteTeam(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.PhantomJS("/usr/local/bin/phantomjs")
        self.driver.implicitly_wait(30)
        self.base_url = "http://localhost/~touche/Test_Contest"
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_add_edit_delete_team(self):
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
        
        driver.get(self.base_url + "/admin/setup_teams.php")
        driver.find_element_by_link_text("Sites").click()
        
        #clears all the sites in the contest, to ensure that there are none and avoid logic errors
        try: del_button = driver.find_element_by_link_text("Delete")
        except NoSuchElementException as e: del_button=None
        while del_button!=None:
            del_button.click()
            try: del_button = driver.find_element_by_link_text("Delete")
            except NoSuchElementException as e: del_button=None
        
        driver.find_element_by_link_text("Teams").click()
        #since there are no sites remaining, it should not be an option to fill out the forms yet.
        try: self.assertFalse(self.is_element_present(By.NAME, "team_name"))
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertRegexpMatches(driver.find_element_by_css_selector("div.innerglow").text, r"^[\s\S]*Sites[\s\S]*$")
        except AssertionError as e: self.verificationErrors.append(str(e))
        #these currently fail, but if there are no sites, we want the php to replace the forms with a message to "Create some Sites first" and this test is looking for the word "Sites" which will not otherwise appear on this page.
        
        driver.find_element_by_link_text("Sites").click()
        driver.find_element_by_name("site_name").clear()
        driver.find_element_by_name("site_name").send_keys("PrimarySite")
        driver.find_element_by_name("submit").click()
        driver.find_element_by_name("site_name").clear()
        driver.find_element_by_name("site_name").send_keys("SecondarySite")
        driver.find_element_by_name("submit").click()
        
        driver.find_element_by_link_text("Teams").click()
        driver.find_element_by_name("team_name").clear()
        driver.find_element_by_name("team_name").send_keys("Team 1")
        driver.find_element_by_name("organization").clear()
        driver.find_element_by_name("organization").send_keys("org")
        driver.find_element_by_name("username").clear()
        driver.find_element_by_name("username").send_keys("team1")
        driver.find_element_by_name("password").clear()
        driver.find_element_by_name("password").send_keys("password")
        Select(driver.find_element_by_name("site_id")).select_by_visible_text("PrimarySite")
        driver.find_element_by_name("coach_name").clear()
        driver.find_element_by_name("coach_name").send_keys("coach")
        driver.find_element_by_name("contestant_1_name").clear()
        driver.find_element_by_name("contestant_1_name").send_keys("a")
        driver.find_element_by_name("contestant_2_name").clear()
        driver.find_element_by_name("contestant_2_name").send_keys("b")
        driver.find_element_by_name("contestant_3_name").clear()
        driver.find_element_by_name("contestant_3_name").send_keys("c")
        #these are commented out to protect another test because the first page upon login is different if there's an option of having an alternate
        #driver.find_element_by_name("alternate_name").clear()
        #driver.find_element_by_name("alternate_name").send_keys("d")
        driver.find_element_by_name("email").clear()
        driver.find_element_by_name("email").send_keys("team1@team.com")
        driver.find_element_by_name("submit").click()
        try: self.assertRegexpMatches(driver.find_element_by_css_selector("div.col-md-5").text, r"^[\s\S]*Team 1[\s\S]*$")
        except AssertionError as e: self.verificationErrors.append(str(e))
       
        driver.find_element_by_name("team_name").clear()
        driver.find_element_by_name("team_name").send_keys("Team 2")
        driver.find_element_by_name("organization").clear()
        driver.find_element_by_name("organization").send_keys("org")
        driver.find_element_by_name("username").clear()
        driver.find_element_by_name("username").send_keys("team2")
        driver.find_element_by_name("password").clear()
        driver.find_element_by_name("password").send_keys("password")
        Select(driver.find_element_by_name("site_id")).select_by_visible_text("PrimarySite")
        driver.find_element_by_name("coach_name").clear()
        driver.find_element_by_name("coach_name").send_keys("coach")
        driver.find_element_by_name("contestant_1_name").clear()
        driver.find_element_by_name("contestant_1_name").send_keys("a")
        driver.find_element_by_name("contestant_2_name").clear()
        driver.find_element_by_name("contestant_2_name").send_keys("b")
        driver.find_element_by_name("contestant_3_name").clear()
        driver.find_element_by_name("contestant_3_name").send_keys("c")
        #same as above.
        #driver.find_element_by_name("alternate_name").clear()
        #driver.find_element_by_name("alternate_name").send_keys("e")
        driver.find_element_by_name("email").clear()
        driver.find_element_by_name("email").send_keys("team2@team.com")
        driver.find_element_by_name("submit").click()
        try: self.assertRegexpMatches(driver.find_element_by_css_selector("div.col-md-5").text, r"^[\s\S]*Team 2[\s\S]*$")
        except AssertionError as e: self.verificationErrors.append(str(e))
        
        driver.find_element_by_name("team_name").clear()
        driver.find_element_by_name("team_name").send_keys("Team 3")
        driver.find_element_by_name("organization").clear()
        driver.find_element_by_name("organization").send_keys("org")
        driver.find_element_by_name("username").clear()
        driver.find_element_by_name("username").send_keys("team2")#the duplicate username should not be allowed but it currently gets stored anyway
        driver.find_element_by_name("password").clear()
        driver.find_element_by_name("password").send_keys("password1")
        Select(driver.find_element_by_name("site_id")).select_by_visible_text("SecondarySite")
        driver.find_element_by_name("coach_name").clear()
        driver.find_element_by_name("coach_name").send_keys("coach")
        driver.find_element_by_name("contestant_1_name").clear()
        driver.find_element_by_name("contestant_1_name").send_keys("a")
        driver.find_element_by_name("contestant_2_name").clear()
        driver.find_element_by_name("contestant_2_name").send_keys("b")
        driver.find_element_by_name("contestant_3_name").clear()
        driver.find_element_by_name("contestant_3_name").send_keys("c")
        driver.find_element_by_name("alternate_name").clear()
        driver.find_element_by_name("alternate_name").send_keys("d")
        driver.find_element_by_name("email").clear()
        driver.find_element_by_name("email").send_keys("team3@team.com")
        driver.find_element_by_name("test_team").click()
        driver.find_element_by_name("submit").click()
        try: self.assertNotRegexpMatches(driver.find_element_by_css_selector("div.col-md-5").text, r"^[\s\S]*team 3[\s\S]*$")#team 3 should not be created and stored and appear on screen but it currently does, so this test fails.
        except AssertionError as e: self.verificationErrors.append(str(e))
        
        driver.find_element_by_xpath("//td[contains(text(),\"Team 1\")]/../td[3]/a").click()
        # ERROR: Caught exception [ERROR: Unsupported command [getSelectedLabel | name=site_id | ]]
        # the previous line's comment was auto-generated from the ide along with the code. idk if the test to make sure the correct site appeared in the site-selection drop down is running or not. It looks like not.
        Select(driver.find_element_by_name("site_id")).select_by_visible_text("PrimarySite")
        driver.find_element_by_name("submit").click()
        driver.find_element_by_xpath("//td[contains(text(),\"team 3\")]/../td[4]/a").click()
        try: self.assertNotRegexpMatches(driver.find_element_by_css_selector("div.col-md-5").text, r"^[\s\S]*team 3[\s\S]*$")
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
