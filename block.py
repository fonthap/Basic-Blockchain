import database
import hashlib
import json
import time


class BlockchaininApp(object):
    def __init__(self):
        self.chain = []
        self.pending_transactions = []

    def new_block(self, transactions_hash = None,previous_hash=None):
        block = {
            'index': len(self.chain) + 1,
            'transactions': self.pending_transactions,
            'transactions_hash' : transactions_hash or self.hash(self.pending_transactions),
            'previous_hash': previous_hash or self.hash(self.chain[-1]),
        }
        self.pending_transactions = []
        self.chain.append(block)
        return block
        
    def new_transactionindatabase(self, team1, team2, score):
        transaction = {
            'transactions':len(self.pending_transactions)+1,
            'Team1': team1,
            'Team2': team2,
            'Score': score,
            'timestamp': time.ctime(time.time()),
        }
        database.insert_db((team1, team2, score, time.ctime(time.time()),'',''))
        self.pending_transactions.append(transaction)
        return self.last_block['index'] + 1

    def new_blockindatabase(self,transactions_hash = None, previous_hash=None):
        block = {
            'index': len(self.chain) + 1,
            'transactions': self.pending_transactions,
            'transactions_hash' : transactions_hash or self.hash(self.pending_transactions),
            'previous_hash': previous_hash or self.hash(self.chain[-1]),
        }
        database.update_db((self.hash(self.pending_transactions) or transactions_hash,previous_hash or self.hash(self.chain[-1]),len(self.chain) + 1))
        self.pending_transactions = []
        self.chain.append(block)
        
        return block
    
    
        

    @property
    def last_block(self):
        return self.chain[-1]

    def new_transaction(self, team1, team2, score, timestamp):
        transaction = {
            'transactions': len(self.pending_transactions)+1,
            'Team1': team1,
            'Team2': team2,
            'Score': score,
            'timestamp': timestamp,
        }
        # database.insert_db((team1, team2, score, time.ctime(time.time()),''))
        self.pending_transactions.append(transaction)
        return self.last_block['index'] + 1

    def hash(self, block):
        string_object = json.dumps(block, sort_keys=True)
        block_string = string_object.encode()
        raw_hash = hashlib.sha256(block_string)
        hex_hash = raw_hash.hexdigest()
        return hex_hash


