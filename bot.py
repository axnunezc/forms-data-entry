from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

class FormsSheetsBot:
    def __init__(self):
        self.chrome_driver_path = "/Users/axel/Downloads/chromedriver"
        self.driver = webdriver.Chrome(executable_path=self.chrome_driver_path)
        
    def submit_forms(self, forms_url, address_list, price_list, link_list):
        for index in range(len(address_list)):
            self.driver.get(forms_url)
            WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((By.XPATH, "//input[@aria-labelledby='i1']")))
            
            # Provide first answer
            sleep(1)
            first_answer_field = self.driver.find_element(By.XPATH, "//input[@aria-labelledby='i1']")
            first_answer_field.send_keys(address_list[index])
            
            # Provide second answer
            sleep(1)
            second_answer_field = self.driver.find_element(By.XPATH, "//input[@aria-labelledby='i5']")
            second_answer_field.send_keys(price_list[index])
            
            # Provide third answer
            sleep(1)
            third_answer_field = self.driver.find_element(By.XPATH, "//input[@aria-labelledby='i9']")
            third_answer_field.send_keys(link_list[index])
            
            # Locate and click submit button
            sleep(1)
            self.driver.find_elements(By.XPATH, "//div[@role='button']")[0].click()
            
            sleep(1)
    