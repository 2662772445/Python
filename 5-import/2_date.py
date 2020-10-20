import datetime 

x = datetime.datetime.now()
print(x)      
print(x.year)
print(x.strftime('Weekday : %A-%w'))
print(x.strftime('Date : %d'))
print(x.strftime('Month : %b-%B-%m'))
print(x.strftime('Year : %y-%Y'))
print(x.strftime('Hour : %I-%H'))
print(x.strftime('Day of year & month: %j-%W'))
print(x.strftime('%c'))
print(x.strftime('Date & Time: %x  %X'))
