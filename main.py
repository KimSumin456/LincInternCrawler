import os

import selenium
from selenium.webdriver import Chrome
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

import time

def OpenPage(target_url, id, pw):
    driver.get(target_url)
    time.sleep(1)

    element_id = driver.find_element(By.ID, 'userId')
    element_password = driver.find_element(By.ID, 'password')
    element_login = driver.find_element(By.ID, 'loginSubmit')
    element_id.send_keys(id)
    element_password.send_keys(pw)
    element_login.click()

    '''
    element_companySearch = driver.find_element(By.XPATH, '//*[@id="nav"]/li[2]/ul/li/ul/li[2]/a') # 비밀번호 변경 메시지 뜨면 오류 남
    element_companySearch.click()

    element_major = driver.find_element(By.NAME, 'majorStr')
    element_major.send_keys(major)
    element_major.send_keys(Keys.ENTER)
    time.sleep(1)
    '''
    
    return

def Crawl_companyInfo(majorStr, filename):
    company_data_texts = ""

    driver.get('https://how.ajou.ac.kr/student/manage/search/index.do?page='+'1'+'&jsSeqTmp=72&jsSeq=72&currentList=1&majorStr=' + majorStr)
    paging = driver.find_element(By.CLASS_NAME, 'paging').find_elements(By.TAG_NAME, 'a')
    page_num = int(paging[-2].text)

    for index_page in range(1, page_num+1):
        driver.get('https://how.ajou.ac.kr/student/manage/search/index.do?page='+str(index_page)+'&jsSeqTmp=72&jsSeq=72&currentList=1&majorStr='+majorStr)
        time.sleep(1)

        companies = driver.find_element(By.CLASS_NAME, 'tbl_type01').find_element(By.TAG_NAME, 'tbody').find_elements(By.TAG_NAME, 'tr')
        for index, value in enumerate(companies):
            company_data_texts += '\n=========='
            #print('\n=====회사구분선=====')
            companyName = value.find_elements(By.TAG_NAME, 'td')[1]
            #print(companyName.text)
            company_data_texts += companyName.text + '==========\n'
            companyName.click()
            time.sleep(1)

            try:
                companyInfo = driver.find_element(By.CLASS_NAME, 'tbl_type02').find_element(By.TAG_NAME, 'tbody')#.find_elements(By.TAG_NAME, "tr")
            except selenium.common.exceptions.NoSuchElementException:
                company_data_texts += '\n\n\n'
                continue
            else:
                #print(companyInfo.text)
                company_data_texts += companyInfo.text
                time.sleep(1)

            element_closeCompany = driver.find_element(By.XPATH, '/html/body/div[4]/div[3]/div/button')
            element_closeCompany.click()
            time.sleep(1)

            company_data_texts += '\n\n\n\n'

    f = open(filename, 'w', encoding='UTF-8')
    f.write(company_data_texts)
    f.close()

    return

options = Options()
options.add_argument('incognito')  # 시크릿 모드 실행
options.add_argument('--start-maximized')  # 최대화
options.add_experimental_option('excludeSwitches', ['enable-logging']) # https://stackoverflow.com/questions/69370457/google-chrome-always-crashes-after-opening-a-page
driver = Chrome("chromedriver_win32\chromedriver", options=options) # deperactionWarning 뜸

id = input('현장실습지원센터(how.ajou.ac.kr) 아이디를 입력하세요: ')
pw = input('현장실습지원센터(how.ajou.ac.kr) 비밀번호를 입력하세요: ')
major = input("전공을 입력하세요: ")

OpenPage('https://how.ajou.ac.kr/jsp/sso/service_front.jsp', id, pw)
Crawl_companyInfo(major, major+'CompanyData.txt')
