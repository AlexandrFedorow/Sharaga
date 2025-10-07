import math

x = [98, 88, 151, 29, 60, 37, 41, 69, 79, 151, 110, 131]
y = [126, 108, 170, 139, 150, 155, 201, 225, 241, 255, 270, 300]


av_x = sum(x)/len(x)
av_y = sum(y)/len(y)

print('Среднее x: ' + str(av_x))
print('Среднее y: ' + str(av_y))

sigma_x2 = sum([i**2 for i in x])/len(x) - av_x**2
sigma_y2 = sum([i**2 for i in y])/len(y) - av_y**2

sigma_x = math.sqrt(sigma_x2)
sigma_y = math.sqrt(sigma_y2)

print('sigma_x2: ' + str(sigma_x2) + ' sigma_x: ' + str(sigma_x))
print('sigma_y2: ' + str(sigma_y2) + ' sigma_y: ' + str(sigma_y))

b1 = (sum([x[i] * y[i] for i in range(len(x))])/len(x) - av_x * av_y) / sigma_x2
b0 = av_y - b1 * av_x

print('b1: ' + str(b1))
print('b0: ' + str(b0))

y_cherta = [b0 + b1 * i for i in x]
print('y_cherta: ' + str(y_cherta))

e = b1 * av_x / av_y
print('Э: ' + str(e))

rxy = (sum([x[i] * y[i] for i in range(len(x))])/len(x) - av_x * av_y) / (sigma_x * sigma_y)
Rxy = rxy ** 2
print('rxy: ' + str(rxy))
print('Rxy: ' + str(Rxy))

A = 1/len(x) * sum([(abs(y[i]-y_cherta[i])/av_y) for i in range(len(x))]) * 100
print('A: ' + str(A))

Ffact = Rxy / (1 - Rxy) * 10
print('Ffact: ' + str(Ffact))

Sy = math.sqrt( sum([(y[i]-y_cherta[i])**2 for i in range(len(x))]) / 10)
print('Sy: ' + str(Sy))

Sb0 = Sy * math.sqrt( sum([i**2 for i in x]) / sum([(i-av_x)**2 for i in x]))
print('Sb0: ' + str(Sb0))

Sb1 = Sy / math.sqrt( sum([(i-av_x)**2 for i in x]) )
print('Sb1: ' + str(Sb1))

tb0 = b0/Sb0
tb1 = b1/Sb1
print('tb0: ' + str(tb0) + ' tb1: ' + str(tb1))

Srxy = math.sqrt( (1-Rxy)/10 )
trxy = rxy/Srxy

print('Srxy: ' + str(Srxy) + ' trxy: ' + str(trxy))