import java.util.*;
import java.io.*;

public class Main {
    static int N;
    static int[][][] dp;
    static StringBuilder answer;

    public static void main(String[] args) throws IOException {
        answer = new StringBuilder();
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        N = Integer.parseInt(br.readLine());
        //dp 문제인데 기억해야할 것들이 많은 경우
        dp = new int[N + 1][2][3];

        //top-down
        //재귀를 이용하는 dp
        //큰 문제에서 쪼개어간다
        answer.append(rec(N, 0, 0));

        System.out.print(answer);
    }

    //재귀적으로 함수를 호출하여 답을 얻는다
    //메모이제이션을 통해 bottom-up의 효율을 찾는다
    //메모이제이션 : 일종의 캐시로 이미 계산한 것을 계산하지 않는다
    public static int rec(int day, int late, int absent) {
        //기저 사례
        if (late == 2 || absent == 3) {
            return 0;
        }

        //성공 조건
        if (day == 0) {
            return 1;
        }

        //dp (캐시) 사용
        if (dp[day][late][absent] != 0) {
            return dp[day][late][absent];
        }

        int tmp = 0;
        //출석
        tmp += rec(day - 1, late, 0);
        //지각
        tmp += rec(day - 1, late + 1, 0);
        //결석
        tmp += rec(day - 1, late, absent + 1);

        //dp (캐시) 에 저장
        dp[day][late][absent] = tmp % 1000000;

        return dp[day][late][absent];
    }

}
