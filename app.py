import streamlit as st
from openai import OpenAI
from PIL import Image
import base64
from io import BytesIO
import os
from dotenv import load_dotenv

load_dotenv(dotenv_path=".env")  # 명시적으로 경로 지정

# API KEY (환경변수에서 가져오기)
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

st.set_page_config(page_title="PINKLUNA AI Marketing Studio", layout="centered")

st.title("PINKLUNA AI Marketing Studio")
st.caption("핑크루나 상품 이미지를 업로드하면 AI가 광고 문구를 자동으로 생성합니다.")

# 이미지 업로드
uploaded_file = st.file_uploader("상품 이미지를 업로드하세요", type=["png", "jpg", "jpeg"])

# 스타일 선택
style = st.selectbox(
    "광고 스타일 선택",
    ["감성", "고급", "귀여움", "할인 강조", "SNS용"]
)

def encode_image(image: Image.Image):
    image = image.convert("RGB")
    buffered = BytesIO()
    image.save(buffered, format="JPEG")
    return base64.b64encode(buffered.getvalue()).decode()

if st.button("광고 문구 생성"):

    if uploaded_file is None:
        st.warning("이미지를 업로드해주세요.")
        st.stop()

    image = Image.open(uploaded_file)
    st.image(image, caption="업로드 이미지", use_container_width=True)

    img_base64 = encode_image(image)

    with st.spinner("AI 분석 중..."):

        # 1 이미지 설명 생성
        description_response = client.responses.create(
            model="gpt-5-mini",
            input=[{
                "role": "user",
                "content": [
                    {
                        "type": "input_text",
                        "text": "이 이미지를 보고 상품의 특징을 자세히 설명해줘."
                    },
                    {
                        "type": "input_image",
                        "image_url": f"data:image/jpeg;base64,{img_base64}"
                    }
                ]
            }]
        )

        description = description_response.output_text

        # 2 광고 문구 생성
        ad_response = client.responses.create(
            model="gpt-5-mini",
            input=f"""
당신은 마케팅 전문가입니다.

다음 상품 설명을 기반으로 {style} 스타일의 광고 문구를 3개 만들어주세요.

상품 설명:
{description}
"""
        )

        ad_text = ad_response.output_text

    st.subheader("상품 분석")
    st.write(description)

    st.subheader("광고 문구")
    st.write(ad_text)
