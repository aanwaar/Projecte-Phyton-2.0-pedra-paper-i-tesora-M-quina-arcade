#Bucle principal del programa
while True:
    def menu(): 
        # Importar l'arxiu amb els jocs.
        import jocs
        print("MINI ARCADE")
        print("Pedra,Paper,Tisora 1")
        print("Endivinar el nombre 2")
        print("Sortir S")
        # Triem el joc
        choice = input("Triem el joc (1 o 2) o sortim amb (S): ")
        if choice == '1':
            jocs.janken()
        elif choice == '2':
            jocs.nana()
        elif choice == 'S' or choice == 's':
            print("Gràcies per provar aquest joc")
            break
# Comprovarem si estem dins del fitxer principal
    if __name__ == "__main__":
        menu()
        break