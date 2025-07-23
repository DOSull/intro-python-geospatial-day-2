import sys

def greeting(name = "world"):
    print(f"Hello {name}")

if __name__ == "__main__":
    if len(sys.argv) > 1:
        greeting(sys.argv[1])
    else:
        greeting()
