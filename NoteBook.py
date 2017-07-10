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

value = input('1.Add 2.List 3.Read 4.Remove  \n')

def Add():
    #if value == 'Add':
    file_name = input('Insert the file name:')
    f = open(file_name, 'w', encoding = 'UTF-8')
    file_content = input('Type your note:')

    f.write(file_content)
    f.close()
    listName = open('listName.txt', 'a', encoding = 'UTF-8')

    listContent = listName.write(file_name+'\n')
    file_name1 = list()
    file_name1 = file_name1.append(listContent)
    #break
def  Read():
    list_name = input('Insert the file name:')

    for name in file_name1 :
        #print(name)
        if name == list_name:
            for word in open(list_name, 'r', encoding='UTF-8'):
                print(list_name)
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

while True:
    if value == 'Add':
        Add()
        break

    elif value == 'Read':
        Read()
        break

    elif value == 'List':
        List()
        break

    elif value == 'Remove':
        Remove()
        break

    else:
        print("Invalid input")
