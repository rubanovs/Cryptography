import sys
import src.caesar as caesar
import src.vigenere as vigenere
import src.vernam as vernam
import src.consts as consts


class Runner:
    def __init__(self):
        self.filename = ""
        self.key_filename = ""
        self.number_of_cipher = 0
        self.mode = 0
        self.shift_value = 0

    def run_caesar(self):
        self.shift_value = int(sys.argv[4])
        cipher = Caesar.Caesar(self.shift_value)
        if self.mode == Consts.Modes.encryption:
            Caesar.Caesar.encrypt(cipher, self.filename)
        elif self.mode == Consts.Modes.decryption:
            Caesar.Caesar.decrypt(cipher, self.filename)
        elif self.mode == Consts.Modes.frequency_analysis:
            Caesar.Caesar.frequency_analysis(cipher, self.filename)

    def run_vigenere(self):
        self.key_filename = sys.argv[4]
        cipher = Vigenere.Vigenere()
        if self.mode == Consts.Modes.encryption:
            Vigenere.Vigenere.encrypt(cipher, self.filename, self.key_filename)
        elif self.mode == Consts.Modes.decryption:
            Vigenere.Vigenere.decrypt(cipher, self.filename, self.key_filename)

    def run_vernam(self):
        self.key_filename = sys.argv[4]
        cipher = Vernam.Vernam()
        if self.mode == Consts.Modes.encryption:
            Vernam.Vernam.encrypt(cipher, self.filename, self.key_filename)
        elif self.mode == Consts.Modes.decryption:
            Vernam.Vernam.decrypt(cipher, self.filename, self.key_filename)

    def run(self):
        if not len(sys.argv) == Consts.Constants.number_of_args:
            print("Wrong amount of arguments")
            sys.exit()

        self.number_of_cipher = int(sys.argv[1])
        self.mode = int(sys.argv[2])
        self.filename = sys.argv[3]

        if self.number_of_cipher == Consts.Ciphers.caesar:
            self.run_caesar()

        elif self.number_of_cipher == Consts.Ciphers.vigenere:
            self.run_vigenere()

        elif self.number_of_cipher == Consts.Ciphers.vernam:
            self.run_vernam()
