
class Person:

    def __init__(self, name, address, phone_number):
        self.__name = name
        self.__address = address
        self.__phone_number = phone_number 

    def print_person(self):
        print('Name:',self.__name)
        print('Addr:',self.__address)
        print('Phone:',self.__phone_number)

class Customer(Person):
    def __init__(self,name,address,phone_number,cust_number,on_list):
        Person.__init__(self,name,address,phone_number)

        #Initialize the cust number and on_list attributes
        self.__cust_number = cust_number
        self.__on_list = on_list

    def print_person(self):
        Person.print_person(self)
        print('Customer Number:',self.__cust_number)
        if self.__on_list:
            print('On mailing list: Yes')
        else:
            print('On mailing list: No')

