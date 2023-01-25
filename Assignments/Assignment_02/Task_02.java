    public static int[] intersection(int[] source1, int start1, int size1, int[] source2, int start2, int size2){
        int[] outputarray = new int[size1];
        boolean chck = false;
        int m =0;
        for (int i=start1,x=0; x<size1; x++, i++){
            int k = i%source1.length;
            for (int j=start2,y=0; y<size2; j++, y++){
                int l = j%source2.length;
                if (source1[k] == source2[l]){
                    chck = true;
                    source2[l] = 0;
                }
            }
            if (chck==true){
                outputarray[m] = source1[k];
                chck = false;
                m+=1;
            }
        }
        return outputarray;
    }
