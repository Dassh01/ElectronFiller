def generateElectronConfiguration(numElectrons):
    """
    Builds standard electron configuration

    Args:
        numElectrons (int): Number of electrons in isotope

    Returns:
        String: Electron configuration
    """
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

def nobleGasCorrection(config, specifier, nobleGas):
    """
    Takes in the electron config, the electron subshell associated with the noble gas in the numElectron range and the nobleGas being used
    Returns the correct noble gas notation

    Args:
        config (String): Feed in the current electron configuration
        specifier (String): Everything behind and including the specifier will be removed in the return
        nobleGas (String): Noble gas being used in the noble gas notation electron configuration 
    Returns:
        String: 
    """
    pos = config.find(specifier)
    if pos != -1:
        newConfig = nobleGas + config[pos + len(specifier):]
        return newConfig
    return "Err; specifier not found"

#"main" area of code
print("Input -1 to quit")
mode = str(input("Noble gas mode? (Y/N): "))
if mode.lower() == 'y':
    nobleGasMode = True
else:
    nobleGasMode = False    
while True:
    if nobleGasMode:
        numElectrons = int(input("Enter the number of electrons present in the atom: "))
        if numElectrons == -1:
            break
        configuration = generateElectronConfiguration(numElectrons)
        #This massive if elif chain handles ranges and assigns noble gas notation to the closest noble gas
        if 2 > numElectrons:
            print("nobleGasMode not applicable")
        elif 10 > numElectrons > 2 :
            nobleGas = "[He]"
            configuration = nobleGasCorrection(configuration,"1s^2",nobleGas)
        elif 18 > numElectrons >= 10:
            nobleGas = "[Ne]"
            configuration = nobleGasCorrection(configuration,"2p^6",nobleGas)
        elif 36 > numElectrons >= 18:
            nobleGas = "[Ar]"
            configuration = nobleGasCorrection(configuration,"3p^6",nobleGas)
        elif 54 > numElectrons >= 36:
            nobleGas = "[Kr]"
            configuration = nobleGasCorrection(configuration,"4p^6",nobleGas)
        elif 86 > numElectrons >= 54:
            nobleGas = "[Xe]"
            configuration = nobleGasCorrection(configuration,"5p^6",nobleGas)
        elif numElectrons > 86:
            nobleGas = "[Rn]"
            configuration = nobleGasCorrection(configuration,"6p^6",nobleGas)
        else:
            configuration = "Err; no valid electron configuration found"
            nobleGas = ""  
              
        print(configuration)         
    else:    
        numElectrons = int(input("Enter the number of electrons present in the atom: "))
        if numElectrons == -1:
            break
        print(generateElectronConfiguration(numElectrons))