import java.util.*;
import java.io.*;

public class Main {
    static int N;
    static int M;
    static int D;
    static int G;
    static int[][] arr;
    static int answer;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        N = Integer.parseInt(st.nextToken());
        M = Integer.parseInt(st.nextToken());
        D = Integer.parseInt(st.nextToken());
        G = 3;

        arr = new int[N + 1][];
        for (int i = 0; i < N; i++) {
            st = new StringTokenizer(br.readLine());
            for (int j = 0; j < M; j++) {
                arr[i][j] = Integer.parseInt(st.nextToken());
            }
        }

        // 3 궁수의 자리를 정한다
        choice();

        System.out.println(answer);

    }

    public static void choice() {

    }

    public static void attack() {

    }

    public static void move() {

    }

    public static void check() {

    }

}
