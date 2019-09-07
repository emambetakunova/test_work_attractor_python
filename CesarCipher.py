class CesarCipher(object):
    _alphabet = None
    _shift = None

    def set_alphabet(self, value):
        self._alphabet = value

    def set_shift(self, value):
        self._shift = value

    def encode(self, plainText):
        if self._alphabet is None or self._shift is None:
            raise ValueError('Please set alphabet and shift')
        encoded_text = ""
        for letter in plainText:
        	try:
        		index = self._alphabet.index(letter)
        	except ValueError:
        		encoded_text += letter
        		continue
        	new_index = index + self._shift
        	try:
        		new_letter = self._alphabet[new_index]
        	except IndexError:
        		new_index = new_index - len(self._alphabet)
        		new_letter = self._alphabet[new_index]
        	encoded_text += new_letter
        return encoded_text

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
cipher = CesarCipher()
cipher.set_alphabet(alphabet)
cipher.set_shift(3)
result = cipher.encode('The quick brown fox jumps over the lazy dog')
print(result)