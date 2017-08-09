#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      pranto
#
# Created:     09-08-2017
# Copyright:   (c) pranto 2017
# Licence:     <your licence>
#-------------------------------------------------------------------------------

print("****************************\n  Application Generator  \n****************************")
fh=open("E:\\file.txt","w")

print "Enter your Name: "
s=raw_input()
print"Enter your Address: "
y=raw_input()
print "Enter Date (dd/mm/yyyy):"
d=raw_input()
print"Enter recievers Name: "
r=raw_input()
print"Enter Company name :"
c=raw_input()
print"Enter Company Address :"
cd=raw_input()
num=y+"\n"+d+"\n\n\n\
"+r+"\n\n\
Chief of "+c+"\n\
"+c+"\n\n\
"+cd+"\n\n\
Dear "+r+":\n\n\
Let me begin by thanking you for your past contributions to our Little League baseball team.\nYour sponsorship aided in the purchase of ten full uniforms and several pieces of baseball equipment for last year's season.\n\
Next month, our company is planning an employee appreciation pancake breakfast honoring retired\nemployees for their past years of service and present employees for their loyalty and dedication in spite of the current \ndifficult economic conditions.\n\
We would like to place an order with your company for 25 pounds of pancake mix and five gallons \nof maple syrup. We hope you will be able to provide these products in the bulk quantities we require.\n\
As you are a committed corporate sponsor and long-time associate, we hope that you will be able to join us for breakfast on December 12, 2016.\n\n\n\n\
Respectfully yours,\n\n"+s



fh.writelines(num)
fh.close()



