import pandas as pd
import streamlit as st
import mafld_data
import os
from matplotlib import pyplot as plt
from PIL import Image

HOME = os.getcwd()
IMG_DIR = os.path.join(HOME, 'img', 'new')
DATA_DIR = os.path.join(HOME, 'data')

def page():
    patient_data = pd.read_csv(os.path.join(DATA_DIR, 'patient_data.csv'))
    patient_rules = pd.read_csv(os.path.join(DATA_DIR, 'patient_rules.csv'))
    # title
    col_l, col_r = st.columns([mafld_data.page_col_left_width, mafld_data.page_col_right_width])
    with col_l:
        st.markdown(mafld_data.page_2_main_title)
        st.markdown(mafld_data.page_2_second_title)
        st.markdown(mafld_data.page_2_introduction, unsafe_allow_html=True)
    with col_r:
        st.markdown('👇**请选择患者ID**')
        st.markdown('\n')
        st.markdown('\n')
        id = patient_data['id'].unique()
        patient_ID = st.selectbox(mafld_data.patient_ID_selectbox_title, id)
        year = st.selectbox(mafld_data.page_1_year_selectbox_title,
                            mafld_data.page_1_year_selectbox_options)
         # hotfix，选项单调整为 2017->2018 的模式
        year = int(year.split('->')[1])
    
    data = patient_data.loc[(patient_data['id']==patient_ID) & (patient_data['Year']==year)]
    data.set_index('id', inplace = True)
    data.index.name = 'patient_ID'
    mafld_result = data['MAFLD'].iloc[0]
    
    rule = patient_rules.loc[(patient_data['id']==patient_ID) & (patient_data['Year']==year)]
    rule.set_index('id', inplace = True)
    rule.index.name = 'patient_ID'

    # draw
    # 患者数据
    st.markdown('---')
    st.markdown(mafld_data.page_2_patient_data_title)
    columns_a = ['BMI','WC','Dbp','ALT','Sbp','GGT','ALP','SUC','a1c','BPC']
    columns_b = ['TG','HDL','FBG','TC','WBC','LDL','GFR','CREA', 'HBA1C']
    st.dataframe(data[columns_a], use_container_width=True)
    st.dataframe(data[columns_b], use_container_width=True)
    st.markdown(mafld_data.page_2_patient_data_content)

    # 预测结果
    st.markdown('---')
    st.markdown(mafld_data.page_2_result_title)
    result_str = str(mafld_result) + '  (患病)' if mafld_result else '  (健康)'
    st.markdown('提取的时序规则')
    columns_1 = ['rule_1','rule_2','rule_3','rule_4','rule_5','rule_6']
    columns_2 = ['rule_7','rule_8','rule_9','rule_10','rule_11','rule_12']
    columns_3 = ['rule_13','rule_14','rule_15','rule_16','rule_17','rule_18']
    columns_4 = ['rule_19','rule_20','rule_21','rule_22','rule_23','rule_24']
    columns_5 = ['rule_25','rule_26','rule_27','rule_28','rule_29','rule_30']
    st.dataframe(rule[columns_1], use_container_width=True)
    st.dataframe(rule[columns_2], use_container_width=True)
    st.dataframe(rule[columns_3], use_container_width=True)
    st.dataframe(rule[columns_4], use_container_width=True)
    st.dataframe(rule[columns_5], use_container_width=True)
    st.markdown('**MAFLD** 预测结果：'+result_str)
    st.markdown(mafld_data.page_2_result_content)

    # 模型可解释性分析
    # imgs
    st.markdown('---')
    st.markdown(mafld_data.page_2_explain_title)
    st.markdown(mafld_data.page_2_explain_content)
    st.markdown('群体可解释性')
    img_l, img_r = (
            Image.open(os.path.join(IMG_DIR, str(year)+'年GBM模型特征重要性排序图.jpg')),
            Image.open(os.path.join(IMG_DIR, str(year)+'年GBM模型特征蜂窝图.jpg'))
        )
    img_width = max(img_l.width, img_r.width)
    img_height = max(img_l.height, img_r.height)
    colp2_l, colp2_r = st.columns([1,1])
    with colp2_l:
        img_l.resize((img_width, img_height))
        st.image(img_l, use_column_width='auto',
                 caption=str(year)+'年GBM模型特征重要性排序图')
    with colp2_r:
        img_r.resize((img_width, img_height))
        st.image(img_r, use_column_width='auto',
                 caption=str(year)+'年GBM模型特征蜂窝图')
    # 群体结论
    st.markdown(mafld_data.page_2_group_conclusion)
    st.markdown(mafld_data.page_2_group_conclusion2)
    col1, col2, col3 = st.columns([1,1,1])
    with col2:
        st.markdown('---')
    st.markdown('个体可解释性')
    img = Image.open(os.path.join(IMG_DIR, 
                                  str(year)+'患者'+str(mafld_data.page_2_patient_id_dict[patient_ID])+'的个体解释图.jpg'))
    st.image(img, use_column_width='auto', caption=str(year)+'患者'+str(patient_ID)+'的个体解释图')