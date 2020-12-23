import java.util.*;

public class Main {

    static int N;
    static boolean[][] visit;
    static int[][] drx;
    static double pos[];
    static double answer;

    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);
        N = sc.nextInt();
        visit = new boolean[30][30];
        drx = new int[][]{{-1, 0}, {1, 0}, {0, 1}, {0, -1}};
        answer = 0;
        pos = new double[4];

        for (int i = 0; i < 4; i++) {
            pos[i] = sc.nextInt() * 0.01;
        }

        dfs(15, 15, 1.0, 0);

        System.out.println(answer);

    }

    public static void dfs(int a, int b, double sum, int cnt) {

        if (N == cnt) {
            answer += sum;
            return;
        }

        visit[a][b] = true;

        for (int i = 0; i < drx.length; i++) {
            int x = a + drx[i][0];
            int y = b + drx[i][1];

            if (x >= 0 && y >= 0 && x < 30 && y < 30) {
                if (visit[x][y] == false) {
                    dfs(x, y, sum * pos[i], cnt + 1);
                }
            }

        }

        visit[a][b] = false;

    }
}