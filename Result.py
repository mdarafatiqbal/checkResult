#! python3
from selenium import webdriver
import pyautogui

def check_result(USN):
    browser = webdriver.Firefox()
    browser.get("http://results.vtu.ac.in/")

    searchElem = browser.find_element_by_css_selector("body > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(3) > td:nth-child(2) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(3) > td:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(2) > td:nth-child(1) > table:nth-child(2) > tbody:nth-child(1) > tr:nth-child(1) > td:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(2) > td:nth-child(1) > b:nth-child(2) > form:nth-child(10) > p:nth-child(1) > input:nth-child(1)")
    searchElem.is_selected
    searchElem.send_keys(USN)
    
    pyautogui.press('enter')

USN = ""

check_result(USN)

