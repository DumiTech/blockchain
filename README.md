=========================================================================

This project was created to better understand this interesting area of blockchain and cryptocurrencies.
What could be a better way of understanding things if not by building them and think creatively?

=========================================================================

**Install all packages**

```
pip install -r requierments.txt
```

**Run the tests**

Make sure to activate the virtual environment

```
py -m pytest  #run this command from the backend directory level
```

**Run scripts**

```
py -m scripts.avg_block_rate    #run this command from the backend directory level
```

**Run the application and the API**

```
py -m app
```

Blockchain
The blockchain is a distributed and decentralized ledger that stores data such as transcations, and that is publicly shared across all the nodes of its network.

The block

- each block acts as a storage unit, it's given a data field which is used to store information in the block itself.
- is given a unique value
- part of a collections of blocks

Cryptographic hash functions -> generates a unique output for every unique input

Ledger (you can make the analogy of the blockchain as a ledger)
Ledger -> is a record keeping a books records, all the economic transactions of an organisation, contracts, payment movements, assets, etc.

Blockchain network -> by connecting to it you get a complete copy of the blockchain ledger with the entire recored history of trasactional data that has occurred through that block change lifetime (updates are made every time a change occurs)

Cryptocurrency is a digital medium of exchange.

Cryptocurrencies do leverage the blockchain, but the cryptocurrency is its own technology that has a blockchain as only one of its layers

Cryptocurrencies 3 main aspects:

1. Blockchain
2. Wallets
3. Mining

The cryptocurrency leverages the blockchain in order to keep a public database of transactions that everyone can access.

The main application of cryptography within a cryptocurrency is to give individuals the ability to generate unique digital signatures. The signature is based on a pair of cryptographic keys, one key is public and the other is private, both beeing stored in a wallet dedicated for each individual (wallet that has a unique address).

Private key makes transactions official.

Mining - miners do the work of adding transactions to the blockchain. When people submit transactions to the cryptocurrency network, that transaction will join the transaction pool. But temporarily, the transaction will be in an unconfirmed state. Miners will then take a group of unconfirmed transactions and use them as a data to be officially recorded within a new block in the chain. But to gain the rights to add a block, the miner must solve a computational puzzle called proof of work.

The puzzle of proof of work is difficult to solve and there's a low probability of randomly solving the puzzle. So a lot of trial and error is required to find the answer to the proof of work algorithm. Is time consuming and computationally expensive. Once a miner does solve the proof of work algorithm, they can create a block consisting of the transactions. By solving the proof of work, they gain the rights to submit that block, containing the transactions to the block chain network. Other miners will recognize the solution since a proof of work is easily verified once another miner presents a solution for you.

As a reward for doing the task of mining, the miner receives some cryptocurrency. Thus miners are continually trying to mine new blocks in hopes of gaining this currency reward.
