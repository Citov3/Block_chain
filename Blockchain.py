import hashlib
import json
from time import time

class  Blockchain(object):

    def __init__(self):

        self.current_transactions = []
        self.chain = []

        #originally, the genesis block is created with a proof of 100 and a previous hash of 1
        self.new_block(previous_hash=1, proof=100)
        
#Create a new Block in the Blockchain
    def new_block(self, proof, previous_hash=None):
        block ={
            'index': len(self.chain) + 1,
            'timestamp': time(),
            'transactions': self.current_transactions,
            'proof': proof,
            'previous_hash': previous_hash or self.hash(self.chain[-1])
        }

        self.current_transactions = [] #resets the hash of the current list of transactions

        self.chain.append(block)
        return block
    
        

    def new_transaction(self, sender, recipient, amount):
        self.current_transactions.append({
            'sender': sender,
            'recipient': recipient,
            'amount': amount
        })
        return self.last_block['index'] + 1


    @property
    def last_block(self):
        return self.chain[-1]
    
        pass

    @staticmethod
    def hash(block):
        pass

    def last_block(self):
        pass



#adds a transaction to the list,
# it returns the index of the block which the transaction will be added to—the next one to be mined.

