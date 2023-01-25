    public static int[] rotateRight(int[] s, int k){
        k = k % s.length;
        int count = 0;
        for (int i = 0; count < s.length; i++) {
            int current = i;
            int prev = s[i];
            do {
                int next = (current + k) % s.length;
                int temp = s[next];
                s[next] = prev;
                prev = temp;
                current = next;
                count++;
            } while (i != current);

        }
        return s;
    }
