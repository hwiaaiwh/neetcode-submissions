class Solution {

    public String encode(List<String> strs) {
        String output = "";
        for (int i = 0; i < strs.size(); i++) {
            int size = strs.get(i).length();
            output += size + ">" + strs.get(i);
        }
        System.out.println(output);
        return output;
    }

    public List<String> decode(String str) {
        List<String> output = new ArrayList<String>();
        if (str.length() == 0) {
            return output;
        }
        String string = "";
        String size = "";
        int j = 0;
        boolean start = true;

        for (int i = 0; i < str.length(); i++) {
            if (j > 0) {
                string += str.charAt(i);
                j--;
            }
            else {
                if ('>' == str.charAt(i)) {
                    if (!start) {
                        output.add(string);
                    }
                    start = false;
                    string = "";
                    j = Integer.parseInt(size);
                    size = "";
                }
                else {
                    
                    size += str.charAt(i);
                }
            }
        }
        output.add(string);
        return output;
    }
    
}
