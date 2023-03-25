# Lists you can make changes by yourself in the lists one example has been given in dotExtension list {'.like this'}
spCharsList = ['.', '!', '#', '$', '&', '*']
numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
dotExtension = ['com', 'in', 'org', 'likethis']

# Variables
spCharsFound = 0
atCheck = 0
noNumbers = True
noUppercase = True
noSpChars = True
noDotExtension = True
noSpace = True
lengthNumbers = len(numbers)
lengthSpChars = len(spCharsList)
lengthDotExtension = len(dotExtension)

email = input("Email: ")
email2 = email.split('@')
email3 = email.split('.')
email4 = email.split()

# Logic
if not (len(email2[0]) <= 3):
    # likethis extension will be allowed eg:[xyz@gmail.likethis] if you dont want it please revmeove the entire enry with the comma
    # The list should look like this ['com','in','org']
    for extension in range(0, lengthDotExtension):
        if email3[1] == dotExtension[extension]:
            noDotExtension = False

    for chars in email:
        if (chars == '@'):
          atCheck += 1
        for spchars in spCharsList:
            if (chars == spchars):
              spCharsFound = +1

    for chars in email2[0]:
      for i in range(0, lengthNumbers):
          if chars == numbers[i]:
             noNumbers = False
      for j in range(0, lengthSpChars):
          if chars == spCharsList[j]:
             noSpChars = False

    if email2[0].lower() == email2[0]:
        noUppercase = False

    if email4[0] != email:
        noSpace = False
    
    if (not (atCheck >= 1 & atCheck != 0)):
        print("Email incorrect : multiple or no \'@\' found")
        exit("Exited Program : Restart Program to recheck")
    if (spCharsFound == 0):
        print("Email incorrect : no special characters found")
        exit("Exited Program : Restart Program to recheck")
    if (noUppercase == True):
        print("Email incorrect : uppercase characters found")
        exit("Exited Program : Restart Program to recheck")
    if (noNumbers == True):
        print("Email incorrect : no numbers found")
        exit("Exited Program : Restart Program to recheck")
    if (noSpChars == True):
        print("Email incorrect : no special characters found")
        exit("Exited Program : Restart Program to recheck")
    if (noDotExtension == True):
        print("Email incorrect : no proper dot extension found")
        exit("Exited Program : Restart Program to recheck")
    if (noSpace == False):
        print("Email incorrect : Space Found")
        exit("Exited Program : Restart Program to recheck")
        
    print(f"Email {email} Valid")
else:
    print("Email incorrect: length of the email is too short")
