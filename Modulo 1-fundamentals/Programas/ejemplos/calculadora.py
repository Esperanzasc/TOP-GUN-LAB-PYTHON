# 2+3-1
# Token(NUMBER, 2) Token(PLUS, "+") Token(NUMBER, 3) Token(MINUS, "-") Token(NUMBER, 1)

# Tokens
# numbers = 0, 1, 2, 3, 4, 5, 6, 7, 8, 9
# minus = -
# plus = +


from enum import Enum


ALLOWED_CHARACTERS = set("0123456789+-/*")


class Tokens(Enum):
    NUMBERS = "NUMBERS"
    MINUS = "MINUS"
    PLUS = "PLUS"
    NULL = "NULL"



class Token:
    def __init__(self, tipo, value):
        self.type = tipo
        self.value = value
    
    def __str__(self):
        return f"Token({self.type.value}, {self.value})"


class Lexer:
    def reset(self, string):
        self.string = string
        self.current_char_position = 0
    
    def get_next_token(self):
        while self.current_char_position < len(self.string):
            if self.string[self.current_char_position].isdigit():
                token = Token(Tokens.NUMBERS, int(self.string[self.current_char_position]))
                self.current_char_position += 1
                return token
            if self.string[self.current_char_position] == "+":
                token = Token(Tokens.PLUS, "+")
                self.current_char_position += 1
                return token
            if self.string[self.current_char_position] == "-":
                token = Token(Tokens.MINUS, "-")
                self.current_char_position += 1
                return token

        return Token(Tokens.NULL, None)


class Interpreter:
    pass


def test():
    token = Token(Tokens.MINUS, "-")
    print(token)

def main():
    string = ""
    lexer = Lexer()
    while string.lower() != "x":
        try:
            string = input("Please enter the operation you want yo do: ")

            lexer.reset(string)
            current_token = lexer.get_next_token()
            while current_token.type != Tokens.NULL:
                print(current_token)
                current_token = lexer.get_next_token()

            if not set(string).intersection(ALLOWED_CHARACTERS):
                print("You are using not allowed characters")

        except KeyboardInterrupt as e:
            break

    print("\nBye, thanks for using our calculator")


if __name__ == "__main__":
    main()
