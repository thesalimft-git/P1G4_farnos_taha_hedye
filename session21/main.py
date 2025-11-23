# {
#     '123': {
#         'owner': 'ali',  
#         'balance': 100.0, 
#         'transactions': [
#             'Account created with initial deposit of $100.0'
#         ]
#     }
# }


from datamanager import DbManager

class BankSystem:
    def __init__(self):
        dbm = DbManager()
        try:
            accounts = dbm.get()
        except:
            accounts = dict()