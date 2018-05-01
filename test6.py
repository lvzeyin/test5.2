#date 2018 5 01
#
# 作业：请采用leastsq拟合一条曲线
# y=a*x*x + b*x +c
# X:  0,1,2,3,-1,-2,-3
# Y: -1.22,1.85,3.22,10.29,2.21,3.72,8.7
#
# 请尝试写出程序，与课堂上相比，多了一阶。
# 请进一步学习
# https://docs.scipy.org/doc/scipy/reference/generated/scipy.optimize.leastsq.html，请理解调用中的func, x0, args三个关键参数。
# 作业：请采用leastsq拟合一条曲线
# y=a*x*x + b*x +c
# X:  0,1,2,3,-1,-2,-3
# Y: -1.22,1.85,3.22,10.29,2.21,3.72,8.7
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import leastsq
plt.figure(figsize=(6,6))
#1英寸=2.54cm
x=np.linspace(-4,4,1000)       #根据需要生成X轴坐标数组的点数
X=np.array([0,1,2,3,-1,-2,-3])           #将一个列表转化为数组
Y=np.array([-1.22,1.85,3.22,10.29,2.21,3.72,8.7])
def f(p):                  # 定义一个函数
    a,b,c=p               #对谁做拟合
    return(Y-(a*X*X+b*X+c))                  # X Y 属于外部变量
r=leastsq(f,[1,0,0])                  # f 是拟合函数  [1,0，0] 是初始参数值
a,b,c =r[0]                   #r0 是拟合结果
print("a=",a,"b=",b,"c=",c)                 #输出拟合完的参数a,b,c

plt.scatter(X,Y,s=20,alpha=1.0,marker='o',label=u'数据点')      #绘制散点图
y=a*x*x + b*x +c                 #散点图函数
#设置坐标轴标签字体大小
ax=plt.gca()
ax.set_xlabel(..., fontsize=20)
ax.set_ylabel(..., fontsize=20)

plt.plot(x, y, color='r',linewidth=1, linestyle=":",markersize=10, label=u'拟合曲线')         #开始画图
plt.legend(loc=0, numpoints=1)
leg = plt.gca().get_legend()
ltext  = leg.get_texts()
plt.setp(ltext, fontsize='xx-large')
#坐标轴意义
plt.xlabel(u'X')
plt.ylabel(u'Y')
#坐标轴长度
plt.xlim(-4, x.max() * 1.1)
plt.ylim(-3, y.max() * 1.1)

plt.xticks(fontsize=20)
plt.yticks(fontsize=20)
#刻度字体大小
plt.legend(loc='upper left')
plt.show()