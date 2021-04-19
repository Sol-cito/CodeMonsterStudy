import java.util.*;

class Solution {
    int N;
    int[][] arr;
    boolean[] visited;
    int answer;

    public static void main(String[] args) {
        Solution s = new Solution();
        int n = 3;
        int[][] computers = {{1, 1, 0}, {1, 1, 0}, {0, 0, 1}};

        s.solution(n, computers);
    }

    public int solution(int n, int[][] computers) {
        N = n;
        arr = computers;
        visited = new boolean[n];
        answer = 0;

        for (int i = 0; i < n; i++) {
            if (!visited[i]) {
                answer++;
                bfs(i);
            }
        }

        //System.out.println(answer);
        return answer;
    }

    public void bfs(int idx) {
        Queue<Integer> queue = new LinkedList<>();
        queue.add(idx);
        visited[idx] = true;

        while (!queue.isEmpty()) {
            int now = queue.remove();
            for (int i = 0; i < N; i++) {
                if (arr[now][i] == 1 && !visited[i]) {
                    queue.add(i);
                    visited[i] = true;
                }
            }
        }
    }

}