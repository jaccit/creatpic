import re
newfile1=r'C:\LITTLEpython\data1.txt'
newfile2=r'C:\LITTLEpython\data2.txt'
file1=open(newfile1,'w',encoding="utf-8")
file2=open(newfile2,'w',encoding="utf-8")
newfile3=r'C:\LITTLEpython\data3.txt'
file3=open(newfile3,'w',encoding="utf-8")
newfile4=r'C:\LITTLEpython\data4.txt'
file4=open(newfile4,'w',encoding="utf-8")
newfile5=r'C:\LITTLEpython\data5.txt'
file5=open(newfile5,'w',encoding="utf-8")
newfile6=r'C:\LITTLEpython\data6.txt'
file6=open(newfile6,'w',encoding="utf-8")
origdata=open(r'C:\LITTLEpython\mixgasprinttxt.txt')


epoch='epoch'
lines=origdata.readlines()
for line in lines:
    # print(line)
    if epoch in line:
        adddata=re.findall(r"\d+\.\d*",line)
        print(adddata)
        #######下面为保存带【】的列表#####
        file1.write(str(adddata)+'\n')
        #######下面为保存去除格式的纯列表#####
        s = str(adddata).replace('[', '').replace(']', '')  # 去除[]
        s = s.replace("'", '').replace(',', '')
        file2.write(s+'\n')
        #######下面为保存为单一属性的文件（train_loss）(test_loss)(train acc)(test acc)####
        file3.write(adddata[0]+'\n')
        file4.write(adddata[1]+'\n')
        file5.write(adddata[5] + '\n')
        file6.write(adddata[6] + '\n')

file1.close()
file2.close()
file3.close()
file4.close()
file5.close()
file6.close()
