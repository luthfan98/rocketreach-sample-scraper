from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd
import time

# Setup Chrome driver
driver = webdriver.Chrome()

# Buka RocketReach login page
driver.get("https://rocketreach.co/login")

print("Please login manually to your RocketReach account...")

# Tunggu sampai user login manual
input("Press Enter after you have logged in manually...")

# Setelah login, misal buka search page
driver.get("https://rocketreach.co/search/all/companies")

# Tunggu page loading
time.sleep(5)

# Ambil contoh data dari search results
contacts = []

cards = driver.find_elements(By.CLASS_NAME, 'result-card')  # Sesuaikan dengan RocketReach real class
for card in cards[:5]:  # Misal ambil 5 kontak untuk contoh
    try:
        full_name = card.find_element(By.CLASS_NAME, 'name').text
        job_title = card.find_element(By.CLASS_NAME, 'title').text
        company = card.find_element(By.CLASS_NAME, 'company-name').text
        email = card.find_element(By.CLASS_NAME, 'email').text
        linkedin = card.find_element(By.CLASS_NAME, 'linkedin').get_attribute('href')
        
        contacts.append({
            "Full Name": full_name,
            "Job Title": job_title,
            "Company Name": company,
            "Email Address": email,
            "LinkedIn Profile": linkedin
        })
    except Exception as e:
        print("Error:", e)

# Simpan ke CSV
df = pd.DataFrame(contacts)
df.to_csv('output/rocketreach_contacts_sample.csv', index=False)

print("Scraping completed! Data saved to 'output/rocketreach_contacts_sample.csv'.")

# Close the browser
driver.quit()