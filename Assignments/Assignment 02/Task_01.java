  public static boolean checkPalindrome(int[] source, int start, int size){
        boolean chck = true;
        for (int i=start, j=0, k=1; j<size; i++,j++,k++){
            if (i!=start+size-k) {
                if (source[i % source.length] != source[(start + size - k) % source.length]) {
                    return false;
                }
            }
        }
        return chck;
    }
