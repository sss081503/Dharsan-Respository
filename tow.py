def towers(n, source, spare, dest):
    if (n==1):
        print ("move disk from", source, "to", dest)
    else:
        towers(n-1, source, dest, spare)
        print("move disk from", source, "to", dest)
        towers(n-1, spare, source, dest)
#def main():
    #towers(4, 'A', 'B', 'C')

def permute(a, idx):
    hi = len(a)
    if idx == hi:
        print(a)
    else:
        for i in range(idx, hi):
            a[idx], a[i] = a[i], a[idx]
            permute(a, idx + 1)
            a[idx], a[i] = a[i], a[idx]
def main():
    a = ['A', 'B', "C", 'D', 'E', 'F', 'G', "H", "I", "J", "K"]
    permute (a, 0)

main()