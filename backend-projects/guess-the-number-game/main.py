import sys
import random

def print_ft(msg):
    sys.stdout.buffer.write(msg.encode() + b"\n")
    sys.stdout.flush()

def input_ft(msg):
    print_ft(msg)
    return sys.stdin.buffer.readline().decode().replace("\n", "")

def validateRange(min, max):
    if(int(min) > int(max)):
        return False
    return True

def getRange():
    while True:
        min = input_ft("最小値を入力してください")
        max = input_ft("最大値を入力してください")
        if(validateRange(min, max)):
            return min, max
        print_ft("無効な範囲です\nもう一度入力してください")

def main():
    print_ft("数字当てゲームを始めます")

    print_ft("まずは数字の範囲を指定してください")
    min, max = getRange()
    answer = random.randint(int(min), int(max))

    print_ft("それではゲームを始めます")
    while True:
        trial = input_ft("予想する数字を入力してください")
        if int(trial) == answer:
            print_ft("正解です")
            break
        if int(trial) < answer:
            print_ft("答えは予想よりも大きいです")
        if int(trial) > answer:
            print_ft("答えは予想よりも小さいです")

if __name__ == "__main__":
    main()