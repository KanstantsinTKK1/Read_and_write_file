
# ____ Another method how you can open and work with file ____ #
# file = open("text.txt")
# contents = file.read()
# print(contents)
# file.close()


# ____Opening and reading file. Firstly should create text.txt on Desktop for reading any text____ #
with open("/Users/tkk1/Desktop/text.txt") as file:
    contents = file.read()
    print(contents)

# ____Create new file with new text____ #
with open("new_text.txt", mode="w") as file:
    file.write('Some new text')

# ____Open the file and add new line with text____ #
with open("../../Desktop/text.txt", mode="a") as file:
    file.write('\n I can add new line with any text.')
