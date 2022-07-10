from selenium import webdriver
import requests
from bs4 import BeautifulSoup
from selenium.webdriver.common.keys import Keys

test_cnt = 1
driver = webdriver.Chrome("C:/Users/wjdtk/Desktop/selenium/chromedriver.exe")
site_url = "http://127.0.0.1/xssboard/"
driver.get(site_url)
print("\n======== CREHACKTIVE INSECURE WEB-SITE QA TEST START ========")
print(f"Test site Title : {driver.title}\n") # 웹 사이트 타이틀 출력

############################## main page test ########################################################

main_url = "http://127.0.0.1/xssboard/"
driver.get(main_url)
get_url = main_url

response = requests.get(get_url)
get_text = response.text
soup = BeautifulSoup(get_text, "html.parser")

print(f"Test Number : {test_cnt}")
print("======== Main Page Test ========")
print(f"Current url : {driver.current_url}") # 현재 위치한 url 출력

if response.status_code == 200: # 성공적으로 페이지 로드 시 
    print(f"Test result : {soup.find('h1').text.strip()} 200 OK\n") # 페이지의 h1 태그 텍스트와 200 OK 문구 출력
else:
    print(f"Test result : {soup.find_next('h1')} page load Fail\n")

test_cnt += 1
############################# Board page test #######################################################

board_url = "http://127.0.0.1/xssboard/index.php?page=board"
driver.get(board_url)
get_url = board_url

response = requests.get(get_url)
get_text = response.text
soup = BeautifulSoup(get_text, "html.parser")

print(f"Test Number : {test_cnt}")
print("======== Board Page Test ========")
print(f"Current Url : {driver.current_url}") # 현재 위치한 url 출력

if response.status_code == 200: # 성공적으로 페이지 로드 시 
    print("Test result : Board 200 OK\n") # 게시판은 h1이 없으므로 Board라고 지정, 200 OK 문구 출력
else:
    print("Test result : Board page load Fail\n")

test_cnt += 1
############################# Join page test #######################################################

join_url = "http://127.0.0.1/xssboard/index.php?page=join"
driver.get(join_url)
get_url = join_url

response = requests.get(get_url)
get_text = response.text
soup = BeautifulSoup(get_text, "html.parser")

print(f"Test Number : {test_cnt}")
print("======== Join Page Test ========")
print(f"Current url : {driver.current_url}") # 현재 위치한 url 출력

if response.status_code == 200: # 성공적으로 페이지 로드 시 
    print(f"Test result : {soup.find('h1').text.strip()} 200 OK\n") # 페이지의 h1 태그 텍스트와 200 OK 문구 출력
else:
    print(f"Test result : {soup.find_next('h1')} page load Fail\n")

test_cnt += 1
############################# Move from Main to Board page test #######################################################

board_url = "http://127.0.0.1/xssboard/index.php"
driver.get(board_url)

print(f"Test Number : {test_cnt}")
print("======== Move from Main Page to Board Page Test ========")
print(f"Current Url : {driver.current_url}\n") # 현재 위치한 url 출력

driver.find_element("xpath", "/html/body/div[1]/nav/a[2]").click()

print(f"After click 'Board' button")
print(f"Current Url : {driver.current_url}") # 현재 위치한 url 출력

get_url = driver.current_url
response = requests.get(get_url)
get_text = response.text
soup = BeautifulSoup(get_text, "html.parser")

if response.status_code == 200: # 성공적으로 페이지 로드 시 
    print("Test result : Board 200 OK\n")
else:
    print("Test result : Board 200 Fail\n")

test_cnt += 1
############################# Move from Main to Join page test #######################################################

board_url = "http://127.0.0.1/xssboard/index.php?page=board"
driver.get(board_url)

print(f"Test Number : {test_cnt}")
print("======== Move from Main Page to Join Page Test ========")
print(f"Current Url : {driver.current_url}\n") # 현재 위치한 url 출력

driver.find_element("xpath", "/html/body/div[1]/nav/a[3]").click()

print(f"After click 'Join' button")
print(f"Current Url : {driver.current_url}") # 현재 위치한 url 출력

get_url = driver.current_url
response = requests.get(get_url)
get_text = response.text
soup = BeautifulSoup(get_text, "html.parser")

if response.status_code == 200: # 성공적으로 페이지 로드 시 
    print(f"Test result : {soup.find('h1').text.strip()} 200 OK\n")
else:
    print(f"Test result : {soup.find_next('h1')} page load Fail\n")

test_cnt += 1
############################# Move from Board to Main page test #######################################################

board_url = "http://127.0.0.1/xssboard/index.php?page=board"
driver.get(board_url)

print(f"Test Number : {test_cnt}")
print("======== Move from Board Page to Main Page Test ========")
print(f"Current Url : {driver.current_url}\n") # 현재 위치한 url 출력

driver.find_element("xpath", "/html/body/div[1]/nav/a[1]").click()

print(f"After click 'Home' button")
print(f"Current Url : {driver.current_url}") # 현재 위치한 url 출력

get_url = driver.current_url
response = requests.get(get_url)
get_text = response.text
soup = BeautifulSoup(get_text, "html.parser")

if response.status_code == 200: # 성공적으로 페이지 로드 시 
    print(f"Test result : {soup.find('h1').text.strip()} 200 OK\n")
else:
    print(f"Test result : {soup.find_next('h1')} page load Fail\n")

test_cnt += 1
############################# Move from Board to Join page test #######################################################

board_url = "http://127.0.0.1/xssboard/index.php?page=board"
driver.get(board_url)

print(f"Test Number : {test_cnt}")
print("======== Move from Board Page to Join Page Test ========")
print(f"Current Url : {driver.current_url}\n") # 현재 위치한 url 출력

driver.find_element("xpath", "/html/body/div[1]/nav/a[3]").click()

print(f"After click 'Join' button")
print(f"Current Url : {driver.current_url}") # 현재 위치한 url 출력

get_url = driver.current_url
response = requests.get(get_url)
get_text = response.text
soup = BeautifulSoup(get_text, "html.parser")

if response.status_code == 200: # 성공적으로 페이지 로드 시 
    print(f"Test result : {soup.find('h1').text.strip()} 200 OK\n")
else:
    print(f"Test result : {soup.find_next('h1')} page load Fail\n")

test_cnt += 1
############################# Move from Join to Main page test #######################################################

board_url = "http://127.0.0.1/xssboard/index.php?page=join"
driver.get(board_url)

print(f"Test Number : {test_cnt}")
print("======== Move from Join Page to Main Page Test ========")
print(f"Current Url : {driver.current_url}\n") # 현재 위치한 url 출력

driver.find_element("xpath", "/html/body/div[1]/nav/a[1]").click()

print(f"After click 'Home' button")
print(f"Current Url : {driver.current_url}") # 현재 위치한 url 출력

get_url = driver.current_url
response = requests.get(get_url)
get_text = response.text
soup = BeautifulSoup(get_text, "html.parser")

if response.status_code == 200: # 성공적으로 페이지 로드 시 
    print(f"Test result : {soup.find('h1').text.strip()} 200 OK\n")
else:
    print(f"Test result : {soup.find_next('h1')} page load Fail\n")

test_cnt += 1
############################# Move from Join to Board page test #######################################################

board_url = "http://127.0.0.1/xssboard/index.php?page=join"
driver.get(board_url)

print(f"Test Number : {test_cnt}")
print("======== Move from Join Page to Main Page Test ========")
print(f"Current Url : {driver.current_url}\n") # 현재 위치한 url 출력

driver.find_element("xpath", "/html/body/div[1]/nav/a[2]").click()

print(f"After click 'Board' button")
print(f"Current Url : {driver.current_url}") # 현재 위치한 url 출력

get_url = driver.current_url
response = requests.get(get_url)
get_text = response.text
soup = BeautifulSoup(get_text, "html.parser")

if response.status_code == 200: # 성공적으로 페이지 로드 시 
    print("Test result : Board 200 OK\n")
else:
    print("Test result : Board 200 Fail\n")

test_cnt += 1

print("======== Test End ========")