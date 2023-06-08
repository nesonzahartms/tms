from pathlib import Path
q = input("vvedite stroka1: ")
w = input("vvedite stroka2: ")
e = input("vvedite stroka3: ")
r = input("vvedite stroka4: ")

current_path = Path(__file__)
current_dir = current_path.parent
print(current_dir)
current_file_name = current_path.stem
print(current_file_name)

my_file = open("homework8.2a", "w")
my_file.write(q + '\n' + w +'\n')
my_file.close()

my_file = open("homework8.2a", "a")
my_file.write(e + '\n' + r +'\n')
my_file.close()

#



