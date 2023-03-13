    public static int[] remove(int[] source, int size, int idx){
        for (int i=0; i<size; i++){
            if (i>=idx){
                source[i] = source[i+1];
            }
        }
        return source;
    }
