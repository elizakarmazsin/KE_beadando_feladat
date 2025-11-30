import random
import string


def get_random_int(min_val, max_val):

    return random.randint(min_val, max_val)


def get_random_choice(data_list):

    if not data_list:
        return "Üres listából nem lehet választani."
    return random.choice(data_list)


def shuffle_list(data_list):

    temp_list = list(data_list)
    random.shuffle(temp_list)
    return temp_list

def generate_secure_password(length=16):

    lower = string.ascii_lowercase
    upper = string.ascii_uppercase
    digits = string.digits
    symbols = string.punctuation

    all_chars = lower + upper + digits + symbols

    password = [
        random.choice(lower),
        random.choice(upper),
        random.choice(digits),
        random.choice(symbols)
    ]

    if length > 4:
        password += [random.choice(all_chars) for _ in range(length - 4)]

    random.shuffle(password)

    return "".join(password[:length])

if __name__ == "__main__":
    print(f"Véletlen szám 1-100 között: {get_random_int(1, 100)}")
    my_list = ["alma", "körte", "szilva"]
    print(f"Véletlen választás: {get_random_choice(my_list)}")
    print(f"Megkevert lista: {shuffle_list(my_list)}")
    print(f"Generált jelszó (16 kar.): {generate_secure_password(16)}")