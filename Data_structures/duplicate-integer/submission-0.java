class Solution {
    public boolean hasDuplicate(int[] nums) {
        boolean checker = false;
        for(int i=0; i<nums.length; i++){
            for(int j= 0; j<nums.length; j++){
                if(i != j && nums[i] == nums[j]){
                    checker = true;
                }
            }
        }
        return checker;
    }

}