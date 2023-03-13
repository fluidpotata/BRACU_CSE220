    public static int[] removeAll(int[] sourse, int size, int element){
        for (int i=0; i<sourse.length; i++){
            if (sourse[i]==element){
                remove(sourse,size,i);
                size -= 1;
                i -= 1;
            }
        }
        return sourse;
    }
