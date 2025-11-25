import streamlit as st
import pandas as pd
import pickle

# ML 모델 로드
model = pickle.load(open("model.pkl", "rb"))

st.title("🎤 공연 위험도 예측 서비스 (AV-HSI Predictor)")

hall = st.selectbox("공연장", ["KSPO DOME", "핸드볼경기장", "올림픽홀", "우리금융아트홀"])
genre = st.selectbox("장르", ["아이돌/댄스/대중가요", '록/밴드/인디', '팝/밴드/재즈', '전자음악/힙합', '갈라', '발라드', '트로트', '인디/어쿠스틱', '뮤지컬/클래식/오케스트라','이벤트/기타' ])
audience = st.slider("관람인원", 0, 110000, 10000, 500)
month = st.selectbox("공연 월", list(range(1, 13)))

if st.button("예측하기"):
    new_data = pd.DataFrame([{
        "공연장": hall,
        "장르": genre,
        "관람인원": audience,
        "MONTH": month
    }])

    pred = model.predict(new_data)[0]

    st.subheader(f"🎯 예측된 AV-HSI: {pred:.2f}")

    if pred >= 81:
        label = "5단계 (위험)"
    elif pred >= 61:
        label = "4단계 (경계)"
    elif pred >= 41:
        label = "3단계 (주의)"
    elif pred >= 21:
        label = "2단계 (괜찮음)"
    else:
        label = "1단계 (안전)"

    st.subheader(f"🚦 위험등급: {label}")
