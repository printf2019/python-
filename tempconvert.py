#tempcomvert
val = input("请输入需要转换的温度数值，如32C或32c:")
if val[-1] in ["C","c"]:
    f = 1.8 * float(val[0:-1]) + 32
    print ("转换后温度为：%.2fF"%f)
elif val[-1] in ["F","f"]:
    c = (float(val[0:-1] - 32) / 1.8
    print ("转换后温度为：%.2fC"%c)
else:
    print('输入错误！')
