class Solution {
    public String mergeAlternately(String word1, String word2) {
        int size = 0;
        if (word1.length() > word2.length()){
            size = word1.length();
        }
        else{
            size = word2.length();
        }
        String answer = "";
        for (int i = 0, j = 0; i < size; i++, j++){
            if (i >= word1.length()){
                return answer + word2.substring(j);
            }

            if (j >= word2.length()){
                return answer + word1.substring(i);
            }
            answer = answer.concat(String.valueOf(word1.charAt(i)));
            answer = answer.concat(String.valueOf(word2.charAt(j)));
        }
        return answer;
    }
}