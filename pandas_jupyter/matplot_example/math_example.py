from matplotlib.patches import Polygon
import numpy as np
import matplotlib.pyplot as plt
# 定义函数
def func(x):
    return 0.5*np.exp(x)+1

# 定义参数
a,b = 0.5,1.5
x = np.linspace(0,2) # 在指定的间隔内返回均匀间隔的数字
y = func(x)

fig,ax = plt.subplots(figsize=(7,4))
plt.plot(x,y,'b',linewidth=2)
plt.ylim(bottom=0)

# 产生积分面积
Ix = np.linspace(a,b)
Iy = func(Ix)
verts = [(a,0)]+list(zip(Ix,Iy))+[(b,0)]
poly = Polygon(verts,facecolor='0.8',edgecolor='0.5')
ax.add_patch(poly)

# 添加数学公式和坐标轴标签
# LaTex代码用$$包括起来
plt.text(0.5 * (a + b), 1, r'$\int_a^b f(x)\mathrm{d}x$', horizontalalignment='center', fontsize=20)
plt.figtext(0.9,0.075,'$x$')
plt.figtext(0.075,0.9,'$f(x)$')

# 设置刻度标签
ax.set_xticks((a,b))
ax.set_xticklabels(('$a$','$b$'))
ax.set_yticks((func(a),func(b)))
ax.set_yticklabels(('$f(a)$','$f(b)$'))
plt.grid(True)
plt.show()