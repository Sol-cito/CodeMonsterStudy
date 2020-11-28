class Sol:
    def password(self):
        N = str(input())
        if N[0] == '0':
            print(0)
            return
        dp = [1] * (len(N) + 1)
        for i in range(1, len(N)):
            n1 = n2 = 0
            if N[i] != '0': n1 = dp[i]
            if N[i - 1] != '0' and int(N[i - 1: i + 1]) <= 26: n2 = dp[i - 1]
            dp[i + 1] = (n1 + n2) % 1000000
            if dp[i + 1] == 0:
                print(0)
                return
        print(dp[len(N)])


if __name__ == '__main__':
    Sol.password(Sol)
