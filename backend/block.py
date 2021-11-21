import time

from crypto_hash import crypto_hash
from config import MINE_RATE

GENESIS_DATA = {
    "timestamp": 1,
    "last_hash": "genesis_last_hash",
    "hash": "genesis_hash",
    "data": [],
    "difficulty": 3,
    "nonce": 'genesis_nonce'
}


class Block:
    """
    Block -> unit of storage
    Store transactions in a blockchain that supports a cryptocurrency.
    """

    def __init__(self, timestamp, last_hash, hash, data, difficulty, nonce):
        self.timestamp = timestamp
        self.last_hash = last_hash
        self.hash = hash
        self.data = data
        self.difficulty = difficulty
        self.nonce = nonce

    def __repr__(self):
        return (
            "Block(\n"
            f"timestamp: {self.timestamp}, \n"
            f"last_hash: {self.last_hash}, \n"
            f"hash: {self.hash}, \n"
            f"data: {self.data}, \n"
            f"difficulty: {self.difficulty}, \n"
            f"nonce: {self.nonce})\n"
        )

    def __eq__(self, other):
        return self.__dict__ == other.__dict__

    def to_json(self):
        """
        Serialize the block into a dictionary of its attributes.
        """
        return self.__dict__

    @staticmethod
    def mine_block(last_block, data):
        """
        Mine a block based on the given last_block and data, until a block hash that meets the leading 0's proof of work requierment is found.
        """
        timestamp = time.time_ns()
        last_hash = last_block.hash
        difficulty = Block.adjust_difficulty(last_block, timestamp)
        nonce = 0
        hash = crypto_hash(timestamp, last_hash, data, difficulty, nonce)

        while hash[0:difficulty] != '0' * difficulty:
            nonce += 1
            timestamp = time.time_ns()
            difficulty = Block.adjust_difficulty(last_block, timestamp)
            hash = crypto_hash(timestamp, last_hash, data, difficulty, nonce)

        return Block(timestamp, last_hash, hash, data,  difficulty, nonce)

    @staticmethod
    def genesis():
        """
        Generate the genesis block.
        """
        return Block(
            GENESIS_DATA["timestamp"],
            GENESIS_DATA["last_hash"],
            GENESIS_DATA["hash"],
            GENESIS_DATA["data"],
            GENESIS_DATA['difficulty'],
            GENESIS_DATA['data']
        )

    @staticmethod
    def adjust_difficulty(last_block, new_timestamp):
        '''
        Calculate the adjusted difficulty according to the MINE_RATE. 
        Increase or decrease the difficulty according to the speed of mined blocks.
        '''
        if (new_timestamp - last_block.timestamp < MINE_RATE):
            return last_block.difficulty + 1

        if (last_block.difficulty - 1) > 0:
            return last_block.difficulty - 1

        return 1

    @staticmethod
    def is_valid_block(last_block, block):
        '''
        Validate the block by enforcing the following rules:
            - the block must have the proper last_hash reference
            - the block must meet the proof of work requierment
            - the difficulty must only adjust by 1
            - the block hash must be a valid combination of the block fields
        '''
        if block.last_hash != last_block.hash:
            raise Exception('The block last_hash must be correct')

        if block.hash[0:block.difficulty] != '0' * block.difficulty:
            raise Exception('The proof of work requirement was not met')

        if abs(last_block.difficulty - block.difficulty) > 1:
            raise Exception('The block difficulty must adjust with 1')

        reconstructed_hash = crypto_hash(
            block.timestamp,
            block.last_hash,
            block.data,
            block.nonce,
            block.difficulty
        )

        if block.hash != reconstructed_hash:
            raise Exception("The block hash must be correct")


# experimentation code:
def main():
    genesis_block = Block.genesis()

    bad_block = Block.mine_block(genesis_block, 'boo')
    bad_block.last_hash = 'different_hash'

    try:
        Block.is_valid_block(genesis_block, bad_block)
    except Exception as e:
        print(f'is_valid_block: {e}')

    # block = Block.mine_block(genesis_block, "first")
    # print(block)


if __name__ == "__main__":
    main()
