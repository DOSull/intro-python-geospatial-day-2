import argparse

parser = argparse.ArgumentParser()
parser.add_argument(
    "-n", "--name", help = "name to greet")
parser.parse_args()
args = parser.parse_args()

def greeting(name = "world"):
    print(f"Hello {name}")

if args.name is None:
    greeting()
else:
    greeting(args.name)