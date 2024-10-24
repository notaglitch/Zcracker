import zipfile
#Written by notaglitch, just for fun.
#I am learning so don't judge and this script may be simple but it does the job.
file_name = input("Enter the file name here: ")
wordl = input("Enter the wordist name: (with the format like: .txt) ")
password = ""

zip_file = zipfile.ZipFile(file_name)

if file_name[-4:] == ".zip":
    pass
else:
    file_name = file_name + ".zip"

with open(wordl, "rb") as file:
    for line in file:
        line = line.strip()

        try:
            zip_file.extractall(pwd=line)
            #print("Password found: ", line)
            password = line
            break
        except:
            print(line)
            continue

if password == "":
    print("Shit!, the password was not found but you can always try another wordlist")
elif password == line:
    print("Password found", line)
else:
    print("An error accured, try again. ")
