from bank_system import BankSystem
from data_manager import DbManager

dbm = DbManager()
try:
    accounts = dbm.get()
except:
    accounts = dict()
    
    
    
    
    
def main():  
    bs = BankSystem(accounts)
    print(accounts)
    bs.create_account(121, 'ali', 100)
    bs.create_account(122, 'reza', 100)
    print(accounts)
    bs.transfer(121, 122, 50)
    print(accounts)
    
    
    
    



main()