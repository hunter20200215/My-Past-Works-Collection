clc;
clear all;
close all;

N=100;
dt=0.001;
g=1;
t=0:dt:1000;
k=1;
b=0.1;
q=0.005;
de=0.1;
x=0:100;a=0;
y=a*x+0.1;

u=zeros(N,length(t));
for jj=1:(N/2)
     u(jj,1)=0;
     for jj=51:N
           u(jj,1)=1;
     end 
end

for ii=2:length(t)
    u(1,ii)=u(1,ii-1)+dt*(g*u(1,ii-1)*(u(1,ii-1)-b)*(1-u(1,ii-1)/k)+q*(u(2,ii-1)-u(1,ii-1)));
    u(N,ii)=u(N,ii-1)+dt*(g*u(N,ii-1)*(u(N,ii-1)-b)*(1-u(N,ii-1)/k)+q*(u(N-1,ii-1)-u(N,ii-1)));
    for jj=2:N-1
    x1=u(jj,ii-1);
    x0=u(jj-1,ii-1);
    x2=u(jj+1,ii-1);
    u(jj,ii)=x1+dt*(g*x1*(x1-b)*(1-x1/k)+q*(x2-x1)+q*(x0-x1));
    u2=u(jj-1,ii);
    u3=u(jj,ii);
    end
    
    if t(ii)==0.1
        u_1=u(:,ii);
    end
    if t(ii)==1
        u_5=u(:,ii);
    end
    if t(ii)==50
        u_10=u(:,ii);
    end
    if t(ii)==100
        u_50=u(:,ii);
    end
    if t(ii)==500
        u_100=u(:,ii);
    end
    if t(ii)==1000;
        u_1000=u(:,ii);
    end
end

    indexx = zeros(1,6);
    subplot(3,2,1)
        hold on
    plot(x,y)
    plot(u_1)
   
aa = 1;
while true
    indexx(1) = aa; 
    aa = aa + 1;
   if (u_1(aa)>b);
      break;
  end
end
 title('t=0.1')
  plot(indexx(1),b,'o')
  text(55,0.3,strcat('x:',num2str(indexx(1)),'y:', num2str(b)));

    subplot(3,2,2)
    hold on 
    plot(u_5)
      plot(x,y)
     title('t=1')
     
     bb=1;
     while true
         
    indexx(2) = bb; 
   bb = bb + 1;
   if (u_5(bb)>b);
      break;
    end
    end

      plot(indexx(2),b,'o')
      text(55,0.3,strcat('x:',num2str(indexx(2)), 'y:', num2str(b)));
    
    subplot(3,2,3)
    hold on 
    plot(u_10)
      plot(x,y)
     title('t=50')
         
    cc=1;
     while true
         cc = cc + 1;
    indexx(3) = cc; 
    
   if (u_10(cc)>b);
      break;
    end
    end
     plot(indexx(3),b,'o')
     text(55,0.3,strcat('x:',num2str(indexx(3)), 'y:', num2str(b)));
     
    subplot(3,2,4)
    hold on 
    plot(u_50)
      plot(x,y)
     title('t=100')
  dd=1;
     while true  
         dd = dd + 1;
    indexx(4) = dd; 
  
   if (u_50(dd)>b);
      break;
    end
     end
     plot(indexx(4),b,'o')
     text(55,0.3,strcat('x:',num2str(indexx(4)), 'y:', num2str(b)));
     
     
    subplot(3,2,5)
    hold on 
    plot(u_100)
      plot(x,y)
     title('t=500')
     ee=1;
     while true
         ee = ee + 1;
    indexx(5) = ee; 
    
   if (u_100(ee)>b);
      break;
    end
    end
     plot(indexx(5),b,'o')
     text(40,0.3,strcat('x:',num2str(indexx(5)), 'y:', num2str(b)));
     
     
    subplot(3,2,6)
    hold on 
    plot(u_1000)
      plot(x,y)
     title('t=1000')
     ff=1;
     while true
    indexx(6) = ff; 
    ff = ff + 1;
   if (u_1000(ff)>b);
      break;
    end
    end
      plot(indexx(6),b,'o')
       text(20,0.3,strcat('x:',num2str(indexx(6)), 'y:', num2str(b)));
      
      
figure(2)   
xx = [0.1,1,50,100,500,1000];
plot(xx,indexx,'-o');grid on;
slope = atan((indexx(5)-indexx(6))./500);
slopedegree=rad2deg(slope);
text(700,(indexx(5)+indexx(6))/2,strcat('slope:',num2str(slopedegree)));

figure(3)
xxx= [0.001,0.002,0.005,0.01,0.02];
yyy= [0.11459,0.11459,1.1458,2.1762,2.1762];
xq =0:0.02;
yq=interp1(yyy,xq);
plot(xxx,yyy,'b--o');
grid on;



    
    


  
    
  

 









