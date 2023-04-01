# v 0.1 {post mode}

import os
import json
import requests
import time
import datetime
import openpyxl

def dump(number,test,string):
    
    with open("result/post/response/TEST " + str(number) + "" + test + ".json", "w")as file:
        file.write(string)

def log(number,test,url,send,status,result):
    
    now = datetime.datetime.now()
    time = now.replace(microsecond=0)
    with open("result/post/post.log", "a")as file:
        log = str(time) + " TEST " + str(number) + ":" + test + str((url,send,status,result))
        file.write(log+"\n")

def xlsx(number,test,url,send,string,status,result):

    send = str(send)
    wbo = openpyxl.Workbook()
    wba = wbo.active
    wba.title = "Test " + str(number)
    wba.append(("TEST ID","TEST TITLE","URL","REQUEST","RESPONSE","STATUS","RESULT"))
    wba.append((number,test,url,send,string,status,result))
    wbo.save("result/post/report/test " + str(number) + " " + test + ".xlsx")
    
def run(test,url,send,check,number):

    try:
        start = time.time()
        response = requests.post(url,json = send)
        end = time.time()
        status = response.status_code
        data = response.json()
        string = json.dumps(data,indent = 4)

        if status == check:
            result = "PASS"
        else:
            result = "FAIL"
                
        print("---" *10 + "TEST",number,"---" *10)
        print("\nTEST NAME: ",test)
        print("\nURL: ",url)
        print("\nREQUEST: ",send)
        print("\nRESPONSE BODY: \n")
        print(string)
        print("\nSTATUS CODE:",status," EXPECTED:",check," RESULT:",result)
        print("\nRESPONSE TIME: ",(end - start)*1000," ms")
        print("\n*COMPLETE*\n")
        print("-" *67 + "\n")
        
        log(number,test,url,send,status,result)
        
        if save_report == True:
            xlsx(number,test,url,send,string,status,result)
            
        if save_response == True:
           dump(number,test,string)   

    except Exception as errstat:
       print("\nTEST ERROR!!!\n")
       print(errstat)
        
print("\n" + " " *10 + "Run {POST mode}" + " " *10)
print("\nPrepare test cases and get to work...\n")
input("Press ENTER to continue...")

save_report = input("Save report ?(Y/N) ")
save_response = input("Save response ?(Y/N) ")
print("Start...\n")

if save_report == "Y":
    save_report = True
else:
    save_report = False

if save_response == "Y":
    save_response = True
else:
    save_response = False
    
def start():
    
    path = os.listdir("testrun/post")
    number = 1
    for test in path:
        load = os.path.abspath("testrun/post/" + test)
        with open(load,"r") as kit:
            data = json.load(kit)
            param = []
            for title,send in data.items():
                param.append(send)
                test = test[:-2]
            run(test,*param,number) #*[url,send,check]           
        number += 1
                
    print("TOTAL COUNT: ",number - 1)                
    repeat = input("\nRepeat testing ?(Y/N)...")
    if repeat == "Y":
        start()
    else:
        print("\nDONE!")
    if save_report or save_response == True:
        view = input("\nView test results ?(Y/N)... ")
        if view == "Y":
            result = os.path.abspath('result/post')
            os.startfile(result)         
            input("\nPress ENTER to complete... ")                  
                   
start()





    

    





