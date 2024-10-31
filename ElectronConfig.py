def generateElectronConfiguration(numElectrons,returnAsList=False,nobleGasMode=False):
    """
    Builds standard electron configuration

    Args:
        numElectrons (int): Number of electrons in isotope

    Returns:
        String: Electron configuration
    """
    
    if numElectrons == 24:
        if nobleGasMode:
            return "[Ar] 3d^5 4s^1"
        else:
            return "1s^2 2s^2 2p^6 3s^2 3p^6 4s^1 3d^5"
    elif numElectrons == 29:
        if nobleGasMode:
            return "[Ar] 3d^10 4s^1"
        else:
            return "1s^2 2s^2 2p^6 3s^2 3p^6 4s^1 3d^10"
        
    subshells = [("1s", 2), ("2s", 2), ("2p", 6), ("3s", 2), ("3p", 6), ("4s", 2), 
                 ("3d", 10), ("4p", 6), ("5s", 2), ("4d", 10), ("5p", 6), ("6s", 2), 
                 ("4f", 14), ("5d", 10), ("6p", 6), ("7s", 2), ("5f", 14), ("6d", 10), 
                 ("7p", 6)]
    
    electronConfiguration = []
    atomicNumber = numElectrons
    for subshell, capacity in subshells:
        if numElectrons <= 0:
            break
        electronsInSubshell = min(numElectrons, capacity)
        electronConfiguration.append(f"{subshell}^{electronsInSubshell}")
        numElectrons -= electronsInSubshell
    if nobleGasMode:
        #This massive if elif chain handles ranges and assigns noble gas notation to the closest noble gas
        electronConfigurationAsString = " ".join(electronConfiguration)
        if 2 > atomicNumber:
            print("nobleGasMode not applicable")
        elif 10 > atomicNumber > 2 :
            nobleGas = "[He]"
            configuration = nobleGasCorrection(electronConfigurationAsString,"1s^2",nobleGas)
        elif 18 > atomicNumber >= 10:
            nobleGas = "[Ne]"
            configuration = nobleGasCorrection(electronConfigurationAsString,"2p^6",nobleGas)
        elif 36 > atomicNumber >= 18:
            nobleGas = "[Ar]"
            configuration = nobleGasCorrection(electronConfigurationAsString,"3p^6",nobleGas)
        elif 54 > atomicNumber >= 36:
            nobleGas = "[Kr]"
            configuration = nobleGasCorrection(electronConfigurationAsString,"4p^6",nobleGas)
        elif 86 > atomicNumber >= 54:
            nobleGas = "[Xe]"
            configuration = nobleGasCorrection(electronConfigurationAsString,"5p^6",nobleGas)
        elif atomicNumber > 86:
            nobleGas = "[Rn]"
            configuration = nobleGasCorrection(electronConfigurationAsString,"6p^6",nobleGas)
        else:
            configuration = "Err; no valid electron configuration found"
            nobleGas = ""
        return ("Configuration: "+configuration)
    else:
        if returnAsList:
            return electronConfiguration
        else:
            configuration = "\nConfig = " + " ".join(electronConfiguration)
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

def unpairAlgorithm(midpoint,electronsInLastSubshell):
    if midpoint*2 > electronsInLastSubshell > midpoint:
        unpairedElectrons = electronsInLastSubshell - (electronsInLastSubshell % midpoint) * 2
    elif electronsInLastSubshell == midpoint*2:
        return 0
    else:
        unpairedElectrons = electronsInLastSubshell
    return unpairedElectrons

def findUnpairedElectrons(config):
    lastSubshellData = config[-1]
    electronsInLastSubshell = int(lastSubshellData[-1])
    
    if 's' in lastSubshellData:
        return (electronsInLastSubshell%2)
        
    elif 'p' in lastSubshellData:
        return unpairAlgorithm(3,electronsInLastSubshell)
    
    elif 'd' in lastSubshellData:
        return unpairAlgorithm(5,electronsInLastSubshell)
    
    elif 'f' in lastSubshellData:
        return unpairAlgorithm(7,electronsInLastSubshell)
    
#"main" area of code
print("""
/======================================\\
|| ____                _      ___  _  ||
|||  _ \  __ _ ___ ___| |__  / _ \/ | ||
||| | | |/ _` / __/ __| '_ \| | | | | ||
||| |_| | (_| \__ \__ \ | | | |_| | | ||
|||____/ \__,_|___/___/_| |_|\___/|_| ||
\======================================/
""")
print("\nInput -1 to quit")
mode = str(input("Noble gas mode? (Y/N): "))
if mode.lower() == 'y':
    nobleGasMode = True
else:
    nobleGasMode = False
    
while True:
    
    numElectrons = int(input("Enter the number of electrons present in the atom: "))
    unpairedElectrons = findUnpairedElectrons(generateElectronConfiguration(numElectrons,True))
    
    if numElectrons == -1:
        break
    elif nobleGasMode:
        configuration = generateElectronConfiguration(numElectrons,False,True)  
        print(configuration)   
        print("Unpaired Electrons = "+str(unpairedElectrons))      
    else:    
        configuration = generateElectronConfiguration(numElectrons)  
        print(configuration)
        print("Unpaired Electrons = "+str(unpairedElectrons))
        
        