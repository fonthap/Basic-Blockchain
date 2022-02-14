import hashlib
import json
import time
import database

class BlockchaininDatabase(object):
    def __init__(self):
        self.chain = []
        self.pending_transactions = []

# Create a new block listing key/value pairs of block information in a JSON object. Reset the list of pending transactions & append the newest block to the chain.

    def new_block(self,transactions_hash = None, previous_hash=None):
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

#Search the blockchain for the most recent block.
    @property
    def last_block(self):
        return self.chain[-1]

# Add a transaction with relevant info to the 'blockpool' - list of pending tx's. 
    def new_transaction(self, team1, team2, score):
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

# receive one block. Turn it into a string, turn that into Unicode (for hashing). Hash with SHA256 encryption, then translate the Unicode into a hexidecimal string.
    def hash(self, block):
        string_object = json.dumps(block, sort_keys=True)
        block_string = string_object.encode()  
        raw_hash = hashlib.sha256(block_string) 
        hex_hash = raw_hash.hexdigest()
        return hex_hash

def setup():
        blockchain = BlockchaininDatabase()

        blockchain.new_block(previous_hash="Dota2 - Esport")
        database.insert_db(('', '', '', '','','Dota2 - Esport'))

        blockchain.new_transaction("T1", "TNC Predator", '2 – 0')
        blockchain.new_block()

        blockchain.new_transaction("Motivate.Trust Gaming", "Execration", '2 – 0')
        blockchain.new_block()

        blockchain.new_transaction("BOOM Esports", "OB.Neon", '2 – 0')
        blockchain.new_block()
        
        blockchain.new_transaction("Team SMG", "Fnatic", '2 – 0')
        blockchain.new_block()

        blockchain.new_transaction("Motivate.Trust Gaming", "TNC Predator", '2 – 0')
        blockchain.new_block()

        blockchain.new_transaction("Execration", "OB.Neon", '2 – 1')
        blockchain.new_block()

        blockchain.new_transaction("T1", "Team SMG", '2 – 0')
        blockchain.new_block()

        blockchain.new_transaction("BOOM Esports", "Fnatic", '2 – 0')
        blockchain.new_block()

        blockchain.new_transaction("Team SMG", "Motivate.Trust Gaming", '2 – 0')
        blockchain.new_block()

        blockchain.new_transaction("BOOM Esports", "Team SMG", '2 – 0')
        blockchain.new_block()


if __name__ == '__main__':
    database.create_db()
    setup()
       

