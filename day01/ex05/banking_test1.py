from the_bank import Account, Bank

if __name__ == "__main__":
    bank = Bank()
    bank.add(Account('Smith Jane', {'zip': '911-745', 'value': 1000.0}))
    bank.add(Account('William John', {'zip': '100-064', 'value': 6460.0, 'ref': '58ba2b9954cd278eda8a84147ca73c87', 'info': None, 'other': 'This is the vice president of the corporation'}))

    if bank.transfer('William John', 'Smith Jane', 545.0) is False:
        print('Failed')
    else:
        print('Success')
