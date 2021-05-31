#Sistema de pacientes
class Patients: #Constructor
    def __init__(self):
        self.__name = "";
        self.__idn = 0;
        self.__gen = "";
        self.__servi = "";
    def seeName(self): #Methods Get and see Dates Patients
        return self.__name;
    def seeId(self):
        return self.__idn;
    def seeGen(self):
        return self.__gen;
    def seeServi(self):
        return self.__servi;
    
    def asignName(self,n):
        self.__name = n;
    def asignId(self,p):
        self.__idn = p;
    def asignGen(self,q):
        self.__gen = q;
    def asignServ(self,z):
        self.__servi = z;

class System: #Usando la función main.
    #La idea es que haya un método principal 
    # desde donde se gestiona la entrada de datos 
    # por teclado y la salida de
    # información a Pantalla
    def __init__(self):
        self.__lista_patients = [];
    def check_patient(self, identi):
        find = False;
        for p in self.__lista_patients:
            if identi == p.seeId():
                find = True;
                break;
        return find;
    def enter_patients(self,pac):
        if self.check_patient(pac.seeId()) == False:
            self.__lista_patients.append(pac);
            return True;
        return True;
    def seeDate_patients(self, c):
        if self.check_patient(c) == False:
            return None;

        for p in self.__lista_patients:
            if c == p.seeId():
                return p;
    def seeNum_patients(self):
        return len(self.__lista_patients);
    
    def Delete_patients(self, c):
        for p in self.__lista_patients:
            if c == p.seeId():
                self.__lista_patients.remove(p);

                return True;
            return False;

        
        
        #print("There are: " + str(len(self.__lista_patients() + "patients")))
def main(): #En programas con múltiples funciones es necesario indicar la función con main
#principal, main, que será la encargada de llamar las otras funciones
    sys = System() #Create instance of system class
    while True:
        while True:

            try:
                option = int(input("1. Enter new patient \n 2. Check patients \n 3. Patients amount \n 4. Delete patient \n 5. Exit "))
                break;
            except TypeError:
                print("Letters are not allowed")
            

        if option == 1:
            #1. Enter patients
            print("To continue request you too many dates");
            #Request Patients dates
            nom = input("Enter patient name: ");
            identi = int(input("Enter ID: "));
            gender = input("Enter Gender: ");
            service = input("Enter Service: ");
            #2. Create Patient Object
            pac = Patients();
            #As patients has empty, I must enter him information
            pac.asignName(nom);
            pac.asignId(identi);
            pac.asignGen(gender);
            pac.asignServ(service);
            #3. This store in the list that within of the system class
            result = sys.enter_patients(pac);
            if result == False:
                print("The patient now exist");
            else: 
                print("Patient add");
            
        elif option == 2:
            #1. Request ID that I like to want
            c = int(input("Enter ID: "));
            p = sys.seeDate_patients(c);
            #2. If you find patient, print dates
            if  p != None:

                print("Name: " + p.seeName());
                print("Id: " + str(p.seeId()));
                print("Gender: " + p.seeGen());
                print("Service: " + p.seeServi());
            else:
                print("Patient not found");
            


        elif option == 3:
            print("Now there are " + str(sys.seeNum_patients()) + " patients");
        elif option == 4:
            c = int(input("Enter ID: "));
            p = sys.seeDate_patients(c);
            print("Name: " + p.seeName());
            print("Id: " + str(p.seeId()));
            print("Gender: " + p.seeGen());
            print("Service: " + p.seeServi());
            sys.Delete_patients(c);
            print("Patient with ID " + str(p.seeId()) + " has remove of Data Base") ;
            continue;


        elif option == 5:
            print("Bye");
            break;
        else:
            print("Impedido xDXd. Choose correct option");
            continue;
#Introspección allow priorizar la función main para ejecutar las demás funciones.
main()
        



"""identi = int(input("Enter ID"));
        for patients in self.__lista_patients:
            if identi == patients.SeeId():
                print("Nombre: " + patients.seeName());
                print("Id: " + patients.seeId());
                print("Género " + patients.seeGen());
                print("Servicio: " + patients.seeServi());
        
    
        p1 = Patients(); #Create us our object
        p1.asignName(nom); #Asign to object p1 our dates
        p1.asignId(identi);
        p1.asignGen(gender);-
        p1.asignServ(service)

        self.__lista_patients(p1); #Save patients in list

        self.__num_patients = len(self.__lista_patients);"""