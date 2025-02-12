import time
from csv import writer
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Thiết lập Chrome Options để tắt thông báo
chrome_options = Options()
chrome_options.add_argument("--disable-notifications")  # Tắt thông báo trình duyệt
chrome_options.add_argument("--disable-popup-blocking")  # Chặn popup không mong muốn
chrome_options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36")
chrome_options.add_argument("--disable-blink-features=AutomationControlled")  # Loại bỏ thuộc tính automation
chrome_options.add_argument("--start-maximized")


# Khởi tạo trình duyệt với Chrome Options
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
driver.get("https://www.vlance.vn/viec-lam-freelance")

def search_role(role):
    search = driver.find_element(By.ID, "input-search-text")
    search.send_keys(role)
    search.send_keys(Keys.ENTER)

def main():
    title = "CNTT"
    search_role(title)
    time.sleep(5)
    try:
        main = WebDriverWait(driver, 10).until(
            ec.presence_of_element_located((By.CSS_SELECTOR, ".content-section.content-fix"))
        )
        jobs = main.find_elements(By.CSS_SELECTOR, ".fr-info.span12")

        header = ['Title', 'Role', 'Salary', 'Address', 'Time left']
        with open('job.csv', 'w', newline='', encoding='utf-8') as f:
            writer_csv = writer(f)
            writer_csv.writerow(header)
            
            for job in jobs:
                title = job.find_element(By.CSS_SELECTOR, "a")
                role = job.find_element(By.CSS_SELECTOR, "span.category")
                salary = job.find_element(By.CSS_SELECTOR, "span.history-job.hidejs")
                address = job.find_element(By.CSS_SELECTOR, "span.location")
                time_left = job.find_element(By.CSS_SELECTOR, "div.remain")
                data = [title.text, role.text, salary.text, address.text, time_left.text]
                print(data, end='\n===========\n')
                writer_csv.writerow(data)
    
    finally:
        driver.quit()

if __name__ == "__main__":
    main()
