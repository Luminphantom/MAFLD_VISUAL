import streamlit as st

# 网站信息
website_icon = '💠'
website_title = 'TARISMAFLDP专家系统'
sidebar_website_title = '# 💠️ TARISMAFLDP专家系统'
sidebar_website_introduction = '''---
**代谢相关脂肪性肝病**<p>非酒精性脂肪肝(NAFLD)是一种与胰岛素抵抗和遗传易感密切相关的代谢应激性肝损伤，
在此基础上合并代谢功能障碍的组合(包括超重/肥胖、2型糖尿病或其他代谢性疾病)，命名为代谢相关脂肪性肝病(MAFLD)'''
sidebar_selectbox_choice = {'caption': '当前所在',
                            'page_community_caption': '时序关联规则演化分析模块',
                            'page_personal_caption': '患者结局预测模块',
                            'page_develop_team_caption': '系统研究团队'}
sidebar_introduction = '''
---
<h2>项目简介</h2><p>
基于MAFLD风险人群健康体检数据，通过机器学习技术分析和改进MAFLD患者结局预测的准确性与可解释性。
<p>
(A)时序关联规则挖掘模块。挖掘患者的疾病特征之间时序关联规则，为后续患者表示及规则演化分析奠定基础。

(B)时序关联规则演化分析模块。以数据挖掘描述性范式分析时序关联规则的演化规律。

(C)结局预测模型。以数据挖掘预测性分析范式，在模型构建过程中融入挖掘的时序关联规则，补充领域知识以提升模型的准确度和可解释性。
'''

# 公用
page_col_left_width = 3
page_col_right_width = 1
analysis_pattern_selectbox_title = '分析模式'
analysis_pattern_selectbox_options = ['横向', '纵向']

# 页 1
page_1_main_title = '## 时序关联规则演化分析模块'
page_1_second_title = ''
page_1_introduction = '''
本模块针对研究对象的MALFD结局的上升、平稳和下降趋势。
① 将时序关联规则数据转换为元组形式以构建网络演化图；
② 对所构建的网络演化图进行横向和纵向深入挖掘；
③ 总结MALFD结局与时序关联规则在相同时间间隔以及不同时间间隔下的差异及其演化规律。<p>
**横向**模式关注同年所有指标的趋势变化；**纵向**模式关注同趋势下多年指标的变化方式
'''
page_1_year_selectbox_title = '年份'
page_1_year_selectbox_options = ['2017->2018', '2018->2019', '2019->2020']
page_1_trend_selectbox_title = 'MAFLD 特征变化趋势'
page_1_trend_eng_map_dict = {'上升': 'up', '平稳': 'eq', '下降': 'dw'}
page_1_trend_selectbox_options = page_1_trend_eng_map_dict.keys()
page_1_ts_rule_explain_title = '### 时序规则图'
page_1_ts_rule_explain_content = '''
'''
page_1_ts_conclusion = '''
上表从单个疾病指标视角展示了演化趋势，而上图从时序关联规则视角展示了演化趋势。综合二者，可以得到以下结论：

结论一：MAFLD的整体变化趋势与其主要疾病指标的变化呈现一致性。在MAFLD三种趋势中，体格检查为主要疾病指标对应的共有体检项目。MAFLD上升趋势患者的指标以肝功能为主，MAFLD平稳趋势缓则的指标以肾功能为主，MAFLD下降趋势患者的指标以血脂为主。

结论二：临床医护人员更应关注MAFLD上升趋势患者GGT指标的上升变化，平稳趋势患者的GFR指标的波动变化以及下降趋势患者TG指标的下降变化，上述疾病指标的变化可能对控制患者群体MAFLD进展具有重要意义。

结论三：临床医护人员还应关注MAFLD不同变化趋势患者群体疾病指标的联合变化情况，需要注意MAFLD上升趋势患者的$\{ALT\_q_1,GGT\_q_1\}$、$\{WC\_q_1,BMI\_q_1\}$和$\{BMI\_q_1,FBG\_q_1\}$规则的协同变化；MAFLD平稳趋势患者的$\{GFR\_q_3,CREA\_q_1\}$、$\{GFR\_q_1,CREA\_q_3\}$和$\{LDL\_q_3,TC\_q_3\}$规则的协同作用；MAFLD下降趋势患者的$\{TG\_q_3,WC\_q_2\}$、$\{TG\_q_3,GGT\_q_3\}$、$\{TG\_q_3,HDL\_q_1\}$和$\{DBP\_q_3,SBP\_q_3\}$​规则的协同变化。这些时序关联规则可能揭示了不同MAFLD变化趋势患者群体疾病进展的复杂机制。
'''
# 页 2
page_2_main_title = '## 患者结局预测模块'
page_2_second_title = ''
page_2_introduction = '''
本页面将展示患者的主要数据，模型的预测结果、患者的时序关联规则和模型可解释性分析

① 患者体检数据

② 模型提取的时序规则

③ 模型预测结果
'''
patient_ID_selectbox_title = 'ID'
patient_ID_selectbox_options = [None, None]
page_2_patient_data_title = '### 患者数据'
page_2_patient_data_content = '''
'''
page_2_result_title = '### 预测结果'
page_2_result_content = '''

'''
page_2_explain_title = '### 可解释性分析'
page_2_explain_content = '''
'''
page_2_patient_id_dict = {948:1,1763:2,66:3,1:4,2229:5,7052:6,5516:7,2700:8,2247:9,5307:10,5594:11}
page_2_group_conclusion = '''
由左图可以发现TG、BMI和WC对于GBM模型的贡献较大，具有较高的特征重要性，时序关联规则以肾功能和体格检查指标为主，需要
重点关注 $\{GFR\_q_3,CREA\_q_1\}$ 这条时序关联规则，可能表示在诊断患者是否患有MAFLD时应当协同考虑肾脏相关指标，
即MALFD合并慢性肾病人群的风险较高。
'''
page_2_group_conclusion2 = '''
右图颜色越深暗表明该样本点的取值越小，颜色越明亮表明该样本点的取值越大。Shap值越大表示该特征对于模型预测患者得MAFLD的贡献越大，反之对于模型预测患者健康的贡献越大。
对于BMI特征，在shap值为的0右侧样本数值越来越大，在shap为0的左侧样本数值越来越小，这表明BMI特征取值越大时患者越容易患病，即BMI特征是MAFLD的危险因素
对于HDL特征，在shap值为0的左侧样本数值较高，右侧样本数值较低，因此当HDL数值越大时，患者越不容易患MALFD，即可以认为HDL是MAFLD的保护因素
对于Gender特征，在shap值为0的左侧取值为1（表示男性），右侧取值为0（表示女性），即认为相较于男性患者，女性患者更容易得MAFLD，出现此情况的原因是患者人群的平均年龄超过50岁，已有研究也证明50岁以上的女性相较于男性更容易患MAFLD
'''