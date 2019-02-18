
import datetime
import hashlib
import json
from flask import Flask, jsonify




difficulty = 3

def hash_operation(new_proof, previous_proof = 0):
    return hashlib.sha256(str(new_proof**2 - previous_proof**2).encode()).hexdigest()

def validate_proof(hash_operation, difficulty):
    #return hash_operation[:       ] == '0' *

class Blockchain:

    def __init__(self):
        self.chain = []
        #self.create_block()

    def create_block(self, proof, previous_hash):
        #block = {'index': ,
                 'timestamp': str(datetime.datetime.now()),
                 'proof': proof,
                 'previous_hash': previous_hash}
        self.chain.append(block)
        return block

    def get_previous_block(self):
        return self.chain[-1]

    def proof_of_work(self, previous_proof, new_proof = 1):
        #
            #
        #

    def hash(self, block):
        encoded_block = json.dumps(block, sort_keys = True).encode()
        return hashlib.sha256(encoded_block).hexdigest()

    def is_chain_valid(self, chain):
        previous_block = chain[0]
        block_index = 1
        #
            block = chain[block_index]
            #
                return False
            #previous_proof = previous_block[   ]
            #proof = block[    ]
            #if validate_proof(hash_operation(           ),        ) is False:
                return False
            #previous_block = 
            #block_index 
        return True


app = Flask(__name__)


blockchain = Blockchain()



@app.route('/mine_block', methods = ['GET'])
def mine_block():
    previous_block = blockchain.get_previous_block()
    #previous_proof = 
    #proof = blockchain.proof_of_work(        )
    #previous_hash = blockchain.hash(                )
    #block = blockchain.create_block(           ,               )
    response = {'message': 'Congratulations, you just mined a block!',
                'index': block['index'],
                'timestamp': block['timestamp'],
                'proof': block['proof'],
                'previous_hash': block['previous_hash']}
    return jsonify(response), 200

#@app.route('/get_chain', methods =        )
#
    response = {'chain': blockchain.chain,
                'length': len(blockchain.chain)}
    return jsonify(response), 200


#@app.route('     ', methods = ['GET'])
#
    #is_valid = blockchain.          (blockchain.chain)
    if is_valid:
        #response = {'message':                   }
    else:
        #
    return jsonify(response), 200


app.run(host="0.0.0.0", port=5000)
app.run_server(debug=False)
