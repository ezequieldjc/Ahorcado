import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

#Driver para Chrome v83
#https://chromedriver.storage.googleapis.com/index.html?path=83.0.4103.39/

class prueba_unittest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(executable_path=r"C:\chromedriver_win32\chromedriver.exe") 

    def test_buscar(self):
        driver = self.driver
        driver.get("https://agiles2020-ahorcado.herokuapp.com/play/")
        self.assertIn("Ahorcado", driver.title)
        elemento = driver.find_element_by_name("name")
        elemento.send_keys("gabi")
        elemento.send_keys(Keys.RETURN)
        time.sleep(5)
        assert "No se Encontro el elemento." not in driver.page_source
    
    def tearDown(self):
        self.driver.close()

if __name__ == '__main__':
    unittest.main()