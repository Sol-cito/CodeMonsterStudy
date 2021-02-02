import java.util.*;
import java.io.*;

public class Main {
    static int T;
    static int N;
    static int[] arr;
    static int answer;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        T = Integer.parseInt(st.nextToken());

        while (T-- > 0) {
            answer = 0;
            st = new StringTokenizer(br.readLine());
            N = Integer.parseInt(st.nextToken());
            arr = new int[N];

            for (int i = 0; i < N; i++) {
                st = new StringTokenizer(br.readLine());
                arr[i] = Integer.parseInt(st.nextToken());
            }



            System.out.println(answer);
        }

    }

}
