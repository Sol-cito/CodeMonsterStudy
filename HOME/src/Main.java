import java.util.*;
import java.io.*;

public class Main {
    static int N;
    static int M;
    static String[] S;
    static String[] arr;
    static Trie root;
    static int answer;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        N = Integer.parseInt(st.nextToken());
        M = Integer.parseInt(st.nextToken());

        S = new String[N];
        for (int i = 0; i < N; i++) {
            st = new StringTokenizer(br.readLine());
            S[i] = st.nextToken();
        }

        arr = new String[M];
        for (int i = 0; i < M; i++) {
            st = new StringTokenizer(br.readLine());
            arr[i] = st.nextToken();
        }

        root = new Trie();

        for (int i = 0; i < N; i++) {
            insert(S[i]);
        }

        answer = 0;

        for (int i = 0; i < M; i++) {
            if (find(arr[i])) {
                answer++;
            }
        }

        System.out.println(answer - 1);

    }

    public static void insert(String word) {
        Trie Node = root;

        for (int i = 0; i < word.length(); i++) {
            char alpha = word.charAt(i);
            int idx = alpha - 'a';

            if (Node.node[idx] == null) {
                Trie tmp = new Trie();
                Node.node[idx] = tmp;
                Node = tmp;
            } else {
                Node = Node.node[idx];
            }
        }

        Node.finish = true;
    }

    public static boolean find(String word) {
        Trie Node = root;

        for (int i = 0; i < word.length(); i++) {
            char alpha = word.charAt(i);
            int idx = alpha - 'a';

            if (Node.node[idx] == null) {
                return false;
            } else {
                Node = Node.node[idx];
            }
        }

        return true;
    }

    public static class Trie {
        Trie[] node;
        boolean finish;

        public Trie() {
            this.node = new Trie[26];
            this.finish = false;
        }
    }

}
