email_address = input("Email address: ")
print("Checking...")

# ...and the rest is up to you



if '@' not in email_address :
    print('@ symbol is missing')
elif email_address.count('@') > 1 :
    print(email_address)
    print((' '*email_address.rfind('@'))+"^--there\'s an extra @ symbol here")
elif email_address[0] == '@' :
    print(' '+email_address)
    print('^--this bit is missing')
elif email_address[-1] == '@':
    print(email_address)
    print((' '*len(email_address))+'^--this bit is missing')
elif email_address[0] == '.' :
    print(email_address)
    print("^--there's a dot here that probably shouldn't")
elif email_address[email_address.find('@')-1] == '.' :
    print(email_address)
    print(' '*email_address.find('@')+"^--there's a dot here that probably shouldn't")
elif email_address.count("..") :
    print(email_address)
    print(' '*email_address.find("..")+'^--there are consecutive dots here')
elif not email_address.count('.',email_address.find('@')) :
    print("The top-level-domain is missing. Did you perhaps intend to write "+email_address+".com?")
else :
    print('Seems legit')