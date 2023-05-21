import sys

# txt文件的目录
QQ_FILE_PATH = "C:\\Users\\yuanbao\\Desktop\\"
# txt文件的文件名
FILE_NAME = "潘丽老师(46495473).txt"


def main():
    fin = open(QQ_FILE_PATH+FILE_NAME, "r", encoding='utf8')
    fout = open(FILE_NAME, "w", encoding='utf8')

    for line in fin.readlines():
        if len(line) > 0:
            if line[0] == '2' and line[1] == '0' or (line[:4] == "http"):
                pass
            else:
                fout.write(line)


if __name__ == '__main__':
    # if len(sys.argv) == 2:
    #     main(sys.argv[1])
    # else:
    #     print('[usage] <input>')
    main()
