import pandas as pd
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

df = pd.read_csv (r"\\uk.wspgroup.com\Central Data\Projects\70075xxx\70075873 - Wokingham-WKH-000000-2021-LCWIP2\03 WIP\Smart Consulting GIS\XLS\Major_Development_Sites_Adjusted.csv",usecols = ['WBC_APP_NO_unique'])

developments = df ['WBC_APP_NO_unique']
print(developments)
#N = 1
N = len(developments)
Records_found=[]

for x in range (N):
  chrome_options = Options()
  global browser
  browser = webdriver.Chrome(r'C:\Users\UKCJR003\Documents\Chrome_Drive\chromedriver.exe')
  browser.get('https://planning.wokingham.gov.uk/FastWebPL/welcome.asp')
  name = developments [x]
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

  for links in attribute_value:
      records = links.get_attribute("outerHTML")
      Records_found.insert(x,records)


Developments_zip = zip(developments,Records_found)
Developments_list = list((Developments_zip))
Developments_w_Records = pd.DataFrame(Developments_list)
#
# print (resultdf)
#
Developments_w_Records.to_csv(r"\\uk.wspgroup.com\Central Data\Projects\70075xxx\70075873 - Wokingham-WKH-000000-2021-LCWIP2\03 WIP\Smart Consulting GIS\XLS\Major_Development_Sites_Records_added.csv");