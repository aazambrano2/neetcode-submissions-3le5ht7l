class Solution {
    public int calPoints(String[] operations) {

        Stack<Integer> s = new Stack<>();

        for(int i = 0; i < operations.length; i++){
            if(operations[i].equals("+")){
                int top = s.pop();
                int newTop = top + s.peek();
                s.push(top);
                s.push(newTop);
            }
            else if(operations[i].equals("D")){
                s.add(s.peek()*2);
            }
            else if(operations[i].equals("C")){
                s.pop();
            }
            else{
                 s.add(Integer.parseInt(operations[i]));
            }
        }
        int answer = 0;
        while(s.size() != 0){
            answer += s.pop();
        }
        
        return answer;
        
    }
}