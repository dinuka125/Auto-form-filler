import pygments
from selenium import webdriver
import pyfiglet
import time
import random
from pygments import console

result = pyfiglet.figlet_format("AUTO FORM FILLER by Dinuka")
print(result)



def Randomize5():
    list1 = [1,2,3,4,5]
    x = (random.choice(list1))
    return x

def Randomize2():
    list1 = [4,5]
    x = (random.choice(list1))
    return x

def Randomize3():
    list1 = [3,4,5]
    x = (random.choice(list1))
    return x

def Randomize4():
    list1 = [2,3,4,5]
    x = (random.choice(list1))
    return x

p12 = [1,2,6,9,10,11,12,13,17]
p13 = [3,4,5,7,8,14,16,18]

p22 = [2,3,5,11,12,15,19,20,22,23,26,27]
p21 = [8,13,14,16,18,24]
p23 = [4,6,7,9,10,17,21,25]


time_gaps = None


no = int(input("Enter the number of times you want to submit the form: "))
if no >= 5:
    print("Default time Gaps Activated ( time gaps will be 2min, 3min, 5min, 7min")
    time_gaps = [2,3,5,7]
else:
    ti= int(input("How many time gap do you need ? ex: type 3 for 3 min: "))
    time_gaps = [ti]



for a in range(1,no+1):

    web = webdriver.Chrome()
    
    web.get('https://docs.google.com/forms/d/193Zw91gbZXKcMMIxOmRxSQaqKi59pNSbNOp2zpIc1bY/edit?ts=61d17167')
    

    time.sleep(0.1)

    next1 = web.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[3]/div/div[1]/div/span')
    next1.click()
    time.sleep(2)

    next2 = web.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[3]/div/div[1]/div[2]/span')
    next2.click()
    time.sleep(2)



    for i in range(1,20):
        if i in p12:
            x = Randomize2()
            if i == 1:
                p = web.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div['+str(i+1)+']/div/div/div[2]/div/span/div/label['+str(x)+']/div[2]/div/div/div[3]')
            else:
                p = web.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div['+str(i+1)+']/div/div/div[2]/div/span/div/label['+str(x)+']/div[2]/div/div/div[3]')
        elif i in p13:
            x = Randomize3()
            p = web.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div['+str(i+1)+']/div/div/div[2]/div/span/div/label['+str(x)+']/div[2]/div/div/div[3]')
        elif i == (15):
            x = Randomize4()
            p = web.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div['+str(i+1)+']/div/div/div[2]/div/span/div/label['+str(x)+']/div[2]/div/div/div[3]')
        elif i == (19):
            x = Randomize5()
            p = web.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div['+str(i+1)+']/div/div/div[2]/div/span/div/label['+str(x)+']/div[2]/div/div/div[3]')
        p.click()
        time.sleep(0.1)


    next3 = web.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[3]/div/div[1]/div[2]/span')
    next3.click()
    time.sleep(0.1)

    for i in range(1,28):
        if i == 1:
            x = Randomize4()
            p = web.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div['+str(i+1)+']/div/div/div[2]/div/span/div/label['+str(x)+']/div[2]/div/div/div[3]')
        elif i in p23:
            x = Randomize3()
            p = web.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div['+str(i+1)+']/div/div/div[2]/div/span/div/label['+str(x)+']/div[2]/div/div/div[3]')    
        elif i in p22:
            x = Randomize2()
            p = web.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div['+str(i+1)+']/div/div/div[2]/div/span/div/label['+str(x)+']/div[2]/div/div/div[3]')
        elif i in p21:
            p = web.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div['+str(i+1)+']/div/div/div[2]/div/span/div/label[5]/div[2]/div/div/div[3]')
        p.click()
        time.sleep(0.1)

        
    next4 = web.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[3]/div/div[1]/div[2]/span')
    next4.click()
    time.sleep(2)  


    path1 = '//*[@id="i5"]/div[3]/div'
    path2 = '//*[@id="i8"]/div[3]/div'


    def getG():
        list3 = [1,2]
        y = (random.choice(list3))
        return 
    y = getG()
    if y == 1:
        dept = web.find_element_by_xpath(path1)
    else:
        dept = web.find_element_by_xpath(path2)    
    dept.click()
    time.sleep(0.1)


    new_path = '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div/span/div/div[1]/label/div'
    new_path2 = '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div/span/div/div[12]/label/div'


    def getG():
        list3 = [1,2,3,4,5,6,7,8,9,10,11,12]
        z = (random.choice(list3))
        return z

    dept_no = getG()
    dept = web.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div/span/div/div['+str(dept_no)+']/label/div')
    dept.click()
    time.sleep(0.5)

    def getW():
        list3 = [1,2,3,4]
        n = (random.choice(list3))
        return n
    w_no = getW()
    work = web.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[4]/div/div/div[2]/div/div/span/div/div['+str(w_no)+']/label/div')
    work.click()
    time.sleep(0.5)



    submit = web.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[3]/div/div[1]/div[2]/span')
    submit.click()
    time.sleep(1)
    web.close()

    "My name is {fname}, I'm {age}".format(fname = "John", age = 36)

    print(pygments.console.colorize("red","Successfully submitted a {a} forms".format(a = a)))
    time_gap = random.choice(time_gaps)
    
    
    print(pygments.console.colorize("red","Waiting...{time_gap} minutes, please don't close the program".format(time_gap=time_gap)))
    time.sleep(time_gap*60)

print(pygments.console.colorize("green","{a} Forms succssfully submitted".format(a=a)))
        
        

        
        


