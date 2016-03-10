import os
def run(**args):
    print "[*] In dirlister module."
    print args
    files = os.listdir(".")
    return str(files)