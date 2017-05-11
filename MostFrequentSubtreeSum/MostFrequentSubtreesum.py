int numberofbits(unsigned int a){
    int count=0;    
    for(int i=0;i<32;i++){
        count+=0x0001&a;
        a>>1;
    }
    return count;
}

int numberofbits1(unsigned int a){
    count=0;
    while(a){
        a=a&&(a-1);
        count++;
    }
    return count;
}

// Complexity: Time - 
int reverseInteger(int a){
    
    int sign=1;
    if(a<0){
        sign=-1;
        a=a*sign;
    }
    
    int lb=0;
    int cb=0;
    
    while(a){
        cb=(lb*10)+(a%10);
        if(cb/10 != lb){
            return 0;
        }
        a=a/10;
        lb=cb;
    }
    
    return cb*sign;
}