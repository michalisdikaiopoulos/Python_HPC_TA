import sys

if __name__ == "__main__":
    numbers = [float(a) for a in sys.argv[1:]]
    mean = sum(numbers) / len(numbers)
    passed = mean >= 5
    print(mean, 'Pass' if passed else 'Fail')