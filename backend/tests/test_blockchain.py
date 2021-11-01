import sys
from block import Block

sys.path.append("../backend")

from blockchain import Blockchain
from block import GENESIS_DATA


def test_block_chain():
    blockchain = Blockchain()

    assert blockchain.chain[0].hash == GENESIS_DATA["hash"]


def test_add_block():
    blockchain = Blockchain()
    data = "test"
    blockchain.add_block(data)

    assert blockchain.chain[-1].data == data
