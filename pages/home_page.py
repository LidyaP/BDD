from selenium.webdriver.support import expected_conditions as EC

from selenium.common import NoAlertPresentException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from browser import Browser
from time import sleep
import logging


class Home_page(Browser):
    LOGIN_BUTTON = (By.ID, "mfHeaderLoginBtn")
    EMAIL = (By.ID, "logusername")
    PASSWORD = (By.ID, "logpassword")
    SIGN_IN = (By.ID, 'login_btn')

    def open_home_page(self):
        self.chrome.get("https://mockflow.com/")

    def click_login_button(self):
        max_try = 3
        attempts = 0
        while attempts < max_try:
            try:
                login_button = self.chrome.find_element(*self.LOGIN_BUTTON)
                if login_button:
                   login_button.click()
                   sleep(1)
                   break
                else:
                    raise AssertionError("Login button element not found")
            except Exception as i:
                logging.error(f"An error occurred while clicking the login button : {str(i)}")
                attempts+=1

    def insert_email(self):
        try:
            user_email = self.chrome.find_element(*self.EMAIL)
            user_email.send_keys("rapunzell2000@yahoo.com")
            sleep(1)
        except Exception as i:
            logging.error(f"An error occurred while inserting the email : {str(i)}")

    def insert_invalid_password(self, password):
        try:
            user_password = self.chrome.find_element(*self.PASSWORD)
            user_password.send_keys(password)
            sleep(1)
        except Exception as i:
            logging.error(f"An error occurred while inserting the password : {str(i)}")

    def click_singin_button(self):
        try:
            sign_in_button = self.chrome.find_element(*self.SIGN_IN)
            sign_in_button.click()
            sleep(1)
        except Exception as i:
            logging.error(f"An error occurred while clicking the sing in button : {str(i)}")

    def login_failed(self, error_message):
        WebDriverWait(self.chrome, 10).until(EC.alert_is_present())
        try:
            alerta = self.chrome.switch_to.alert
            alerta_text = alerta.text
            assert error_message in alerta_text
            alerta.accept()#nu am pus accept alert
            logging.info("Login failed {}".format(error_message))#nu pusesem {} dupa failed
        except NoAlertPresentException:
            assert False, "Expected alert not found"
        sleep(1)

    def insert_password(self):
        try:
            userpassword = self.chrome.find_element(*self.PASSWORD)
            userpassword.send_keys("Ianuarie_01")
            sleep(1)
        except Exception as i:
            logging.error(f"An error occurred while inserting the password: {str(i)}")


    def my_account_page(self):
        account_url = "https://wireframepro.mockflow.com/"
        assert self.chrome.current_url == account_url
        logging.info("Test passed : Current URL match the expected account URL")
        sleep(1)








