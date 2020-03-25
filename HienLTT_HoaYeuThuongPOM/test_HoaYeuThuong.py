from selenium import webdriver 
from selenium.webdriver.common.action_chains import ActionChains

import pytest 
## pip install pytest
## pytest   test_tamgiac.py
import time 
from datetime import date
import unittest
from ddt import data, unpack, ddt 

### WEB-COnfig
from LIBs.all_configs_function import *
# Utility Functions
from LIBs.all_utility_functions import *


### POM - TEST OBJect
from POM.PO_HomeHYT import * 
from POM.PO_SearchResults import*

### Data LIBs
from LIBs.CSV_TestData import *

## Load Data
dta = CSVTestData(r".\Data\HoaYeuThuong_TCs.csv")
tcdata = dta.TData["Data"]["raw"]

class Test_ActionPy_HoaYeuThuong():
    countCLS = 0

    @classmethod
    def setup_class(cls):
        cls.baseurl = "https://hoayeuthuong.com/"
        cls.browser = callWebDriver()   
        cls.browser.implicitly_wait(10) ##
        xday = date.today()
        cls.xDate = str(xday.year) + "." + str(xday.month) + "." + str(xday.day)

    ##@pytest.fixture
    def setup_method(self, method):
        Test_ActionPy_HoaYeuThuong.countCLS += 1
        self.statePASS = False
        self.browser.get(self.baseurl)

    @pytest.mark.parametrize("LoaiHoa, MucTien", tcdata)
    def test_HYT(self, LoaiHoa, MucTien):
        xHome = PO_HomeHYT(self.browser)
        #Get thong tin tim kiem
        xHome.click_Search(LoaiHoa, MucTien)
        print_allValues(xHome.xResults)
      
        xSearch = PO_SearchResults(self.browser) 
        #Get ket qua tim kiem
        xSearch.do_GetResults()
        print_allValues(xSearch.xResults)
        self.statePASS = True
    
    def teardown_method(self, method):
        if (self.statePASS == False):
            self.browser.save_screenshot(r".\TestResults\Test-" + self.xDate + "-num-" + str(Test_ActionPy_HoaYeuThuong.countCLS) + ".png")  

    @classmethod
    def teardown_class(cls):
        print("")
        #cls.browser.quit()

# if __name__ == "__main__":
#     pytest.main()