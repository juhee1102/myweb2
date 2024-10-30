import streamlit as st


과목 = st.selectbox("과목을 선택하세요",
                    ["확률과 통계",
                     "미분과 적분",
                     "기하와 벡터", "정보"])
st.subheader(f"당신이 선택한 과목은 {과목}입니다.")


won = 0
ch1 = st.checkbox("짜장면(5000원)")
ch2 = st.checkbox("짬뽕(7000원)")
ch3 = st.checkbox("탕수육(15000원)")
if ch1:
    won += 5000
if ch2:
    won += 7000
if ch3:
    won += 15000

st.subheader("선택한 음식의 가격은"+str(won)+"입니다.")



hello = st.button("Hello")
bye = st.button("Bye")

if bye:
    st.write("안녕히가세요~")
else:
    st.write("안녕하세요~")




st.title("🍔title")
st.header("😘😘header")
st.subheader("sub")
st.markdown("markdown")
st.write("write :red[제일작은글씨]")