
import java.util.*;

public class Main {

    static boolean[][] visit;
    static String[][] arr;
    static String[][] arr2;
    static int N;
    static String M;
    static int[] cnt;
    static int[][] drx;

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String answer = "";
        N = sc.nextInt();
        arr = new String[N + 1][N + 1];
        arr2 = new String[N + 1][N + 1];
        visit = new boolean[N + 1][N + 1];
        cnt = new int[2];
        drx = new int[][]{{-1, 0}, {1, 0}, {0, -1}, {0, 1}};

        for (int i = 1; i < N + 1; i++) {
            M = sc.next();
            String[] tmp = M.split("");
            for (int j = 1; j < N + 1; j++) {
                arr[i][j] = tmp[j - 1];
                arr2[i][j] = tmp[j - 1];
                if (arr2[i][j].equals("G")) {
                    arr2[i][j] = "R";
                }
            }
        }


        for (int i = 1; i < N + 1; i++) {
            for (int j = 1; j < N + 1; j++) {
                if (visit[i][j] == false) {
                    bfs(i, j, arr);
                    cnt[0]++;
                }
            }
        }

        visit = new boolean[N + 1][N + 1];
        for (int i = 1; i < N + 1; i++) {
            for (int j = 1; j < N + 1; j++) {
                if (visit[i][j] == false) {
                    bfs(i, j, arr2);
                    cnt[1]++;
                }
            }
        }

        answer = cnt[0] + " " + cnt[1];
        System.out.println(answer);
    }

    static class Point {
        int x;
        int y;

        public Point(int x, int y) {
            this.x = x;
            this.y = y;
        }
    }

    public static void bfs(int a, int b, String[][] list) {
        Queue<Point> queue = new LinkedList<Point>();
        queue.add(new Point(a, b));
        visit[a][b] = true;

        while (!queue.isEmpty()) {
            Point p = queue.poll();

            for (int i = 0; i < 4; i++) {
                int x = p.x + drx[i][0];
                int y = p.y + drx[i][1];

                if (x > 0 && x < N + 1 && y > 0 && y < N + 1) {
                    if (!visit[x][y] && list[x][y].equals(list[a][b])) {
                        visit[x][y] = true;
                        queue.add(new Point(x, y));
                    }
                }
            }
        }

    }

}
