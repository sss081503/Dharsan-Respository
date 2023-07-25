
def main():

    n = int(input())
    x = list(map(int, input().split()))

    # print n-1 lines
    # each line contains A/B in reduced form
    # format: "1/2"

    for i in range(n-1):
        a = x[0]
        b = x[i+1]

        while a % b == 0 and b != 1:
            a = a/b
            b = b/b
        a = int(a)
        b = int(b)
        print(str(a) + '/' + str(b))


if __name__ == "__main__":
    main()
