import java.util.*;

public class Main {

    static int K;
    static int V;
    static int E;
    static ArrayList<Integer>[] arr;
    static String[] visit;
    static String answer;

    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);
        K = sc.nextInt();

        while (K-- > 0) {

            V = sc.nextInt();
            E = sc.nextInt();
            arr = new ArrayList[V + 1];
            visit = new String[V + 1];
            answer = "YES";

            for (int i = 1; i < V + 1; i++) {
                arr[i] = new ArrayList<>();
            }

            for (int j = 0; j < E; j++) {
                int a = sc.nextInt();
                int b = sc.nextInt();
                arr[a].add(b);
                arr[b].add(a);
            }

            bfs();

            System.out.println(answer);
        }

    }

    public static void bfs() {

        Queue<Integer> q = new LinkedList<>();

        for (int i = 1; i < V + 1; i++) {
            if (visit[i] == null) {
                q.add(i);
                visit[i] = "A";
            }

            while (!q.isEmpty()) {
                int now = q.poll();

                for (int j = 0; j < arr[now].size(); j++) {
                    int next = arr[now].get(j);

                    if (visit[next] == visit[now]) {
                        answer = "NO";
                        return;
                    }

                    if (visit[next] == null) {
                        q.add(next);
                        if (visit[now] == "A") {
                            visit[next] = "B";
                        }
                        if (visit[now] == "B") {
                            visit[next] = "A";
                        }
                    }

                }
            }
        }

    }

}
