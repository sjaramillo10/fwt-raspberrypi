clc;
clear all;
sig = 'db10';
load db10;
S=db10;
name = 'filter_bank.txt';
file = fopen(name,'w');
for i=1:length(S)
    fprintf(file,'%f\n',S(i));
end
fclose(file);
display('END')
