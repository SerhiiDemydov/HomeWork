class UserRegistration(Exception):
    pass


class PswLongError(UserRegistration):
    pass


class PswItemError(UserRegistration):
    pass


class NameLongError(UserRegistration):
    pass


class NameItemError(UserRegistration):
    pass


class EmailLongError(UserRegistration):
    pass


class EmailItemError(UserRegistration):
    pass

class EmailIncorrect(UserRegistration):
    pass

class UserAlreadyRegistered(UserRegistration):
    pass


class Registration:
    all_users = {}

    black_list = [' ', '/', '?', r'\\', '!', '|', '@', '#', '$', '%',
                  '^', '&', '*', '(', ')', '_', '-', '=', '+', '{', '}',
                  '[', ']', ',', '.', '<', '>']

    black_list_email = [' ', '/', '?', r'\\', '!', '|', '#', '$', '%',
                        '^', '&', '*', '(', ')', '_', '-', '=', '+', '{', '}',
                        '[', ']', ',', '<', '>']

    # should_list_items_email = ['@', '.']

    def new_user(self, user_name: str, user_psw: str, user_email: str):

        if self.name_long_check(user_name) is False:
            raise NameLongError('Name must be 3-20 characters long')
        if self.name_item_check(user_name) is False:
            raise NameItemError('Forbidden symbol used in name')

        if self.psw_long_check(user_psw) is False:
            raise PswLongError('Password must be 6-20 characters long')
        if self.psw_item_check(user_psw) is False:
            raise PswItemError('Forbidden symbol used in password')

        if self.email_long_check(user_email) is False:
            raise EmailLongError('Email must be 10-30 characters long')
        if self.email_item_check(user_email) is False:
            raise EmailItemError('Forbidden symbol used in email')
        if self.email_should_item_check(user_email) is False:
            raise EmailIncorrect('Email is incorrect')
        if user_email in self.all_users.keys():
            raise UserAlreadyRegistered('This e-mail is already registered')
        else:
            self.all_users.update({user_email: user_psw})
        print(self.all_users)
        return 200

    def name_long_check(self, name):
        if 3 <= len(name) <= 20:
            return True
        else:
            return False

    def name_item_check(self, name):
        for l in name:
            if l in self.black_list:
                return False

    def psw_long_check(self, psw):
        if 6 <= len(psw) <= 20:
            return True
        else:
            return False

    def psw_item_check(self, psw):
        for l in psw:
            if l in self.black_list:
                return False

    def email_long_check(self, email):
        if 10 <= len(email) <= 30:
            return True
        else:
            return False

    def email_item_check(self, email):
        for l in email:
            if l in self.black_list_email:
                return False

    def email_should_item_check(self, email):
        x = False
        for l in email:
            if l == '@' or x == True:
                x = True
                if l == '.':
                    return True
        return False
