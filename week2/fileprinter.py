filename = 'csvfile.csv'
outputfile = 'test.txt'
names = ("Aleksander", "Lars", "Peter", "Ole", "jens", "Olga", "Allan")
newlist=[]
def print_file_content(file):
    with open(file) as file_object:
        lines = file_object.readlines()
    for line in lines:
        print(line.strip())

def write_list_to_file(output_file, lst):
    with open(outputfile, 'w') as file_object:
        for name in lst:
            file_object.write(name.strip()+ "\n")

def read_csv(file):
    with open(file) as file_object:
        lines = file_object.readlines()
    for line in lines:
        newlist.append(line)
    print(newlist)



if __name__ == '__main__':
    print_file_content(filename)
    write_list_to_file(outputfile, names)
    print_file_content(outputfile)
    read_csv(filename)
