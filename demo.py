from selenium import webdriver
options = webdriver.ChromeOptions()
options.add_argument('--headless')
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')
# open it, go to a website, and get results
browser = webdriver.Chrome('chromedriver',options=options)
states = ['ANDAMAN & NICOBAR ISLANDS']
    

browser.get('https://www.icicilombard.com/IL-HEALTH-CARE/Customer/GetHospitalList')

hospitalData = []

hos = dict()

for state in states:
    
    select = Select(browser.find_element_by_id('ddlStateList'))
    select.select_by_visible_text(state)
    table = browser.find_element_by_id('ddlStateList')
    div = browser.find_element_by_id('divSearchData')
    hospital_names_list=browser.find_elements_by_class_name('clsHospName')
    address_names_list=browser.find_elements_by_class_name('clsAddress')
    city_names_list=browser.find_elements_by_class_name('clsCity')
    area_names_list=browser.find_elements_by_class_name('clsArea')
    state_names_list=browser.find_elements_by_class_name('clsState')
    for i in range(len(hospital_names_list)):
      tempData = {
        "name": hospital_names_list[i].text,
        "city": city_names_list[i].text,
        "area":  area_names_list[i].text,
        "state":  state_names_list[i].text
      }
      hospitalData.append(tempData)
    print(hospitalData)
    print(len(hospitalData))
