import streamlit as st
import random

# 페이지 기본 설정
st.set_page_config(page_title="오늘의 점심 추천", page_icon="🍽️")

st.title("🍽️ 오늘 뭐 먹지? 점심 메뉴 추천기")
st.write("버튼을 누르면 오늘의 점심 메뉴를 랜덤으로 골라드립니다!")

# 점심 메뉴 리스트
lunch_menus = [
    "김치찌개", "된장찌개", "제육볶음", "돈까스", 
    "초밥", "짜장면", "짬뽕", "수제버거", 
    "쌀국수", "비빔밥", "순대국밥", "크림 파스타",
    "떡볶이 & 튀김", "닭갈비", "칼국수", "마라탕"
]

# 추천 버튼 생성
if st.button("🎲 오늘의 점심 메뉴 추천받기", type="primary"):
    selected_menu = random.choice(lunch_menus)
    st.balloons()
    st.success(f"오늘의 추천 메뉴는 **{selected_menu}**입니다! 맛있게 드세요! 😋")
