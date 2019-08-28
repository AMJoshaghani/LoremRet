import argparse, sys

lorem = """Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum."""

res = lorem.split() 

def return_words(num: int=1):
	strings = ''
	for i in res[0:num]:
		strings += i + " "
	print(strings)

def return_paragraphs(num: int=1):
	lorem_paragraph = lorem + '\n'
	print(lorem_paragraph * num)

parser = argparse.ArgumentParser(description='A simple CLI app for generating LoremIpsum!')
   
parser.add_argument('-w', '--word', dest='word', type=int, required=False, 
    help="return few LoremIpsum word from given number")

parser.add_argument('-p', '--paragraphs', dest='paragraph', type=int, required=False, 
    help="return few LoremIpsum paragraph from given number")

args = parser.parse_args()

if args.word:
	return_words(args.word)

elif args.paragraph:
	return_paragraphs(args.paragraph)
else:
	sys.exit(parser.print_help())
