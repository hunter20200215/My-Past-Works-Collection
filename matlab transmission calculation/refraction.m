clc;clear;
layer_n=5;
d1=0.1;
ele1=2;
n1=1;
lam=0.1;
sita1=pi/4;
ele0=8.85*10^(-12);
mu0=4*pi*10^(-7);
n2= ele1^0.5;
sita2=asin(n1*sin(sita1)/n2);
delta1= 2*pi/lam*d1*n1*sqrt(1-(n1^2*sin(sita1)^2/n2^2));
nti=n1/cos(sita1); %TM mode%

