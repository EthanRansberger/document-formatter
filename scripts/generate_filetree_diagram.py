import os

def generate_file_tree_diagram():
    os.system('tree /F > FILETREE.txt')

if __name__ == "__main__":
    generate_file_tree_diagram()
