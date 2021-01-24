import java.util.*;
import java.io.*;

public class Main {
    static String A;
    static String B;
    static int[][] dp;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        A = st.nextToken();
        st = new StringTokenizer(br.readLine());
        B = st.nextToken();

        int lenA = A.length();
        int lenB = B.length();
        dp = new int[1001][1001];
        StringBuffer answer = new StringBuffer();

        for (int i = 1; i <= lenA; i++) {
            for (int j = 1; j <= lenB; j++) {
                if (A.charAt(i - 1) == B.charAt(j - 1)) {
                    dp[i][j] = dp[i - 1][j - 1] + 1;
                } else {
                    dp[i][j] = Math.max(dp[i - 1][j], dp[i][j - 1]);
                }
            }
        }

        while (!(lenA == 0 || lenB == 0)) {
            if (dp[lenA][lenB] == dp[lenA][lenB - 1]) {
                lenB--;
            } else if (dp[lenA][lenB] == dp[lenA - 1][lenB]) {
                lenA--;
            } else if (dp[lenA][lenB] - 1 == dp[lenA - 1][lenB - 1]) {
                answer.append(A.charAt(lenA - 1));
                lenA--;
                lenB--;
            }
        }

        System.out.println(answer.length());
        System.out.println(answer.reverse().toString());

    }

}
