import java.util.*;

public class Solution {
    public int solve(String string) {

        int len_string = string.length();
        if(len_string == 0 ||  len_string == 1){
            return len_string;
        }
        
        int max_len = 0;

        int p1 = 0;
        int p2 = 0;

        HashMap<String, Integer> map = new HashMap<String, Integer>();


        while(p2 < len_string){
            String letter = string.substring(p2, p2 + 1);
            if(map.containsKey(letter)){
                // already seen
                int actual_len = p2 - p1;
                // sliding pointer
                if (p1 > map.get(letter)){
                    // this is previous data info
                    p1 = p2;
                    // sum 1 for offset
                    actual_len += 1;
                }
                else{
                    p1 = map.get(letter) + 1;
                }

                if(actual_len > max_len)
                    max_len = actual_len;
            }
            map.put(letter, p2);
            // add or update found positions
            p2 += 1;
            
        }

            

        return max_len;
        
    }

    public void test(LinkedList<String> testCases, LinkedList<Integer> expected){

        for(int i=0; i<testCases.size(); i++){
            int answer = new Solution().solve(testCases.get(i));
            if(answer == expected.get(i)){
                System.out.println("OK");
            }
            else{
                System.out.println("Error: for test case " + (i+1) + ", expected: " + expected.get(i) + ", solved: " + answer);
            }
        }
        

    }
    
    public static void main(String[] args){
        LinkedList<String> testCases = new LinkedList<String>();
        LinkedList<Integer> expected = new LinkedList<Integer>();
        
        testCases.add("abcbda");
        testCases.add("abccabb");
        testCases.add("cccccc");
        testCases.add("");
        
        expected.add(4);
        expected.add(3);
        expected.add(1);
        expected.add(0);
        
        
        new Solution().test(testCases, expected);
    }
}


