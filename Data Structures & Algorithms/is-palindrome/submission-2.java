class Solution {
    public boolean isPalindrome(String s) {
        int i = 0;
        int j = s.length() - 1;

        while (i <= j) {
            char a = s.charAt(i);
            char b = s.charAt(j);

            if (!alnum(a)) {
                i++;
            }
            else if (!alnum(b)) {
                j--;
            }
            else if (Character.toLowerCase(a) == Character.toLowerCase(b)) {
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
