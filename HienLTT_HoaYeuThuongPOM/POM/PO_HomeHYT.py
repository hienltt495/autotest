### WEB-B01. KHAI BÁO THƯ VIỆN
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
## SEL-LIBs
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

# support LIBs
from time import sleep 
import unittest

# Utility Functions
from LIBs.all_utility_functions import *

### Khai báo Page
class PO_HomeHYT(unittest.TestCase):
    id_chuDe = (By.XPATH, "//select[@id='ctl00_cphContent_ucQuickSearch_ddlOccasion']")
    id_mucGia = (By.XPATH, "//select[@id='ctl00_cphContent_ucQuickSearch_ddlPrice']")
    id_btn_Tim = (By.XPATH, "//input[@id='ctl00_cphContent_ucQuickSearch_btnSearch']")

    def __init__(self, webDriver):
        self.webBrowser = webDriver

    def set_ChuDe(self, LoaiHoa):
        ui_chuDe = self.webBrowser.find_element(self.id_chuDe[0], self.id_chuDe[1])
        ui_chuDe.click()
        time.sleep(2)
        ui_select_ChuDe = self.webBrowser.find_element(By.XPATH, "//option[@value='" + LoaiHoa + "']")
        ui_select_ChuDe.click()
        
    def set_MucGia(self, MucTien):
        ui_mucGia = self.webBrowser.find_element(self.id_mucGia[0], self.id_mucGia[1])
        ui_mucGia.click()
        ui_select_MucGia = self.webBrowser.find_element(By.XPATH, "//option[@value='" + MucTien + "']")
        ui_select_MucGia.click()
    
    def click_timKiem(self):
        ui_timKiem = self.webBrowser.find_element(self.id_btn_Tim[0], self.id_btn_Tim[1])
        ui_timKiem.click()

    def get_Title(self):
        return self.webBrowser.title

    def get_all_properties(self, LoaiHoa, MucTien):
        list_ids = {
            "LoaiHoa" : {
                "ID" : (By.XPATH, "//option[@value='" + LoaiHoa + "']"),
                "Name" : "Loại hoa cần tìm:",
                "Property" : "innerText",
            },
            "MucTien" : {
                "ID" : (By.XPATH, "//option[@value='" + MucTien + "']"),
                "Name" : "Mức tiền cần tìm:",
                "Property" : "innerText",            
            }              
        }
        xResults = get_allValues(self.webBrowser, list_ids)
        return xResults
    def check_Title(self):
        if self.assertIn("Shop hoa tươi", self.get_Title(), "Faillll") == None:
            print("\n**************")
            print("\nShop hoa tươi có trong title!!!!\n")
            print("**************\n")

    def click_Search(self, LoaiHoa, MucTien):
        self.set_ChuDe(LoaiHoa)
        self.set_MucGia(MucTien)
        self.check_Title()
        self.xResults = self.get_all_properties(LoaiHoa, MucTien)
        self.click_timKiem()