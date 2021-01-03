import java.util.*;

public class Main {

    static int R;
    static int C;
    static char[][] arr;
    static int[][] d_day;
    static int[][] visit;
    static int[][] drx;
    static Point start;
    static Point end;

    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);
        R = sc.nextInt();
        C = sc.nextInt();
        arr = new char[R + 1][C + 1];
        d_day = new int[R + 1][C + 1];
        visit = new int[R + 1][C + 1];
        drx = new int[][]{{-1, 0}, {1, 0}, {0, 1}, {0, -1}};

        for (int i = 0; i < R; i++) {
            String str = sc.next();
            arr[i] = str.toCharArray();

            for (int j = 0; j < C; j++) {
                if (arr[i][j] == 'S') {
                    start = new Point(i, j);
                } else if (arr[i][j] == 'D') {
                    end = new Point(i, j);
                }
            }
        }

        flush();
        bfs();

        if (visit[end.a][end.b] == 0) {
            System.out.println("KAKTUS");
        } else {
            System.out.println(visit[end.a][end.b]);
        }

    }

    public static void flush() {
        Queue<Point> q = new LinkedList<>();

        for (int i = 0; i < R; i++) {
            for (int j = 0; j < C; j++) {
                if (arr[i][j] == '*') {
                    q.add(new Point(i, j));
                }
            }
        }

        while (!q.isEmpty()) {
            Point p = q.poll();

            for (int[] ints : drx) {
                int x = p.a + ints[0];
                int y = p.b + ints[1];

                if (x >= 0 && y >= 0 && x < R && y < C) {
                    if (d_day[x][y] == 0 && arr[x][y] == '.') {
                        d_day[x][y] = d_day[p.a][p.b] + 1;
                        q.add(new Point(x, y));
                    }
                }
            }
        }

    }

    public static void bfs() {
        Queue<Point> q = new LinkedList<>();
        q.add(new Point(start.a, start.b));

        while (!q.isEmpty()) {
            Point p = q.poll();

            for (int[] ints : drx) {
                int x = p.a + ints[0];
                int y = p.b + ints[1];

                if (x >= 0 && y >= 0 && x < R && y < C) {
                    if (visit[x][y] == 0 && arr[x][y] != 'X' && arr[x][y] != '*' && arr[x][y] != 'S') {
                        if (d_day[x][y] == 0 || d_day[x][y] > visit[p.a][p.b] + 1) {
                            visit[x][y] = visit[p.a][p.b] + 1;
                            q.add(new Point(x, y));
                        }
                    }
                }
            }
        }
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
