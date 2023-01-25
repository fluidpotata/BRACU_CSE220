    public static boolean sameRepetition(int[] source) {
        int[] repTrack = new int[source.length];
        for (int i = 0, j = 1; i < source.length; i++) {
            if (source[i] != 0) {
                for (int k = i+1; k < source.length; k++) {
                    if (source[i] == source[k]) {
                        j += 1;
                        source[k] = 0;
                    }

                }
                if (j>1) {
                    repTrack[i] = j;
                }
                j = 1;
            }
        }

        for (int i = 0; i < repTrack.length; i++) {
            if (repTrack[i] != 0) {
                for (int j = i+1; j < repTrack.length; j++) {
                    if (repTrack[i] == repTrack[j]){
                            return true;
                    }

                }
            }
        }
        return false;
    }
