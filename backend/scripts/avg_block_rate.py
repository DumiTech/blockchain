import time

from config import SECONDS
from blockchain import Blockchain
# this script contains code that mines a bunch of new blocks

blockchain = Blockchain()

times = []

for i in range(900):
    start_time = time.time_ns()
    blockchain.add_block(i)
    end_time = time.time_ns()

    mining_time = (end_time - start_time) / SECONDS
    times.append(mining_time)

    avg_time = sum(times) / len(times)

    print(f'New block difficulty: {blockchain.chain[-1].difficulty}\n')

    print(f'Time to mine new block: {mining_time}s\n')
    print(f'Average time to add blocks: {avg_time}s\n')
