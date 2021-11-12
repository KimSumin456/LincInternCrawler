import os

import selenium
from selenium.webdriver import Chrome
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

import time

def OpenPage(target_url, id, pw, major):
    driver.get(target_url)
    time.sleep(1)

    element_id = driver.find_element(By.ID, "userId")
    element_password = driver.find_element(By.ID, "password")
    element_login = driver.find_element(By.ID, "loginSubmit")
    element_id.send_keys(id)
    element_password.send_keys(pw)
    element_login.click()

    element_companySearch = driver.find_element(By.XPATH, '//*[@id="nav"]/li[2]/ul/li/ul/li[2]/a') # 비밀번호 변경 메시지 뜨면 오류 남
    element_companySearch.click()

    element_major = driver.find_element(By.NAME, "majorStr")
    element_major.send_keys(major)
    element_major.send_keys(Keys.ENTER)
    
    return

def Crawl_companyInfo():
    return

options = Options()
options.add_argument('incognito')  # 시크릿 모드 실행
options.add_argument("--start-maximized")  # 최대화
options.add_experimental_option('excludeSwitches', ['enable-logging']) # https://stackoverflow.com/questions/69370457/google-chrome-always-crashes-after-opening-a-page
driver = Chrome("chromedriver_win32\chromedriver", options=options) # deperactionWarning 뜸

id = input("현장실습지원센터(how.ajou.ac.kr) 아이디를 입력하세요: ")
pw = input("현장실습지원센터(how.ajou.ac.kr) 비밀번호를 입력하세요: ")
major = input("전공을 입력하세요: ")

OpenPage("https://how.ajou.ac.kr/jsp/sso/service_front.jsp", id, pw, major)
Crawl_companyInfo()
