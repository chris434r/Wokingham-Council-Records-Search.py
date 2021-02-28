import pandas as pd
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


chromedriver_location = r"/Users/chrisryan/Chrome Driver/chromedriver"
df = pd.read_csv (r"/Users/chrisryan/Wokingham-Council-Records-Search.py/Input data/"
                  r"Major_Development_Sites_Adjusted.csv", usecols = ['WBC_APP_NO_unique'])

development_sites = df ['WBC_APP_NO_unique']

N = 1
#N = len(development_sites)
Records_found=[]

for x in range (N):
  chrome_options = Options()
  global browser
  browser = webdriver.Chrome(chromedriver_location)
  browser.get('https://planning.wokingham.gov.uk/FastWebPL/welcome.asp')
  name = development_sites [x]
  searchbar = browser.find_element_by_id ('ApplicationNumber')
  searchbar.click ()
  searchbar.send_keys (name)
  sendbutton =browser.find_element_by_id ('Submit')
  sendbutton.click()
  while True:
      try:
         attribute_value = WebDriverWait(browser, 2).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="page-body"]/table[2]/tbody/tr[4]/td'))).find_elements_by_xpath('/html/body/div/div[1]/div/div/table[2]/tbody/tr[4]/td')
         break
      except (TimeoutError):
          print('Timeout Error')
          break
      except (Exception):
          print ('Exception Error')
          break
      except (RuntimeError):
          print('Runtime error')
          break
      except (TypeError):
          print ('TypeError')
          break
      except (NameError):
          print ('Name Error')
          break

      records = links.get_attribute("outerHTML")
      Records_found.insert(x,records)


Developments_zip = zip(development_sites,Records_found)
Developments_list = list((Developments_zip))
Developments_w_Records = pd.DataFrame(Developments_list)
#
# print (resultdf)
#
Developments_w_Records.to_csv(r"/Users/chrisryan/Wokingham-Council-Records-Search.py/Output/Major_Development_Sites_Records_added.csv");