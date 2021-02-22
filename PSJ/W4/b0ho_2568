import java.util.*;
import java.io.*;

public class Main {
    static int N;
    static Pair[] arr;
    static int[] list;
    static Pair[] print;
    static boolean[] visit;
    static int cnt;
    static StringBuilder answer;

    public static void main(String[] args) throws IOException {
        answer = new StringBuilder();
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        N = Integer.parseInt(br.readLine());
        arr = new Pair[N];
        list = new int[N];
        print = new Pair[N];
        visit = new boolean[500001];

        if (N == 1) {
            System.out.println(0);
            return;
        }

        for (int i = 0; i < N; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            int a = Integer.parseInt(st.nextToken());
            int b = Integer.parseInt(st.nextToken());
            arr[i] = new Pair(a, b);
            visit[a] = true;
        }

        //왼쪽 전봇대를 기준으로 정렬
        Arrays.sort(arr);

        list[0] = arr[0].y;
        //출력을 위한 배열을 추가
        print[0] = new Pair(0, arr[0].x);
        int j = 0;
        for (int i = 1; i < N; i++) {
            if (list[j] < arr[i].y) {
                j++;
                list[j] = arr[i].y;
                print[i] = new Pair(j, arr[i].x);
            } else {
                int lb = lowerBound(0, j, arr[i].y);
                list[lb] = arr[i].y;
                print[i] = new Pair(lb, arr[i].x);
                cnt++;
            }
        }

        answer.append(cnt + "\n");

        for (int i = N - 1; i >= 0; i--) {
            if (print[i].x == j) {
                visit[print[i].y] = false;
                j--;
            }
        }

        for (int i = 0; i <= 500000; i++) {
            if (visit[i]) {
                answer.append(i + "\n");
            }
        }

        System.out.print(answer);
    }

    public static int lowerBound(int start, int end, int target) {
        while (start < end) {
            int mid = (start + end) / 2;

            if (list[mid] >= target) {
                end = mid;
            } else {
                start = mid + 1;
            }
        }

        return end;
    }

    public static class Pair implements Comparable<Pair> {
        int x;
        int y;

        Pair(int x, int y) {
            this.x = x;
            this.y = y;
        }

        @Override
        public int compareTo(Pair a) {
            return this.x - a.x;
        }
    }

}
