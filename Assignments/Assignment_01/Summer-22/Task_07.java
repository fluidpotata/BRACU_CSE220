    public static boolean splittingArray(int[] source){
        for(int i=1, j=source.length-1,s1=0,s2=0; i<source.length-1; i++){
            for (int k=0;k<i;k++){
                s1 += source[k];
            }
            for (int x=j; x>=i; x--){
                s2 += source[x];
            }
            if (s1==s2){
                return true;
            }
            s1 = 0;
            s2 = 0;
        }
        return false;
    }
