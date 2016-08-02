% This file generates the low pass and high
% pass filter coefficients for the DWT
clc; clear all;
wavelet = 'db10';
name = 'filter_bank.txt';
[Lo_D,Hi_D] = wfilters(wavelet,'d');
S = [Lo_D Hi_D];
file = fopen(name,'w');
for i=1:length(S)
    fprintf(file,'%f\n',S(i));
end
fclose(file);
display('END')
