package BaekJoon;

import java.util.Arrays;
import java.util.Scanner;

public class Question_11057 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int input = sc.nextInt();
        int[] dp = new int[10];
        Arrays.fill(dp, 1);
        for (int i = 0; i < input; i++) {
            for (int j = 0; j < 10; j++) {
                int cnt = 0;
                for (int k = j; k < 10; k++) {
                    cnt += dp[k] % 10007;
                }
                dp[j] = cnt;
            }
        }
        System.out.println(dp[0] % 10007);
    }
}
