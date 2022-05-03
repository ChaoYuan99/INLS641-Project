import pandas as pd
import matplotlib.pyplot as plt


all_cases_df = pd.read_csv('C:/Users/ycapp/Desktop/All_cases_trend.csv')
print(all_cases_df.head())

case_df = pd.DataFrame(all_cases_df)

date = case_df['DATE']
case_count = case_df['CASE_COUNT']
case_count_7_avg = case_df['CASE_COUNT_7DAY_AVG']
print(date)
print(case_count_7_avg)

c = '#76ACF0'
g = [0,194,387,560,773]


plt.figure(figsize=(12, 6))


plt.bar(date, case_count, color = c)
plt.plot(date, case_count_7_avg, color='#0E69F0', linestyle='solid', linewidth='3')
#plt.title('World Daily Increases in Confirmed Cases', size=30)
#plt.xlabel('Days Since 1/22/2020', size=30)
#plt.ylabel('# of Cases', size=30)
plt.legend(['Seven-day Average of New Cases', 'New York City Increase in COVID-19 Cases'], prop={'size': 10}, loc='upper left', frameon=False)
# 标题
plt.title('NYC Daily Increases in Confirmed Cases', size=20)
# 增加刻度信息，默认是数据对应的label，但一般不合适
plt.xticks(g, size = 10)
plt.yticks(size=10)
# 消除刻度线
plt.tick_params(top=False, bottom=False, left=False, right=False)
# 消除部分边框
ax = plt.gca()
ax.spines['top'].set_visible(False)
ax.spines['left'].set_visible(False)
ax.spines['right'].set_visible(False)

# 增加横向辅助线 axh是横线 axv是纵向
plt.axhline(y=10000,color='#E6F1F4',linestyle='solid',lw=1)
plt.axhline(y=20000,color='#E6F1F4',linestyle='solid',lw=1)
plt.axhline(y=30000,color='#E6F1F4',linestyle='solid',lw=1)
plt.axhline(y=40000,color='#E6F1F4',linestyle='solid',lw=1)
plt.axhline(y=50000,color='#E6F1F4',linestyle='solid',lw=1)

plt.show()
