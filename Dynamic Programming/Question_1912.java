package BaekJoon;

import java.util.Scanner;

public class Question_1912 {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int n = scanner.nextInt();
        int[] arr = new int[n];
        arr[0] = scanner.nextInt();
        int answer = arr[0];
        for (int i = 1; i < n; i++) {
            int s = scanner.nextInt();
            arr[i] = Math.max(arr[i - 1] + s, s);
            answer = Math.max(answer, arr[i]);
        }
        System.out.println(answer);
    }
}