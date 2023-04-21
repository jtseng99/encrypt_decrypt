#CH9 PE3
#part 2 : loading and using the encryption data files

import pickle

def get_enc_dict():
    infile = open('encrypt.dat','rb')
    enc_dt = pickle.load(infile)
    infile.close()
    return enc_dt

def get_dec_dict():
    infile = open('decrypt.dat','rb')
    dec_dt = pickle.load(infile)
    infile.close()
    return dec_dt

def enc_file():
    inpath = input("Enter path of file to encrypt:")
    outpath = input("Enter the name of new file:")

    cipher_dt = get_enc_dict()
    infile = open(inpath,'r')
    outfile = open(outpath,'w')

    my_str = infile.read()
    for ch in my_str:
        outfile.write(cipher_dt.get(ch,ch))

    infile.close()
    outfile.close()

def dec_file():
    inpath = input("Enter path of file to decrypt:")
    outpath = input("Enter the name of new file:")

    cipher_dt = get_dec_dict()
    infile = open(inpath,'r')
    outfile = open(outpath,'w')

    my_str = infile.read()
    for ch in my_str:
        outfile.write(cipher_dt.get(ch,ch))

    infile.close()
    outfile.close()

def main():
    print("Enter 1 to encrypt file. Enter 2 to decrypt file.")
    choice = input()
    if choice == "1":
        enc_file()
    elif choice == "2":
        dec_file()
    else:
        print("Error")


main()

