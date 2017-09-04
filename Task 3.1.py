def insertcomma(string, point):
    string = string[:point-3] + "," + string[point-3:]      #function to insert comma
    return string

dp = 3                                                      #define no. decimal places
amount = float(input("Input amount:"))
amount = round(amount, dp)                                  #rounding to defined decimal places
amount = str(amount)                                        #typecast to string
dot = amount.find('.')                                      #find decimal point
amount = amount + "0"*(dp-len(amount[dot+1:]))              #pads to defined decimal places
amount = insertcomma(amount, dot)                           #insert comma for thousands place
print("$"+amount.rjust(11,"0"))                             #add leading currencing and leading padding with 0s