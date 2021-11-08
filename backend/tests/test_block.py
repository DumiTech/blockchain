import time
import sys
import pytest

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


@pytest.fixture
def last_block():
    return Block.genesis()


@pytest.fixture
def block(last_block):
    return Block.mine_block(last_block, 'test')


def test_is_valid_block(last_block, block):
    Block.is_valid_block(last_block, block)


def test_is_valid_block_bad_last_hash(last_block, block):
    block.last_hash = 'test_purposes_last_hash'

    with pytest.raises(Exception, match='last_hash must be correct'):
        Block.is_valid_block(last_block, block)


def test_is_valid_block_bad_proof_of_work(last_block, block):
    block.hash = 'fff'

    with pytest.raises(Exception, match='proof of work requirement was not met'):
        Block.is_valid_block(last_block, block)


def test_is_valid_block_difficulty(last_block, block):
    jumped_difficulty = 10
    block.difficulty = jumped_difficulty
    block.hash = f'{"0" * jumped_difficulty}1111asdf'

    with pytest.raises(Exception, match='block difficulty must adjust with 1'):
        Block.is_valid_block(last_block, block)


def test_is_valid_block_bad_block_hash(last_block, block):
    block.hash = '00' * 12 + 'qwerty'

    with pytest.raises(Exception, match='block hash must be correct'):
        Block.is_valid_block(last_block, block)
