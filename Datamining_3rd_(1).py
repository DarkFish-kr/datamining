import pandas as pd


Fish = pd.read_csv('/Users/jun/Library/Mobile Documents/com~apple~CloudDocs/Github/datamining/Fish_Quality_Data.csv', encoding='utf-8')
Fish

# 문제 1. 연도별 평균 품질 분석
# 연도(Year)별 평균 Body_Fat 과 평균 Quality_Score 를 구하세요. 그리고 어떤 연도에 평균 품질 점수가 가장 높았는지 확인하세요.

import pandas as pd

# 1. 연도별 평균 구하기
yearly_avg = Fish.groupby('Year')[['Body_Fat', 'Quality_Score']].mean()

# 2. 품질 점수를 기준으로 내림차순 정렬하기
sorted_avg = yearly_avg.sort_values(by='Quality_Score', ascending=False)

# 3. 정렬된 데이터의 가장 첫 번째 행의 인덱스(연도) 가져오기
best_year = sorted_avg.index[0]
best_score = sorted_avg.iloc[0]['Quality_Score']

print(f"가장 평균 품질 점수가 높은 연도는 {best_year}년 ({best_score:.2f}점) 입니다.")

# 문제 2. 고품질 여부에 따른 품질 점수 차이
# 고품질(High_Quality=True) 그룹과 비고품질(False) 그룹의 평균 품질 점수를 비교하세요. 어떤 그룹이 평균 점수가 더 높으며, 그 차이는 얼마인가요?

# 1. 고품질 그룹과 비고품질 그룹으로 데이터를 직접 나눔
high_quality_group = Fish[Fish['High_Quality'] == True]
low_quality_group = Fish[Fish['High_Quality'] == False]

# 2. 각각의 평균 구하기
mean_true = high_quality_group['Quality_Score'].mean()
mean_false = low_quality_group['Quality_Score'].mean()

# 3. 차이 계산 및 출력
score_diff = abs(mean_true - mean_false)
print(f"고품질 평균: {mean_true:.2f}점, 비고품질 평균: {mean_false:.2f}점")
print(f"두 그룹의 점수 차이는 {score_diff:.2f}점 입니다.")

# 문제 3. 이상치 시각화
# 체지방률(Body_Fat)과 품질 점수(Quality_Score)의 이상치를 boxplot 으로 시각화하세요. 이상치는 무엇이며, 어떤 값들이 일반 범위를 벗어났나요?

import matplotlib.pyplot as plt

# 1. 시각화 (기본 boxplot)
Fish[['Body_Fat', 'Quality_Score']].plot.box()
plt.title("Boxplot of Body_Fat & Quality_Score")
plt.show()

# 2. Body_Fat의 IQR 계산
Q1 = Fish['Body_Fat'].quantile(0.25)
Q3 = Fish['Body_Fat'].quantile(0.75)
IQR = Q3 - Q1

# 3. 조건에 맞는 이상치 데이터만 추출
condition = (Fish['Body_Fat'] < Q1 - 1.5 * IQR) | (Fish['Body_Fat'] > Q3 + 1.5 * IQR)
body_fat_outliers = Fish[condition]

print("\n[Body_Fat 이상치 데이터]")
print(body_fat_outliers['Body_Fat'])  