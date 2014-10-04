"""Return next id (as a string)
the id will be (until we run out of room)
7 base-62 digits.
We will start at hXrl33t, increment by a large prime
748585161281; 13:11:7:5:3:0:13_62 is a good one
this index space is of size 62^7 ~ 3.5 trillion"""
def next_id(current_id):
    awesome_prime = 748585161281
    return Base62Converter.to_string(Base62Converter.to_62(current_id) + awesome_prime)

class Base62Converter(object):
    """Converts stuff to and from strings"""
    # 0 < ... 9 < a < ... z < A < ... Z
    chars = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9",
             "a", "b", "c", "d", "e", "f", "g", "h", "i", "j",
             "k", "l", "m", "n", "o", "p", "q", "r", "s", "t",
             "u", "v", "w", "x", "y", "z", "A", "B", "C", "D",
             "E", "F", "G", "H", "I", "J", "K", "L", "M", "N",
             "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X",
             "Y", "Z"]

    """Only return strings of 7 digits, i.e. take
    modulo 62^7 of num, return string representation"""
    @staticmethod
    def to_string(num):
        string = ""
        num = num % 62**7
        for power in range(6, 0, -1):
            val = int(num / (62**power))
            num -= val * 62**power
            string += Base62Converter.chars[val]
        return string

    """Return 7 digit string to number"""
    @staticmethod
    def to_62(string):
        num = 0
        for i in range(7):
            val = Base62Converter.chars.index(string[-i])
            num += val * 62**i
        return num