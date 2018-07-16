from phonebook import PhoneBook
import unittest


class TestPhoneBook(unittest.TestCase):

    def test_add_record(self):
        phone = PhoneBook('numbers.txt')
        phone.add_record(record='sam 1299939')
        assert phone.phone_book['sam']

    def test_search(self):
        phone = PhoneBook('numbers.txt')
        phone.add_record(record='harry 1299929')
        query = 'harry'
        assert phone.search(query=query) == 'harry=1299929'


if __name__ == "__main__":
    unittest.main()
