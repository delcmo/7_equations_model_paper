clc; clear all;

% defaults values from Relap7
gamma_liquid = 2.35;
cv_liquid    = 1816;
q_liquid     = -1.167e6;
P_inf_liquid = 1e9;

gamma_vapor = 1.43;
cv_vapor    = 1040;
q_vapor     = 2.03e6;
P_inf_vapor = 0;

% input file values
gamma_liquid = 4.4;
gamma_vapor = 1.4;
P_inf_liquid = 6e8;

% initial values for P and rho
P1 = 2e8;
P2 = 1e5;
rho_liquid = 1000;
rho_vapor = 50;

% trying to compute T liquid ...
T_liquid1   = (P1 + P_inf_liquid)/(cv_liquid*(gamma_liquid-1)*rho_liquid)
T_liquid2   = (P2 + P_inf_liquid)/(cv_liquid*(gamma_liquid-1)*rho_liquid)

T_liquid1 = 129.5672454; % in marco's input
rho_liquid = (P1 + P_inf_liquid)/(cv_liquid*(gamma_liquid-1)*T_liquid1)
T_liquid2 = 97.19162996; % in marco's input
rho_liquid = (P2 + P_inf_liquid)/(cv_liquid*(gamma_liquid-1)*T_liquid2)

% T vapor computed below give the same value as in the input in order to
% have rho_vap=50
T_vapor1   = (P1 + P_inf_vapor)/(cv_vapor*(gamma_vapor-1)*rho_vapor)
T_vapor2   = (P2 + P_inf_vapor)/(cv_vapor*(gamma_vapor-1)*rho_vapor)




