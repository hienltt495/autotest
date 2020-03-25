import csv
import sys 
import codecs

class CSVTestData:
    # TDstate = False 
    # TData = { 
    #     "MetaTag" : {} ,
    #     "Head" : {} , 
    #     "Data" : {} }

    def __init__(self, dtfilename):
        self.openReadFile(dtfilename)
       
    def getTCsRaw(self, index):
        return self.TData["Data"]["raw"][index]

    def getTCsDict(self, index):
        return self.TData["Data"]["TestCase"][index]

    def openReadFile(self, dtfilename):
        self.TDstate = False
        self.TDstage = None
        self.TData = { 
            "MetaTag" : { "raw" : [] , "param" : {} } ,
            "Head" : {  "raw" : [] , "param" : {}  , "Tags" : []  } , 
            "Data" : { "raw" : [] , "TestCase" : []  }
        }

        try:
            with open(dtfilename, encoding='utf-8') as csvfile:
                csvReader = csv.reader(csvfile, dialect=csv.excel)
                index = 0                
                for row in csvReader:
                    remainrow = self.stripStr(row)
                    if (not self.isCommentRow(remainrow)):
                        xStage = self.isSection(remainrow)
                        if (xStage is None):
                            if (self.TDstage != None): #is not
                                ## Thêm vào Dữ Liệu
                                self.addNewRow(remainrow)
                        else: 
                            self.TDstage = xStage
                csvReader.close()
            self.TDstate = True   
        except:
            self.TDstate = False
            self.ErrMsg = u"Lỗi đâu đó lúc xử lý CSV File !"

    def addNewRow(self, dtrow):
        xRowFunc = {
            "MetaTag" : self.addNewMeta,
            "Head" : self.addNewHead,
            "Data" : self.addNewData
        }        
        xRowFunc[self.TDstage](dtrow)

    def addNewMeta(self, dtrow):
        self.TData["MetaTag"]["raw"].append(dtrow)
        self.TData["MetaTag"]["param"][dtrow[0]] = dtrow
                

    def addNewHead(self, dtrow):
        self.TData["Head"]["raw"].append(dtrow)
        self.TData["Head"]["param"][dtrow[0]] = dtrow
        self.TData["Head"]["Tags"].append(dtrow[0])
        

    def addNewData(self, dtrow):
        self.TData["Data"]["raw"].append(dtrow)
        tcData = self.mappingTagData(self.TData["Head"]["Tags"], dtrow)
        self.TData["Data"]["TestCase"].append(tcData)
        

    def mappingTagData(self, tags, rowdata):
        xnum = len(tags)
        numData = len(rowdata)

        if (xnum > numData):
            xnum = numData

        tagData = {}
        for i in range(xnum):
            tagData[tags[i]] = rowdata[i]

        return tagData

    def stripStr(self, dtrow):
        newData = []
        for cell in dtrow:
            newData.append(cell.strip()) 
        return newData

    def isCommentRow(self, dtrow):
        if (dtrow is not None): 
            if (len(dtrow) > 0):
                return (dtrow[0].strip().startswith(u"##"))      
        return True 
    
    def isSection(self, dtrow):
        dictMap = { 
            "METATAG:" : "MetaTag", 
            "HEAD:" : "Head", 
            "DATA:" : "Data" }
        try: 
            value = dictMap[dtrow[0]]
        except:
            value = None
        return value
    