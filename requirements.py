import os

def sysChecks():
    pip=os.system("pip3")
    if pip == '\'pip3\' is not recognized as an internal or external command,operable program or batch file.':
        print('Please install PIP3 for the software to work :))')
        exit()
        
    # try:
    #     pip=os.system("pip3")
    # except Exception as e: 
    #     print("{}\nPlease install PIP3 for the software to work :))".format(e))
    #     exit()      

def main():
    sysChecks()
    rarfile=os.system("pip3 install rarfile pyfiglet py-term")
    if rarfile!=None:
        os.system("pip3 install termcolor")
    else:
        print("Cannot install rarfile,pyfiglet,py-term.\nConsider installing the scripts seperately.")
        exit()
    print("All systems are a go! :))")

if __name__ == "__main__":
    main()