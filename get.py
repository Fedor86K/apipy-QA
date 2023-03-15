# v 0.1 {get mode}

import os
import json
import requests
import time
import datetime
import openpyxl

def log(url,send,status):
    
    now = datetime.datetime.now()
    time = now.replace(microsecond=0)
    with open("log/get.log", "a")as file:
        log = str(time) + " " + str((url,send,status))
        file.write(log+"\n")

def xlsx(number,title,url,send,string,status):

    wbo = openpyxl.Workbook()
    wba = wbo.active
    wba.title = "Test" + str(number)
    wba.append(("TEST ID","TEST TITLE","URL","REQUEST","RESPONSE","STATUS", "RESULT"))
    wba.append((number,title,url,send,string,status))
    wbo.save("report/get/test " + str(number)+".xlsx")
    
def run(url,send,title,number):

    try:
        response = requests.get(url + send)
        status = response.status_code
        data = response.json()
        string = json.dumps(data, indent = 4)
                
        print("---"*10 + "TEST " + str(number) + "---"*10)
        print("\nTEST: " + title)
        print("\nURL: " + url)
        print("\nREQUEST: " + send)
        print("\nRESPONSE BODY: \n")
        print(string)
        print("\nSTATUS CODE: " + str(status) + "\n")
        print("\n*COMPLETE*\n")
        print("-"*67 + "\n")
        log(url,send,status)
        
        if save == True:
           xlsx(number,title,url,send,string,status)   

    except Exception as errstat:
       print("\nTEST ERROR!!!\n")
       print(errstat)
        
print("\n" + " "*10 + "Run {GET mode}" + " "*10)
print("\nPrepare test cases and get to work...\n")
input("Press ENTER to continue...")

report = input("Save report ?(Y/N)")

if report == "Y":
    save = True
else:
    save = False

def start():
    
    test_list = os.listdir("testrun/get")
    number = 1
    for test_file in test_list:
        test = os.path.abspath("testrun/get/" + test_file)
        with open(test,"r") as kit:
            test = json.load(kit)
            for title, send in test.items():
                url = test["URL"]
                if title != "URL":
                    run(url,send,title,number)
                    number += 1
                    
    repeat = input("\nRepeat testing ?(Y/N)...")
    if repeat == "Y":
        start()
    else:
        print("\nDONE!")
        if save == True:
            view = input("\nView report files ?(Y/N)... ")
            if view =="Y":
                report = os.path.abspath('report/get')
                os.startfile(report)   
        input("\nPress ENTER to complete... ")                
                   
start()





    

    





