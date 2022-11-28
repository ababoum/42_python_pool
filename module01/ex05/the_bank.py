'''
Module containing classes for a bank simulation
'''


import sys


class Account:
    '''
    A bank Account
    '''

    ID_COUNT = 1

    def __init__(self, name, **kwargs):
        self.__dict__.update(kwargs)
        self.id = self.ID_COUNT
        Account.ID_COUNT += 1
        self.name = name
        if not hasattr(self, 'value'):
            self.value = 0
        if self.value < 0:
            raise AttributeError("Attribute value cannot be negative.")
        if not isinstance(self.name, str):
            raise AttributeError("Attribute name must be a str object.")

    def transfer(self, amount):
        '''Transfer an amount from/to the account'''
        self.value += amount


def iscorrupted(account: Account) -> bool:
    '''
    Evaluates if an account is corrupted
    '''

    # Even number of attributes
    if len(account.__dict__) % 2 == 0:
        return True
    # An attribute starting with 'b'
    if any(item[0] == 'b' for item in account.__dict__):
        return True
    # Does not have at least zip or addr
    if not (
        any(item[0:3] == 'zip' for item in account.__dict__) or
            any(item[0:4] == 'addr' for item in account.__dict__)):
        return True
    # Does not have name, id, and value
    if not (
        hasattr(account, 'name')
            and hasattr(account, 'id')
            and hasattr(account, 'value')
    ):
        return True
    # name is not str, id is not int, or value is not int/float
    if not isinstance(account.name, str) \
            or not isinstance(account.id, int) \
            or not isinstance(account.value, (int, float)):
        return True
    return False


class Bank:
    """The bank"""

    def __init__(self):
        self.accounts = []

    def add(self, new_account) -> bool:
        """ Add new_account in the Bank
        @new_account: Account() new account to append
        @return True if success, False if an error occured
        """
        # test if new_account is an Account() instance and if
        # it can be appended to the attribute accounts
        if not isinstance(new_account, Account):
            print("new_account is not an Account object", file=sys.stderr)
            return False
        if hasattr(new_account, 'name') \
                and any(account.name == new_account.name for account in self.accounts):
            print(
                "new_account doesn't have a name, or the name is already registered in the bank",
                file=sys.stderr)
            return False
        self.accounts.append(new_account)
        return True

    def transfer(self, origin: str, dest: str, amount):
        """" Perform the fund transfer
        @origin: str(name) of the first account
        @dest: str(name) of the destination account
        @amount: float(amount) amount to transfer
        @return True if success, False if an error occured
        """
        if not isinstance(origin, str) or not isinstance(dest, str):
            print("Origin and Dest must be strings", file=sys.stderr)
            return False

        # Retrieve the accounts in the bank
        origin_account = [
            item for item in self.accounts if item.name == origin]
        dest_account = [item for item in self.accounts if item.name == dest]
        if not origin_account:
            print("Origin account not found in the bank", file=sys.stderr)
            return False
        elif not dest_account:
            print("Destination account not found in the bank", file=sys.stderr)
            return False
        origin_account = origin_account[0]
        dest_account = dest_account[0]

        # Run the verifications and proceed with transfer if everything OK
        if amount < 0 or origin_account.value < amount:
            print(
                "Transfer cannot be executed (incorrect amount or insufficient funds)",
                file=sys.stderr)
            return False
        if not iscorrupted(dest_account) and not iscorrupted(origin_account):
            if dest != origin:
                origin_account.transfer(-amount)
                dest_account.transfer(amount)
            return True
        print(
            "Transfer cannot be executed (corrupted account)",
            file=sys.stderr)
        return False

    def fix_account(self, name):
        """ fix account associated to name if corrupted
        @name: str(name) of the account
        @return True if success, False if an error occured
        """
        if not isinstance(name, str):
            print("Account name must be a string", file=sys.stderr)
            return False
        account = [item for item in self.accounts if item.name == name]
        if not account:
            print("Account to fix not found in the bank", file=sys.stderr)
            return False
        account = account[0]

        # Delete attributes starting with 'b'
        if any(item[0] == 'b' for item in account.__dict__):
            for key in list(account.__dict__.keys()):
                if key[0] == 'b':
                    delattr(account, key)
        # Does not have at least zip or addr -> add zip
        if not (
            any(item[0:3] == 'zip' for item in account.__dict__) or
                any(item[0:4] == 'addr' for item in account.__dict__)):
            setattr(account, 'zip', '00000')
        # Does not have name, id, and value
        if not (
            hasattr(account, 'name')
                and hasattr(account, 'id')
                and hasattr(account, 'value')
        ):
            return False
        # name is not str, id is not int, or value is not int/float
        if not isinstance(account.name, str) \
                or not isinstance(account.id, int) \
                or not isinstance(account.value, (int, float)):
            return False
        # Even number of attributes
        if len(account.__dict__) % 2 == 0:
            setattr(account, 'filler', 0)
        return True


if __name__ == '__main__':

    bank = Bank()
    john = Account(
        'William John',
        zip='100-064',
        brother="heyhey",
        value=6460.0,
        ref='58ba2b9954cd278eda8a84147ca73c87',
        info=None,
        other='This is the vice president of the corporation',
        lol="hihi"
    )
    bank.add(john)
    print(f"Is {john.name} account corrupted? {iscorrupted(john)}")
    bank.fix_account(john.name)
    print(f"Is {john.name} account corrupted? {iscorrupted(john)}")

    print("********************************************")

    john1 = Account(
        'William John Bis',
        zip='100-064',
        rother="heyhey",
        value=6460.0,
        ref='58ba2b9954cd278eda8a84147ca73c87',
        info=None,
        other='This is the vice president of the corporation',
    )

    bank.add(john1)
    print(f"Is {john1.name} account corrupted? {iscorrupted(john1)}")
    bank.fix_account(john1.name)
    print(f"Is {john1.name} account corrupted? {iscorrupted(john1)}")

    print("********************************************")

    john2 = Account(
        'William John Ter',
        zip='100-064',
        rother="heyhey",
        ref='58ba2b9954cd278eda8a84147ca73c87',
        info=None,
        other='This is the vice president of the corporation',
        lol="lolilol"
    )

    bank.add(john2)
    print(f"Is {john2.name} account corrupted? {iscorrupted(john2)}")
    bank.fix_account(john2.name)
    print(f"Is {john2.name} account corrupted? {iscorrupted(john2)}")

    print("********************************************")

    bank.add(Account(
        'Jane',
        zip='911-745',
        value=1000.0,
        ref='1044618427ff2782f0bbece0abd05f31'
    ))

    jhon = Account(
        'Jhon',
        zip='911-745',
        value=1000.0,
        ref='1044618427ff2782f0bbece0abd05f31'
    )

    bank.add(jhon)

    print("testing a valid transfer")
    print(jhon.value)
    print(bank.transfer("Jane", "Jhon", 500))
    print(jhon.value)

    print("---------")

    print(bank.transfer("Jane", "Jhon", 1000))
    print(jhon.value)

