import java.util.*;

public class Main {

    static int N;
    static int K;
    static Jewelry[] N_arr;
    static int[] K_arr;
    static PriorityQueue<Integer> pq;
    static long answer;

    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);

        N = sc.nextInt();
        K = sc.nextInt();
        N_arr = new Jewelry[N];
        K_arr = new int[K];
        pq = new PriorityQueue<>();

        for (int i = 0; i < N; i++) {
            N_arr[i] = new Jewelry(sc.nextInt(), sc.nextInt());
        }

        for (int i = 0; i < K; i++) {
            K_arr[i] = sc.nextInt();
        }

        Arrays.sort(N_arr);
        Arrays.sort(K_arr);

        for (int i = 0, j = 0; i < K; i++) {
            while (true) {
                if (j >= N || N_arr[j].m > K_arr[i]) {
                    break;
                }
                int tmp = N_arr[j++].v;
                pq.add(-tmp);
                //System.out.println(tmp);
            }

            if (!pq.isEmpty()) {
                int tmp = pq.poll();
                answer += Math.abs(tmp);
                //System.out.println(tmp);
            }
        }

        System.out.println(answer);

    }

    public static class Jewelry{
        int m;
        int v;

        public Jewelry(int m, int v) {
            this.m = m;
            this.v = v;
        }
    }

}
