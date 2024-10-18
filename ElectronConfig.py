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
        #note to self - the first number here is the amount of electron holders
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

def nobleGasCorrection(config, specifier):
    pos = config.find(specifier)
    if pos != -1:
        newConfig = config[pos + len(specifier):]
        return newConfig
    return "err - specifier not found"

#"main" area of code
print("Type -1 to quit")
mode = str(input("Noble gas mode? (Y/N): "))
if mode.lower() == 'y':
    nobleGasMode = True
else:
    nobleGasMode = False    
while True:
    if nobleGasMode:
        numElectrons = int(input("Enter the number of electrons present in the atom: "))
        configuration = generateElectronConfiguration(numElectrons)
        if 2 > numElectrons:
            print("nobleGasMode not applicable")
        elif 10 > numElectrons > 2 :
            nobleGas = "[He]"
            configuration = nobleGasCorrection(configuration,"1s^2")
        elif 18 > numElectrons >= 10:
            nobleGas = "[Ne]"
            configuration = nobleGasCorrection(configuration,"2p^6")
        elif 36 > numElectrons >= 18:
            nobleGas = "[Ar]"
            configuration = nobleGasCorrection(configuration,"3p^6")
        elif 54 > numElectrons >= 36:
            nobleGas = "[Kr]"
            configuration = nobleGasCorrection(configuration,"4p^6")
        elif 86 > numElectrons >= 54:
            nobleGas = "[Xe]"
            configuration = nobleGasCorrection(configuration,"5p^6")
        elif numElectrons > 86:
            nobleGas = "[Rn]"
            configuration = nobleGasCorrection(configuration,"6p^6")
        else:
            configuration = "error"
            nobleGas = "error"    
        print(nobleGas + configuration)         
    else:    
        numElectrons = int(input("Enter the number of electrons present in the atom: "))
        if numElectrons == -1:
            break
        print(generateElectronConfiguration(numElectrons))