import java.util.*;

public class Main {

    static int T;
    static int A;
    static int B;
    static boolean[] visit;
    static int tmp;
    static String answer;

    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);
        T = sc.nextInt();

        while (T-- > 0) {

            A = sc.nextInt();
            B = sc.nextInt();
            visit = new boolean[10000];

            bfs();

            System.out.println(answer);
        }
    }


    public static void bfs() {
        Queue<Point> q = new LinkedList<>();
        q.add(new Point(A, ""));
        visit[A] = true;

        while (!q.isEmpty()) {
            Point p = q.poll();
            int num = p.a;
            String func = p.b;

            if (num == B) {
                answer = func;
            }

            tmp = num * 2 % 10000;
            if (!visit[tmp]) {
                visit[tmp] = true;
                q.add(new Point(tmp, func + "D"));
            }

            tmp = num - 1 < 0 ? 9999 : num - 1;
            if (!visit[tmp]) {
                visit[tmp] = true;
                q.add(new Point(tmp, func + "S"));
            }

            tmp = num % 1000 * 10 + num / 1000;
            if (!visit[tmp]) {
                visit[tmp] = true;
                q.add(new Point(tmp, func + "L"));
            }

            tmp = num % 10 * 1000 + num / 10;
            if (!visit[tmp]) {
                visit[tmp] = true;
                q.add(new Point(tmp, func + "R"));
            }

        }

    }

    public static class Point {
        int a;
        String b;

        public Point(int a, String b) {
            this.a = a;
            this.b = b;
        }

    }

}
