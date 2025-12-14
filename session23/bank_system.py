# {
#     '123': {
#         'owner': 'ali',  
#         'balance': 100.0, 
#         'transactions': [
#             'Account created with initial deposit of $100.0'
#         ]
#     }
# }

# 123- ali (100)


class BankSystem:
    def __init__(self, accounts):
        self.accounts = accounts
    
    def create_account(self, id:int, name:str, amount:float):
        self.accounts[id] = {
            'owner': name,  
            'balance': amount, 
            'history': [
                f'Account created with initial deposit of ${amount}'                    
            ]
        }
      
    def deposit(self, id:int, amount:float):
        balance = self.accounts.get(id).get('balance')
        if balance:
            self.accounts[id]['balance'] += amount
            self.accounts[id]['history'].append(f'deposite ${amount} at 20:20')               
        
    def withdraw(self, id:int, amount:float):
        balance = self.accounts.get(id).get('balance')
        if balance:
            self.accounts[id]['balance'] -= amount
            self.accounts[id]['history'].append(f'withdraw ${amount} at 20:20')               
            
    def transfer(self, id_from:int, id_to:int, amount:float):
        self.withdraw(id_from, amount)
        self.deposit(id_to, amount)
    
    def show_info(self):
        for id in self.accounts:
            print(f"{id}- {self.accounts[id]['owner']} (${self.accounts[id]['balance']})")
            
        
            
            
            
            
            
            







# class ==> map
# object, instance 

# method ==> function
# property ==> variable



