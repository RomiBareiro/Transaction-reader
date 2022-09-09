import pymongo
import logging

def insert_historic_balance(balance_info):

    print(balance_info)
    client = pymongo.MongoClient('mongodb://localhost:27017/')

    balance_db = client['historial']

    collection = balance_db["customers"]

    x = collection.insert_one(balance_info)
    
    logging.debug(x.inserted_id) 

    return x.inserted_id

if __name__ == "__main__":
    info = {'user_name': 'romina ivanna bareiro', 'trx_qtty': [0, 0, 0, 0, 0, 0, 2, 2, 0, 0, 0, 0], 'debit': [0, 0, 0, 0, 0, 0, -10.3, -20.46, 0, 0, 0, 0], 'credit': [0, 0, 0, 0, 0, 0, 60.5, 10.0, 0, 0, 0, 0]}
    id = insert_historic_balance(info)
