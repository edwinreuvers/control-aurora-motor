# -*- coding: utf-8 -*-
"""
Created on Tue Jan 12 17:53:12 2021

@author: ers670
"""

import numpy as np
import matplotlib.colors as colors
import matplotlib.transforms as mtransforms
import matplotlib.patches as patches
from matplotlib.path import Path

#%%
def FigStyle(**kwargs):
    # Set default values for optional inputs
    fontname    = kwargs.get('fontname', 'lmodern')        # Default to 'lmodern' if 'fontname' is not provided
    fontsize    = kwargs.get('fontsize', 11)               # Default to 11 if 'fontsize' is not provided
    grid        = kwargs.get('grid', 'off') 
        
    # Standard style
    style = {
        'lines.linestyle': "-",
        'lines.linewidth': 1,
        # Box off
        'axes.spines.bottom': True,
        'axes.spines.left': True,
        'axes.spines.right': False,
        'axes.spines.top': False,
        'legend.frameon': False,
        # legend tight
        'legend.borderpad': 0,
        # 'axes.autoscale.tight': True, ????
        # 'savefig.bbox_inches': 'tight',????
        'axes.axisbelow': True,
    }
     
    # Fontsize
    style_ftsize = {
        "font.size": fontsize,                    # Set font size
        "legend.fontsize": fontsize,              # Set legend font size
        "legend.title_fontsize": fontsize,        # Set legend title font size
        "axes.titlesize": fontsize,               # Set title font size
        }
    
    if fontname in ('libertinus', 'Libertinus'):
        style_ftname = {
            "text.usetex": True,
            "text.latex.preamble": "\n".join([
                r"\usepackage{libertine}",
                r"\usepackage[libertine]{newtxmath}",
                r"\usepackage[default,lf]{sourcesanspro}",
                r'\def\mathdefault{\textsf}'
                ]),
            "font.family": "sans-serif",        # Set font family to sans-serif
        }
    elif fontname in ('Minion Pro', 'MinionPro', 'minion pro', 'minionpro'):
        style_ftname = {
            "text.usetex": True,
            "text.latex.preamble": "\n".join([
                r"\usepackage[lf]{MinionPro}",
                r"\usepackage{MyriadPro}",
                r'\def\mathdefault{\textsf}'
                ])
            }
    elif fontname in ('lmodern', 'Latin Modern', 'latin modern'):
        style_ftname = {
            "text.usetex": True,
            "font.family": "serif",        # Set font family to sans-serif
            "text.latex.preamble": "\n".join([
                r"\usepackage{lmodern}",
                r'\def\mathdefault{\textsf}'
                ])
            }
    if grid == 'on':
        style_grid = {
            # Define nice grid
            'axes.grid': True,
            'grid.alpha': 1.0,
            'grid.color': '#eee',
            'grid.linestyle': '--',
            'grid.linewidth': 1,
            
            'axes.grid.which': 'both',             # Apply grid to both major and minor

            # xtick/ytick
            'xtick.direction': 'in',
            'xtick.major.size': 0.0,
            'xtick.minor.size': 0.0,
            'ytick.direction': 'in',
            'ytick.major.size': 0.0,
            'ytick.minor.size': 0.0,
            }
    else: 
        style_grid = {
            # Define nice grid
            'axes.grid': False,
            
            'xtick.direction': 'in',
            'xtick.major.size': 3,
            'xtick.minor.size': 1.5,
            'ytick.direction': 'in',
            'ytick.major.size': 3,
            'ytick.minor.size': 1.5,
            } 
    
    style.update({**style_ftsize, **style_ftname, **style_grid})
    return style

#%%
def GetColors(num):
    """
    GetColors give proper colors depending on number of lines. These colors
    are colorblind are BW-print friendly.
    """
    
    if num == 1:
        colors = 1
    elif num == 2:
        colors = 2
    elif num == 3:
        colors = 3
    elif num == 4:
        colors = 4
    elif num == 5:
        colors = ["000","000","000","000","000"]
          
    #%%            
    return colors
#%%
def plotPanel(fig,axs,labels,xshift=-3,yshift=6,ha='right'):
    for (ax,label) in zip(axs, labels):
        # label physical distance to the left and up:
        trans = mtransforms.ScaledTranslation(xshift/72, yshift/72, fig.dpi_scale_trans)
        ax.text(0.0, 1.0, label, transform=ax.transAxes + trans,
                fontsize='medium', va='top',ha=ha,fontweight="bold")

#%% 
def TruncateColormap(cmap, minval=0.0, maxval=1.0, n=100):
    new_cmap = colors.LinearSegmentedColormap.from_list(
        'trunc({n},{a:.2f},{b:.2f})'.format(n=cmap.name, a=minval, b=maxval),
        cmap(np.linspace(minval, maxval, n)))
    return new_cmap

#%% 
def plotStim(ax,tStimOn,tStimOff,**kwargs):
    lw = kwargs.get('lw', 1)
    color = kwargs.get('color', 'k')
    y = kwargs.get('y',0)
    
    # Plot STIM(t)
    verts = [
       (tStimOn, y-lw),  # left, bottom
       (tStimOn, y+lw),  # left, top
       (tStimOff, y+lw),  # right, top
       (tStimOff, y-lw),  # right, bottom
    ]

    codes = [
        Path.MOVETO,
        Path.LINETO,
        Path.LINETO,
        Path.LINETO,
    ]
    
    path = Path(verts, codes)
    patch = patches.PathPatch(path, facecolor=color, lw=0)
    ax.add_patch(patch)