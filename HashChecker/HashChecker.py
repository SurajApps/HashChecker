import hashlib
import argparse


def Check():
    argspec = ""
    path = ""
    checksum = ""

    def MD5():
        nonlocal path, checksum
        # Path is the location of the file (can be set a different way)
        BLOCK_SIZE = 65536  # The size of each read from the file

        file_hash = hashlib.md5()  # Create the hash object, can use something other than `.sha256()` if you wish
        with open(path, 'rb') as f:  # Open the file to read it's bytes
            fb = f.read(BLOCK_SIZE)  # Read from the file. Take in the amount declared above
            while len(fb) > 0:  # While there is still data being read from the file
                file_hash.update(fb)  # Update the hash
                fb = f.read(BLOCK_SIZE)  # Read the next block from the file
        calc_md5 = file_hash.hexdigest()

        if(checksum == calc_md5):
            print("The file has not been tampered with, and is OK to use.")
        else:
            print("The file has been tampered with, and is NOT OK to use.")
        # print(file_hash.hexdigest())  # Get the hexadecimal digest of the hash

    def SHA256():
        nonlocal path, checksum
        # Path is the location of the file (can be set a different way)
        BLOCK_SIZE = 65536  # The size of each read from the file

        file_hash = hashlib.sha256()  # Create the hash object, can use something other than `.sha256()` if you wish
        with open(path, 'rb') as f:  # Open the file to read it's bytes
            fb = f.read(BLOCK_SIZE)  # Read from the file. Take in the amount declared above
            while len(fb) > 0:  # While there is still data being read from the file
                file_hash.update(fb)  # Update the hash
                fb = f.read(BLOCK_SIZE)  # Read the next block from the file
        calc_sha256 = file_hash.hexdigest()

        if (checksum == calc_sha256):
            print("The file has not been tampered with, and is OK to use.")
        else:
            print("The file has been tampered with, and is NOT OK to use.")
        # print(file_hash.hexdigest())  # Get the hexadecimal digest of the hash

    parser = argparse.ArgumentParser()
    parser.add_argument('-f', '--file', help='Select the file to be checked', required=True, action="store", type=str)
    parser.add_argument('-s', '--sha256', help='Check the SHA256 checksum of the file', required=False, action="store_true")
    parser.add_argument('-m', '--md5', help='info / public / private', required=False, action="store_true")
    parser.add_argument('-c', '--checksum', help='Enter the MD5 or SHA256 checksum of the file', required=True, action="store", type=str)
    args = vars(parser.parse_args())

    path = args["file"]
    checksum = args["checksum"]


    if (args['md5'] == True):
        MD5()
    if (args['sha256'] == True):
        SHA256()

    print(path)


Check()
