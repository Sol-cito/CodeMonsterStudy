
import java.util.*;

public class Main {

    static int F;
    static int S;
    static int G;
    static int U;
    static int D;
    static int[] list;
    static String answer;

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        F = sc.nextInt();
        S = sc.nextInt();
        G = sc.nextInt();
        U = sc.nextInt();
        D = sc.nextInt();
        list = new int[F + 1];

        bfs();

        System.out.println(answer);

    }


    public static void bfs() {
        Queue<Integer> queue = new LinkedList<>();
        queue.add(S);
        list[S] = 1;

        while (!queue.isEmpty()) {
            int now = queue.poll();

            if (now == G) {
                answer = list[now] - 1 + "";
                return;
            }

            int Up = now + U;
            if (Up <= F && list[Up] == 0) {
                list[Up] = list[now] + 1;
                queue.add(Up);
            }

            int Down = now - D;
            if (Down >= 1 && list[Down] == 0) {
                list[Down] = list[now] + 1;
                queue.add(Down);
            }

        }

        answer = "use the stairs";

    }

}
