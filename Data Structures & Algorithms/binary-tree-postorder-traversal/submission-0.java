/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */
class Solution {
    private List<Integer> answer = new ArrayList<Integer>();
    public List<Integer> postorderTraversal(TreeNode root) {
        postorder(root);
        return answer;
    }

    private void postorder(TreeNode root){
        if(root==null){
            return;
        }
        postorder(root.left);
        postorder(root.right);
        answer.add(root.val);
    }
}