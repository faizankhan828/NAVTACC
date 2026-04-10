import pandas as pd
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Patch

df = pd.read_csv('data/Titanic.csv')

# Q1: Line Chart - PassengerId vs Fare
plt.figure(figsize=(12, 6))
plt.plot(df['PassengerId'], df['Fare'], linewidth=1.5, color='steelblue', alpha=0.7)
plt.title('Fare Monitoring Across Passengers', fontsize=14, fontweight='bold')
plt.xlabel('Passenger ID', fontsize=12)
plt.ylabel('Fare ($)', fontsize=12)
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.savefig('Q1_line_chart_passengerId_vs_fare.png', dpi=300, bbox_inches='tight')
plt.close()

# Q2: Line Chart - Age vs Fare
df_age = df.dropna(subset=['Age', 'Fare']).sort_values('Age')
plt.figure(figsize=(12, 6))
plt.plot(df_age['Age'], df_age['Fare'], linewidth=1.5, color='coral', alpha=0.7)
plt.title('Ticket Prices Trend: Age vs Fare', fontsize=14, fontweight='bold')
plt.xlabel('Age (years)', fontsize=12)
plt.ylabel('Fare ($)', fontsize=12)
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.savefig('Q2_line_chart_age_vs_fare.png', dpi=300, bbox_inches='tight')
plt.close()

# Q3: Bar Chart - Passengers by Class
pclass = df['Pclass'].value_counts().sort_index()
plt.figure(figsize=(10, 6))
bars = plt.bar(pclass.index, pclass.values, color=['#1f77b4', '#ff7f0e', '#2ca02c'], edgecolor='black')
plt.title('Passenger Count by Class', fontsize=14, fontweight='bold')
plt.xlabel('Passenger Class', fontsize=12)
plt.ylabel('Number of Passengers', fontsize=12)
plt.xticks([1, 2, 3], ['1st Class', '2nd Class', '3rd Class'])
for bar in bars:
    plt.text(bar.get_x() + bar.get_width()/2., bar.get_height(), f'{int(bar.get_height())}', ha='center', va='bottom', fontweight='bold')
plt.tight_layout()
plt.savefig('Q3_bar_chart_pclass_distribution.png', dpi=300, bbox_inches='tight')
plt.close()

# Q4: Grouped Bar Chart - Survival by Gender
surv = pd.crosstab(df['Sex'], df['Survived'], normalize='index') * 100
x = np.arange(len(surv.index))
width = 0.35
plt.figure(figsize=(10, 6))
bars1 = plt.bar(x - width/2, surv[0], width, label='Did Not Survive', color='#d62728', edgecolor='black')
bars2 = plt.bar(x + width/2, surv[1], width, label='Survived', color='#2ca02c', edgecolor='black')
plt.title('Survival Rate by Gender', fontsize=14, fontweight='bold')
plt.xlabel('Gender', fontsize=12)
plt.ylabel('Percentage (%)', fontsize=12)
plt.xticks(x, surv.index)
plt.legend(fontsize=11)
plt.grid(True, axis='y', alpha=0.3)
for bars in [bars1, bars2]:
    for bar in bars:
        plt.text(bar.get_x() + bar.get_width()/2., bar.get_height(), f'{bar.get_height():.1f}%', ha='center', va='bottom', fontsize=10)
plt.tight_layout()
plt.savefig('Q4_grouped_bar_chart_sex_vs_survived.png', dpi=300, bbox_inches='tight')
plt.close()

# Q5: Histogram - Age Distribution
plt.figure(figsize=(10, 6))
plt.hist(df['Age'].dropna(), bins=30, color='skyblue', edgecolor='black')
plt.title('Age Distribution of Passengers', fontsize=14, fontweight='bold')
plt.xlabel('Age (years)', fontsize=12)
plt.ylabel('Frequency', fontsize=12)
plt.grid(True, axis='y', alpha=0.3)
plt.tight_layout()
plt.savefig('Q5_histogram_age_distribution.png', dpi=300, bbox_inches='tight')
plt.close()

# Q6: Histogram - Fare Distribution
plt.figure(figsize=(10, 6))
plt.hist(df['Fare'].dropna(), bins=40, color='lightcoral', edgecolor='black')
plt.title('Fare Distribution of Passengers', fontsize=14, fontweight='bold')
plt.xlabel('Fare ($)', fontsize=12)
plt.ylabel('Frequency', fontsize=12)
plt.grid(True, axis='y', alpha=0.3)
plt.tight_layout()
plt.savefig('Q6_histogram_fare_distribution.png', dpi=300, bbox_inches='tight')
plt.close()

# Q7: Scatter Plot - Age vs Fare
df_scatter = df.dropna(subset=['Age', 'Fare'])
plt.figure(figsize=(10, 6))
plt.scatter(df_scatter['Age'], df_scatter['Fare'], alpha=0.5, s=40, color='steelblue', edgecolors='black', linewidth=0.5)
plt.title('Age vs Fare Relationship', fontsize=14, fontweight='bold')
plt.xlabel('Age (years)', fontsize=12)
plt.ylabel('Fare ($)', fontsize=12)
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.savefig('Q7_scatter_plot_age_vs_fare.png', dpi=300, bbox_inches='tight')
plt.close()

# Q8: Scatter Plot - Age vs Fare (colored by survival)
plt.figure(figsize=(11, 6))
colors = ['red' if x == 0 else 'green' for x in df_scatter['Survived']]
plt.scatter(df_scatter['Age'], df_scatter['Fare'], c=colors, alpha=0.5, s=40, edgecolors='black', linewidth=0.5)
plt.legend(handles=[Patch(facecolor='red', edgecolor='black', label='Did Not Survive'), Patch(facecolor='green', edgecolor='black', label='Survived')], fontsize=11, loc='upper right')
plt.title('Survival Analysis: Age vs Fare', fontsize=14, fontweight='bold')
plt.xlabel('Age (years)', fontsize=12)
plt.ylabel('Fare ($)', fontsize=12)
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.savefig('Q8_scatter_plot_advanced_survival.png', dpi=300, bbox_inches='tight')
plt.close()

# Q9: Pie Chart - Survival Ratio
surv_count = df['Survived'].value_counts().sort_index()
plt.figure(figsize=(9, 7))
plt.pie(surv_count, labels=['Did Not Survive', 'Survived'], autopct='%1.1f%%', colors=['#ff9999', '#99ff99'], explode=(0.05, 0.05), startangle=90, textprops={'fontsize': 11, 'weight': 'bold'})
plt.title('Survival Rate Overview', fontsize=14, fontweight='bold')
plt.tight_layout()
plt.savefig('Q9_pie_chart_survival_ratio.png', dpi=300, bbox_inches='tight')
plt.close()

# Q10: Pie Chart - Class Distribution
pclass_dist = df['Pclass'].value_counts().sort_index()
plt.figure(figsize=(9, 7))
plt.pie(pclass_dist, labels=['1st Class', '2nd Class', '3rd Class'], autopct='%1.1f%%', colors=['#FFD700', '#C0C0C0', '#CD7F32'], explode=(0.05, 0.05, 0.05), startangle=90, textprops={'fontsize': 11, 'weight': 'bold'})
plt.title('Passenger Class Distribution (Market Share)', fontsize=14, fontweight='bold')
plt.tight_layout()
plt.savefig('Q10_pie_chart_pclass_distribution.png', dpi=300, bbox_inches='tight')
plt.close()

# Q11: Box Plot - Fare by Class
df_fare = df.dropna(subset=['Fare'])
plt.figure(figsize=(10, 6))
bp = plt.boxplot([df_fare[df_fare['Pclass'] == i]['Fare'].values for i in [1, 2, 3]], tick_labels=['1st Class', '2nd Class', '3rd Class'], patch_artist=True)
for patch, color in zip(bp['boxes'], ['#1f77b4', '#ff7f0e', '#2ca02c']):
    patch.set_facecolor(color)
    patch.set_alpha(0.7)
plt.title('Fare Distribution by Passenger Class (Outlier Detection)', fontsize=14, fontweight='bold')
plt.xlabel('Passenger Class', fontsize=12)
plt.ylabel('Fare ($)', fontsize=12)
plt.grid(True, axis='y', alpha=0.3)
plt.tight_layout()
plt.savefig('Q11_box_plot_fare_by_class.png', dpi=300, bbox_inches='tight')
plt.close()

# Q12: Box Plot - Age by Gender
df_age_box = df.dropna(subset=['Age'])
plt.figure(figsize=(10, 6))
bp = plt.boxplot([df_age_box[df_age_box['Sex'] == 'male']['Age'].values, df_age_box[df_age_box['Sex'] == 'female']['Age'].values], tick_labels=['Male', 'Female'], patch_artist=True)
for patch, color in zip(bp['boxes'], ['#1f77b4', '#ff7f0e']):
    patch.set_facecolor(color)
    patch.set_alpha(0.7)
plt.title('Age Distribution by Gender', fontsize=14, fontweight='bold')
plt.xlabel('Gender', fontsize=12)
plt.ylabel('Age (years)', fontsize=12)
plt.grid(True, axis='y', alpha=0.3)
plt.tight_layout()
plt.savefig('Q12_box_plot_age_by_gender.png', dpi=300, bbox_inches='tight')
plt.close()

# Q13: Heatmap - Correlation Matrix
corr = df[['PassengerId', 'Survived', 'Pclass', 'Age', 'SibSp', 'Parch', 'Fare']].corr()
plt.figure(figsize=(10, 8))
im = plt.imshow(corr, cmap='coolwarm', aspect='auto', vmin=-1, vmax=1)
cols = ['PassengerId', 'Survived', 'Pclass', 'Age', 'SibSp', 'Parch', 'Fare']
plt.xticks(range(len(cols)), cols, rotation=45, ha='right')
plt.yticks(range(len(cols)), cols)
plt.colorbar(im, label='Correlation Coefficient')
for i in range(len(cols)):
    for j in range(len(cols)):
        plt.text(j, i, f'{corr.iloc[i, j]:.2f}', ha="center", va="center", color="black", fontsize=9)
plt.title('Correlation Matrix Heatmap', fontsize=14, fontweight='bold', pad=20)
plt.tight_layout()
plt.savefig('Q13_heatmap_correlation_matrix.png', dpi=300, bbox_inches='tight')
plt.close()

# Q14: Stacked Area Chart - Survival by Class
surv_class = pd.crosstab(df['Pclass'], df['Survived']).sort_index()
plt.figure(figsize=(10, 6))
plt.stackplot(surv_class.index, surv_class[0], surv_class[1], labels=['Did Not Survive', 'Survived'], colors=['#ff9999', '#99ff99'], alpha=0.8)
plt.title('Stacked Area Chart: Survival Trend Across Classes', fontsize=14, fontweight='bold')
plt.xlabel('Passenger Class', fontsize=12)
plt.ylabel('Number of Passengers', fontsize=12)
plt.xticks([1, 2, 3], ['1st Class', '2nd Class', '3rd Class'])
plt.legend(loc='upper left', fontsize=11)
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.savefig('Q14_stacked_area_chart_class_survival.png', dpi=300, bbox_inches='tight')
plt.close()

# Q15: Combined Dashboard - Histogram and Scatter
fig, axes = plt.subplots(1, 2, figsize=(14, 5))
axes[0].hist(df['Age'].dropna(), bins=30, color='skyblue', edgecolor='black')
axes[0].set_title('Age Distribution of Passengers', fontsize=12, fontweight='bold')
axes[0].set_xlabel('Age (years)', fontsize=11)
axes[0].set_ylabel('Frequency', fontsize=11)
axes[0].grid(True, axis='y', alpha=0.3)

colors_scatter = ['red' if x == 0 else 'green' for x in df_scatter['Survived']]
axes[1].scatter(df_scatter['Age'], df_scatter['Fare'], c=colors_scatter, alpha=0.5, s=40, edgecolors='black', linewidth=0.5)
axes[1].set_title('Age vs Fare (Colored by Survival)', fontsize=12, fontweight='bold')
axes[1].set_xlabel('Age (years)', fontsize=11)
axes[1].set_ylabel('Fare ($)', fontsize=11)
axes[1].grid(True, alpha=0.3)
axes[1].legend(handles=[Patch(facecolor='red', edgecolor='black', label='Did Not Survive'), Patch(facecolor='green', edgecolor='black', label='Survived')], fontsize=10)

fig.suptitle('Titanic Dataset: Combined Dashboard Visualization', fontsize=15, fontweight='bold', y=1.02)
plt.tight_layout()
plt.savefig('Q15_combined_visualization_dashboard.png', dpi=300, bbox_inches='tight')
plt.close()

print("✓ All 15 visualizations generated successfully!")
