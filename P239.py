import hashlib
import json
from time import time

chain = []

def block(proof, previous_hash = None):
	transaction= {
		'sender': 'Satoshi',
		'recipient': 'Mike',
		'amount': '5 ETH'
	}

	data = {
	'block_height' : 1,
	'timestamp' : time(),
	'transactions' : transaction,
	'Block Reward' : "2.557430954505356948 Ether (2+ 0.557430954505356948)",
	'Uncles Reward' : "0",
	'Difficulty' : "7,317,161,775,076,869",
	'Total Difficulty' : "28,115,205,704,610,921,164,128",
	'Size' : "56,528 bytes",
	'Gas Used' : "14,935,987 (99.87%)",
	'Gas Limit' : "14,935,987",
	'proof' : proof,
	'previous_hash' : previous_hash
	}

	chain.append(block)
	print("block information:", data)
	string_object = json.dumps(data)
	block_string  =string_object.encode()

	raw_hash = hashlib.sha256(block_string)
	hex_hash = raw_hash.hexdigest()
	print("Hash code of block:", hex_hash)

block(previous_hash="No previous hash. Since this is the first block.", proof=000)