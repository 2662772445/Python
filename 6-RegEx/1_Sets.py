# RegEx - Regular expression

import re 

txt = "The rain in spain, 8 times before 11:45:33"

# Sets '[]'
x = re.findall("ai", txt);                  print('1.',x)        # if 'ai' is available in txt thn it'll print       
x = re.findall("[a-i]", txt);               print('2.',x)        # print upto a to i letters  
x = re.findall("[^arni]", txt);             print('3.',x)        # remove a,r,n,i from txt
x = re.findall("[012]", txt);               print('4.',x)        # print 0,1,2 if available
x = re.findall("[0-9]", txt);               print('5.',x)        # print digit upto 0 to 9 
x = re.findall("[0-3][0-9]", txt);          print('6.',x)        # Returns a match for any two-digit no. from 00 and 39
x = re.findall("[0-9a-zA-Z]", txt);         print('7.',x)        # Returns a match for any character alphabetically or digitally between a-z,A-Z,0-9
