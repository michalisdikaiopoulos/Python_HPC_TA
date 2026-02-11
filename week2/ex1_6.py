import sys

if __name__ == "__main__":
    numbers = [int(a) for a in sys.argv[1:]]
    numbers = [n for n in numbers if n % 2 == 0]
    print(numbers)