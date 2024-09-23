output = []

def flatten(data):
    li = data.pop(0)
    if isinstance(li, int):
        output.extend([li])
    if isinstance(li, list):
        for ele in li:
            return flatten(ele)
    print(li)
    if li == None:
        return output

def main():
    example=[[1,2,3], [4,[5,6]], [7,[8,9]]]
    print(flatten(example))

if __name__=="__main__":
    main()
