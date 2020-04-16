clc;clear all;
% Wave Properties ~ ~ -~'
f=input('\nlncident wave frequency?\n');
w=2*pi*f;
fprintf('Incident wave polarization?\n');
fprintf('1 = Transverse Electric (TE or perpendicular)\n') ;
Pol=input('2 = Transverse Magnetic (TM or parallel)\n');
if Pol~=1 && Pol~=2
fprintf('Error, must be 1 or 2, please start over\n')
end
fprintf(' incident angles (0 to 85 degrees, 0 is normal \n')
Angles=input('to surface). incident angle (degrees)\n');
if Angles<0 || Angles>85
fprintf('Error, must be 0 to 85, please start over\n')
end
AL=length(Angles);
% Target Properties ~"� "�"
fprintf('Number of layers? (At least 3) Layer 1 is air, last layer');
L=input('\nis either dielectric (may be air) or PEC\n');
if L~=round(L)
    fprintf('Error, must have integer number of layers\n')
end
if L<3
    fprintf('Error, must have 3 or more layers\n')
end
PEC=0;
fprintf('\nLayer 1 is air\n')
fprintf('Relative electric permittivity = 1 \n')
    er(1)=1;
    fprintf('Relative magnetic permeability = 1 \n')
    mr(1)=1;
    fprintf('Static Conductivity = 0 \n')
S(1)=0;
for b=2:L-1
fprintf('\nLayer %g is dielectric\n',b)
dl(b)=input('Thickness (mm) \n');
fprintf('Relative electric permittivity\n')
er(b)=input('Input complex values as x-i*y\n');
fprintf('Relative magnetic permeability\n')
mr(b)=input('Input complex values as x-i*y\n');
S(b)=input('Static conductivity (real)\n');
if imag(S(b))~=0
    S(b)=real(S(b));
    fprintf('Imaginary part of sigma ignored\n')
end
if imag(er(b))~=0 | imag(mr(b))~=0
    fprintf('Layer %g is lossy\n',b)
end
end
d=.001*dl; % thickness (meters)
fprintf('\nIf Layer %g is PEC, enter 1 now, otherwise enter 0',L)
PEC=input('\n');
if PEC==1
    fprintf('Layer %g is PEC\n',L)
    S(L)=Inf; % can use a real conductivity here
    % treat (sigma+j*omega*epsilon)/(j*omega*epsilonO) as er
    er(L)=1-i*S(L)/(w*8.854185e-12);%calculate the ?
    mr(L)=1; % dummy value
else
fprintf('Layer %g is dielectric\n',L)
fprintf('Relative electric permittivity\n')
er(L)=input('Input complex values as x+i*y\n');
fprintf('Relative magnetic permeability\n')
mr (L)=input('Input complex values as x+i*y\n');
S(L)=input('Static conductivity (real)\n');
if imag(S(L))~=0
S(L)=real(S(L));
fprintf('Imaginary part of sigma ignored\n')
end
    if imag(er(L))~=0 | imag(mr(L))~=0 | S(L)~=0
        fprintf('Layer %g is lossy, loss will not affect answer',L)
    end
end
e=er*8.854185e-12;
m=mr*4*pi*1e-7;
% Angles, Propagation Constants, Admittances ~ ~
% calculate angles thru each layer via Snell's law
Ang=[Angles*pi/180; zeros(L-1,AL)];
G(1)=sqrt((S(1)+j*w*e(1))*(j*w*m(1))); % propagation const in air
Y(1)=sqrt((S(1)+j*w*e(1))/(j*w*m(1))); % admittance of air
for b=2:L-1
G(b)=sqrt(j*w*m(b)*(S(b)+j*w*e(b)));
Y(b)=sqrt((S(b)+j*w*e(b))/(j*w*m(b)));
Ang(b,:)=asin(sin(Ang(b-1,:))*G(b-1)/G(b));
end
% find attenuation through all layers (except 1, L)
if PEC==1
G(L)=Inf*(1+j); % sqrt(Inf*j*w*m)
Y(L)=Inf*(-1+j); % sqrt(Inf/(j*w*m))
Ang(L,:)=0;
else
G(L)=sqrt((S(L)+j*w*e(L))*(j*w*m(L)));
Y(L)=sqrt((S(L)+j*w*e(L))/(j*w*m(L)));
Ang(L,:)=asin(sin(Ang(L-1,:))*G(L-1)/G(L));
end
% reflected ray angles are negatives of incident ray angles
% Reflectivity and Transmissivity
mll=zeros(1,AL);

m12=zeros(1,AL);
m21=zeros(1,AL);
m22=zeros(1,AL) ;
Yt=zeros(L,AL);
refN=zeros(1,AL);
refD=zeros(1,AL);
ref=zeros(1,AL);
tran=zeros(1,AL);
% find tilted admittance
if Pol==1 % TE case
for b=1:L
Yt(b,:)=Y(b).*cos(Ang(b,:));
end
else % TM case
for b=1:L
Yt(b, :)=Y(b) ./cos(Ang(b, : ) ) ;
end
end
% find ref & tran coeff
for a=1:AL
Mtot=eye(2);
% find characteristic matrix of each layer and overall
for b=2:L-1
D=1i*G(b)*d(b)*cos(Ang(b,a));
M=[cos(D) -i/Yt(b,a)*sin(D); -i*Yt(b,a)*sin(D) cos(D)];
Mtot=Mtot*M;
end
m11(a)=M(1,1);
m12(a)=M(1,2);
m21(a)=M(2,1);
m22(a)=M(2,2);
end
% find transmissivity, reflectivity, absorptivity
if PEC==1
Yt(L,:)=1; % dummy value
ref=(m12.*Yt(1,:)-m22)/(m12.*Yt(1,:)+m22);
tran=0;
AbsorN=real(m12.*conj(m22));
Absorp=4*Yt(1,:).*AbsorN./(abs(m12.*Yt(1,:)+m22).^2);
Transm=0;
else
Yt(L, :)=Y(L) ./cos(Ang(L, :));
refN=Yt(1,:).*(m11+Yt(L,:).*m12)-m21-Yt(L,:).*m22;
refD=Yt(1,:).*(m11+Yt(L,:).*m12)+m21+Yt(L,:).*m22;
ref=refN./refD;
tran=2*real(Yt(1,:))./refD;
AbsorN=real((m11+Yt(L,:).*m12).*conj(m21+Yt(L,:).*m22)-Yt(L,:));
Absorp=4*Yt(1,:).*AbsorN./(refD.*conj(refD));
Transm=real(Yt(L,:))./real(Yt(1,:)).*tran.*conj(tran);
end
fprintf('determined the reflec Coeff=\n')
abs(ref)
fprintf('determined the trans Coeff=\n')
abs(tran)
fprintf('Homogenized complex permittivity=\n')
epsilon_equal=(1-abs(ref))/(1+abs(ref))


