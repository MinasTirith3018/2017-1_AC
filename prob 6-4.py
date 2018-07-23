# -*- coding: utf-8 -*-
"""

@author: Canopus
"""
#Hw6-4


import numpy as np
from numpy import *
import matplotlib.pyplot as plt
from scipy import ndimage

#read image
img=plt.imread('M51_hw.jpg')

lx,ly,lz=img.shape

R=img[:,:,0]
G=img[:,:,1]
B=img[:,:,2]

RF=np.fft.fft2(R)
GF=np.fft.fft2(G)
BF=np.fft.fft2(B)

RF_shift=np.fft.fftshift(RF)
GF_shift=np.fft.fftshift(GF)
BF_shift=np.fft.fftshift(BF)

kx=np.fft.fftfreq(ly,1./ly)
ky=np.fft.fftfreq(lx,1./lx)
kx_shift=np.fft.fftshift(kx)
ky_shift=np.fft.fftshift(ky)


Rp=abs(RF)**2
Rp_shift=abs(RF_shift)**2 
Rp[0,0],Rp_shift[0,0]=1.e-10,1.e-10            
lRp=np.log10(Rp)
lRp_shift=np.log10(Rp_shift)

Gp=abs(GF)**2
Gp_shift=abs(GF_shift)**2 
Gp[0,0],Gp_shift[0,0]=1.e-10,1.e-10            
lGp=np.log10(Gp)
lGp_shift=np.log10(Gp_shift)

Bp=abs(BF)**2
Bp_shift=abs(BF_shift)**2 
Bp[0,0],Bp_shift[0,0]=1.e-10,1.e-10            
lBp=np.log10(Bp)
lBp_shift=np.log10(Bp_shift)


Rkr=np.zeros((lx,ly))
for i in range(lx):
   for j in range(ly):
       Rkr[i,j]=sqrt(kx_shift[j]**2+ky_shift[i]**2)
       
plt.subplot(321),plt.pcolormesh(kx_shift,ky_shift,lRp_shift), plt.axis('equal'),plt.xlabel('kx_shift'),plt.ylabel('ky_shift'),\
plt.subplot(323),plt.pcolormesh(kx_shift,ky_shift,lGp_shift),plt.axis('equal'),plt.xlabel('kx_shift'),plt.ylabel('ky_shift'),\
plt.subplot(325),plt.pcolormesh(kx_shift,ky_shift,lBp_shift),\
plt.axis('equal'),plt.xlabel('kx_shift'),plt.ylabel('ky_shift'),\
plt.subplot(322),plt.plot(Rkr,lRp_shift,'ro'),plt.xlabel('Kr'),plt.ylabel('log10(power)'),plt.subplot(324),plt.plot(Rkr,lGp_shift,'go'),plt.xlabel('Kr'),plt.ylabel('log10(power)'),plt.subplot(326),plt.plot(Rkr,lBp_shift,'bo'),plt.xlabel('Kr'),plt.ylabel('log10(power)'),plt.savefig('Hw6-4-(a)2.png')



#%% (b)
kcut=30
X,Y=np.ogrid[0:lx,0:ly]

mask1=(X-lx/2.)**2+(Y-ly/2.)**2 > kcut**2

RFmask, GFmask, BFmask = RF_shift,GF_shift, BF_shift
      
RFmask[mask1]= 1.e-10*complex(1,1)     
GFmask[mask1]= 1.e-10*complex(1,1)
BFmask[mask1]= 1.e-10*complex(1,1)

iFRshift=np.fft.ifftshift(RFmask)
iFGshift=np.fft.ifftshift(GFmask)
iFBshift=np.fft.ifftshift(BFmask)

iFR=np.fft.ifft2(iFRshift)
iFG=np.fft.ifft2(iFGshift)
iFB=np.fft.ifft2(iFBshift)

img1=np.zeros((lx,ly,lz))
img1[:,:,0],img1[:,:,1],img1[:,:,2]=iFR.real.astype(np.int8),iFG.real.astype(np.int8),iFB.real.astype(np.int8)

plt.figure(figsize=(10,8)),plt.imshow(-img1),plt.savefig('Hw6-4(b).png')
#%%    (c)
mask2=(X-lx/2.)**2+(Y-ly/2.)**2 <= kcut**2
RFmask, GFmask, BFmask = RF_shift,GF_shift, BF_shift

RFmask[mask2]= 1.e-10*complex(1,1)     
GFmask[mask2]= 1.e-10*complex(1,1)
BFmask[mask2]= 1.e-10*complex(1,1)

iFRshift=np.fft.ifftshift(RFmask)
iFGshift=np.fft.ifftshift(GFmask)
iFBshift=np.fft.ifftshift(BFmask)

iFR=np.fft.ifft2(iFRshift)
iFG=np.fft.ifft2(iFGshift)
iFB=np.fft.ifft2(iFBshift)

img2=np.zeros((lx,ly,lz))
img2[:,:,0],img2[:,:,1],img2[:,:,2]=iFR.real.astype(np.int8),iFG.real.astype(np.int8),iFB.real.astype(np.int8)

plt.figure(figsize=(10,8)),plt.imshow(img2),plt.savefig('Hw6-4(c).png')
