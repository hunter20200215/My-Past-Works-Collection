clc;clear all;
g=1;
q=0.01;
sigma=1;
n=1;
for j=1:100
   q_ij(j)=q/(sigma*(2*pi)^0.5)*(exp(-(n-j)^2/sigma^2)); 
   plot(j,q_ij(j),'r--o');
   hold on;
    
end
g=1;
q=0.01;
sigma=1;
n=20;
for j=1:100
   q_ij(j)=q/(sigma*(2*pi)^0.5)*(exp(-(n-j)^2/sigma^2)); 
   plot(j,q_ij(j),'r--o');
   hold on;
    
end
g=1;
q=0.01;
sigma=1;
n=50;
for j=1:100
   q_ij(j)=q/(sigma*(2*pi)^0.5)*(exp(-(n-j)^2/sigma^2)); 
   plot(j,q_ij(j),'r--o');
   hold on;
    
end
g=1;
q=0.01;
sigma=1;
n=70;
for j=1:100
   q_ij(j)=q/(sigma*(2*pi)^0.5)*(exp(-(n-j)^2/sigma^2)); 
   plot(j,q_ij(j),'r--o');
   hold on;
    
end
g=1;
q=0.01;
sigma=1;
n=100;
for j=1:100
   q_ij(j)=q/(sigma*(2*pi)^0.5)*(exp(-(n-j)^2/sigma^2)); 
   plot(j,q_ij(j),'r--o');
   hold on;
    
end



