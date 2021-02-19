import java.util.*;
import java.io.*;

public class Main {
    static int N;
    static int[] arr;
    static int max;
    static int[] dp;
    static StringBuilder answer;

    public static void main(String[] args) throws IOException {
        answer = new StringBuilder();
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        N = Integer.parseInt(br.readLine());
        arr = new int[N];
        dp = new int[N];
        dp[0] = 1;

        if (N == 1) {
            System.out.println(0);
            return;
        }

        StringTokenizer st = new StringTokenizer(br.readLine());
        for (int i = 0; i < N; i++) {
            arr[i] = Integer.parseInt(st.nextToken());
        }

        for (int i = 1; i < N; i++) {
            dp[i] = 1;
            for (int j = 0; j < i; j++) {
                if (arr[i] < arr[j] && dp[i] < dp[j] + 1) {
                    dp[i] = dp[j] + 1;
                }
                max = Math.max(max, dp[i]);
            }
        }

        answer.append(N - max);
        System.out.print(answer);
    }

}
