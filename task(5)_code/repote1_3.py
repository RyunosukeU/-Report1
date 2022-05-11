import sys
input = sys.stdin.readline
import time
import bisect

# 品物の個数とナップサックの容量を入力
N, W = map(int, input().split())

# 品物の重さと価値を入力
wv = [list(map(int, input().split())) for _ in range(N)]

# 品物を全て選んだ場合の価値の合計を計算
V = sum(x[1] for x in wv)

# 最小化問題なのでdpテーブルをINFで初期化
# 1 << 60は2**60, pow(2, 60)と同義
INF = 1 << 60

# i行目への遷移はi-1行目のみから行われるため、工夫するとdpテーブルは1行で済む
dp = [INF] * (V + 1)
dp[0] = 0

# 価値jを達成するための最小の重さ = min(dp[j], dp[max(0, j - v)] + w)
start_time = time.perf_counter()
for w, v in wv:
    dp_tmp = dp[:]
    for j in range(1, V + 1):
        # j - vが負の場合は0からの遷移としてよい
        idx_prev = max(0, j - v)
        dp_tmp[j] = min(dp[j], dp[idx_prev] + w)
    dp = dp_tmp
    
end_time = time.perf_counter()
elapsed_time = end_time - start_time

# 重さWで達成できる最大価値を求める
print("合計価格:",bisect.bisect_right(dp, W) - 1)
print("計算時間: ",  elapsed_time)