package BaekJoon;

import java.util.Arrays;
import java.util.Scanner;

public class Question_10844 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int input = sc.nextInt();
        long[] dp = new long[10];
        Arrays.fill(dp, 1);
        dp[0] = 0;
        for (int i = 1; i < input; i++) {
            long[] newDp = new long[10];
            newDp[0] = dp[1] % 1000000000;
            for (int j = 1; j < 9; j++) {
                newDp[j] = (dp[j - 1] % 1000000000 + dp[j + 1] % 1000000000) % 1000000000;
            }
            newDp[9] = dp[8] % 1000000000;
            dp = newDp;
        }
        long answer = 0;
        for (int i = 0; i < dp.length; i++) {
            answer += dp[i];
        }
        System.out.println(answer % 1000000000);
    }
}
