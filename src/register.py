import pymongo
from logging import debug

def save_in_cluster(balance_info, conn_string='mongodb://localhost:27017'):
    """Save email information to mongodb cluster
    """
    debug("conn string: ", conn_string)
    client = pymongo.MongoClient(conn_string)

    balance_db = client['historial']
    collection = balance_db["customers"]

    x = collection.insert_one(balance_info)
    
    debug(x.inserted_id) 

    return x.inserted_id

if __name__ == "__main__":
    info = {'user_name': 'romina ivanna bareiro', 'trx_qtty': [0, 0, 0, 0, 0, 0, 2, 2, 0, 0, 0, 0], 'debit': [0, 0, 0, 0, 0, 0, -10.3, -20.46, 0, 0, 0, 0], 'credit': [0, 0, 0, 0, 0, 0, 60.5, 10.0, 0, 0, 0, 0]}
    id = save_in_cluster(info)
