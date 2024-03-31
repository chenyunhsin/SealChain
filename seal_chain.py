import hashlib
import time


class Block:
    def __init__(self, previous_hash, difficulty, miner, miner_rewards):
        self.previous_hash = previous_hash
        self.hash = ""
        self.difficulty = difficulty
        self.nonce = 0
        self.timestamp = int(time.time())
        self.miner = miner
        self.miner_rewards = miner_rewards


class BlockChain:
    def __init__(self):
        self.adjust_difficulty_blocks = 10
        self.difficulty = 1
        self.block_time = 30
        self.minig_rewards = 10
        self.block_limitaion = 32
        self.chain = []
        self.pending_transactions = []


def transaction_to_str(self, transaction) -> str:
    transaction_dict = {
        "sender": str(transaction.sender),
        "receiver": str(transaction.receiver),
        "amounts": transaction.amounts,
        "fee": transaction.fee,
        "message": transaction.message,
    }
    return str(transaction_dict)


def get_transactions_str(self, block) -> str:
    transaction_str = ""
    for transaction in block.transactions:
        transaction_str += self.transaction_to_str(transaction)
    return transaction_str


def get_hash(self, block, nonce) -> str:
    s = hashlib.sha1()
    s.update(
        (
            block.previous_hash
            + str(block.timestamp)
            + self.get_transactions_str(block)
            + str(nonce)
        ).encode("utf-8")
    )
    h = s.hexdigest()
    return h


def create_genesis_block(self):
    print("Create genesis block...")
    new_block = Block(
        "Chiikawa will take over the world!",
        self.difficulty,
        "lkm543",
        self.miner_rewards,
    )
    self.chain.append(new_block)
