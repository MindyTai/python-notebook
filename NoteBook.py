import os,sys

print('Hello,welcome to ChaCha’s notebook!!!')
print('You can choose add , list, read ,or remove here.')
print('If you want to finish the program ,just press the key enter.')
print('\n')
print('Functions:')
print('Add: insert the title and the body')
print('List: print all notes(title and body')
print('Read：search the title  and print one note(title and body)')
print('Remove: search the title and remove one note')
print('\n')
print('Hi,please pick one of the orders:')



def Add():
    #if value == 'Add':
    file_name = input('Insert the file name:')
    f = open(file_name, 'w', encoding = 'UTF-8')
    file_content = input('Type your note:')

    f.write(file_content)
    f.close()
    listName = open('listName.txt', 'a', encoding = 'UTF-8')
    listContent = listName.write(file_name+'\n')
    #NewList = list()
    #NewList = NewList.append(listContent)
    #break
def Read():
    list_name = input('Insert the file name:')

    for name in open('listName.txt', 'r', encoding='UTF-8') :

        if name.strip() == list_name:
            for word in open(name.strip(), 'r', encoding='UTF-8'):
                print(name)
                print('\n')
                print(word,end='')
                break


        else:
            if name != list_name:
                continue
    print('\n')
def List():
    print('List all the file name and cotents:')

    for namee in open('listName.txt', 'r', encoding='UTF-8'):
        #for namee in file_name1:
        for word in open(namee.strip(), 'r', encoding='UTF-8'):
            print(namee)
            print('\n')
            print(word,end='')
            print('\n')
            print('\n')
def Remove():
    remove_value = input('Remove the file:')

    for namee in open('listName.txt', 'r', encoding='UTF-8'):
        if namee.strip() == remove_value:
            os.remove(namee.strip())
            open('listName.txt', 'r', encoding='UTF-8').close()

    f = open('listName.txt', 'r', encoding='UTF-8')
    lines = f.readlines()
    #print(lines)
    f.close()

    f = open('listName.txt', 'w', encoding='UTF-8')
    for line in lines:
        if line!=remove_value + "\n":
            f.write(line)
    f.close()



        # listName裡的file還留著！

while True:

    value = input('1.Add 2.List 3.Read 4.Remove  \n')
    if value == 'Add':
        Add()
        continue

    elif value == 'Read':
        Read()
        continue

    elif value == 'List':
        List()
        continue

    elif value == 'Remove':
        Remove()
        continue

    else:
        print("Invalid input")
        continue
