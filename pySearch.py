#jrkong's command line searcher

import urllib
import argparse
import webbrowser
import re

argparser = argparse.ArgumentParser()
argparser.add_argument("-s", action="append", help="Takes a query to search for and searches it.", nargs="*")
argparser.add_argument("-e", "--engine", help="Changes the name or alias of a search engine and sets it as the search engine for the session", nargs="+")
argparser.add_argument("-d", "--domain", help="Changes the domain extention", nargs="+")
argparser.add_argument("-b", "--browser", help="Changes the web browser", nargs="+")

args = argparser.parse_args()


    
#print available broswers
def printAvailableBrowsers(invalid):
        print("You have selected an invalid or unreigstered browser: " + invalid + ".\nHere is a list of available browsers")
        for i in webbrowser._browsers:
            print("\t"+i)
#end of printAvailableBrowsers

class Search:
    def __init__(self, searchIn = None, engineIn = "google", domainIn = "ca", browser=None):
        self.searchRaw = searchIn
        self.searchQuery = ""
        self.engine = engineIn
        self.domain = domainIn
        self.browser = browser
        self.url = ""
        self.searchString = "/search?q="
    #end of constructor
    
    #set browser
    def setBrowser(self, browser):
        regex = {'chrome':'(google|chrome|google chrome|google-chrome)', 
                 'firefox':'(firefox|mozilla|mozilla firefox|mozilla-firefox)',
                 'iexplore':'(ie|internet explorer|internet-explorer|iexplorer|iexplore)',
                 'safari':'safari'}
        for i in regex:
            match = re.search(regex[i], browser, re.IGNORECASE)
            if match:
                browser = i
        self.browser = browser
    #end of setBrowser

    #set search engine
    def setEngine(self, engineIn):
        self.engine = engineIn
    #end of setEngine

    #set domain engine
    def setDomain(self, domainIn):
        self.domain = domainIn
    #end of setdomain
    
    #set search Query
    def setQuery(self, searchIn):
        self.searchRaw = searchIn
    #end of setQuery
    
    #get browser
    def getBrowser(self):
        try:
            webbrowser.get(self.browser).open_new_tab(self.url)
        except:
            printAvailableBrowsers(self.browser)
    #end of get browser

    def buildLink(self):
        if self.engine == "amazon":
            self.searchString = "/s/keywords="
            self.searchQuery = "%20".join(self.searchRaw)
        elif self.engine == "twitter":
            self.searchQuery = " ".join(self.searchRaw)
        else:
            self.searchQuery = "+".join(self.searchRaw)
        #end of search exceptions
        self.url = "http://www." + self.engine + "." + self.domain + self.searchString + self.searchQuery
    #end of link building

    def openBrowser(self):
        if self.browser is None:
            webbrowser.open_new_tab(self.url)
        else:
            self.getBrowser()
    #end of openBrowser()
#end of Query


searchObj = Search()

if args.engine is not None:
    searchObj.setEngine(args.engine[0])

if args.domain is not None:
    searchObj.setDomain(args.domain[0])
if args.browser is not None:
    searchObj.setBrowser(args.browser[0])
#end of cmd args handling

for search in args.s:
    searchObj.setQuery(search)
    searchObj.buildLink()
    searchObj.openBrowser()