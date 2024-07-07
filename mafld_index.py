#!/usr/bin/python
# -*- coding: utf-8 -*-
import streamlit as st
import mafld_data
import mafld_sidebar


def main():
    # 初始化页面配置
    st.set_page_config(layout='wide',
                       page_icon=mafld_data.website_icon,
                       page_title=mafld_data.website_title,
                       initial_sidebar_state='auto')
    hide_streamlit_style = '<style>#MainMenu {visibility: hidden;}footer {visibility: hidden;}</style>'
    st.markdown(hide_streamlit_style, unsafe_allow_html=True)
    # 侧边栏
    mafld_sidebar.sidebar()
    # 所有页面由 sidebar 引申出来


if __name__ == '__main__':
    main()
