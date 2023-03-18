# v 0.1 {get mode}

import os
import json
import requests
import time
import datetime
import openpyxl

def dump(number,title,string):
    
    with open("result/get/response/TEST " + str(number) + "" + title + ".json", "w")as file:
        file.write(string)

def log(number, url, send, status):
    
    now = datetime.datetime.now()
    time = now.replace(microsecond = 0)
    with open("result/get/get.log", "a")as file:
        log = str(time) + " TEST " + str(number) + ":" + str((url,send,status))
        file.write(log + "\n")

def xlsx(number,title,url,send,string,status):

    wbo = openpyxl.Workbook()
    wba = wbo.active
    wba.title = "Test " + str(number)
    wba.append(("TEST ID","TEST TITLE","URL","REQUEST","RESPONSE","STATUS", "RESULT"))
    wba.append((number,title,url,send,string,status))
    wbo.save("result/get/report/test " + str(number)+".xlsx")
    
def run(url,send,title,number):

    try:
        start = time.time()
        response = requests.get(url + send)
        end = time.time()
        status = response.status_code
        data = response.json()
        string = json.dumps(data,indent = 4)
                
        print("---" *10 + "TEST ",number,"---" *10)
        print("\nTEST: ",title)
        print("\nURL: ",url)
        print("\nREQUEST: ",send)
        print("\nRESPONSE BODY: \n")
        print(string)
        print("\nSTATUS CODE: ",status )
        print("\nRESPONSE TIME: ",(end - start)*1000," ms")
        print("\n*COMPLETE*\n")
        print("-" *67 + "\n")
        
        log(number,url,send,status)
        
        if save_report == True:
            send = str(send)
            xlsx(number,title,url,send,string,status)
            
        if save_response == True:
           dump(number,title,string)        

    except Exception as errstat:
       print("\nTEST ERROR!!!\n")
       print(errstat)
        
print("\n" + " " *10 + "Run {GET mode}" + " " *10)
print("\nPrepare test cases and get to work...\n")
input("Press ENTER to continue...")

save_report = input("Save report ?(Y/N)")
save_response = input("Save response ?(Y/N)")

if save_report == "Y":
    save_report = True
else:
    save_report = False

if save_response == "Y":
    save_response = True
else:
    save_response = False    

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

    print("TOTAL COUNT: ",number - 1)                
    repeat = input("\nRepeat testing ?(Y/N)...")
    if repeat == "Y":
        start()
    else:
        print("\nDONE!")
        if save_report or save_request == True:
            view = input("\nView test results ?(Y/N)... ")
            if view == "Y":
                result = os.path.abspath('result/get')
                os.startfile(result)         
    input("\nPress ENTER to complete... ")                
                   
start()





    

    





