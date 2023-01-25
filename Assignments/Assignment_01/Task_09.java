    public static int countMaxBunch(int[] source){
        boolean chck = false;
        int prev = source[0];
        int max = 0;
        for (int i=1,current=1; i<source.length;i++){
            if (prev == source[i]){
                current+=1;
                if (max<current){
                    max = current;
                }

            }
            else {
                current = 1;
            }
            prev = source[i];
        }
        return max;
        
    }
