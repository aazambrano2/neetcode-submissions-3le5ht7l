class Solution {
    public int maxArea(int[] heights) {

        if(heights.length == 0 || heights == null){
            return 0;
        }

        int l = 0, r = heights.length - 1;
        int answer = 0;
        while(l < r){
            int area = Math.min(heights[l],heights[r]) * (r - l);
            answer = Math.max(answer,area);
            if(heights[l] < heights[r]){
                l++;
            } else {
                r--;
            }
        }
        return answer;
        
    }
}
