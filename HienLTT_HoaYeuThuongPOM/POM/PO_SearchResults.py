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

class PO_SearchResults(unittest.TestCase):
    
    id_mucGia = (By.XPATH, "//select[@id='ctl00_cphContent_ucSearchAdvance_ddlPrice']//option[@selected='selected']")
    id_sortOrder = (By.XPATH, "//select[@id='ctl00_cphContent_ucSearchAdvance_ddlSortOrder']//option[@selected='selected']")
    id_theLoai = (By.XPATH, "//select[@id='ctl00_cphContent_ucSearchAdvance_ddlCategory']//option[@selected='selected']")
    id_chuDe = (By.XPATH, "//select[@id='ctl00_cphContent_ucSearchAdvance_ddlTopic']//option[@selected='selected']")
    id_hoaTuoi = (By.XPATH, "//select[@id='ctl00_cphContent_ucSearchAdvance_ddlFlowers']//option[@selected='selected']")
    id_mauSac = (By.XPATH, "//select[@id='ctl00_cphContent_ucSearchAdvance_ddlColor']//option[@selected='selected']")

    def __init__(self, webDriver):
        self.webBrowser = webDriver

    def get_all_properties(self):
        list_ids = {
            "MucGia" : {
                "ID" : self.id_mucGia,
                "Name" : "Mức giá:",
                "Property" : "innerText",
            },
            "SortOrder" : {
                "ID" : self.id_sortOrder,
                "Name" : "Sort order:",
                "Property" : "innerText",            
            },
            "TheLoai" : {
                "ID" : self.id_theLoai,
                "Name" : "Thể loại:",
                "Property" : "innerText",
            },
            "ChuDe" : {
                "ID" : self.id_chuDe,
                "Name" : "Chủ đề:",
                "Property" : "innerText",
            },
            "HoaTuoi" : {
                "ID" : self.id_hoaTuoi,
                "Name" : "Hoa tươi:",
                "Property" : "innerText",
            },
            "MauSac" : {
                "ID" : self.id_mauSac,
                "Name" : "Màu sắc:",
                "Property" : "innerText",
            },
            "WeFound": {
                "ID": (By.XPATH, "//h1[@class='title']"),
                "Name": "",
                "Property": "innerText",
            },
            "Title": {
                "ID": (By.XPATH, "//a[@id='ctl00_cphContent_ucSearchItems_ucItems_rptItems_ctl01_hplTitle']"),
                "Name": "Title:",
                "Property": "innerText",
            },
            "Price": {
                "ID": (By.XPATH, "//span[@id='ctl00_cphContent_ucSearchItems_ucItems_rptItems_ctl01_lblVNPrice']"),
                "Name": "Price:",
                "Property": "innerText",
            }
        }
        xResults = get_allValues(self.webBrowser, list_ids)
        return xResults
    
    def get_number(self):
        list_result = self.webBrowser.find_elements(By.XPATH, "//div[@class='item']")
        return len(list_result)
    
    def get_number_WeFound(self):
        ui_wefound = self.webBrowser.find_element(By.XPATH, "//h1[@class='title']")
        str_found = ui_wefound.get_property("innerText").split(": ")
        return int(str_found[1])

    def get_all_flowers(self):
        str_title_1 ="//a[@id='ctl00_cphContent_ucSearchItems_ucItems_rptItems_ctl"
        str_title_2 = "_hplTitle']"
        str_price_1 = "//span[@id='ctl00_cphContent_ucSearchItems_ucItems_rptItems_ctl"
        str_price_2 = "_lblVNPrice']"
        item1 = 0
        item2 = 1
        str_number = str(self.get_number())
        if self.get_number() < 10:
            str_number = "0" + str(self.get_number())
        while item1 < 2:
            while item2 < 10:     
                if (str(item1) + str(item2) > str_number):
                    break
                else:
                    ui_title = self.webBrowser.find_element(By.XPATH, str_title_1 + str(item1) + str(item2) + str_title_2)
                    print('\nTitle: ', ui_title.get_property("innerText"))
                    ui_price = self.webBrowser.find_element(By.XPATH, str_price_1 + str(item1) + str(item2) + str_price_2)
                    print('Price: ', ui_price.get_property("innerText"))
                    item2 += 1
            item1 += 1
            item2 = 0    
    def check_WeFound(self):
        #Check we found
        if self.assertGreaterEqual(self.get_number_WeFound(), self.get_number()) == None:
            print("\n**************")
            print("\nSố lượng hiện We Found >= số lượng kết quả trang đầu\n")
            print("**************\n")

    def do_GetResults(self):
        self.xResults = self.get_all_properties()
        self.check_WeFound()
        self.get_all_flowers()
        self.get_number()