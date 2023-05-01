class Account(object):
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
        self.value += amount

class Bank(object):
    """The bank"""
    def __init__(self):
        self.accounts = []
    def add(self, new_account):
        """ Add new_account in the Bank
        @new_account: Account() new account to append
        @return True if success, False if an error occured
        """
        namelst = []
        for name in self.accounts:
            namelst.append(name.name)
        if isinstance(new_account, Account):
            if new_account.name in namelst:
                return False
            try:
                self.accounts.append(new_account)
                return True
            except:
                return False
    def iscorrupted(self, account):
            if not hasattr(account,'id') or not hasattr(account, 'value'):
                return True
            if not isinstance(account.id, int):
                return True
            if not isinstance(account.value, (int, float)):
                return True
            if len(account.__dict__) % 2 == 0:
                return True
            for acc in account.__dict__:
                if acc.startswith("b"):
                    return True
            for acc in account.__dict__:
                if acc.startswith("zip") or acc.startswith("addr"):
                    return False
            return True
    def transfer(self, origin, dest, amount):
        """" Perform the fund transfer
        @origin: str(name) of the first account
        @dest: str(name) of the destination account
        @amount: float(amount) amount to transfer
        @return True if success, False if an error occured
        """
        namelst = []
        for name in self.accounts:
            namelst.append(name.name)
        if not isinstance(origin, str):
            return False
        if not isinstance(dest, str):
            return False
        if origin in namelst:
            for acc in self.accounts:
                if acc.name == origin:
                    or_account = acc
        else:
            return False
        if dest in namelst:
            for acc in self.accounts:
                if acc.name == dest:
                    dst_account = acc
        else:
            return False   
        if not isinstance(amount, (int, float)):
            return False
        if self.iscorrupted(or_account) or self.iscorrupted(dst_account):
            return False
        if amount > or_account.value or amount < 0:
            return False
        or_account.transfer(-amount)
        dst_account.transfer(amount)
        return True
    def fix_account(self, name):
        """ fix account associated to name if corrupted
        @name: str(name) of the account
        @return True if success, False if an error occured
        """
        if not isinstance(name, str):
            return False
        namelst = []
        for names in self.accounts:
            namelst.append(names.name)
        if name in namelst:
            for acc in self.accounts:
                if acc.name == name:
                    tf_account = acc
        else:
            return False
        if not hasattr(tf_account,'id'):
            account.id = 1111
        if not hasattr(tf_account, 'value'):
            account.value = 0
        if not isinstance(tf_account.id, int):
            try:
                tf_account.id = int(account.id)
            except:
                tf_acount.id = 1111
        if not isinstance(tf_account.value, (int, float)):
            try:
                tf_account.value = float(tf_account.id)
            except:
                tf_acount.value = 0
        for acc in tf_account.__dict__:
            if acc.startswith("b"):
                del acc
        addzip = True
        for acc in tf_account.__dict__:
            if acc.startswith("zip") or acc.startswith("addr"):
                addzip = False
                break
        if addzip == True:
            tf_account.zip = "123-456"
        if len(tf_account.__dict__) % 2 == 0:
            tf_account.fixed = "fixedlength"
        return True

