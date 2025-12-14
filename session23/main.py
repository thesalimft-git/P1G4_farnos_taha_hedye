from bank_system import BankSystem
from data_manager import DbManager
from funcs import show_menu


dbm = DbManager()
try:
    accounts = dbm.get()
except:
    accounts = dict()

bs = BankSystem(accounts)
      
def main():  
    while True:
        show_menu()
        command = input('select from menu: ')
        
        match command:
            case '1':
                bs.show_info()
                
            case '2':
                id = input('id: ')
                name = input('name: ')
                amount = input('amount: ')
                bs.create_account(int(id), name, float(amount))
                
            case '3':
                id = input('id: ')
                amount = input('amount: ')
                bs.deposit(int(id), float(amount))
                                                   
                
            case '4':
                id = input('id: ')
                amount = input('amount: ')
                bs.withdraw(int(id), float(amount))
                                                   
            case '5':
                id_from = input('from id: ')
                id_to = input('to id: ')
                amount = input('amount: ')
                bs.transfer(int(id_from), int(id_to), float(amount))  
            
            case '6':
                dbm.set(accounts)
                break
        
    
    
    
    



main()