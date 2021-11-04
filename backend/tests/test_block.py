import time
import sys

from block import Block, GENESIS_DATA
from config import MINE_RATE, SECONDS

sys.path.append("../backend")

TEST_DELAY_TIME = MINE_RATE / SECONDS


def test_mine_block():
    last_block = Block.genesis()
    data = "test"
    block = Block.mine_block(last_block, data)

    assert isinstance(block, Block)
    assert block.data == data
    assert block.last_hash == last_block.hash
    assert block.hash[0:block.difficulty] == '0' * block.difficulty



def test_genesis():
    genesis = Block.genesis()

    assert isinstance(genesis, Block)
    assert genesis.timestamp == GENESIS_DATA["timestamp"]
    assert genesis.last_hash == GENESIS_DATA["last_hash"]
    assert genesis.hash == GENESIS_DATA["hash"]
    assert genesis.data == GENESIS_DATA["data"]
    assert genesis.difficulty == GENESIS_DATA["difficulty"]

    # for key, value in GENESIS_DATA.items():
    #     getattr(genesis, key) == value


def test_increased_time_mined_block():
    last_block = Block.mine_block(Block.genesis(), 'first')
    mined_block = Block.mine_block(last_block, 'second')

    assert mined_block.difficulty == last_block.difficulty + 1


def test_decrease_time_mined_block():
    last_block = Block.mine_block(Block.genesis(), 'first')
    time.sleep(TEST_DELAY_TIME)
    mined_block = Block.mine_block(last_block, 'second')

    assert mined_block.difficulty == last_block.difficulty - 1


def test_secure_mined_block():
    last_block = Block(
        time.time_ns(),
        'test_last_hash',
        'test_hash',
        'test_data',
        1,
        0
    )

    time.sleep(TEST_DELAY_TIME)
    mined_block = Block.mine_block(last_block, 'second')

    assert mined_block.difficulty == 1
