import hashlib
import os
from numpy.core.defchararray import upper
import getpass

# Here key is the Encrypted password in SHA1 and val is the number of times, it's been decrypted.
def found(key, val):
    print("\nUnfortunately, your password has been found"
          " in the SHA1 decrypted Password's List")
    print("Here is the encrypted version of your password: ", key)
    print("This password has been decrypted ", val, "number of times")
    print("Sorry! But you should change it.")


def main():


    isFound = 0
    # This dict will contain all the hashes with their counts
    dict = {}

    # This will be the password to search
    pwd = getpass.getpass("Enter your password: ")
    # Hashing the password to SHA1 standards
    hashobj = hashlib.sha1(pwd.encode('utf-8'))
    hex_dig = hashobj.hexdigest()

    # To_add will be added to the url for the curl request, and tail will be the actual
    # hash we try and match our responses with.
    to_add = hex_dig[:5]
    tail = upper(hex_dig[5:])

    # Creating the new url to send the curl request, using first five hashed characters of our password
    basic_url = 'https://api.pwnedpasswords.com/range/'
    new_url = basic_url+to_add

    # Sending command through terminal and saving response in site_response
    cmd = "curl "+new_url
    site_response = os.popen(cmd).read()
    site_response = site_response.splitlines()

    # Splitting the response based into the hash and it's count
    for word in site_response:
        newWord, count = word.split(':')
        dict[newWord] = count

    # Finding key in dict, if Found, run function found().
    for key in dict:
        if (tail == key):
            found(key, dict[key])
            isFound = 1

    if(isFound==0):
        print("Congratulations, your password has not YET been decrtypted!")
        print("It doesn't mean it hasn't leaked. :(")

    exit(1)


if __name__ == '__main__':
    main()