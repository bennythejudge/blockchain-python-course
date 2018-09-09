#!/usr/bin/env python
##########################################
#  build a blockchain in Python
##########################################
import names
import random

MINING_REWARD = 10

genesis_block = {
    'previous_hash': '',
    'index': 0,
    'transactions': []
}
blockchain = [genesis_block]
open_transactions = []
owner = 'me'
participants = set()

def verify_transactions():
    return all([verify_transaction(tx) for tx in open_transactions])

def verify_transaction(transaction):
    sender_balance = get_balance(transaction['sender'])
    print("inside verify_transaction with sender_balance: " + str(sender_balance))

    print("verify_transaction:  transaction['amount'] {}".format( transaction['amount']))
    print()
    print()

    return sender_balance >= transaction['amount']

def verify_chain():
    for (index, block) in enumerate(blockchain):
        if index == 0:
            continue  # skip the genesis block
        elif block['previous_hash'] != hash_block(blockchain[index - 1]):
            return False
    return True


def hash_block(block):
    return '-'.join(str([block[k] for k in block]))


def get_balance(participant):
    # for each block in the block chain
    #     for each tx in the block
    # something like that
    # print("get_balance1: {}".format([block for block in blockchain]))
    # print("get_balance2: {}".format([block['transactions'] for block in blockchain]))
    # print("get_balance3: {}".format([[tx['amount'] for tx in block['transactions']] for block in
    #              blockchain]))
    # transactions sender
    print()
    print()
    print("DEBUG: entering get_balance for {}".format(participant))
    tx_sender = [[tx['amount'] for tx in block['transactions'] if tx['sender'] == participant] for block in
                 blockchain]

    print("DEBUG: tx_sender: {}".format(tx_sender))


    # get the full list of trx - consider also open transactions which otherwise could exceed the balance
    open_tx_sender = [tx['amount'] for tx in open_transactions if tx['sender'] == participant]

    print("DEBUG: open_tx_sender: {}".format(open_tx_sender))

    tx_sender.append(open_tx_sender)

    print("DEBUG: tx_sender: {}".format(tx_sender))

    #print("tx_sender: {}".format(tx_sender))
    amount_sent = 0
    for entries in tx_sender:
        #print("entries: {}".format(entries))
        for tx in entries:
            amount_sent += tx
            print("DEBUG: loops tx_sender: tx {} amount_sent: {}".format(tx,amount_sent))

    # transactions receiver
    transactions_recipient = [[tx['amount'] for tx in block['transactions'] if tx['recipient'] == participant] for block in
                 blockchain]
    print("transactions_recipient: {}".format(transactions_recipient))
    amount_received = 0
    for entries in transactions_recipient:
        #print("entries: {}".format(entries))
        for tx in entries:
            amount_received += tx
            #print("amount_sent: {}".format(amount_sent))
    # print(tx_sender)
    return amount_received - amount_sent


def mine_block():
    reward_transaction = {
        'sender': 'MINING',
        'recipient': owner,
        'amount': MINING_REWARD
    }
    copied_transactions = open_transactions[:]
    participants.add(owner)
    copied_transactions.append(reward_transaction)
    print("Entering mine_block with open_transactions: {}".format(copied_transactions))
    last_block = get_last_blockchain_value()
    print("last_block: {}".format(last_block))
    hashed_block = hash_block(last_block)
    print(hashed_block)
    block = {
        'previous_hash': hashed_block,
        'index': len(blockchain),
        'transactions': copied_transactions
    }
    blockchain.append(block)
    print("Leaving mine_block")
    return True


def get_last_blockchain_value():
    """ returns the last value of the current blockchain """
    return blockchain[-1]


def add_transaction(recipient, sender=owner, amount=1.0):
    """ Append a new value + a point to last block to the blockchain
    :param sender:
    :param recipient:
    :param amount: (default = 1.0)
    :return:
    """
    transaction = {
        'sender': sender,
        'recipient': recipient,
        'amount': amount
    }

    if verify_transaction(transaction):
        print("DEBUG: inside add_transaction: true branch")
        open_transactions.append(transaction)
        print("sender: {}".format(sender))
        print("recipient: {}".format(recipient))
        participants.add(sender)
        participants.add(recipient)
        print("DEBUG: participants: {}".format(participants))
        return True

    return False


def get_user_choice():
    user_input = input('Your choice: ')
    return user_input


def get_transaction_value():
    recipient_input = input('Recipient: ')
    amount_input = float(input('Amount: '))
    return (recipient_input, amount_input)


def print_participants():
    print(participants)


def enter_a_bunch_of_transactions():
    print("DEBUG: Adding 10 transactions")
    for i in range(0, 11):
        recipient = names.get_first_name()
        amount = random.randint(1, 10)
        if add_transaction(recipient, amount=amount):
            print("Add transaction successful")
        else:
            print("Add transaction failed")
    print("open_transaction: {}".format(open_transactions))
    print("DEBUG: Done with enter_a_bunch_of_transactions")


##### main ########################################
waiting_for_input = 1

while waiting_for_input:
    print('Please select one option:')
    print('1: add new transaction')
    print('2: output the blockchain')
    print('3: mine a new block')
    print('4: list participants')
    print('5: add 10 transactions')
    print('6: show balance')
    print('7: print open_transactions')
    print('8: check open transactions validity')
    print('h: alter the blockchain')
    print('q: quit')
    user_choice = get_user_choice()
    if user_choice == '1':
        trx_tuple = get_transaction_value()
        recipient, amount = trx_tuple
        if add_transaction(recipient, amount=amount):
            print("Add transaction successful")
            print("open_transaction: {}".format(open_transactions))
        else:
            print("Add transaction failed")
    elif user_choice == '2':
        print()
        print("This is the blockchain:")
        for block in blockchain:
            print("Block: {}".format(block))
        print("End blockchain")
        print()
    elif user_choice == '3':
        if mine_block():
            open_transactions = []
    elif user_choice == '4':
        print_participants()
    elif user_choice == '5':
        enter_a_bunch_of_transactions()
    elif user_choice == '6':
        print("Printing balance")
        [print("balance: {} {}".format(entity, get_balance(entity))) for entity in participants]
        print("done printing balance")
    elif user_choice == '7':
        print("Printing open_transactions")
        print(open_transactions)
        print("done printing open_transactions")
    elif user_choice == '8':
        if verify_transactions():
            print('All open transactions are valid')
        else:
            print('There are invalid open transactions')
    elif user_choice == 'q':
        waiting_for_input = 0
    elif user_choice == 'h':
        if len(blockchain) >= 1:
            blockchain[0] = {
                'previous_hash': '',
                'index': 0,
                'transactions': [{'sender': 'Chris', 'recipient': 'Max', 'amount': 11}]
            }
    else:
        print('Invalid choice, try again')
    if not verify_chain():
        # print_blockchain_elements()
        print('Invalid blockchain {}'.format(blockchain))
        break
else:
    print('User left!')

print("Done!")
