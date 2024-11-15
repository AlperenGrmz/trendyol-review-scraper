from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import time
import pandas as pd
import requests
import random

def fetch_categories(base_url):
    driver.get(base_url)

    try:
        close_button = WebDriverWait(driver, 30).until(
            EC.element_to_be_clickable((By.CLASS_NAME, "modal-close"))
        )
        close_button.click()
    except Exception as e:
        print(f"Pop-up kapatılamadı: {e}")
    
    try:
        menu_element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, "onboarding"))  
        )
        
        actions = ActionChains(driver)
        actions.move_to_element(menu_element).perform()
        
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, "category-title"))
        )
    except Exception as e:
        print(f"Kategoriler yüklenemedi: {e}")
        return []


    categories = driver.find_elements(By.CLASS_NAME, "category-title")
    subcategories = []

    for category in categories:
        try:
            actions.move_to_element(category).perform()
            time.sleep(1)  

            html_content = driver.page_source
            soup = BeautifulSoup(html_content, 'html.parser')
            
            subcategory_elements = soup.find_all("a", class_="category-titles")
            for category in subcategory_elements:
                category_name = category.get_text(strip=True)
                category_link = category['href']
                subcategories.append({"name": category_name, "link": category_link})
            
            for category in subcategories:
                print(f"Name: {category["name"]} Link: {category["link"]}") 
            
        except Exception as e:
            print(f"{category.text} kategorisine ulaşırken hata oluştu: {e}")
    
    return subcategories

def rating_count(div):
    i = 0
    star_w = div.find_all("div", class_="full")
    for full in star_w:
        style = full.get("style")
        if style:
            styles = style.split(";")
            width = styles[0].split(":")[1].replace("%", "").replace("px", "").strip()
            try:
                if int(width) == 100:
                    i += 1
            except ValueError:
                print(f"Geçersiz width değeri: {width}")
    return i

options = Options()
options.add_argument("--headless")
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")


base_url = "https://www.trendyol.com/"
driver = webdriver.Chrome(options=options)

categories = fetch_categories(base_url)

product_links = []

for category in categories:
    category_url = category['link']
    print(f"İstek atılan kategori URL: {category_url}")

    for page_num in range(1, 2):
        page_url = f"{category_url}?pi={page_num}"
        print(f"İstek atılan sayfa URL: {page_url}")

        response = requests.get(page_url)
        soup = BeautifulSoup(response.content, "html.parser")
        
        link_array = soup.find_all("div", class_="product-down")
        for product in link_array:
            a_tag = product.find("a")
            if a_tag:
                product_link = "https://www.trendyol.com" + a_tag.get("href")
                print(product_link)
                product_links.append(product_link)
        
        wait_time = random.uniform(5, 10)
        print(f"{wait_time:.2f} saniye bekleniyor...")
        time.sleep(wait_time)


def scarape_comments(product_links):
    for product_link in product_links:
        driver.get(product_link + "/yorumlar")
        wait_time = random.uniform(5, 10)
        time.sleep(wait_time)
        html_content = driver.page_source
        soup = BeautifulSoup(html_content, 'html.parser')
        divs = soup.find_all("div", class_="comment")

        for div in divs:
            comment_text = div.find("div", class_="comment-text")
            comment_rating = div.find("div", class_="comment-rating")
            rating = rating_count(comment_rating)
    
            if comment_text:
                comments_data.append({
                "Rating": rating,
                "Comment": comment_text.get_text(strip=True)
            })
            print(f"Rating: {rating} Comment: {comment_text.get_text(strip=True)}\n")

comments_data = []
scarape_comments(product_links)
df = pd.DataFrame(comments_data)
df.to_csv('comments.csv', index=False)

driver.quit()
