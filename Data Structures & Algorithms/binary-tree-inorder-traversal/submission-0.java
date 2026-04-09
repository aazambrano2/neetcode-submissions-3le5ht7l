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
    
    public List<Integer> inorderTraversal(TreeNode root) {
        inorder(root);
        return answer;
    }

    private void inorder(TreeNode root){
        if (root == null){
            return;
        }
        inorderTraversal(root.left);
        answer.add(root.val);
        inorderTraversal(root.right); 
    }
}