import datetime
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

# 現在日を取得
dt_now = datetime.datetime.now()
dt_now_ymd = datetime.datetime(dt_now.year, dt_now.month, dt_now.day)

# 誕生日を入力し変数にセット
yyyy = int(input("Your Birthday Year (19xx or 20xx): "))
mm = int(input("Your Birthday Month (1-12): "))
dd = int(input("Your Birthday Day (1-31): "))
dt_bd = datetime.datetime(year=yyyy, month=mm, day=dd)
# 2000年4月1日生まれのテスト
#dt_bd = datetime.datetime(2000, 4, 1)

# 誕生日から現在日までの日数を計算
dt_diff = dt_now_ymd - dt_bd
dt_diff_days = dt_diff.days

# グラフ開始日 2日前
dt_start_delta = 2
# グラフ終了日 30日前
dt_end_delta = 30

# グラフの描画開始日
dt_start = dt_now_ymd - datetime.timedelta(days=dt_start_delta)
# グラフの描画終了日 30日後まで
dt_end = dt_now_ymd + datetime.timedelta(days=dt_end_delta)
# グラフの描画範囲
dt_range = dt_end - dt_start  + datetime.timedelta(days=1)

# データ生成
dates = [dt_start + datetime.timedelta(days=i) for i in range(dt_range.days)]
# 身体(Physical)
vals1 = [np.sin(2 * np.pi * (i + dt_diff_days - dt_start_delta) / 23) for i in range(dt_range.days)]
# 感情(Sensitivity)
vals2 = [np.sin(2 * np.pi * (i + dt_diff_days - dt_start_delta) / 28) for i in range(dt_range.days)]
# 知性(Intellectual)
vals3 = [np.sin(2 * np.pi * (i + dt_diff_days - dt_start_delta) / 33) for i in range(dt_range.days)]

# アスペクト比を縦1横2とする
plt.figure(figsize=plt.figaspect(0.5))

# グラフにプロット
ax = plt.subplot()
ax.plot(dates, vals1, color='red')
ax.plot(dates, vals2, color='green')
ax.plot(dates, vals3, color='blue')

# X軸フォーマット
xfmt = mdates.DateFormatter('%m/%d')
# X軸間隔を日付とする
xloc = mdates.DayLocator()
# 日付表示を90度ローテーション
ax.xaxis.set_tick_params(rotation=90)
# 日付を目盛りとする
ax.xaxis.set_major_locator(xloc)
# フォーマット設定
ax.xaxis.set_major_formatter(xfmt)

# 注釈
# 1日目の位置に体力
ax.text(dt_start + datetime.timedelta(days=1), 1.2, 'Physical', color='red')
# 5日目の位置に感情
ax.text(dt_start + datetime.timedelta(days=5), 1.2, 'Sensitivity', color='green')
# 9日目の位置に知性
ax.text(dt_start + datetime.timedelta(days=9), 1.2, 'Intellectual', color='blue')

# X軸の開始と終了
ax.set_xlim(dt_start, dt_end)
# グリッド表示
ax.grid(True)
# グラフ画像保存
plt.savefig('my-biorhythm.png')
# # グラフ出力
plt.show()
