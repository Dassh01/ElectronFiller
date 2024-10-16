def generateElectronConfiguration(numElectrons):
    subshells = [("1s", 2), ("2s", 2), ("2p", 6), ("3s", 2), ("3p", 6), ("4s", 2), 
                 ("3d", 10), ("4p", 6), ("5s", 2), ("4d", 10), ("5p", 6), ("6s", 2), 
                 ("4f", 14), ("5d", 10), ("6p", 6), ("7s", 2), ("5f", 14), ("6d", 10), 
                 ("7p", 6)]
    
    electronConfiguration = []
    unpairedElectrons = 0
    
    for subshell, capacity in subshells:
        if numElectrons <= 0:
            break
        electronsInSubshell = min(numElectrons, capacity)
        electronConfiguration.append(f"{subshell}^{electronsInSubshell}")
        numElectrons -= electronsInSubshell
        
        #unpaired electron fix
        if "s" in subshell:
            if electronsInSubshell == 1:
                unpairedElectrons += 1
        elif "p" in subshell:
            unpairedElectrons += (3 - electronsInSubshell // 2)
        elif "d" in subshell:
            unpairedElectrons += (5 - electronsInSubshell // 2)
        elif "f" in subshell:
            unpairedElectrons += (7 - electronsInSubshell // 2)
    
    configuration = "\nConfig = " + " ".join(electronConfiguration)
    if unpairedElectrons > 0:
        configuration += f"\nUnpaired electrons: {unpairedElectrons}\n"
    else:
        configuration += f"\nAll electrons paired!\n"
    
    return configuration

print("Type -1 to quit")
while True:
    numElectrons = int(input("Enter the number of electrons: "))
    if numElectrons == -1:
        break
    print(generateElectronConfiguration(numElectrons))