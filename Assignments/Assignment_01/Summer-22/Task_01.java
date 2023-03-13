import java.util.Arrays;

public class Assignment_01 {
    public static void main(String[] args){
        int[] source_1 = {10,20,30,40,50,60};
        System.out.println(Arrays.toString(shiftLeft(source_1,3)));
    }
}

    public static int[] shiftLeft(int[] source, int k){
        for (int i=0; i<source.length; i++, k++){
            if (k>(source.length-1)){
                source[i] = 0;
            }
            else{
                source[i] = source[k];
            }
        }
        return source;
    }
