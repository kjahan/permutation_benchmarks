import sys

def permutation(input_, start_):
    l = len(input_)
    
    if start_ >= l:
        print(input_)
    else:
        permutation(input_, start_ + 1)
    
    for i in range(start_ + 1, l):
        newinput_ = swap(input_, start_, i)
        permutation(newinput_, start_ + 1)

def swap(s, i, j):
    t = list(s)
    t[i], t[j] = t[j], t[i]
    return ''.join(t)

def main():
    if len(sys.argv) < 2:
        sys.exit("not correct usage")
    input_ = sys.argv[1]
    permutation(input_, 0)

if __name__ == "__main__":
    main()
