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
        st.markdown('👇**Please select patient ID**')
        st.markdown('\n')
        st.markdown('\n')
        id = patient_data['id'].unique()
        patient_ID = st.selectbox(mafld_data.patient_ID_selectbox_title, id)
        year = st.selectbox(mafld_data.page_1_year_selectbox_title,
                            mafld_data.page_1_year_selectbox_options)
        # hotfix，选项单调整为 2017->2018 的模式
        year0, year = year.split('->')
        year0, year = int(year0), int(year)

    data0 = patient_data.loc[(patient_data['id'] == patient_ID) & (patient_data['Year'] == year0)]
    data0.set_index('id', inplace=True)
    data0.index.name = 'patient_ID'
    mafld_result0 = data0['MAFLD'].iloc[0]
    data = patient_data.loc[(patient_data['id'] == patient_ID) & (patient_data['Year'] == year)]
    data.set_index('id', inplace=True)
    data.index.name = 'patient_ID'
    mafld_result = data['MAFLD'].iloc[0]

    rule = patient_rules.loc[(patient_rules['id'] == patient_ID) & (patient_rules['Year'] == year)]
    rule.set_index('id', inplace=True)
    rule.index.name = 'patient_ID'

    # draw
    # 患者数据
    st.markdown('---')
    st.markdown(mafld_data.page_2_patient_data_title)
    col_l, col_r = st.columns([1, 1])
    c1 = ['BMI', 'WC', 'DBP', 'ALT', 'SBP', 'GGT', 'ALP', 'SUC', 'a1c', 'BPC']
    c2 = ['TG', 'HDL', 'FBG', 'HBA1C', 'TC', 'WBC', 'LDL', 'GFR', 'CREA', 'MAFLD']
    with col_l:
        st.markdown('### ' + str(year0))
        st.dataframe(data0[c1], use_container_width=True)
        st.markdown('Continued')
        st.dataframe(data0[c2], use_container_width=True)
    with col_r:
        st.markdown('### ' + str(year))
        st.dataframe(data[c1], use_container_width=True)
        st.markdown('Continued')
        st.dataframe(data[c2], use_container_width=True)

    st.markdown(mafld_data.page_2_patient_data_content)

    # 预测结果
    st.markdown('---')
    st.markdown(mafld_data.page_2_result_title)
    result_str = str(mafld_result) + '  (Illness)' if mafld_result else '  (Health)'
    st.markdown(str(year0)+'->'+str(year)+' Temporal association rules' +' extracted from '+ ' physical checkup user: '+str(patient_ID))
    st.dataframe(rule.dropna(axis=1))
    st.markdown('#### **MAFLD** Prediction Result' )
    if not mafld_result:
        st.markdown('<h5 style="background-color:MediumSeaGreen;">0 (Health)</h5>', unsafe_allow_html=True)
    else:
        st.markdown('<h5 style="background-color:Tomato;">1 (Illness)</h5>', unsafe_allow_html=True)
    st.markdown(mafld_data.page_2_result_content)

    # 模型可解释性分析
    # imgs
    st.markdown('---')
    st.markdown(mafld_data.page_2_explain_title)
    st.markdown(mafld_data.page_2_explain_content)
    st.markdown('**Global Interpretable**')
    img_l, img_r = (
        Image.open(os.path.join(IMG_DIR, str(year) + '年GBM模型特征重要性排序图.jpg')),
        Image.open(os.path.join(IMG_DIR, str(year) + '年GBM模型特征蜂窝图.jpg'))
    )
    img_width = max(img_l.width, img_r.width)
    img_height = max(img_l.height, img_r.height)
    colp2_l, colp2_r = st.columns([1, 1])
    with colp2_l:
        img_l.resize((img_width, img_height))
        st.image(img_l, use_column_width='auto',
                 caption= 'Feature Importance Ranking Plot for the GBM Model in ' + str(year) )
    with colp2_r:
        img_r.resize((img_width, img_height))
        st.image(img_r, use_column_width='auto',
                 caption='Feature Hexbin Plot for the GBM Model in ' + str(year))
    # 群体结论
    st.markdown(mafld_data.page_2_group_conclusion)
    st.markdown(mafld_data.page_2_group_conclusion2)
    col1, col2, col3 = st.columns([1, 1, 1])
    with col2:
        st.markdown('---')
    st.markdown('**Local Interpretable**')
    img = Image.open(os.path.join(IMG_DIR,
                                  str(year) + '患者' + str(
                                      mafld_data.page_2_patient_id_dict[patient_ID]) + '的个体解释图.jpg'))
    st.image(img, use_column_width='auto', caption= ' Individual interpretation chart for the ' + 'patient: ' + str(patient_ID) + ' in ' + str(year))
