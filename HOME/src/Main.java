import java.util.*;

public class Main {

    static int T;
    static int w;
    static int h;
    static char[][] arr;
    static int[][] fire;
    static Queue<Fire> fire_q;
    static boolean[][] visit;
    static int[][] drx;
    static Person start;
    static int answer;

    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);
        T = sc.nextInt();

        while (T-- > 0) {

            h = sc.nextInt();
            w = sc.nextInt();
            arr = new char[w][h];
            fire = new int[w][h];
            fire_q = new LinkedList<>();
            visit = new boolean[w][h];
            drx = new int[][]{{-1, 0}, {1, 0}, {0, 1}, {0, -1}};

            for (int i = 0; i < w; i++) {
                for (int j = 0; j < h; j++) {
                    fire[i][j] = w * h;
                }
            }

            for (int i = 0; i < w; i++) {
                String str = sc.next();
                arr[i] = str.toCharArray();

                for (int j = 0; j < h; j++) {
                    if (arr[i][j] == '@') {
                        start = new Person(i, j, 0);
                    }
                    if (arr[i][j] == '*') {
                        fire_q.add(new Fire(i, j));
                        fire[i][j] = 0;
                    }
                }

            }

            //print(arr);

            fire();

            move();

            if (answer == -1) {
                System.out.println("IMPOSSIBLE");
            } else {
                System.out.println(answer);
            }

        }

    }

    public static void fire() {

        while (!fire_q.isEmpty()) {

            for (int i = 0; i < fire_q.size(); i++) {
                Fire p = fire_q.poll();
                int x = p.a;
                int y = p.b;

                for (int[] ints : drx) {
                    int nx = x + ints[0];
                    int ny = y + ints[1];

                    if (nx >= 0 && ny >= 0 && nx < w && ny < h) {
                        if (arr[nx][ny] != '#') {
                            if (fire[nx][ny] > fire[x][y] + 1) {
                                fire[nx][ny] = fire[x][y] + 1;
                                fire_q.add(new Fire(nx, ny));
                            }
                        }
                    }

                }

            }

        }

    }

    public static void move() {
        Queue<Person> q = new LinkedList<>();
        q.add(new Person(start.a, start.b, start.c));
        visit[start.a][start.b] = true;

        while (!q.isEmpty()) {
            Person p = q.poll();
            int x = p.a;
            int y = p.b;
            int cnt = p.c;

            if (x == 0 || y == 0 || x == w - 1 || y == h - 1) {
                answer = cnt + 1;
                return;
            }

            for (int[] ints : drx) {
                int nx = x + ints[0];
                int ny = y + ints[1];

                if (nx >= 0 && ny >= 0 && nx < w && ny < h) {
                    if (arr[nx][ny] == '.') {
                        if (!visit[nx][ny]) {
                            if (fire[nx][ny] > cnt + 1) {
                                visit[nx][ny] = true;
                                q.add(new Person(nx, ny, cnt + 1));
                            }
                        }
                    }
                }

            }

        }

        answer = -1;

    }

    public static class Fire {
        int a;
        int b;

        public Fire(int a, int b) {
            this.a = a;
            this.b = b;
        }
    }

    public static class Person {
        int a;
        int b;
        int c;

        public Person(int a, int b, int c) {
            this.a = a;
            this.b = b;
            this.c = c;
        }

    }

    public static void print(char[][] array) {
        for (int z = 0; z < w; z++) {
            for (int y = 0; y < h; y++) {
                System.out.print(array[z][y]);
            }
            System.out.println();
        }
    }

}
