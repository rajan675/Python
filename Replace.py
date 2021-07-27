letter= ''' My name is Name 
and date is Date '''
NAME= input("Enter your Name ")
DATE= input("Enter date ")
letter=letter.replace("Name",NAME)
letter=letter.replace("Date",DATE)
print(letter)