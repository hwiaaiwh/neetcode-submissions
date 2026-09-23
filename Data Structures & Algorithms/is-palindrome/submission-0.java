class Solution {
    public boolean isPalindrome(String s) {
        String newS = "";
        for (int i = 0; i < s.length(); i++) {
             if (Character.isDigit(s.charAt(i))) {
                newS += s.charAt(i);
            }
            else if (Character.isLetter(s.charAt(i))) {
                newS += Character.toLowerCase(s.charAt(i));
            }
        }
        
        for (int i = 0; i < newS.length() / 2; i++) {
            if (newS.charAt(i) != newS.charAt(newS.length() - i - 1)) {
                return false;
            }
        }
        return true;
    }
}
