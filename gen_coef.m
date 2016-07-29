clc;
clear all;
sig = 'db10';
load db10;
S=db10;
name = strcat(sig,'_bank.txt');
file = fopen(name,'w');
for i=1:length(S)
    fprintf(file,'%f\n',S(i));
end
fclose(file);
display('END')