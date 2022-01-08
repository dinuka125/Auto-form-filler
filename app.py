from selenium import webdriver
import time
import random

no = int(input("Enter the number of times you want to submit the form: "))
# x=1
# while x<=no:
#     web = webdriver.Chrome()
#     web.get('https://docs.google.com/forms/d/193Zw91gbZXKcMMIxOmRxSQaqKi59pNSbNOp2zpIc1bY/edit?ts=61d17167')
    
    
    
#     web.close()
#     x=x+1


def getRandomNo():
    list1 = [1,2,3,4,5]
    x = (random.choice(list1))
    return x



x = getRandomNo()

web = webdriver.Chrome()
web.get('https://docs.google.com/forms/d/193Zw91gbZXKcMMIxOmRxSQaqKi59pNSbNOp2zpIc1bY/edit?ts=61d17167')

time.sleep(0.1)

next1 = web.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[3]/div/div[1]/div/span')
next1.click()
time.sleep(2)

next2 = web.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[3]/div/div[1]/div[2]/span')
next2.click()
time.sleep(2)


# def p1q1():
#     x = getRandomNo()
#     p1q1 = web.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/span/div/label['+str(x)+']/div[2]/div/div/div[3]')
#     p1q1.click()
#     time.sleep(0.1)

# p1q1()

# def p1q2():
#     x = getRandomNo()
#     p1q2 = web.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/span/div/label['+str(x)+']/div[2]/div/div/div[3]')
#     p1q2.click()
#     time.sleep(0.1)

# p1q2()    

# def p1q3():
#     x = getRandomNo()
#     p1q3 = web.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[4]/div/div/div[2]/div/span/div/label['+str(x)+']/div[2]/div/div/div[3]')
#     p1q3.click()
#     time.sleep(0.1)

# p1q3()

# def p1q4():
#     x = getRandomNo()
#     p1q4 = web.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[5]/div/div/div[2]/div/span/div/label['+str(x)+']/div[2]/div/div/div[3]')
#     p1q4.click()
#     time.sleep(0.1)

# p1q4()
    
# def p1q5():
#     x = getRandomNo()
#     p1q5 = web.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[6]/div/div/div[2]/div/span/div/label['+str(x)+']/div[2]/div/div/div[3]')
#     p1q5.click()
#     time.sleep(0.1)

# p1q5()

# def p1q6():
#     x = getRandomNo()
#     p1q6 = web.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[7]/div/div/div[2]/div/span/div/label['+str(x)+']/div[2]/div/div/div[3]')
#     p1q6.click()
#     time.sleep(0.1)

# p1q6()

for i in range(2,21):
    x = getRandomNo()
    p = web.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div['+str(i)+']/div/div/div[2]/div/span/div/label['+str(x)+']/div[2]/div/div/div[3]')
    p.click()
    time.sleep(0.1)


next3 = web.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[3]/div/div[1]/div[2]/span')
next3.click()
time.sleep(0.1)

for i in range(2,29):
    x = getRandomNo()
    p = web.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div['+str(i)+']/div/div/div[2]/div/span/div/label['+str(x)+']/div[2]/div/div/div[3]')
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