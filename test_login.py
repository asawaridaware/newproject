

#from telnetlib import EC
#import pytest
#from conftest import setup
#from conftest  import By
#from selenium.webdriver.support import expected_conditions as EC

import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

@pytest.mark.usefixtures("setup")
class TestLoginAndClosePopup:
    def test_login(self):
        # login details
        driver = self.driver #new
       #wait = self.wait
        
        
        username = self.driver.find_element(By.XPATH, "//input[@id='identity']")
        username.send_keys(8805482636)

        password = self.driver.find_element(By.XPATH, "//input[@id='password']")
        password.send_keys(12345)

        time.sleep(1)
        login_button = self.driver.find_element(By.XPATH, "//button[@id='button-login']")
        login_button.click()

        time.sleep(1)
        dropdown = self.driver.find_element(By.XPATH, "//select[@id='multipleFlats']")
        dropdown.click()

        select_account = self.driver.find_element(By.XPATH, "//option[@value='201705']")
        select_account.click()

        time.sleep(1)
        login_button = self.driver.find_element(By.XPATH, "//button[@id='button-login']")
        login_button.click()

        
        wait = WebDriverWait(driver, 30)
        
        close_popup = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@class='pull-left btn ng-binding']")))
        
        time.sleep(10)
        close_popup.click()

if __name__ == "__main__":

    pytest.main()



































