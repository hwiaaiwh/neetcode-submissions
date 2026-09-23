class Solution {
    public int[] productExceptSelf(int[] nums) {
        int[] newNums = new int[nums.length];
        int max = 1;
        int zero = -1;
        for (int i = 0; i < nums.length; i++) {
            if (nums[i] == 0) {
                if (zero == -1) {
                    zero = i;
                }
                else {
                    Arrays.fill(newNums, 0);
                    return newNums;
                }
            }
            else {
                max *= nums[i];
            }
        }
        if (zero != -1) {
            Arrays.fill(newNums, 0);
            newNums[zero] = max;
            return newNums;
        }
        else {
            Arrays.fill(newNums, max);
            for (int i = 0; i < nums.length; i++) {
                newNums[i] /= nums[i];
            }
            return newNums;
        }
    }
}  
