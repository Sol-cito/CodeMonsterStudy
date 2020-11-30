package BaekJoon;

import java.util.Scanner;

public class Question_11052 {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int n = scanner.nextInt();
        int[] cardArr = new int[n];
        for (int i = 0; i < n; i++) {
            cardArr[i] = scanner.nextInt();
        }
        long[] dp = new long[n + 1];
        for (int i = 1; i <= n; i++) { // 카드 수
            for (int j = 0; j < cardArr.length; j++) {
                dp[i] = i - (j + 1) >= 0 ? Math.max(dp[i], dp[i - (j + 1)] + cardArr[j]) : dp[i];
            }
        }
        System.out.println(dp[n]);
    }
}
