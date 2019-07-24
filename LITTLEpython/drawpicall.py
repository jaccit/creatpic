import matplotlib.pyplot as plt
import numpy as np
plt.figure(figsize=(10,8))
A=np.load('fornp.npy')
x = A[:, 0]

y1 = A[:, 1]
y2 = A[:, 2]

y3=A[:, 6]
y4=A[:, 7]
# print(type(y2))
#############LOSS###########
# plt.plot(x, y1, color='tab:blue',linewidth=2.5, label="train")  # 将$包围的内容渲染为数学公式
# plt.plot(x, y2, color='tab:orange',linewidth=2.5, label="test")
#############accuracy#######
plt.plot(x, y3, color='tab:blue',linewidth=2.5, label="train")  # 将$包围的内容渲染为数学公式
plt.plot(x, y4, color='tab:orange',linewidth=2.5, label="test")


############字体设置#########

font1 = {'family': 'serif',
        'color':  'black',
        'weight': 'bold',
        'size': 18,
        }
font2 = {'family': 'Calibri',      #字体
        'color':  'navy',          #颜色
        'weight': 'bold',         #宽度
        'size': 25,                 #大小
         }
###########################

plt.xlabel("Epoch(times)",fontdict=font1)
plt.ylabel("Accuracy",fontdict=font1)
plt.title('The curves of train and test accuracy',fontdict=font2)



################loss配置文件#############
# plt.xlim(-10, 210)
# plt.ylim(-0.01,0.21)
#
# my_x_ticks = np.arange(0, 201, 20)
# my_y_ticks = np.arange(0, 0.21, 0.02)
################accuracy配置文件############
plt.xlim(-10, 210)
plt.ylim(0.88,1)

my_x_ticks = np.arange(0, 201, 20)
my_y_ticks = np.arange(0.88, 1 , 0.01)



plt.xticks(my_x_ticks)
plt.yticks(my_y_ticks)
plt.tick_params(labelsize=15)



# plt.legend(loc='upper right', edgecolor='red',prop={'size':25})
plt.legend(loc='lower right', edgecolor='red',prop={'size':25})

plt.savefig('ACCdata')
plt.show()