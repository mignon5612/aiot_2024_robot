import time

def main():
    number = 0
    fps = 60
    delay_time = 1/60
    prv_time = time.time()
    while time.time() < prv_time + 5:
        number += 1
        time.sleep(delay_time)

    print(f"number of tick 5scond : {number}")

if __name__ == "__main__":
    main()