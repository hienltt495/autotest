
### B01. KHAI BÁO THƯ VIỆN
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import time 

def callChrome():    
    ### Chrome Config
    # chrome_options = webdriver.ChromeOptions()
    # prefs = {"profile.default_content_setting_values.notifications" : 2}
    # chrome_options.add_experimental_option("prefs",prefs)
    # driver = webdriver.Chrome(chrome_options=chrome_options)
    webBrowser = webdriver.Chrome()
    return webBrowser

def callWebDriver(xBrowser="Firefox"):
    ### CHUAN BI THONG TIN CONFIG
    RUN_options = webdriver.FirefoxOptions()
    RUN_options.add_argument("--start-maximized")
    RUN_options.add_argument("--start-fullscreen")
    RUN_options.set_preference("dom.webnotifications.enabled", False)
    RUN_options.set_preference("dom.push.enabled", False)
    RUN_options.add_argument('--disable-notifications')
    RUN_options.add_argument('--disable-extensions')
    ### B02. gọi DRIVER
    webBrowser = webdriver.Firefox(
        executable_path=r".\webDriver\geckodriver.exe"
        , options= RUN_options
        , service_log_path=r".\xLogs\xFirefox.log"
        )      
    ##
    webBrowser.maximize_window()
    webBrowser.implicitly_wait(10)
    return webBrowser


### urlHub = 'http://127.0.0.1:4444/wd/hub'
def callRemote_WebDriver(urlHUB, xBrowser="Firefox"):
    ### CHUAN BI THONG TIN CONFIG
    RUN_options = webdriver.FirefoxOptions()
    RUN_options.add_argument("--start-maximized")
    RUN_options.add_argument("--start-fullscreen")
    RUN_options.set_preference("dom.webnotifications.enabled", False)
    RUN_options.set_preference("dom.push.enabled", False)
    RUN_options.add_argument('--disable-notifications')
    RUN_options.add_argument('--disable-extensions')
    ### Remote config
    capabilities = DesiredCapabilities.FIREFOX.copy()

    ### B02. gọi DRIVER
    webBrowser = webdriver.Remote(
        command_executor=  urlHUB
        , desired_capabilities=capabilities
        #, options= RUN_options
        )      
    ##
    webBrowser.maximize_window()
    webBrowser.implicitly_wait(10)
    return webBrowser