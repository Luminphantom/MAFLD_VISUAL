import streamlit as st
import mafld_data
import mafld_page_community
import mafld_page_personal


def sidebar():
    st.sidebar.markdown(mafld_data.sidebar_website_title, unsafe_allow_html=True)
    st.sidebar.markdown(mafld_data.sidebar_website_introduction, unsafe_allow_html=True)
    pass
    st.sidebar.markdown('---')
    option = st.sidebar.selectbox(mafld_data.sidebar_selectbox_choice['caption'],
                                  (mafld_data.sidebar_selectbox_choice['page_community_caption'],
                                   mafld_data.sidebar_selectbox_choice['page_personal_caption'],))
    if option == mafld_data.sidebar_selectbox_choice['page_community_caption']:
        mafld_page_community.page()
    elif option == mafld_data.sidebar_selectbox_choice['page_personal_caption']:
        mafld_page_personal.page()
    st.sidebar.markdown(mafld_data.sidebar_introduction, unsafe_allow_html=True)
    # st.sidebar.markdown(mafld_data.sidebar_team, unsafe_allow_html=True)
    st.sidebar.markdown(' ')
    # st.sidebar.image(mafld_data.sidebar_team_logo, use_column_width='auto')
    # st.sidebar.markdown(mafld_data.sidebar_repos, unsafe_allow_html=True)
