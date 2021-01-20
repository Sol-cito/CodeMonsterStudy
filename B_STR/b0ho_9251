import java.util.*;

public class Main {

    static char[] A;
    static char[] B;
    static int[][] dp;
    static int answer;

    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);

        A = sc.next().toCharArray();
        B = sc.next().toCharArray();

        dp = new int[A.length+1][B.length+1];

        for (int i = 1; i <= A.length; i++) {
            for (int j = 1; j <= B.length; j++) {
                if (A[i - 1] == B[j - 1]) {
                    dp[i][j] = dp[i - 1][j - 1] + 1;
                } else {
                    dp[i][j] = Math.max(dp[i - 1][j], dp[i][j - 1]);
                }
            }
        }

        answer = dp[A.length][B.length];

        System.out.println(answer);

    }

}
