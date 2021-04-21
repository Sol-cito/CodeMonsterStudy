import java.util.*;

class Solution {

    public static void main(String arsg[]) {
        Solution s = new Solution();
        int[] a = {93, 30, 55};
        int[] b = {1, 30, 5};
        System.out.println(s.solution(a, b));
    }

    public int[] solution(int[] progresses, int[] speeds) {
        Queue<Integer> queue = new LinkedList();
        ArrayList<Integer> list = new ArrayList<>();
        int[] answer;

        for (int i = 0; i < progresses.length; i++) {
            int num;
            if ((100 - progresses[i]) % speeds[i] == 0) {
                num = (100 - progresses[i]) / speeds[i];
            } else {
                num = (100 - progresses[i]) / speeds[i] + 1;
            }
            queue.add(num);
        }

        while (!queue.isEmpty()) {
            int cnt = 1;
            int now = queue.poll();
            while (!queue.isEmpty() && now >= queue.peek()) {
                queue.poll();
                cnt++;
            }
            list.add(cnt);
        }

        answer = new int[list.size()];

        for (int i = 0; i < list.size(); i++) {
            answer[i] = list.get(i);
        }

        return answer;
    }
}