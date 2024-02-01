# -*- coding:utf-8 -*-
# 导入模块
import sys
 

if __name__== "__main__":
    if len(sys.argv) != 2:
        print("sys argv error, %s binary_file_name" % sys.argv[0])
    else:
        infile_name = sys.argv[1]
        outstr = ""
        fin = open(infile_name, "rb")
        fout = open("outfile.txt", "w")
        while True :
            data1 = fin.read(1)
            if not data1:
                break
            print("data1: %s" % format(data1[0], '02X'))
            if data1[0] == 0xfe:
                data2 = fin.read(1)
                if not data2:
                    break
                print("data2: %s" % format(data2[0], '02X'))
                if data2[0] == 0x55:
                    if outstr:
                        outstr += "\n"
                        fout.write(outstr)
                    outstr = "FE 55 "
                else:
                    outstr += format(data1[0], '02X') + " "
                    outstr += format(data2[0], '02X') + " "
            else:
                outstr += format(data1[0], '02X') + " "
        fin.close()
        fout.close()

