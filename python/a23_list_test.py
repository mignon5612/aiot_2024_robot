def main():
    # li1 = []
    # li1 = list()
    li1 = [123, 333, 1.2, 'list element']
    print(type(li1))
    print(li1)
    print(li1[0])
    print(li1[1])
    print(li1[2:4])
    li1[1] = "삼삼삼"
    print(li1)

if __name__=="__main__":
    main()
