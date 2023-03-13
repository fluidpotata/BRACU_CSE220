    public static int[] shiftRight(int[] source, int k){
        int limit = k;
        for (int i=0; i<limit; i++,k++){
            if (k<source.length){
                source[(k)] = source[i];
                source[i] = 0;
            }
            else{
                source[i] = 0;
            }
        }
        return source;
    
