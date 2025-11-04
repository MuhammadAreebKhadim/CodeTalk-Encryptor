# import random
# import string

# def encode_word(word):
#     if len(word) >= 3:
#         first_letter = word[0]
#         new_word = word[1:] + first_letter
#         random_chars = ''.join(random.choices(string.ascii_letters, k=3))
#         return random_chars + new_word + random_chars
#     else:
#         return word[::-1]

# def decode_word(word):
#     if len(word) < 3:
#         return word[::-1]
#     else:
#         core_word = word[3:-3]
#         last_letter = core_word[-1]
#         return last_letter + core_word[:-1]

# def process_message(message, mode):
#     words = message.split()
#     if mode == 'encode':
#         return ' '.join(encode_word(word) for word in words)
#     elif mode == 'decode':
#         return ' '.join(decode_word(word) for word in words)
#     else:
#         return "Invalid mode selected."

# def main():
#     try:
#         mode = int(input("Press 1 to encode or 0 to decode the message: ").strip())
#         if mode not in [0, 1]:
#             raise ValueError("Invalid input. Please enter 1 or 0.")
#         message = input("Enter the message: ").strip()
#         mode_str = 'encode' if mode == 1 else 'decode'
#         result = process_message(message, mode_str)
#         print("Result:", result)
#     except ValueError as e:
#         print(e)

# if __name__ == "__main__":
#     main()






# REAL PROGRAM WITH SECURITY AND SURETY!
import random
import string

print("Welcome To Our Code Talk\U0001F60A . Ensure the Coreect Encrypting/Decrypting Key🔑 .")
def generate_random_chars(length):
    return ''.join(random.choices(string.ascii_letters, k=length))

def encode_word(word, num_random_chars):
    if len(word) >= 3:
        first_letter = word[0]
        new_word = word[1:] + first_letter
        random_chars = generate_random_chars(num_random_chars)
        return random_chars + new_word + random_chars
    else:
        return word[::-1]

def decode_word(word, num_random_chars):
    if len(word) < 3:
        return word[::-1]
    else:
        core_word = word[num_random_chars:-num_random_chars]
        last_letter = core_word[-1]
        return last_letter + core_word[:-1]

def process_message(message, mode, num_random_chars):
    words = message.split()
    if mode == 'encode':
        return ' '.join(encode_word(word, num_random_chars) for word in words)
    elif mode == 'decode':
        return ' '.join(decode_word(word, num_random_chars) for word in words)
    else:
        return "Invalid mode selected."

def main():
    unsuccessful_attempts = 0
    while True:
        try:
            mode = int(input("Press  1️⃣  to encode,  2️⃣  to decode, or  0️⃣  to quit: ").strip())
            if mode == 0:
                print("Quitting the program 👋. Thanks for Encrypting Trust of our Program!\U0001F642 \n Take Care $ Ensure the Safety!\U0001F970 ")
                break
            elif mode not in [1, 2]:
                raise ValueError("Invalid input. Please enter  1️⃣ , 2️⃣ , or 0️⃣.")
            
            while unsuccessful_attempts < 3:
                key = input("Enter the Encryption/Decryption Key 🔑 : ").strip()
                if key == "aabbii":
                    break
                else:
                    unsuccessful_attempts += 1
                    print(f"❌ Invalid key. Please use the correct key!🔑 .\n You have {3 - unsuccessful_attempts} attempts left!\U0001F604 .")
            
            if unsuccessful_attempts >= 3:
                print("⚠️  Warning! You have entered the wrong key three times\U0001F636 .")
                break
            
            num_random_chars = int(input("Enter the number of characters for Code/Decode words 🔢 :  ").strip())
            message = input("Enter the message for Code/Decode Talk 📝: ").strip()
            mode_str = 'encode' if mode == 1 else 'decode'
            result = process_message(message, mode_str, num_random_chars)
            print("Result:", result)
        except ValueError as e:
            print(e)

if __name__ == "__main__":
    main()
