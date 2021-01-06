import java.util.*;

public class Main {

    static int N;
    static int M;
    static char[][] arr;
    static char[][] tmp;
    static boolean[][] visit;
    static int[][] drx;
    static int answer;

    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);
        N = sc.nextInt();
        arr = new char[N][M];
        tmp = new char[N][M];
        visit = new boolean[N][M];
        drx = new int[][]{{-1, 0}, {1, 0}, {0, 1}, {0, -1}};
        answer = 100;

        for (int i = 0; i < N; i++) {
            String str = sc.next();
            arr[i] = str.toCharArray();
        }

        for (int i = 1; i < N - 1; i++) {
            for (int j = 1; j < M - 1; j++) {
                if (!visit[i][j] && arr[i][j] == 1) {
                    answer = Math.min(answer, bfs(i, j, 0));
                }
            }
        }

        if (answer == 100) {
            answer = -1;
        }

        System.out.println(answer);

    }

    public static int bfs(int a, int b, int n) {
        Queue<Point> q = new LinkedList<>();
        q.add(new Point(a, b));
        visit[a][b] = true;

        while (!q.isEmpty()) {
            Point p = q.poll();
            int x = p.a;
            int y = p.b;

            for (int[] d : drx) {
                int nx = x + d[0];
                int ny = y + d[1];

                if (nx >= 0 && ny >= 0 && nx < N && ny < M) {
                    if (!visit[nx][ny]) {
                        if (arr[nx][ny] == 1) {
                            q.add(new Point(nx, ny));
                            visit[nx][ny] = true;
                        }
                    }
                    if (arr[nx][ny] == 'O' && tmp[nx][ny] == 'R') {
                        return n;
                    }
                    if (arr[nx][ny] == 'O' && tmp[nx][ny] == 'B') {
                        return 100;
                    }
                }
            }
        }
        return n;
    }

    public static class Point {
        int a;
        int b;

        public Point(int a, int b) {
            this.a = a;
            this.b = b;
        }
    }

}
