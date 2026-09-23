class Solution {
    public boolean isPalindrome(String s) {
        int i = 0;
        int j = s.length() - 1;

        while (i <= j) {

            if (!alnum(s.charAt(i))) {
                i++;
            }
            else if (!alnum(s.charAt(j))) {
                j--;
            }
            else if (Character.toLowerCase(s.charAt(i)) == Character.toLowerCase(s.charAt(j))) {
                i++;
                j--;
            }
            else {
                return false;
            }
        }
        return true;
    }

    private boolean alnum(char c) {
        return ((c >= 'A' && c <= 'Z') || 
            (c >= 'a' && c <= 'z') || 
            (c >= '0' && c <= '9'));
    }
}
