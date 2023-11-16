import numpy as np
import cdflib
import matplotlib.pyplot as plt

import matplotlib as mpl
import matplotlib.animation as animation

fileGEO = 'im_k0_geo_20000523_v01.cdf'
cdfGEO = cdflib.CDF(fileGEO)


file = 'twins1_l1_lad_20181211_v01.cdf'
cdf = cdflib.CDF(file)

epoch = cdf.varget('EPOCH')
lad1 = cdf.varget('lad1_2_data')

plt.plot(epoch,lad1)

"""
fileEUV = 'image_h0_euv_img0_20000523_v01.cdf'
cdfEUV = cdflib.CDF(fileEUV)

epochGEO = cdfGEO.varget('EPOCH')
epochEUV = cdfEUV.varget('EPOCH')
geoUpper = cdfGEO.varget('UPPER_GEO')
geoMiddle = cdfGEO.varget('MIDDLE_GEO')
geoLower = cdfGEO.varget('LOWER_GEO')
spinX = cdfEUV.varget('GCI_S_C_SPIN_AXIS_X')
spinY = cdfEUV.varget('GCI_S_C_SPIN_AXIS_Y')
spinZ = cdfEUV.varget('GCI_S_c_SPIN_AXIS_Z')

fig1 = plt.figure()
ax1 = plt.subplot2grid((3,3),(0,0),colspan = 3)
ax2 = plt.subplot2grid((3,3),(1,0),colspan = 3)
ax3 = plt.subplot2grid((3,3),(2,0),colspan = 3)
ax1.set_title('GEO Upper')
ax2.set_title('GEO Middle')
ax3.set_title('GEO Lower')

ax1.set(ylabel = 'Counts')
ax2.set(ylabel = 'Counts')
ax3.set(xlabel = 'Degrees (˚)', ylabel = 'Counts')

t = np.linspace(0,144)

timeGEO = [1]
shortenedUpper = np.zeros([1,180])
shortenedMiddle = np.zeros([1,180])
shortenedLower = np.zeros([1,180])
for i in range(len(epochEUV)):
    difference_array = np.absolute(epochGEO - epochEUV[i])
    index = difference_array.argmin()
    timeGEO.append(epochGEO[index])
    shortenedUpper = np.vstack([shortenedUpper, geoUpper[index,::2]])
    shortenedMiddle = np.vstack([shortenedMiddle, geoMiddle[index,::2]])
    shortenedLower = np.vstack([shortenedLower, geoLower[index,::2]])

timeGEO = timeGEO[1:]
shortenedUpper = shortenedUpper[1:]
shortenedMiddle = shortenedMiddle[1:]
shortenedLower = shortenedLower[1:]

artists1 = []
for i in range(len(t)):
    Upper = shortenedUpper[i,:]
    Middle = shortenedMiddle[i,:]
    Lower = shortenedLower[i,:]
    
    plotUpper, = ax1.plot(range(0,360,2),Upper, color = 'tab:red')
    plotMiddle, = ax2.plot(range(0,360,2),Middle, color = 'tab:green')
    plotLower, = ax3.plot(range(0,360,2),Lower, color = 'tab:blue')


    artists1.append([plotUpper, plotMiddle, plotLower])

ani1 = animation.ArtistAnimation(fig = fig1, artists = artists1, interval = 40, blit = False)
plt.show()

fig2 = plt.figure()
ax4 =  plt.subplot2grid((3,3),(0,0),colspan = 3)
ax5 = plt.subplot2grid((3,3),(1,0),colspan = 3)
ax6 = plt.subplot2grid((3,3),(2,0),colspan = 3)

posX, = ax4.plot(t[0],spinX[0])
posY, = ax5.plot(t[0],spinY[0])
posZ, = ax6.plot(t[0],spinZ[0])

ax4.set(xlim = [0,144])
ax5.set(xlim = [0,144])
ax6.set(xlim = [0,144], ylim = [6e12,10e12])

def update(frame):
    posX.set_xdata(t[:frame])
    posX.set_ydata(spinX[:frame])
    posY.set_xdata(t[:frame])
    posY.set_ydata(spinY[:frame])
    posZ.set_xdata(t[:frame])
    posZ.set_ydata(spinZ[:frame])
    
    return (posX, posY, posZ)

ani2 = animation.FuncAnimation(fig = fig2, func = update, frames = 144, interval = 40)
plt.show()

'''
fig1 = plt.figure()
ax1 = plt.subplot2grid((3,4),(0,0),colspan = 4)
ax2 = plt.subplot2grid((3,4),(1,0),colspan = 4)
ax3 = plt.subplot2grid((3,4),(2,0),colspan = 4)
ax1.set_title('GEO Upper')
ax2.set_title('GEO Middle')
ax3.set_title('GEO Lower')

ax1.set(ylabel = 'Counts')
ax2.set(ylabel = 'Counts')
ax3.set(xlabel = 'Degrees (˚)', ylabel = 'Counts')

time = cdfGEO.varget('EPOCH')
geoUpper = cdfGEO.varget('SV_X')
geoMiddle = cdfGEO.varget('SV_Y')
geoLower = cdfGEO.varget('SV_X')

artists1 = []
for i in range(len(time)):
    Upper = cdfGEO.varget('ORB_X')[i,::2]
    Middle = cdfGEO.varget('ORB_Y')[i,::2]
    Lower = cdfGEO.varget('ORB_Z')[i,::2]
    
    plotUpper, = ax1.plot(range(0,360,2),Upper, color = 'tab:red')
    plotMiddle, = ax2.plot(range(0,360,2),Middle, color = 'tab:green')
    plotLower, = ax3.plot(range(0,360,2),Lower, color = 'tab:blue')


    artists1.append([plotUpper, plotMiddle, plotLower])

ani1 = animation.ArtistAnimation(fig = fig1, artists = artists1, interval = 40, blit = False, repeat = False)
plt.show()

fig2 = plt.figure()
ax4 = plt.subplot2grid((2,4),(0,0),colspan = 4)
ax5 = plt.subplot2grid((2,4),(1,0))
ax6 = plt.subplot2grid((2,4),(1,1))
ax7 = plt.subplot2grid((2,4),(1,2))
ax8 = plt.subplot2grid((2,4),(1,3))
    
artists2 = []
for i in range(len(time)):
    hv = [cdfGEO.varget('HV')[i]] * 180
    vis1 = cdfGEO.varget('VISIBLE_SUN1')[i,::2]
    vis2 = cdfGEO.varget('VISIBLE_SUN2')[i,::2]
    uv1 = cdfGEO.varget('UV_SUN1')[i,::2]
    uv2 = cdfGEO.varget('UV_SUN2')[i,::2]
    
    plotHV, = ax4.plot(range(0,360,2),hv, color = 'tab:orange')
    plotVis1, = ax5.plot(range(0,360,2),vis1, color = 'tab:red')
    plotVis2, = ax6.plot(range(0,360,2),vis2, color = 'tab:green')
    plotUV1, = ax7.plot(range(0,360,2),uv1, color = 'tab:blue')
    plotUV2, = ax8.plot(range(0,360,2),uv2, color = 'tab:purple')
    
    artists2.append([plotHV, plotVis1, plotVis2, plotUV1, plotUV2])
    
ani2 = animation.ArtistAnimation(fig = fig2, artists = artists2, interval = 40, blit = False, repeat = False)
plt.show()
'''
"""