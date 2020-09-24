class Account(object):
     ID_COUNT = 1
     def __init__(self, name, **kwargs):
         self.id = self.ID_COUNT
         self.name = name
         self.__dict__.update(kwargs)
         if hasattr(self, 'value'):
             self.value = 0
             Account.ID_COUNT += 1

     def transfer(self, amount):
         self.value += amount

class Bank(object):
    def __init__(self):
        self.account = []


    def add(self, account):
        self.account.append(account)

    def corrupted(self, i):
        count = 0
        signal = 0
        signal1 = 1
        signal2 = 1
        attributes = dir(banks.account[i]) #Use dir to look at all atributes inside class
        for att in attributes:
            if att[0] != '_':
                count += 1
            if att[0] != 'b':
                signal = 1
            if att[0:3] != "zip" or att[0:4] != "addr":
                signal1 = 0
            if att[0:2] == "id":
                signal2 -= 0.25
            if att[0:4] == "name":
                signal2 -= 0.25
            if att[0:5] == "value":
                signal2 -= 0.25
        if count % 2 == 0 or signal1 or signal2:
            return True


    def transfer(self, origin, dest, amount):
        try:
            i = 0
            while self.account[i].id != int(origin) and self.account[i].name != str(origin):
                i += 1
            origin = i
            i = 0
            while self.account[i].id != int(dest) and self.account[i].name != str(dest):
                i += 1
            dest = i
        except:
            return False
        if self.corrupted(origin) == True:
            return False
        if self.corrupted(dest) == True:
            return False
        if self.account[origin].value < amount:
            return False
        return True

    def fix_account(self, account):
        try:
            i = 0
            while self.account[i].id != int(account) and self.account[i].name != str(account):
                i += 1
            account = i
        except:
            return False
        self.account[i].name = str(self.account[i].name)
        self.account[i].id = int(self.account[i].id)
