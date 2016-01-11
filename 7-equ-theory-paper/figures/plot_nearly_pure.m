clear all; close all; clc;

% 1 alpha_liquid	
% 2 alpha_vapor	
% 3 density_liquid	
% 4 density_vapor	
% 5 pressure_liquid	
% 6 pressure_vapor	
% 7 velocity_liquid	
% 8 velocity_vapor	
% 9 visc_max_liq_aux	
%10 visc_max_vap_aux	
%11 beta_max_aux	
%12 vtkValidPointMask	
%13 arc_length	
%14 Points:0	
%15 Points:1	
%16 Points:2

A = csvread('200_1000cells.csv',1,0);
[n ~]=size(A);
freqA=1:40:n;
B = csvread('200_200cells.csv',1,0);
[n ~]=size(B);
freqB=1:10:n;

%%%%%%%%%%%%%%%% alpha liquid
figure; hold on;
i=1;
plot(A(freqA,14),A(freqA,i),'xr','MarkerSize',8);
plot(B(freqB,14),B(freqB,i),'ob','MarkerSize',6);
leg=char('1000 cells'); leg=char(leg,'200 cells'); h_legend=legend(leg);set(h_legend,'FontSize',11);
plot(A(:,14)    ,A(:,i)    ,'r-','LineWidth',1.3); 
plot(B(:,14)    ,B(:,i)    ,'b-','LineWidth',1.3); 
grid on; xlabel('x (m)');
ylabel('Volume fraction');
hold off;
print('Nearly_pure_alpha_compare','-dpng')
print('Nearly_pure_alpha_compare','-depsc')
%%%%%%%%%%%%%%%% pressure liquid
figure; hold on;
i=5;
plot(A(freqA,14),A(freqA,i),'xr','MarkerSize',8);
plot(B(freqB,14),B(freqB,i),'ob','MarkerSize',6);
leg=char('1000 cells'); leg=char(leg,'200 cells'); h_legend=legend(leg);set(h_legend,'FontSize',11);
plot(A(:,14)    ,A(:,i)    ,'r-','LineWidth',1.3); 
plot(B(:,14)    ,B(:,i)    ,'b-','LineWidth',1.3); 
grid on; xlabel('x (m)');
ylabel('Pressure, Pa');
hold off;
print('Nearly_pure_pressure_compare','-dpng')
print('Nearly_pure_pressure_compare','-depsc')
%%%%%%%%%%%%%%%% velocity liquid
figure; hold on;
i=7;
plot(A(freqA,14),A(freqA,i),'xr','MarkerSize',8);
plot(B(freqB,14),B(freqB,i),'ob','MarkerSize',6);
leg=char('1000 cells'); leg=char(leg,'200 cells'); h_legend=legend(leg);set(h_legend,'FontSize',11);
plot(A(:,14)    ,A(:,i)    ,'r-','LineWidth',1.3); 
plot(B(:,14)    ,B(:,i)    ,'b-','LineWidth',1.3); 
grid on; xlabel('x (m)');
ylabel('Velocity, m/s');
hold off;
print('Nearly_pure_velocity_compare','-dpng')
print('Nearly_pure_velocity_compare','-depsc')

%%%%%%%%%%%%%%%% density liquid
figure; hold on;
i=3;
plot(A(freqA,14),A(freqA,i),'xr','MarkerSize',8);
plot(B(freqB,14),B(freqB,i),'ob','MarkerSize',6);
leg=char('1000 cells'); leg=char(leg,'200 cells'); h_legend=legend(leg);set(h_legend,'FontSize',11);
plot(A(:,14)    ,A(:,i)    ,'r-','LineWidth',1.3); 
plot(B(:,14)    ,B(:,i)    ,'b-','LineWidth',1.3); 
grid on; xlabel('x (m)');
ylabel('Density, kg/m^3');
hold off;
print('Nearly_pure_density_liq_compare','-dpng')
print('Nearly_pure_density_liq_compare','-depsc')
%%%%%%%%%%%%%%%% density vapor
figure; hold on;
i=4;
plot(A(freqA,14),A(freqA,i),'xr','MarkerSize',8);
plot(B(freqB,14),B(freqB,i),'ob','MarkerSize',6);
leg=char('1000 cells'); leg=char(leg,'200 cells'); h_legend=legend(leg);set(h_legend,'FontSize',11);
plot(A(:,14)    ,A(:,i)    ,'r-','LineWidth',1.3); 
plot(B(:,14)    ,B(:,i)    ,'b-','LineWidth',1.3); 
grid on; xlabel('x (m)');
ylabel('Density, kg/m^3');
hold off;
print('Nearly_pure_density_vap_compare','-dpng')
print('Nearly_pure_density_vap_compare','-depsc')


%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
return

%%%%%%%%%%%%%%%% alpha liquid/vapor
figure; hold on;
i=1;
plot(A(:,14),A(:,i),'r-','LineWidth',1.3); 
i=2;
plot(A(:,14),A(:,i),'b-','LineWidth',1.3); 
leg=char('liquid'); leg=char(leg,'gas');h_legend=legend(leg);set(h_legend,'FontSize',11);
grid on; xlabel('x (m)');
ylabel('Volume fraction');
hold off
print('Nearly_pure_alpha_1000cells','-dpng')
print('Nearly_pure_alpha_1000cells','-depsc')
%%%%%%%%%%%%%%%% pressure liquid/vapor
figure; hold on;
i=5;
plot(A(freqA,14),A(freqA,i),'xr','MarkerSize',8);
i=6;
plot(A(freqA,14),A(freqA,i),'ob','MarkerSize',6);
i=5;
plot(A(:,14),A(:,i),'r-','LineWidth',1.3); 
i=6;
plot(A(:,14),A(:,i),'b-','LineWidth',1.3); 
leg=char('liquid'); leg=char(leg,'gas');h_legend=legend(leg);set(h_legend,'FontSize',11);
grid on; xlabel('x (m)');
ylabel('Pressure, Pa');
hold off
print('Nearly_pure_pressure_1000cells','-dpng')
print('Nearly_pure_pressure_1000cells','-depsc')
%%%%%%%%%%%%%%%% velocity liquid/vapor
figure; hold on;
i=7;
plot(A(freqA,14),A(freqA,i),'xr','MarkerSize',8);
i=8;
plot(A(freqA,14),A(freqA,i),'ob','MarkerSize',6);
i=7;
plot(A(:,14),A(:,i),'r-','LineWidth',1.3); 
i=8;
plot(A(:,14),A(:,i),'b-','LineWidth',1.3); 
leg=char('liquid'); leg=char(leg,'gas');h_legend=legend(leg);set(h_legend,'FontSize',11);
grid on; xlabel('x (m)');
ylabel('Velocity, m/s');
axis tight
hold off
print('Nearly_pure_velocity_1000cells','-dpng')
print('Nearly_pure_velocity_1000cells','-depsc')
%%%%%%%%%%%%%%%% density liquid/vapor
figure; hold on;
i=3;
plot(A(freqA,14),A(freqA,i),'xr','MarkerSize',8);
i=4;
plot(A(freqA,14),A(freqA,i),'ob','MarkerSize',6);
i=3;
plot(A(:,14),A(:,i),'r-','LineWidth',1.3); 
i=4;
plot(A(:,14),A(:,i),'b-','LineWidth',1.3); 
leg=char('liquid'); leg=char(leg,'gas');h_legend=legend(leg);set(h_legend,'FontSize',11);
grid on; xlabel('x (m)');
ylabel('Density, kg/m^3');
axis tight
hold off
print('Nearly_pure_density_1000cells','-dpng')
print('Nearly_pure_density_1000cells','-depsc')
%%%%%%%%%%%%%%%% viscosity liquid/vapor
figure; hold on;
i=9;
plot(A(freqA,14),A(freqA,i),'xr','MarkerSize',8);
i=10;
plot(A(freqA,14),A(freqA,i),'ob','MarkerSize',6);
i=11;
plot(A(freqA,14),A(freqA,i),'sk','MarkerSize',6);
i=9;
plot(A(:,14),A(:,i),'r-','LineWidth',1.3); 
i=10;
plot(A(:,14),A(:,i),'b-','LineWidth',1.3); 
i=11;
plot(A(:,14),A(:,i),'k-','LineWidth',1.3); 
leg=char('liquid'); leg=char(leg,'gas'); leg=char(leg,'vol. frac.'); h_legend=legend(leg);set(h_legend,'FontSize',11);
grid on; xlabel('x (m)');
ylabel('Viscosity');
axis tight
hold off
print('Nearly_pure_viscosity_1000cells','-dpng')
print('Nearly_pure_viscosity_1000cells','-depsc')
