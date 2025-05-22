# -*- coding: utf-8 -*-
"""
Created on Fri Feb 12 10:25:50 2021

@author: ers670
"""

import numpy as np
import matplotlib.pyplot as plt
from CustFig import FigStyle
customlay = FigStyle(fontname='l',fontsize=10,grid='false')
plt.rcParams.update(plt.rcParamsDefault)
plt.rcParams.update(customlay)

#%%
space = 0; 
fig = plt.figure(figsize=(6.382, 1.66), constrained_layout=True) 
gs = fig.add_gridspec(1, 1, height_ratios=[1])
ax = [fig.add_subplot(gs[i]) for i in range(0,1)]

#%% Subplot 1,1
time = np.linspace(0,0.6,6001)
pi = np.zeros([1000,1]);
ps = np.concatenate((np.ones([50,1]),np.zeros([50,1])));
ps2 = np.concatenate((ps,ps,ps,ps,ps,ps,ps,ps,ps,ps))

stim = np.concatenate((pi,ps2,ps2,ps,np.zeros([2901,1])))
ax[0].plot(time,stim, color="k") 

ax[0].set_xlabel('Time (s)')
ax[0].set_xlim(0,0.4) 
ax[0].set_xticks([0,0.1,0.2,0.3,0.4])
ax[0].set_xticklabels([0.0,0.1,0.2,0.3,0.4])
ax[0].set_ylabel('Signal to stimulator')
ax[0].set_ylim(0,1) 
ax[0].set_yticks([0,1])
ax[0].set_yticklabels([0,1])

plt.show()

fig.savefig("Fig_Sig2DS3.png", dpi=300, bbox_inches="tight", pad_inches=space)
fig.savefig("Fig_Sig2DS3.pdf", dpi=300, bbox_inches="tight", pad_inches=space)
