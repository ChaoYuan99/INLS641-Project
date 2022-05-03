import pandas as pd
import matplotlib.pyplot as plt

all_death_df = pd.read_csv('C:/Users/ycapp/Desktop/All_cases_trend.csv')
print(all_death_df.head())

case_df = pd.DataFrame(all_death_df)

date = case_df['DATE']
death_count = case_df['DEATH_COUNT']
death_count_7_avg = case_df['DEATH_COUNT_7DAY_AVG']
print(date)
print(death_count_7_avg)

c = 'grey'
g = [0,194,387,560,773]


plt.figure(figsize=(12, 6))


plt.bar(date, death_count, color = c)
plt.plot(date, death_count_7_avg, color='black', linestyle='solid', linewidth='3')
#plt.title('World Daily Increases in Confirmed Cases', size=30)
#plt.xlabel('Days Since 1/22/2020', size=30)
#plt.ylabel('# of Cases', size=30)
plt.legend(['Seven-day Average of Deaths', 'New York City Increase in Deaths'], prop={'size': 10}, loc='upper right', frameon=False)
# 标题
plt.title('NYC Daily Increases in Deaths', size=20)
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

plt.axhline(y=100,color='#E6F1F4',linestyle='solid',lw=1)
plt.axhline(y=200,color='#E6F1F4',linestyle='solid',lw=1)
plt.axhline(y=300,color='#E6F1F4',linestyle='solid',lw=1)
plt.axhline(y=400,color='#E6F1F4',linestyle='solid',lw=1)
plt.axhline(y=500,color='#E6F1F4',linestyle='solid',lw=1)
plt.axhline(y=600,color='#E6F1F4',linestyle='solid',lw=1)



plt.show()
