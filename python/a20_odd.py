def main():
    a = int(input("숫자를 넣으세요."))
    if a % 2:
        print(f"{a} 는 홀수입니다.")
    else:
        print(f"{a} 는 짝수입니다.")

if __name__=="__main__":
    main()