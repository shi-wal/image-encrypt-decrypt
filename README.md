# image-encrypt-decrypt
This project has been created to encrypt any file or image using AES (Advance Encryption Standard) algorithm  also known by its original name Rijndael, is a specification for the encryption of electronic data established by the U.S. National Institute of Standards and Technology in 2001.  <br/>
This algorithm is a symmetric-key algorithm, meaning the same key is used for both encrypting and decrypting the data. In this code, I've used key-size of 256 bits for encryption & decryption. <br/>
For giving this project a front-end look, I've used Python's famous GUI toolkit named Tkinter.

## How AES encryption works?
Symmetric, also known as secret key, ciphers use the same key for encrypting and decrypting, so the sender and the receiver must both know and use the same secret key. Each cipher encrypts and decrypts data in blocks of 128 bits using cryptographic keys of 128, 192 and 256 bits, respectively. There are 10 rounds for 128-bit keys, 12 rounds for 192-bit keys and 14 rounds for 256-bit keys. A round consists of several processing steps that include substitution, transposition and mixing of the input plaintext to transform it into the final output of ciphertext.

## Libraries needed to install
Tkinter- it comes along with the Python. We don't need to install it separately. <br/>
Crypto- pip install crypto <br/>
PIL- pip install pillow 

## License
This project is under MIT license.
