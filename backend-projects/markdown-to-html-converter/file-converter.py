import markdown
import sys

def main():
    try:
        if sys.argv[1] == "markdown":
                inputpath = sys.argv[2]
                outputpath = sys.argv[3]
                with open(inputpath, "r", encoding="utf-8") as f:
                    contents = f.read()
                html = markdown.markdown(contents)
                with open(outputpath, "w", encoding="utf-8") as f:
                    f.write(html)
        else:
            print("無効なコマンドです")
    except FileNotFoundError:
        print("入力ファイルが存在しません")
    except IndexError:
        print("引数の数が正しくありません")

if __name__ == "__main__":
    main()