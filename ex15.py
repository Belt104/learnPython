form sys import argv

script, file = agrv

txt = open(filename)

print(f"Here's your file {filename}:")
print(txt.read())

print("type the filename again:")
file_again =input("> ")

txt_again = open (file_again)

print(txt_again.read())
