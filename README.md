# Facebook Automation Script

This Python script automates several actions on Facebook using Selenium WebDriver. It demonstrates how to log in, search for a user, send a friend request, and like a random post.

## Disclaimer

**IMPORTANT:** This script is for educational purposes only. Using automation scripts on Facebook may violate their terms of service. Use at your own risk.

## Prerequisites

- Python 3.x
- Selenium WebDriver
- Chrome WebDriver

## Installation

1. Install the required Python packages:

   ```
   pip install selenium
   ```

2. Download and install the Chrome WebDriver that matches your Chrome browser version.

## Usage

1. Update the login credentials in the script:

   ```python
   email_field.send_keys("YOUR_EMAIL_OR_PHONE")
   password_field.send_keys("YOUR_PASSWORD")
   ```

2. Modify the search query if needed:

   ```python
   search_box.send_keys("Jeevan Panda")
   ```

3. Run the script:

   ```
   python facebook_automation.py
   ```

## Features

- Automated login to Facebook
- Search for a specific user
- Send a friend request
- Like a random post on the news feed

## Cautions

- This script includes waiting times to mimic human behavior and avoid detection. However, frequent use may still lead to account restrictions.
- Ensure you have the right to access and interact with the accounts and content involved.
- Facebook's layout and element identifiers may change, which could break the script.

## Customization

You can modify the script to perform different actions or adjust the waiting times as needed. Always ensure your actions comply with Facebook's policies and respect user privacy.

## Troubleshooting

If you encounter issues:
- Ensure your Chrome WebDriver version matches your Chrome browser version.
- Check if Facebook has updated its layout or element identifiers.
- Adjust the waiting times if pages are loading slowly.

## Disclaimer

The authors of this script are not responsible for any misuse or any violations of Facebook's terms of service that may result from using this script.
