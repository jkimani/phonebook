

class PhoneBook(object):

    def __init__(self, filename=None):
        self.filename = filename
        self.phone_book = {}

    def build(self):
        try:
            with open(self.filename, 'r') as file:
                counter = 1
                record_count = 0
                for line in file.read().splitlines():

                    if counter == 1:
                        record_count = int(line)

                    elif counter != 1 and counter <= record_count + 1:
                        # Read entries for phonebook
                        self.add_record(record=line)

                    else:
                        print(self.search(query=line.lower()))

                    counter += 1
        except Exception as e:
            print(str(e))

    def add_record(self, record):
        record = record.split(' ')
        self.phone_book[record[0].lower()] = record[1]

    def search(self, query):
        phone_number = self.phone_book.get(query, None)
        if phone_number:
            return "{}={}".format(query, phone_number)
        else:
            return "Not found"


if __name__ == '__main__':
    PhoneBook(filename='numbers.txt').build()
