import java.util.*;
import java.io.*;

public class Main {
    static int T;
    static int N;
    static String[] S;
    static Trie root;
    static String[] answer;

    public static void main(String[] args) throws IOException {
        StringBuilder sb = new StringBuilder();
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        T = Integer.parseInt(br.readLine());
        answer = new String[T];

        while (T-- > 0) {
            answer[T] = "YES";
            root = new Trie();
            N = Integer.parseInt(br.readLine());
            S = new String[N];

            for (int i = 0; i < N; i++) {
                S[i] = br.readLine();
            }

            for (int i = 0; i < N; i++) {
                if (answer[T].equals("YES")) {
                    insert(S[i]);
                    System.out.println();
                }
            }

            sb.append(answer[T] + "\n");
        }

        System.out.println(sb.toString());
    }

    public static void insert(String word) {
        Trie Node = root;

        for (int i = 0; i < word.length(); i++) {
            char alpha = word.charAt(i);
            int idx = alpha - 48;
            System.out.print(idx);

            if (Node.finish) {
                answer[T] = "NO";
                return;
            } else if (Node.node[idx] == null) {
                Node.node[idx] = new Trie();
            }

            Node = Node.node[idx];
        }

        Node.finish = true;
    }

    public static class Trie {
        Trie[] node;
        boolean finish;

        public Trie() {
            this.node = new Trie[10];
            this.finish = false;
        }
    }

}
