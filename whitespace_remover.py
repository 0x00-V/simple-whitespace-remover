import sys

def remove_whitespace(input):
    output = "".join(input.split()) 
    print("Whitespace Removed: \n")
    print(output)
    print("\n-----------------------------------------------------")

if len(sys.argv) < 2:
    print("Incorrect usage: python whitespace_remover.py <input>")
    sys.exit(1)

input = " ".join(sys.argv[1:])

remove_whitespace(input)
