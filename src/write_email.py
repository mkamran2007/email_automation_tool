import subprocess

def write_email():
    file_path = "./data/templates/default.txt"
    temp_file = "./data/templates/temp.txt"

    with open(file_path) as file:
        content = file.read()
    
    with open(temp_file, "w") as file:
        file.write(content)
    
    subprocess.call(["notepad.exe", temp_file])

    print("Your email has been saved in temp.txt")

