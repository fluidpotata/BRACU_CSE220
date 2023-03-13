import java.util.Arrays;

public class Assignment_01 {
    public static void main(String[] args){
        int[] source_2 = {10,20,30,40,50,60};
        System.out.println(Arrays.toString(rotateLeft(source_2,3)));
    }
  

public static int[] rotateLeft(int[] source, int k){
        int[] newArray = new int[source.length];
        for (int i=0,tmp=0; i<(source.length); i++,k++){
            newArray[i] = source[k%source.length];
        }
        return newArray;
    }
  
}

