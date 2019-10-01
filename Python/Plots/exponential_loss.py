import matplotlib
import matplotlib.pyplot as plt
import numpy as np 
'''
Exponential Loss and Early Exponential Loss visual comparison
A. Jain, A. Singh, H. S. Koppula, S. Soh, and A. Saxena, “Recurrent Neural Networks for driver activity anticipation via sensory-fusion architecture,” in IEEE International Conference on Robotics and Automation, 2016.
F. H. Chan, Y. T. Chen, Y. Xiang, and M. Sun, “Anticipating accidents in dashcam videos,” in Asian Conference on Computer Vision (ACCV), 2016.
P. Wang, S. Lien and M. Lee, “A Learning-Based Prediction Model for Baby Accidents,” 2019 IEEE International Conference on Image Processing (ICIP), Taipei, Taiwan, 2019, pp. 629–633.
'''

'''
Let's assume that a sample is 100 frames long and the accident happens at frame T
tau = T/5 - Wang et al.
'''
T = 90
tau = T/5

yt=np.log(0.2)
x = np.linspace(0, 100)

el = -np.exp(-(T-x))*yt
eel = -(1-np.exp(-(x/tau)))*yt

fig, (ax1, ax2) = plt.subplots(2)

ax1.plot(x, el, '-k')
ax1.set_title('Exponential Loss')

ax2.plot(x, eel, '-k')
ax2.set_title('Early Exponential Loss')

for ax in (ax1, ax2):
    ax.set(ylabel='loss')
    ax.set(xlabel='time (frames)')
    ax.set_yticklabels([])
    ax.axvline(x=T, color='r')

ax1.set_ylim(0, 3.5)
ax1.fill_between(x, 0, el, facecolor='k')
ax2.fill_between(x, 0, eel, facecolor='k')

plt.show()