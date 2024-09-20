def main():
    # score = input("학점 입력>")
    # try:
    #     if not score.isdigit():
    #         raise
    #     score = float(score)
    #     if score > 4.5:
    #         raise
    #     if score < 0:
    #         raise
    # except:
    #     exit()

    score = float(input("학점 입력>"))

    if score == 4.5:
        print(f"학점 {score}점으로 신입니다.")
    elif score >= 4.2:
        print(f"학점 {score}점으로 교수님의 사랑입니다.")
    elif score >= 3.5:
        print(f"학점 {score}점으로 현 체제의 수호자입니다.")
    elif score >= 2.8:
        print(f"학점 {score}점으로 일반인입니다.")
    elif score >= 2.3:
        print(f"학점 {score}점으로 일탈을 꿈꾸는 소시민입니다.")
    elif score >= 1.75:
        print(f"학점 {score}점으로 오락문화의 선구자입니다.")
    elif score >= 1.0:
        print(f"학점 {score}점으로 불가축천민입니다.")
    elif score >= 0.5:
        print(f"학점 {score}점으로 자벌레입니다.")
    elif score >= 0:
        print(f"학점 {score}점으로 플랑크톤입니다.")
    else:
        print(f"학점 {score}점으로 시대를 앞서가는 혁명의 씨앗입니다.")



if __name__=="__main__":
    main()
