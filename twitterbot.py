from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import os
import sys

os.system('cls')
WEB_PAGE = "https://twitter.com/login"
DRIVER_PATH = "DRIVER_LOC"
USER = "SUA_CONTA"
PASSWORD = "SUA_SENHA"
driver = webdriver.Chrome(executable_path=DRIVER_PATH)
driver.get(WEB_PAGE)
time.sleep(5)
print(' Conectado ao site Twitter! ')
time.sleep(2)
print('>>> Colocando usuário... ')
time.sleep(1)
user_input = driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div[2]/form/div/div[1]/label/div/div[2]/div/input')
user_input.send_keys(USER)
print('>>> Login colocado! ')
time.sleep(1)
print('>>> Colocando senha...')
time.sleep(1)
user_pass = driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div[2]/form/div/div[2]/label/div/div[2]/div/input')
user_pass.clear()
time.sleep(1)
user_pass.send_keys(PASSWORD)
print('>>> Senha colocada!')
time.sleep(1)
user_pass.send_keys(Keys.ENTER)
print("\n Espere...")
time.sleep(5)
print("\n>>> Login feito com sucesso")
time.sleep(1)
print('\n Limpando tela...')
time.sleep(1.5)
os.system('cls')

contador = 1

while (contador < x ):
    print(' _____________________________________________________________')
    print('\n\n\033[32m>>>\033[m Escrevendo tweet...')
    tweet = driver.find_element_by_xpath('''//*[@id='react-root']/div/div/div[2]/main/div/div/div/div/div
                                                      /div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[1]/div/div
                                                      /div/div/div/div/div/div/div/div[1]/div/div/div/div[2]/div
                                                      /div/div/div''')
    tweet.send_keys("'-'-'-'-'-'-'-':", contador)

    print(">>> click tweet")
    time.sleep(2)
    tweet_btn = driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[4]/div/div/div[2]/div[3]/div/span/span')
    tweet_btn.click()
    print(">>> tweet sent")
    contador = contador + 1 
    print('\n  Número de vezes: ', contador)
    time.sleep(2)
    
else:
    driver.quit()
    sys.exit()

