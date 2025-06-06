import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import colorama
from colorama import Fore, Style
import os
from pystyle import Center, Colorate, Colors, Anime
import colorama
import os

while True:
    os.system('cls')
    print(Colorate.Horizontal(Colors.blue_to_cyan,"""
    
        ____      __       ___  __   
       /  _/___  / /____  / / |/ /   
       / // __ \/ __/ _ \/ /|   /    
     _/ // / / / /_/  __/ //   |     
    /___/_/ /_/\__/\___/_//_/|_|_____
                              /_____/
    
        ┏━━━━━━━━━━━━━━━━━━━━━┓
        ┃    Author : Ego     ┃
        ┃ github.com/EgooDev  ┃
        ┗━━━━━━━━━━━━━━━━━━━━━┛
                              
    """))
    
    search_term = input("Your search: ")
    result_count = int(input("How many results to display: "))
    print(Colors.green,"Connecting...")
    options = uc.ChromeOptions()
    options.headless = True 
    options.add_argument("--headless=new") 
    driver = uc.Chrome(options=options)
    
    try:
        driver.get("https://intelx.io")
        print(Fore.CYAN + "Searching...")
        print(Fore.RED + "IF YOU GET ERROR USE VPN OR PROXY" + Fore.RESET)
        search_box = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "Term"))
        )
        search_box.send_keys(search_term)
        search_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, "btnSearch"))
        )
        search_button.click()
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, "search-result"))
        )
    
        while True:
            results = driver.find_elements(By.CLASS_NAME, "search-result")
            if len(results) >= result_count:
                break  
            time.sleep(2) 
    
        print(Fore.GREEN + f"\nTotal results found: {len(results)}\n" + Fore.RESET)
    
        for index, result in enumerate(results[:result_count]):  
            print(f"Result {index + 1}: {result.text}\n" + "-"*50)
    
        input(Fore.YELLOW + "\nPress Enter to exit..." + Fore.RESET)
    
    finally:
        driver.quit()
    
