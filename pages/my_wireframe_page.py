from pyshadow.main import Shadow
from selenium.webdriver.support import expected_conditions as EC

from selenium.common import NoAlertPresentException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from browser import Browser
from time import sleep
import logging



class My_wireframe(Browser):
    OFFER_CLOSE_BUTTON = (By.ID, 'sp_close_bar')
    OFFER = (By.ID, 'sp_widget_area')

    def i_see_the_offer(self):
        try:
            offer = WebDriverWait(self.chrome, 10).until(EC.presence_of_element_located(self.OFFER))
            assert offer.is_displayed()
            logging.info("The offer is visible")
        except Exception as i:
            logging.error(f"An error occurred while checking the offer visibility : {str(i)}")


    def close_the_offer(self):
        try:
            offer_close = self.chrome.find_element(*self.OFFER_CLOSE_BUTTON)
            offer_close.click()
            logging.info("The offer was successfully closed ")
        except Exception as e:
            logging.error(f"An error occurred while closing the offer : {str(e)}")

    def offer_is_closed(self):
        try:
            offer1 = WebDriverWait(self.chrome, 10).until(EC.presence_of_element_located(self.OFFER))
            assert not offer1.is_displayed()
            logging.info("The offer is no longer displayed")
        except Exception as e:
            logging.error(f"An error occurred while checking the displayed offer")