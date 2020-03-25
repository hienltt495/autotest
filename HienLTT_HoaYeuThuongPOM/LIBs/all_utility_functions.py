from selenium import webdriver
import time 

errorCount = 0

def print_Infor(self, node, xPName, itemName=""):
    ui_item = node.find_element_by_xpath(xPName)
    print(itemName, "\t", ui_item.get_property("innerText"))

def find_UI_Element(webBrowser, objDefine):
    global errorCount
    ui_Object = None
    try:
        ui_Object = webBrowser.find_element(objDefine["Identity"][0], objDefine["Identity"][1])
    except:
        errorCount += 1
        print("[]...error - find element ", errorCount)
    return ui_Object

def find_UI_Elements(webBrowser, objDefine):
    global errorCount
    ui_Object = None
    try:
        ui_Object = webBrowser.find_elements(objDefine["Identity"][0], objDefine["Identity"][1])
    except:
        errorCount += 1
        print("[]...error(s) - find elements ", errorCount)
    return ui_Object

def find_UI_Simple(webBrowser, objDefine, objName =""):
    global errorCount
    ui_Object = None
    try:
        ui_Object = webBrowser.find_element(objDefine[0], objDefine[1])
    except:
        errorCount += 1
        print("[]...error - find simple element ", objName, errorCount)
    return ui_Object

#################################################
### FORMAT
# list_ids = {
#            "DiaDiem" : {
#                "ID" : self.id_Query,
#                "Name" : "Địa Phương đến ở",
#                "Property" : "innerText",
#                "Value" : "",
#                "Type" : "text"
#            }
#        } '''
def get_value(webBrowser, id_element):
    xUI_element = find_UI_Simple(webBrowser, id_element["ID"], id_element["Name"])
    xResult = id_element
    if (xUI_element == None):
        xResult["Value"] = None 
        xResult["state"] = -1
    else:
        xResult["Value"] = xUI_element.get_property(xResult["Property"]) 
        xResult["state"] = 1
    return xResult 

def get_allValues(webBrowser, id_elements):
    xResults = {}
    for key in id_elements.keys():
        xResults[key] = get_value(webBrowser, id_elements[key])
    return xResults

def print_allValues(id_elements, partName=""):
    print("\n********* ", partName)
    for key in id_elements.keys():
        vals = id_elements[key]
        print(vals["Name"], vals["Value"])


#################################################

