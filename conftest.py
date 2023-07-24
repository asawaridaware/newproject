
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions as EC
import time
from selenium.webdriver.support.wait import WebDriverWait



@pytest.fixture(scope="class")
def setup(request):


     # Open a URL
  #driver=webdriver.Chrome(executable_path='C:\chromedriver(py)\chromedriver.exe') 

  driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())


  wait = WebDriverWait(driver,10)  
  driver.get('https://test.isocietymanager.com/isocietymanager.com/login.html')
  print(driver.title)
  driver.maximize_window()
  request.cls.driver = driver   #this driver should availabe for every requsting class(who is calling this particular fixture)
  request.cls.wait = wait 
  yield
  driver.close()