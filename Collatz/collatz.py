import sys

def main():

    f = sys.stdin
    array = map(int, f.readline().split())

    while array[0] != 0:
        collatzify(array)
        array = map(int, f.readline().split())


def collatzify(array):

    dict1 = {}
    dict2 = {}
    dict1[array[0]] = 0
    dict2[array[1]] = 0

    steps1 = 0
    steps2 = 0

    latest_val1 = array[0]
    latest_val2 = array[1]

    while True:
        if latest_val1 in dict2:
            print array[0], "needs", dict1[latest_val1], "steps,", array[1], \
            "needs", dict2[latest_val1], "steps, they meet at", latest_val1
            break
        elif latest_val2 in dict1:
            print array[0], "needs", dict1[latest_val2], "steps,", array[1], \
            "needs", dict2[latest_val2], "steps, they meet at", latest_val2
            break

        if latest_val1 != 1:
            if latest_val1 % 2 == 0:
                latest_val1 = latest_val1 / 2
            else:
                latest_val1 = latest_val1 * 3 + 1

            steps1 = steps1 + 1
            dict1[latest_val1] = steps1

        if latest_val2 != 1:
            if latest_val2 % 2 == 0:
                latest_val2 = latest_val2 / 2
            else:
                latest_val2 = latest_val2 * 3 + 1

            steps2 = steps2 + 1
            dict2[latest_val2] = steps2


if __name__ == "__main__":
    main()
