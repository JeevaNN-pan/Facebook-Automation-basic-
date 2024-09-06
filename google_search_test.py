from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.keys import Keys
import random
import time

def test_facebook_login_search_and_like():
    driver = webdriver.Chrome()
    
    try:
        # Login process
        driver.get("https://www.facebook.com/")
        time.sleep(3)  # Wait for 3 seconds
        
        email_field = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.ID, "email"))
        )
        email_field.send_keys("8951225448")
        time.sleep(2)  # Wait for 2 seconds
        
        password_field = driver.find_element(By.ID, "pass")
        password_field.send_keys("//k5UApNwkd!WWy")
        time.sleep(2)  # Wait for 2 seconds
        
        login_button = driver.find_element(By.NAME, "login")
        login_button.click()
        
        # Wait for login to complete
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, "x1lliihq"))
        )
        
        print("Login completed successfully!")
        time.sleep(5)  # Wait for 5 seconds after login
        
        # Search for user
        search_box = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//input[@placeholder='Search Facebook']"))
        )
        search_box.send_keys("Jeevan Panda")
        time.sleep(2)  # Wait for 2 seconds
        search_box.send_keys(Keys.RETURN)
        
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//div[@role='main']"))
        )
        time.sleep(3)  # Wait for 3 seconds
        
        first_result = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//div[@role='main']//a[contains(@href, '/jeevan.panda')]"))
        )
        first_result.click()
        
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//div[@aria-label='Add Friend']"))
        )
        time.sleep(3)  # Wait for 3 seconds
        
        add_friend_button = driver.find_element(By.XPATH, "//div[@aria-label='Add Friend']")
        add_friend_button.click()
        
        print("Friend request sent successfully!")
        time.sleep(5)  # Wait for 5 seconds after sending friend request
        
        # Navigate to Facebook homepage
        driver.get("https://www.facebook.com")
        time.sleep(5)  # Wait for 5 seconds for homepage to load
        
        # Wait for the feed to load
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//div[@role='feed']"))
        )
        
        # Find all like buttons
        like_buttons = driver.find_elements(By.XPATH, "//div[@aria-label='Like' or @aria-label='Like ']")
        
        # Choose a random like button and click it
        if like_buttons:
            random_like_button = random.choice(like_buttons)
            random_like_button.click()
            print("Liked a random post successfully!")
        else:
            print("No posts available to like.")
        
        time.sleep(5)  # Wait for 5 seconds before closing
        
    except TimeoutException:
        print("Test failed: Timed out waiting for page elements")
    except Exception as e:
        print(f"Test failed. An error occurred: {str(e)}")
    
    finally:
        # Close the browser
        driver.quit()

# Run the test
test_facebook_login_search_and_like()