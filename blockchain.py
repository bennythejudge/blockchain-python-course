blockchain = []
open_transactions = []
owner = 'me'


def mine_block():
    pass

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
    open_transactions.append(transaction)

def get_user_choice():
    user_input = input('Your choice: ')
    return user_input

def get_transaction_value():
    recipient_input = input('Recipient: ')
    amount_input = float(input('Amount: '))
    return (recipient_input, amount_input)

##### main ########################################
waiting_for_input = 1
while waiting_for_input:
    print('Please select one option:')
    print('1: add new transaction')
    print('2: output the blockchain')
    print('h: alter the blockchain')
    print('q: quit')
    user_choice = get_user_choice()
    if user_choice == '1':
        trx_tuple = get_transaction_value()
        recipient, amount = trx_tuple
        add_transaction(recipient, amount=amount)
        print(open_transactions)
    elif user_choice == '2':
        for block in open_transactions:
            print("Block: {}".format(block))
    elif user_choice == 'q':
        waiting_for_input = 0
    elif user_choice == 'h':
        pass
    else:
        print('Invalid choice, try again')

print("Done!")

