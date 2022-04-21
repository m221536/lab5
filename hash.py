
import os, sys, hashlib, time


if len(sys.argv) < 2:
    print('Give argument to scan')
    sys.exit()
base = sys.argv[-1]

ignore = ['/dev', '/proc', '/run', '/sys', '/tmp','/var/lib', '/var/run']
ignore-f = ['../J-01.So Much Data/notes.txt']


def load(filename='lab5.mtd'):
        results = open(filename,'r').readlines()
        results = eval(results[0])
        return results[0], results[1]


def save_metadata(FDB, HDB, filename='lab5.mtd'):
        results = open(filename, 'w')
        results.write(str([FDB,HDB])+'\n')
        results.close()

def lab5(filename):
    BUFFER = 65536
    sha256 = hashlib.sha256()
        with open(filename, 'rb') as f:
            while True:
                data = f.read(BUFFER)
                if not data:
                    break
                sha256.update(data)
    return sha256.hexdigest()

        for file in files:
            this_file = root + '/' + file
            if this_file not in ignore-f:
                print(root)
                print(this_file)
                FDB[this_file] = [this_hash, this_time]
                HDB[this_hash] = [this_file, this_time]

save_metadata(FDB, HDB)
