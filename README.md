
#  CodeTalk – Mini Encryption & Decryption Program

**CodeTalk** is a simple and fun Python-based encryption/decryption program.  
It allows you to securely encode or decode messages using a key and customizable random characters.  
Think of it as your secret messenger – only those with the correct key can unlock your message! 

##  Features

-  Encode and decode any message.
-  Choose how many random letters to add for stronger encryption.
-  Requires a secret key (`aabbii`) for secure access.
-  Three-attempt limit to prevent unauthorized decoding.
-  User-friendly command-line interface with emojis and friendly prompts.

##  How It Works

###  Encoding
1. Takes each word of your message.
2. Moves the first letter to the end.
3. Adds random letters (prefix and suffix).
4. Returns a coded version of your text.

###  Decoding
1. Removes random letters.
2. Moves the last letter of the core word back to the front.
3. Restores your original message.


## Requirements

- Python 3.x  
  *(You can check your version by running `python --version` in your terminal.)*

No external libraries are required — it only uses Python’s built-in `random` and `string` modules.

##  Installation & Usage

1. **Clone the Repository:**
   ```bash
      git clone https://github.com/<your-username>/CodeTalk-Encryptor.git
   cd CodeTalk-Encryptor
   
 Run the Program: 
 ```bash
       python code_talk.py
