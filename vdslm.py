from vdslm_train import *
from vdslm_generate import *
from termcolor import colored

def main():
    import os
    from sys import argv
    os.system('clear')
    if len(argv) < 2:
        print(colored("No arguments provided. \nExiting...","red"))
        exit()
    if argv[1] == '-t':
        train()
    elif argv[1] == '-g':
        to_gen = 50
        if len(argv) > 2:
            to_gen = int(argv[2])
        generate(to_gen)
    elif argv[1] == '-f':
        os.system('python3 ./vdslm.py -t && python3 ./vdslm.py -g')
    else:
        print(colored("No valid argument provided.","red"))
        print(colored("Valid arguments: -f for first run, -t to train or -g to generate","magenta"))


if __name__ == "__main__":
    main()