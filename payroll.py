import time
#this method calculates the number of hours and the rate of pay
def cal_hours(hours, rate):
    global gross_pay
    #if the hours are less than 40 then multiply the rate by hours
    if hours < 40:
        gross_pay = rate * hours
#if the hours are over 40 then multipy the rate times 40 then subtract 40 from hours and multiply the rate
# by 1.5 and multipy the remaining hours
    elif hours > 40:
        gross_pay = rate * 40
        hours = hours - 40
        rate = rate * 1.5
        gross_pay = gross_pay + (rate * hours)
#return the gross payment
    return gross_pay
#this method calculates the tax
def cal_tax(gross_pay, stax, ftax, ben):
    global net_pay
    global ded
    stax = stax / 100
    ftax = ftax / 100
    ben = ben / 100

    fded = ftax * gross_pay
    sded = stax * gross_pay
    cben = ben * gross_pay

    net_pay = gross_pay - fded - sded - cben
    ded = fded + sded + cben

    return net_pay, ded
#this method calculates monthly pay
def month_pay(net_pay):
    global monthly
    monthly = net_pay / 24

run = True

while run:

    global name
    name = input("enter name:")
        
    pay_type = input("Are you a full-time or part-time? ")
    accepted_strings = {'part-time', 'full-time'}
    if pay_type == "part-time":
        #asks user for input then converts them to int
        hnum = input("Hours worked? ")
        hours = float(hnum)
        rnum = input("Hourly rate? ")
        rate = float(rnum)
        bnum = input("Benefits? ")
        ben = float(bnum)


        cal_hours(hours, rate)
        #asks user for input then converts them to int
        fnum = input("Federal tax percent: ")
        ftax = float(fnum)
        stnum = input("State tax percent: ")
        stax = float(stnum)

        cal_tax(gross_pay, stax, ftax,ben)
    elif pay_type == 'full-time':
        #asks user for input then converts them to int
        snum = input("Yearly salary? ")
        sal = float(snum)
        gross_pay = sal

        fnum = input("Federal tax percent: ")
        ftax = float(fnum)
        stnum = input("State tax percent: ")
        stax = float(stnum)
        bnum = input("Benefits? ")
        ben = float(bnum)

        cal_tax(gross_pay, stax, ftax, ben)
        month_pay(net_pay)
    #prints the user name, gross pay, net pay, and deductions
    print("Hello, {}!".format(name))
    print("Gross pay: {}".format(gross_pay))
    print("Net pay: {}".format(net_pay))
    print("Deductions: {}".format(round(ded, 2)))
    time.sleep(5) #5 seconds until program quit

            
    run = False
