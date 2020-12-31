
import java.util.*;

public class Main {

    static boolean[][] visit;
    static char[][] arr;
    static int N;
    static int M;
    static int[][] drx;
    static int answer;

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        N = sc.nextInt();
        M = sc.nextInt();
        arr = new char[N][M];
        visit = new boolean[N][M];
        drx = new int[][]{{-1, 0}, {1, 0}, {0, -1}, {0, 1}};

        for (int i = 0; i < N; i++) {
            String tmp = sc.next();
            for (int j = 0; j < M; j++) {
                arr[i][j] = tmp.charAt(j);
            }
        }


        for (int i = 0; i < N; i++) {
            for (int j = 0; j < M; j++) {
                if (arr[i][j] == 'L') {
                    visit = new boolean[N][M];
                    answer = Math.max(answer, bfs(i, j));
                }
            }
        }

        System.out.println(answer);

    }

    static class Point {
        int x;
        int y;
        int c;

        public Point(int x, int y, int c) {
            this.x = x;
            this.y = y;
            this.c = c;
        }
    }

    public static int bfs(int a, int b) {
        Queue<Point> queue = new LinkedList<>();
        queue.add(new Point(a, b, 0));
        visit[a][b] = true;

        while (!queue.isEmpty()) {
            Point p = queue.poll();

            for (int i = 0; i < 4; i++) {
                int x = p.x + drx[i][0];
                int y = p.y + drx[i][1];
                int c = p.c;

                if (x >= 0 && x < N && y >= 0 && y < M) {
                    if (!visit[x][y] && arr[x][y] == 'L') {
                        visit[x][y] = true;
                        queue.add(new Point(x, y, c + 1));
                        answer = Math.max(answer, c + 1);
                    }
                }
            }
        }

        return answer;
    }

}
