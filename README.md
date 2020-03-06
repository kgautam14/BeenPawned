# BeenPawned

Short Description: This code checks whether your password has been leaked or not.

Simply run via command line or terminal and it will ask you to enter your password. 

How it Works:
1. Your password is encrypted using Hashlib module in python3.
2. The first five letters of this hashed string is sent to the website https://api.pwnedpasswords.com/range/ZZZZZ.
3. Here ZZZZZ is the first 5 characters of you hashed password.
4. The response from the url is saved in a dictionary: Key = Hashed Passwords, Value = Number of times they have been leaked.
5. If your hashed password matches a key. You are given the Found() output.

