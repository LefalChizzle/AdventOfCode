import time

start_time = time.time()

def checkRequirements(pwd):
    hasdouble = False
    requirements = False
    if pwd[1] >= pwd[0]:
        if pwd[1] == pwd[0]:
            hasdouble = True
        if pwd[2] >= pwd[1]:
            if pwd[2] == pwd[1]:
                hasdouble = True
            if pwd[3] >= pwd[2]:
                if pwd[3] == pwd[2]:
                    hasdouble = True
                if pwd[4] >= pwd[3]:
                    if pwd[4] == pwd[3]:
                        hasdouble = True
                    if pwd[5] >= pwd[4]:
                        if pwd[5] == pwd[4]:
                            hasdouble = True
                        if hasdouble:
                            requirements = True
                            pwd_list.append(pwd)
    return requirements, pwd_list
                        
                            
total_password = 0
pwd_list = []

for pwd in range(231832,767346):
    requirements, pwd_list = checkRequirements(str(pwd))
    if requirements:
        total_password += 1
       
print("PART 1 - Total passwords: " + str(total_password))

part2_passwords = []

for word in pwd_list:
    count = {}
    for chars in word:
        count[chars] = word.count(chars)
    if 2 in count.values():
        part2_passwords.append(word)


print("PART 2 - Total passwords " + str(len(part2_passwords)))

end_time = time.time()
total_time = end_time - start_time
print("Total time: " + str(total_time) + " seconds")
