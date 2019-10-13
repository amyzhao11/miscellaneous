%%%%%%%%%%HILL%%%%%%%%
% HFFKXGMQSCRV
hill=uint8('HFFKXGMQSCRV');

hill=hill-65;
hill=double(hill);
matrix=[7 5 23 12 18 17; 5 10 6 16 2 21];

k_inv=19*[6 -3;-9 2];
k_inv=mod(k_inv,26);


result=[mod(k_inv*matrix(:,1),26).' mod(k_inv*matrix(:,2),26).' mod(k_inv*matrix(:,3),26).' mod(k_inv*matrix(:,4),26).' mod(k_inv*matrix(:,5),26).' mod(k_inv*matrix(:,6),26).']


numtochar(result)