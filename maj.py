#Shell reconer
import os 
import webbrowser
device = "none"
device = input("entrez l'IP cible >")
def loopback():
    command = input("Reconer("+device+")> ")
    if command == "aide":
        print(''' 

        
        

        ------------- DEDSEC ---------------

                D    D    D
                DD  D D  DD
                D DD   DD D
                D DD   DD D
                DD  D D  DD
                D    D    D

        
        -devlopé par Le Théoritien-
        -traduit par Canardcoincoin (c'est aussi moi qui ai fait tout les truc stylé)-

        ====================
        Commandes de base :
        aide : déroule le menu d'aide 
        inst-deps : installer les dépendances 
        C-Target : change l'IP cible
        ====================
        Commandes de Scan :
        nmap-dvs : (-O) search for the remote system
        nmap-full : (all) Full nmap scan 
        nmap-full-H : (all -Pn) full nmap scan without host discorvery
        nmap-dvs-H : search for the remote scan without host discovery (-Pn)
        ====================
        Commandes d'Exportation :
        Xport-nmap-dvs : export the nmap scan (.txt file)
        ====================
        Commande qui servira peut être à quelque chose dans le futur
        -*Delta_Quantinium*- : en gros c'est pour défoncer un PC
        ''')
        loopback()
    elif command == "verify-vir":
        vtbchck = input("virus to be checked >>> ")
        print("Virus total will opened pleas upload the virus ")
        print("wait 10 seconds")
        time.sleep(5)
        webbrowser.open_new("virustotal.fr")   
        loopback()    

    elif command == "inst-dep":
        import os 
        os.system("sudo apt-install openvas")
        os.system("sudo apt install gvm")
        os.system("sudo apt install nmap")
        os.system("gvm-check-setup")    
        loopback()
    elif command == "exit":
        print("quitting ["+device+"]")
        import time
        time.sleep(1)
        print("cleaning cach ...")
        time.sleep(2)
        quit()
    elif command == "Xport-nmap-dvs":
        filesrt = input(".txt file destination >>> ")
        print("the txt file will saved on '"+ filesrt +"'")
        os.system("sudo nmap -O "+device+" "+filesrt)
        loopback()
    elif command == "update":
        print("Updating pleas wait :")
        print("getting updates ...[github.com/h-tech-dev36/ReconerShell] ")
        os.system("git clone https://github.com/H-Tech-Dev36/Reconer-Shell.git")
        loopback()

    else:
        print("'"+command+"' is not a command ! type 'help' to view commands.")
        loopback()

loopback()
