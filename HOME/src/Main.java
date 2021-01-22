import java.util.*;

public class Main {

    static int N;
    static HashMap<String, Integer> list;
    static String[] tmp;
    static boolean[] visit;
    static int answer;

    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);

        N = sc.nextInt();
        list = new HashMap();
        tmp = new String[N];
        visit = new boolean[N];

        for (int i = 0; i < N; i++) {
            String str = sc.next();
            list.put(str, i);
        }

        for (int i = 0; i < N; i++) {
            tmp[i] = sc.next();
        }

        for (int i = 0; i < N; i++) {
            for (int j = i + 1; j < N; j++) {
                if (list.get(tmp[i]) > list.get(tmp[j])) {
                    answer++;
                    break;
                }
            }
        }

        System.out.println(answer);

    }

}
