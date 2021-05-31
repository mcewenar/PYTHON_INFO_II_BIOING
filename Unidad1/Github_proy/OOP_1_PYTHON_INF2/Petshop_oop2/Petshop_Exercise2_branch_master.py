#Petshop
import datetime;
class Pets:
    def __init__(self):
        self.__name = "";
        self.__num_his = 0;
        self.__type = "";
        self.__pes = 0;
        self.__date = "";
        self.__list_medi = [];
    
    def see_weight(self):
        return self.__pes;
    def see_name(self):
        return self.__name;
    def see_histo(self):
        return self.__num_his;
    def see_type(self):
        return self.__type;
    def see_date(self):
        return self.__date;
        #return self.__date;
    def see_medi(self):
        return self.__medi;
    def see_listmedi(self):
        return self.__list_medi;
    def see_enter_date(self):
        return self.__enter_date;
    

    def asign_weight(self,a):
        self.__pes=a;
    def asign_name(self,s):
        self.__name = s;
    def asign_histo(self,d):
        self.__num_his = d;
    def asign_type(self,f):
        self.__type = f;
    def asign_date(self,g):
        #datetime.datetime.now();
        #self.datetime.now() = g;
        self.__date = g;
    def asign_listmedi(self,h):
        self.__list_medi = h;

    def asign_enter_date(self,o):
        self.__enter_date = o;
    


class Medicine:
    def __init__(self):
        self.__name = "";
        self.__dosis = 0;

    def see_name(self):
        return self.__name;
    def see_dosis(self):
        return self.__dosis;
    
    def asign_name(self,q):
        self.__name = q;
    def asign_dosis(self,w):
        self.__dosis = w;
class System:
    def __init__(self):
        self.__pets_list = [];
        #self.__pets_num = len(self.__pets_list)
    def enter_pet(self, m):
        self.__pets_list.append(m);

    def check_exist(self, nhc):
        found = False;
        for m in self.__pets_list:
            if nhc == m.see_histo():
                found = True
                break
        return found
    def strftime(self,nhc):
        exist = self.check_exist(nhc)
        if exist == True:
            current_time = datetime.datetime.now() 
            return current_time;
        else:
            print("Pet don't exist");
    def seePets(self,nhc):
        for m in self.__pets_list:
            if nhc == m.see_histo():
                return m;
    
    def see_enter_date(self,nhc):
        exist = self.check_exist(nhc);
        if exist == True:
            m = self.seePets(nhc)
            
            return m.see_enter_date()
        else: 
            return "The pet don't exist"

        
    def num_pets(self):
        return len(self.__pets_list);

    def see_medicament(self, historia): 
        for masc in self.__pets_list:
            if historia == masc.see_histo():
                return masc.see_listmedi();
        return None;
    def delete_pets(self, hist):
        for masc in self.__pets_list:
            if hist == masc.see_histo():
                self.__pets_list.remove(masc);
                return True;
        return False;
def main():
    p1 = System();
    while True:
        print(" To continued, choose the next option: \n")
        menu = int(input(" 1. Enter Pet \n 2. See date enter pet \n 3. See amount pets enter in the system \n 4. See medicine \n 5. Delete pet \n 6. Exit "))
        if menu == 1:
            if p1.num_pets() >= 10:
                print("Dont have enought space");
                continue;
            history=int(input("\n Enter the clinic history of the pet: "))
            #checking=p1.num_pets(history);
            if p1.check_exist(history) == False:
                name = input("Enter the name: ");
                type = input("Enter the type: ");
                wei = input("Enter the weight: ");
                d = int(input(" Enter day"))
                m = int(input("Enter month"))
                a = int(input("Enter Year"))
                f = datetime.datetime(a,m,d)
                nm = int(input("Enter amount medicamentos: "))
                list_med=[];
            
                for me in range(0,nm):
                    name_med = input("Medicine Name: ");
                    dosis = int(input("Enter dosis: "));
                    medicin = Medicine();
                    medicin.asign_dosis(dosis);
                    medicin.asign_name(name_med);
                    list_med.append(medicin);
                #date = p1.datetime.now();
                pet = Pets();
                pet.asign_enter_date(f.strftime("%x"))
                pet.asign_listmedi(list_med);
                pet.asign_name(name);
                pet.asign_histo(history);
                pet.asign_weight(wei);
                pet.asign_type(type);
                p1.enter_pet(pet);
                
            else: 
                print("Already pet exist with this clinic history");
        elif menu == 2:
            nhc = int(input("Enter clinic history of pets "))
            
            datee = p1.see_enter_date(nhc)
            print("The pet with: " + str(nhc) + " was joined on " + str(datee))
            #p2 = Pets()
            #q = int(input("enter clinic history of pet"));
            #p2.asign_date(q)
            #date = p2.see_date();
            #date = p1.see_enter_date(q);
            #if date != None:
                #print("Date is " + str(date))
        elif menu == 3:
            nume = p1.num_pets();
            print("There are " + str(nume) + " pets");
        elif menu == 4:
            q = int(input("Enter clinic history: "));
            medica = p1.see_medicament(q);
            if medica != None:
                print("Medicament supply is ")
                for m in medica:
                    print(f"\n - {m.see_name()}");

            else: 
                print("The history enter is not valid");
        elif menu == 5:
            q = int(input("Enter clinic history that you to delet"));
            delete = p1.delete_pets(q);
            if delete == True:
                print("Delete pet with clinic history " + str(q));
            else: 
                print("Don't pet delete");
        elif menu == 6:
            print("See you later");
            break;
main();
