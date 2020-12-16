
import java.util.*;

public class Main {

    static ArrayList<Integer>[] arr;
    static int N;
    static int R;
    static int Q;
    static int[] answer;
    static boolean[] visit;
    static int[] query;

    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);
        N = sc.nextInt();
        R = sc.nextInt();
        Q = sc.nextInt();
        arr = new ArrayList[N + 1];
        answer = new int[N + 1];
        visit = new boolean[N + 1];
        query = new int[Q];

        for (int i = 1; i < N + 1; i++) {
            arr[i] = new ArrayList<>();
        }

        // 트리연결
        for (int i = 0; i < N - 1; i++) {
            int a = sc.nextInt();
            int b = sc.nextInt();
            arr[a].add(b);
            arr[b].add(a);
        }

        for (int i = 0; i < Q; i++) {
            query[i] = sc.nextInt();
        }

        //한번에 모두 구하기
        dfs(R);

        for (int i = 0; i < Q; i++) {
            System.out.println(answer[query[i]]);
        }

    }

    public static int dfs(int now) {

        if (answer[now] == 0) {
            visit[now] = true;
            answer[now] = 1;

            for (int i = 0; i < arr[now].size(); i++) {
                int next = arr[now].get(i);

                if (visit[next] == false) {
                    //재귀할 때마다 = 이어진 정점으로 내려갈때마다
                    //카운터 증가하며 개수 저장
                    //지금 서브쿼리와 다음 서브쿼리의 개수 차이는 1임
                    answer[now] += dfs(next);
                }
            }

        }

        return answer[now];
    }

}
