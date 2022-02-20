import os
from blocker import checktime
exe_list = []

def blockexe(time_start, time_end): #block từ time_start -> time_end (2 cái này là string) vd: "18:00"
    if checktime.checktime(time_start, time_end):
        print("exe still blocked")

        for exe in exe_list:
            cmd_string = "taskkill /f /im  " + exe 
            os.system(cmd_string) # os.system là để chạy command trên cmd


