import streamlit as st

# 网站信息
website_icon = '💠'
website_title = 'IPSMAFLD Decision Support System'
sidebar_website_title = '# 💠️ IPSMAFLD Decision Support System'
sidebar_website_introduction = '''---
<h2>Introduction to MAFLD</h2><p>Nonalcoholic fatty liver disease (NAFLD) is a metabolic stress-induced liver injury closely associated with insulin resistance and genetic susceptibility. 

The disease spectrum encompasses a range of conditions from simple steatosis (NAFL) to nonalcoholic steatohepatitis (NASH), as well as the associated cirrhosis and hepatocellular carcinoma. 

When superimposed with metabolic dysregulation, which includes a combination of overweight/obesity, type 2 diabetes, or other metabolic disorders, the condition is termed Metabolic Associated Fatty Liver Disease (MAFLD).'''
sidebar_selectbox_choice = {'caption': 'Current location',
                            'page_community_caption': 'Temporal Association Rule Evolution Analysis Module',
                            'page_personal_caption': 'Patient Outcome Prediction Module',
                            'page_develop_team_caption': '系统研究团队'}
sidebar_introduction = '''
---
<h2>Project Introduction</h2><p>
Based on health checkup data from the MAFLD risk people, this study utilizes data mining and machine learning techniques to analyze and enhance the accuracy and interpretability of MAFLD patient outcome predictions.
<p>
(A)Temporal Association Rule Mining Module.

(B)Temporal Association Rule Evolution Analysis Module.

(C)Outcome Prediction Model.
'''

# 公用
page_col_left_width = 3
page_col_right_width = 1
analysis_pattern_selectbox_title = 'Analysis Mode'
analysis_pattern_selectbox_options = ['horizontal', 'vertical']

# 页 1
page_1_main_title = '## Temporal Association Rules Evolution Analysis Module'
page_1_second_title = ''
page_1_introduction = '''
The current module is dedicated to analyzing the upward(progression), stable(stability), and downward(revesal) trends of MAFLD outcomes in the research subjects.

① The temporal association rules data is transformed into tuple form to construct an evolutionary network graph.
② An in-depth horizontal and vertical excavation of the constructed evolutionary network graph is conducted.
③ The module summarizes the differences and evolutionary patterns between MAFLD outcomes and temporal association rules across the same and different time intervals. <p>
**horizontal** mode focuses on the trend changes of all indicators in the same year; **vertical** mode focuses on how indicators change over the years in the same trend
'''
page_1_year_selectbox_title = 'Period'
page_1_year_selectbox_options = ['2017->2018', '2018->2019', '2019->2020']
page_1_trend_selectbox_title = 'Trends in MAFLD characteristics'
page_1_trend_eng_map_dict = {' upward': 'up', ' stable': 'eq', ' downward': 'dw'}
page_1_trend_selectbox_options = page_1_trend_eng_map_dict.keys()
page_1_ts_rule_explain_title = '### Temporal Association Rules Plot'
page_1_ts_rule_explain_content = '''
'''
page_1_ts_conclusion = '''
Table 1 presents the evolutionary trends from the perspective of individual disease indicators, while Figures showcase the trends from the perspective of temporal association rules. Integrating both provides the following conclusions:

Conclusion 1: The overall trend of MAFLD changes is consistent with the changes in its main disease indicators. Among the three MAFLD trends, physical examination items are the common health checkup projects corresponding to the main disease indicators. For patients with an upward trend in MAFLD, the indicators are primarily related to liver function; for those with a stable trend, the indicators are mainly related to kidney function; and for patients with a downward trend, the indicators are primarily related to blood lipids.

Conclusion 2: Clinical medical staff should pay more attention to the upward changes in the GGT indicator in patients with an upward trend in MAFLD, the fluctuating changes in the GFR indicator in patients with a stable trend, and the downward changes in the TG indicator in patients with a downward trend. Changes in these disease indicators may be of significant importance for controlling the progression of MAFLD in patient populations.

Conclusion 3: Clinical medical staff should also pay attention to the joint changes in disease indicators in patient populations with different MAFLD trend changes. It is important to monitor the synergistic changes of rules $\{ALT\_q_1,GGT\_q_1\}$、$\{WC\_q_1,BMI\_q_1\}$ and $\{BMI\_q_1,FBG\_q_1\}$ in patients with an upward trend in MAFLD; rules $\{GFR\_q_3,CREA\_q_1\}$、$\{GFR\_q_1,CREA\_q_3\}$ and $\{LDL\_q_3,TC\_q_3\}$ in patients with a stable trend; rules $\{TG\_q_3,WC\_q_2\}$、$\{TG\_q_3,GGT\_q_3\}$、$\{TG\_q_3,HDL\_q_1\}$ and $\{DBP\_q_3,SBP\_q_3\}$ in patients with a downward trend. These temporal association rules may reveal the complex mechanisms underlying the progression of diseases in patient populations with different MAFLD trend changes.
'''
# 页 2
page_2_main_title = '## Patient Outcome Prediction Module'
page_2_second_title = ''
page_2_introduction = '''
This page will present the principal data of the patients, the model's predictive outcomes, the temporal association rules of the patients, and an analysis of the model's interpretability.

① Patient physical checkup data；
② Temporal association rules for model extraction；
③ Model prediction results。
'''
patient_ID_selectbox_title = 'ID'
patient_ID_selectbox_options = [None, None]
page_2_patient_data_title = '### Patient Data'
page_2_patient_data_content = '''
'''
page_2_result_title = '### Prediction Result'
page_2_result_content = '''

'''
page_2_explain_title = '#### Model interpretability analysis'
page_2_explain_content = '''
'''
page_2_patient_id_dict = {948:1,1763:2,66:3,1:4,2229:5,7052:6,5516:7,2700:8,2247:9,5307:10,5594:11}
page_2_group_conclusion = '''
From Figure on the left, it can be observed that TG, BMI, and WC exhibit significant contributions to the GBM model, demonstrating high feature importance. The temporal association rules are primarily based on renal function and physical examination indicators, with a particular focus on the temporal association rule  $\{GFR\_q_3,CREA\_q_1\}$ . This may suggest that when diagnosing whether a patient has MAFLD, it is essential to consider renal-related indicators in conjunction, indicating a higher risk in the population with comorbid MAFLD and chronic kidney disease.
'''
page_2_group_conclusion2 = '''
In the right plot, darker shades indicate lower values for the sample points, while lighter shades signify higher values. A larger Shap value suggests that the feature contributes more significantly to the model's prediction of MAFLD in patients, and conversely, contributes more to the model's prediction of good health.

For the BMI feature, as the Shap value approaches zero from the right side, the sample values increase, and as they approach from the left side, the sample values decrease. This indicates that a higher BMI increases the likelihood of disease, identifying BMI as a risk factor for MAFLD.

Regarding the HDL feature, higher sample values are observed on the left side of the Shap value equals zero, and lower sample values on the right side. Thus, an increased HDL level is associated with a reduced risk of MAFLD, suggesting that HDL may act as a protective factor against MAFLD.

As for the Gender feature, the left side of the Shap value equals zero represents the value 1 (indicating males), and the right side represents the value 0 (indicating females). This implies that females are more susceptible to MAFLD compared to males. The reasoning behind this observation is that the average age of the patient population exceeds 50 years, and existing studies have also shown that postmenopausal women are more prone to MAFLD than men.
'''
