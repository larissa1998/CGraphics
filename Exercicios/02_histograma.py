import cv2
import numpy as np
from matplotlib import pyplot as plt

path = "mamao.jpeg"

img = cv2.imread(path)

print(img.shape)
h,w,c = img.shape
hn = int(h/4)
wn = int(w/4)
resized = cv2.resize(img,(wn,hn))
histR = np.zeros(256, np.float)
histV = np.zeros(256, np.float)
histA = np.zeros(256, np.float)
# tem as seguinte caracteristica (altura, largura e canais)
for i in range(hn):
    for j in range(wn):
        pixelVermelho = resized[i,j,2]
        histR[resized[i,j,2]] = histR[resized[i,j,2]] + 1
        pixelVerde = resized[i, j, 1]
        histV[resized[i, j, 1]] = histV[resized[i, j, 1]] + 1
        pixelAzul = resized[i, j, 0]
        histA[resized[i, j, 0]] = histA[resized[i, j, 0]] + 1
print(histR)

#tabela de probabilidades...
pixeis = hn*wn
histR = histR/pixeis
histV = histV/pixeis
histA = histA/pixeis
print(histR)

color = ('r','g','b')
plt.plot(histR,color = color[0])
plt.xlim([0,255])
plt.plot(histV,color = color[1])
plt.xlim([0,255])
plt.plot(histA,color = color[2])
plt.xlim([0,255])
plt.show()