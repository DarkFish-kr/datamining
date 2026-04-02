import matplotlib.font_manager as fm
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns

# 나눔고딕 폰트 설정
font_path = '/usr/share/fonts/truetype/nanum/NanumGothic.ttf'
fm.fontManager.addfont(font_path)
plt.rc('font', family='NanumGothic')
# 폰트 캐시 갱신
fm._load_fontmanager(try_read_cache=False)

Fish = pd.read_csv('/Users/jun/Library/Mobile Documents/com~apple~CloudDocs/Github/datamining/Data folder/fish_growth.csv', encoding='utf-8')
Fish

plt.rc('font', family="NanumGothic")
plt.rcParams['axes.unicode_minus'] = False

plt.title("대한민국")
plt.plot([-1, 2, 3, 4])
plt.show()

year = [2014, 2017, 2020, 2023]
price = [25000, 31000, 53000, 63000]
plt.plot(year, price, 'rd:')

plt.axis([2013, 2024, 20000, 70000])
plt.show()

plt.plot(np.random.randn(10), 'k', label='one')
plt.plot(np.random.randn(10)*3, 'r--', label='two')
plt.plot(np.random.randn(10)*10, 'g.', label='three')

plt.legend()
plt.show()

plt.subplot(2, 2, 1)
plt.plot(np.random.randn(10), 'b--')
plt.subplot(2, 2, 2)
plt.plot(np.random.randn(100), 'r', alpha=0.7)
plt.subplot(2, 2, 3)
plt.plot(np.random.randn(10), 'y')
plt.subplot(2, 2, 4)
plt.plot(np.random.randn(10), 'g.')

year = [2014, 2017, 2020, 2023]
price = [25000, 31000, 53000, 63000]
plt.scatter(year, price, c='g', s=50 , marker='^')
plt.show()

numbers = [5, 4, 4, 1, 6, 3, 4, 1, 2, 2]
plt.hist(numbers, bins=6)
plt.show()

# 한글 폰트 설정 확인
plt.rc('font', family='NanumGothic')
plt.rcParams['axes.unicode_minus'] = False

# 2. 파일 읽어오기
Fish = pd.read_csv('/content/fish_growth.csv', encoding='utf-8')

# 3. 데이터 파악하기
print("--- Data Head ---")
print(Fish.head())

print("\n--- Data Tail ---")
print(Fish.tail())

print("\n--- Descriptive Statistics ---")
print(Fish.describe())

fig = plt.figure(figsize=(10, 6))

# 첫 번째 그래프: 히스토그램
plt.subplot(1, 2, 1) # 1행 2열 중 1번째
plt.hist(Fish['중량'], bins=15)
plt.title('물고기 중량 분포 (Histogram)')
plt.xlabel('중량')
plt.ylabel('빈도')

# 두 번째 그래프: 산점도
plt.subplot(1, 2, 2) # 1행 2열 중 2번째
plt.plot(Fish['수온'], Fish['성장량'], alpha=0.5)
plt.title('수온에 따른 성장량 (Scatter Plot)')
plt.xlabel('수온')
plt.ylabel('성장량')

plt.tight_layout()
plt.show()

# 하나의 그래프에 같이 그리기
plt.figure(figsize=(10,6))

# df 대신 Fish를 사용해야 합니다.
plt.plot(Fish['날짜'], Fish['중량'], 'k--', label='중량')
plt.plot(Fish['날짜'], Fish['성장량'], 'r--', label='성장량')
plt.plot(Fish['날짜'], Fish['수온'], 'g.', label='수온')

plt.title('날짜에 따른 수온, 중량, 성장량 변화')
plt.xlabel('날짜')
plt.ylabel('값')
plt.legend()
plt.grid(True, alpha=0.3)

plt.xticks(rotation=45) # 날짜가 겹치지 않게 회전
plt.show()

numbers = [0, 1.4, 1.6, 1.8, 1.85, 1.9, 2.2, 2.5, 5.7, 9]
plt.boxplot(numbers)
plt.show()

subject = ['KOR', 'ENG', 'MATH']
grade = [85, 76, 55]

plt.title('Report')
plt.xlabel('Subject')
plt.ylabel('grade')

plt.bar(subject, grade)
plt.ylim(0,100)
plt.text(0,90, 'Good!')
plt.show()

example_series = pd.Series([20, 15, 5, 5, 10], index=['Apple', 'Banana', 'Cherry', 'Kiwi', 'Grape'])
plt.pie(example_series, labels=example_series.index, autopct='%.1f%%')
plt.show()