    public static int[] arraySeries(int n){
        int k = n*n;
        int[] detArray = new int[k];
        int x=n;
        for (int i=k-1,j=1; i>=0; i--){
            detArray[i] = j;
            if (j<x){
                if (j!=0) {
                    j += 1;
                }
            }


            else{
                j=0;
            }
            if (i%n==0){
                x -=1;
                j=1;
            }

        }
        return detArray;
    }
