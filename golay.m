w=[1 1 1 0 0 0 1 0 0  1 0 0 0  0 0  1 0 1  0 0 1 0 0 1];
%w_star=[w 0];
w_star=w;
b=[1 1 0 1 1 1 0 0 0 1 0 ]; %first row of B matrix
B = zeros(12,12);
B(1,1:11) = b;
for i=2:11
        B(i,:)= [b(i:11) b(1:i)]; %cyclic shift using first row
end

B(12,:)=[ones(1,11) 0]; %add row of 1s with 0 on the end
B(:,12) = [ones(11,1); 0]; %add column of 1s with 0 on the end

s=w_star*[eye(12);B]; %syndrome given by w* multiplied by G where G=[I; B]
s=mod(w_star*[eye(12);B],2); 
sum(mod(w_star*[eye(12);B],2));

for i=1:12
    disp(['row ',num2str(i)])
    disp(['syndrome= ',num2str(mod(s+B(i,:),2))])
    disp(['weight= ',num2str(sum(mod(s+B(i,:),2)))])
    
    if sum(mod(s+B(i,:),2))<=2
        ['yes j = ',num2str(i)]
        
    end
    disp(' ')

end

%second syndrome
disp('second syndrome')
s_dash=s*B;
s_dash=mod(s*B,2);
for i=1:12
    disp(['row ',num2str(i)])
    disp(['syndrome= ',num2str(mod(s_dash+B(i,:),2))])
    disp(['weight= ',num2str(sum(mod(s_dash+B(i,:),2)))])
    
    if sum(mod(s_dash+B(i,:),2))<=2
        ['yes j = ',num2str(i)]
        
    end
    disp(' ')
end

%we know b_5 is the answer so e=[theta_5 s'+b_j]
theta_5([1:4 6:12])=0;
theta_5(5)=1;
e=[theta_5 mod(s_dash+B(i,:),2)];
c_star=mod(e+w_star,2);
c=c_star(1:23);
disp(['c = ',num2str(c)])