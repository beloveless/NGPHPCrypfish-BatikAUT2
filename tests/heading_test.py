import unittest
import os
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

class BatikWebsiteTestCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        # Inisialisasi pengaturan untuk browser Firefox
        option = webdriver.FirefoxOptions()
        option.add_argument('--headless')  # Menjalankan browser tanpa antarmuka grafis
        cls.browser = webdriver.Firefox(options=option)

        try:
            cls.url = os.environ['URL']  # Mengambil URL dari variabel lingkungan
        except:
            cls.url = "http://localhost"

    def test(self):
        # Menjalankan serangkaian pengujian
        self.page_heading_check()
        self.add_cart()
        self.remove_cart_check()

    def page_heading_check(self):  
        access_url = 'http://' + self.url + '/index.php'
        self.browser.get(access_url)

        heading_element = self.browser.find_element(By.TAG_NAME, 'h1')
        print("Heading text:", heading_element.text)
        self.assertIn('WELCOME TO\nSTORE BATIK TULIS', heading_element.text)  

    def add_cart(self):  
        access_url = 'http://' + self.url + '/index.php'
        self.browser.get(access_url)

        self.browser.find_element(By.XPATH, '//*[@id="navbarNav"]/ul/li[2]/a').click() 
        time.sleep(1)
        self.browser.find_element(By.NAME, 'Add_To_Cart').click() 
        self.browser.find_element(By.CLASS_NAME, 'btn-outline-success').click() 

        cart=self.browser.find_element(By.XPATH, '/html/body/div/div/div[2]/table/tbody/tr/td[1]')
        self.assertIn('1', cart.text)  

    def remove_cart_check(self):  
        access_url = 'http://' + self.url + '/mycart.php'
        self.browser.get(access_url)

        self.browser.find_element(By.NAME, 'Remove_Item').click() 
        total=self.browser.find_element(By.ID, 'gtotal')
        self.assertIn('0', total.text)
    
    @classmethod
    def tearDownClass(cls):
        cls.browser.quit()

if __name__ == '__main__':
    unittest.main(verbosity=2, warnings='ignore')
