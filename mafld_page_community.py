import pandas as pd
import streamlit as st
import mafld_data
from matplotlib import pyplot as plt
import os
from PIL import Image

HOME = os.getcwd()
IMG_DIR = os.path.join(HOME, 'img', 'new')
DATA_DIR = os.path.join(HOME, 'data')


def page():
    # title
    col_l, col_r = st.columns([mafld_data.page_col_left_width, mafld_data.page_col_right_width])
    with col_l:
        st.markdown(mafld_data.page_1_main_title)
        st.markdown(mafld_data.page_1_second_title)
        st.markdown(mafld_data.page_1_introduction, unsafe_allow_html=True)
    with col_r:
        st.markdown('👇**请选择合适的时序分析模式**')
        st.markdown('\n')
        st.markdown('\n')
        analysis_pattern = st.selectbox(mafld_data.analysis_pattern_selectbox_title,
                                        mafld_data.analysis_pattern_selectbox_options)
    st.markdown('---')
    if analysis_pattern == '横向':
        horizontal_comparative_analysis()
    elif analysis_pattern == '纵向':
        vertical_comparative_analysis()
    else:
        horizontal_comparative_analysis()
    # 结论
    st.markdown('---')
    st.markdown('### 分析结论')
    conclusion_table_img = Image.open(
        os.path.join(IMG_DIR, 'page_1_conclusion_table.png')
    )
    st.image(conclusion_table_img, use_column_width='auto', caption='表1：MAFLD三种趋势对应的主要疾病指标趋势及其所属体检项目')
    st.markdown('#### 解读')
    st.markdown(mafld_data.page_1_ts_conclusion)



def horizontal_comparative_analysis():
    col_l, col_r = st.columns([mafld_data.page_col_left_width, mafld_data.page_col_right_width])
    with col_r:
        year = st.selectbox(mafld_data.page_1_year_selectbox_title,
                            mafld_data.page_1_year_selectbox_options)
        # hotfix，选项单调整为 2017->2018 的模式
        year = int(year.split('->')[1])
    with col_l:
        st.markdown(mafld_data.page_1_ts_rule_explain_title)
        st.markdown(mafld_data.page_1_ts_rule_explain_content)

    # draw
    col_l, col_m, col_r = st.columns([1, 1, 1])
    trend = list(mafld_data.page_1_trend_eng_map_dict.keys())
    img1, img2, img3 = (
    Image.open(os.path.join(IMG_DIR, mafld_data.page_1_trend_eng_map_dict[trend[0]] + '_' + str(year) + '.png')),
    Image.open(os.path.join(IMG_DIR, mafld_data.page_1_trend_eng_map_dict[trend[1]] + '_' + str(year) + '.png')),
    Image.open(os.path.join(IMG_DIR, mafld_data.page_1_trend_eng_map_dict[trend[2]] + '_' + str(year) + '.png')))
    img_width = max(img1.width, img2.width, img3.width)
    img_height = max(img1.height, img2.height, img3.height)
    with col_l:
        img1 = img1.resize((img_width, img_height))
        st.image(img1, use_column_width='auto',
                 caption=str(year - 1) + '->' + str(year) + ' 特征' + trend[0] + '趋势的时序规则图')
    with col_m:
        img2 = img2.resize((img_width, img_height))
        st.image(img2, use_column_width='auto',
                 caption=str(year - 1) + '->' + str(year) + ' 特征' + trend[1] + '趋势的时序规则图')
    with col_r:
        img3 = img3.resize((img_width, img_height))
        st.image(img3, use_column_width='auto',
                 caption=str(year - 1) + '->' + str(year) + ' 特征' + trend[2] + '趋势的时序规则图')


def vertical_comparative_analysis():
    col_l, col_r = st.columns([mafld_data.page_col_left_width, mafld_data.page_col_right_width])
    with col_r:
        trend_zh = st.selectbox(mafld_data.page_1_trend_selectbox_title,
                                mafld_data.page_1_trend_selectbox_options)
    with col_l:
        st.markdown(mafld_data.page_1_ts_rule_explain_title)
        st.markdown(mafld_data.page_1_ts_rule_explain_content)

    # draw
    col_l, col_m, col_r = st.columns([1, 1, 1])
    trend = mafld_data.page_1_trend_eng_map_dict[trend_zh]
    img1, img2, img3 = (Image.open(os.path.join(IMG_DIR, trend + '_' + str(2018) + '.png')),
                        Image.open(os.path.join(IMG_DIR, trend + '_' + str(2019) + '.png')),
                        Image.open(os.path.join(IMG_DIR, trend + '_' + str(2020) + '.png')))
    img_width = max(img1.width, img2.width, img3.width)
    img_height = max(img1.height, img2.height, img3.height)
    with col_l:
        year = 2018
        img1 = img1.resize((img_width, img_height))
        st.image(img1, use_column_width='auto',
                 caption=str(year - 1) + '->' + str(year) + ' 特征' + trend_zh + '趋势的时序规则图')
    with col_m:
        year = 2019
        img2 = img2.resize((img_width, img_height))
        st.image(img2, use_column_width='auto',
                 caption=str(year - 1) + '->' + str(year) + ' 特征' + trend_zh + '趋势的时序规则图')
    with col_r:
        year = 2020
        img3 = img3.resize((img_width, img_height))
        st.image(img3, use_column_width='auto',
                 caption=str(year - 1) + '->' + str(year) + ' 特征' + trend_zh + '趋势的时序规则图')

