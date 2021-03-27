import unittest
from Registration import *


class TestRegistration(unittest.TestCase):
    def setUp(self) -> None:
        self.test_reg = Registration()

    def test_new_user(self):
        name = "Serhii"
        psw = "safgas2fsa"
        email = "dasdasfa@gmail.com"
        self.assertEqual(self.test_reg.new_user(name, psw, email), 200)

        name1 = "Max"
        psw1 = "safgas2fsafsa"
        email1 = "max2@gmail.com"
        self.assertEqual(self.test_reg.new_user(name1, psw1, email1), 200)

    def test_same_user(self):
        name = "Serhii"
        psw = "safgas2fsa"
        email = "dasdasfa@gmail.com"
        self.test_reg.new_user(name, psw, email)

        name1 = "Serhii"
        psw1 = "safgas2fsafsa"
        email1 = "dasdasfa@gmail.com"
        with self.assertRaises(UserAlreadyRegistered):
            self.test_reg.new_user(name1, psw1, email1)

    def test_long_name(self):
        # Name must be 3-20 characters long
        name = "Se"
        psw = "safgfsg23"
        email = "dasdasfa@gmail.com"
        with self.assertRaises(NameLongError):
            self.test_reg.new_user(name, psw, email)

        name1 = "Maxasdgasdfrewagfswtgsdfg"
        psw1 = "safgas2fsa"
        email1 = "max2@gmail.com"
        with self.assertRaises(NameLongError):
            self.test_reg.new_user(name1, psw1, email1)

    def test_item_name(self):
        # Forbidden symbol used in name
        name = "Serhii}"
        psw = "safgfsg23"
        email = "dasdasf432a@gmail.com"
        with self.assertRaises(NameItemError):
            self.test_reg.new_user(name, psw, email)

    def test_long_psw(self):
        # Password must be 6-20 characters long
        name = "Serhii"
        psw = "safg"
        email = "dasdasfa@gmail.com"
        with self.assertRaises(PswLongError):
            self.test_reg.new_user(name, psw, email)

        name1 = "Max"
        psw1 = "safgas2fsasafsdagasdrgsdfgadsfa"
        email1 = "max2@gmail.com"
        with self.assertRaises(PswLongError):
            self.test_reg.new_user(name1, psw1, email1)

    def test_item_psw(self):
        # Forbidden symbol used in password
        name = "Serhii"
        psw = "safg?[7"
        email = "dasdasf432a@gmail.com"
        with self.assertRaises(PswItemError):
            self.test_reg.new_user(name, psw, email)

    def test_long_email(self):
        # Email must be 10-30 characters long
        name = "Serhii"
        psw = "safgsadg"
        email = "@ail.com"
        with self.assertRaises(EmailLongError):
            self.test_reg.new_user(name, psw, email)

        name1 = "Max"
        psw1 = "safgas2fs"
        email1 = "max2asdfasdgasdfqwefgasgasdfawsfqwegdf@gmail.com"
        with self.assertRaises(EmailLongError):
            self.test_reg.new_user(name1, psw1, email1)

    def test_item_email(self):
        # Forbidden symbol used in email
        name = "Serhii"
        psw = "safgagsdf"
        email = "dasdasf43 a@gmail.com"
        with self.assertRaises(EmailItemError):
            self.test_reg.new_user(name, psw, email)

    def test_incorrect_email(self):
        # Email is incorrect
        name = "Serhii"
        psw = "safgagsdf"
        email = "dasdasf43agmail.com"
        with self.assertRaises(EmailIncorrect):
            self.test_reg.new_user(name, psw, email)

        name1 = "Serhii"
        psw1 = "safgagsdf"
        email1 = "dasdasf43a@gmailbcom"
        with self.assertRaises(EmailIncorrect):
            self.test_reg.new_user(name1, psw1, email1)

        name2 = "Serhii"
        psw2 = "safgagsdf"
        email2 = "dasdasf.43a@gmailbcom"
        with self.assertRaises(EmailIncorrect):
            self.test_reg.new_user(name2, psw2, email2)
