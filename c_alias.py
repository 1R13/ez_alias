from sys import argv
import os

bashrc: str = "/home/" + os.getlogin() + "/.bashrc"

def usage():
    print("Usage:  c_alias [options]\n"+
        "\nOptions:\n"+"-l\t\t\t\t\tlist all aliases\n"+
        "-a <alias_name> <alias_function>\tadd alias\n"+
        "-r <alias_name>\t\t\t\tremove alias\n"+
        "-f <alias_name>\t\t\t\tfind alias")

def add_alias(name, func):
    if len(argv) == 4:
        alias_name: str = name
        alias_func: str = func
        line = "alias " + alias_name + "='" + alias_func + "'"
        with open(bashrc, "a") as file:
            if input("New alias : %s\nConfirm? (Y/n) " % line.replace("\n", "")).upper() == "Y":
                file.write("\n" + line)
                print("New alias added.")
                quit()
            else:
                print("Aborting…")
                quit()
        os.system("source " + bashrc)
    else:
        usage()
        quit()

def del_alias(alias_name, l=False):
    if l:
        alias_name = alias_name[alias_name.index(" ") + 1: alias_name.index("=")]
    with open(bashrc, "r") as file:
            data = file.readlines()
            for l in data:
                if l.__contains__(alias_name+"="):
                    if input("Are you sure to remove %s (y/n):" % l.replace("\n", "")).upper() == "Y":
                        data.remove(l)
                        with open(bashrc, "w") as out:
                            out.writelines(data)
                            os.system("source " + bashrc)


def rem_alias():     # TODO make listing
    if len(argv) == 3:
        del_alias(argv[2])
    elif len(argv) == 2:
        list_all(True)
    else:
        usage()
        quit()

def list_all(r=False):
    with open(bashrc, "r") as file:
        data = file.readlines()
        aliase = []

        for i in range(len(data)):
            if data[i].__contains__("alias "):
                aliase.append(data[i])
        
    
        for i in range(len(aliase)):
            if r:
                print(str(i+1) + ". " + aliase[i].replace("\n", ""))
            else:
                print(aliase[i].replace("\n", ""))
        if not r:
            quit()
        index = int(input("Enter alias to delete : "))
        del_alias(aliase[index-1], True)
                

def find_alias(name):
    result = []
    with open(bashrc, "r") as file:
        data = file.readlines()
        for l in data:
            if l.__contains__(name) and l.__contains__("alias "):
                result.append(l)
    for l in result:
        print(l)

def main():
    try:
        if argv.__contains__("-h") or len(argv) == 1:
            usage()
            quit()
        elif argv.__contains__("-a"):
            add_alias(argv[2], argv[3])
            quit()
        elif argv.__contains__("-r"):
            rem_alias()
            quit()
        elif argv.__contains__("-l"):
            list_all()
            quit()
        elif argv.__contains__("-f"):
            find_alias(argv[2])
            quit()
        else:
            print("No options given!\n")
            usage()
            quit()
    except IndexError:
        print("missing arguments")
        usage()
        quit()
main()