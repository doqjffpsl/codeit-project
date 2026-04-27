#  PINKLUNA AI Marketing Studio

# 프로젝트 보고서 파일_pdf
- [보고서](https://drive.google.com/file/d/102EG_3M4_eLbaRKebhdw2Ad5muDio5Hb/view?usp=drive_link)

---

## 1. 프로젝트 소개

**PINKLUNA AI Marketing Studio**는 실제 소상공인 의류 매장인 *PINKLUNA*의 운영 경험을 바탕으로 기획된 생성형 AI 기반 광고 콘텐츠 자동 생성 서비스입니다.  

사용자는 상품 이미지를 업로드하기만 하면, AI가 이미지의 특징을 분석하고 브랜드 톤에 맞는 광고 문구를 자동으로 생성합니다.

이 프로젝트는 디자인 리소스나 마케팅 경험이 부족한 소상공인이 손쉽게 광고 콘텐츠를 제작할 수 있도록 돕는 것을 목표로 합니다.


---

##  2. 프로젝트 목표

- 생성형 AI를 활용한 실전 서비스 구현
- 이미지 기반 광고 문구 자동 생성 시스템 구축
- 소상공인의 마케팅 제작 비용 및 시간 절감
- 실제 배포 가능한 웹 서비스 경험

---

##  3. 주요 기능

###  1) 상품 이미지 업로드
- 사용자가 상품 이미지를 업로드

###  2) AI 이미지 분석
- OpenAI 모델을 활용하여 이미지 특징 분석
- 상품의 스타일, 특징, 분위기 자동 추출

###  3) 광고 문구 자동 생성
- 선택한 스타일(감성 / 고급 / 귀여움 / 할인 강조 / SNS용)에 맞는 광고 문구 3개 생성

###  4) 실시간 결과 출력
- 상품 설명 + 광고 문구 즉시 확인


---

##  4. 기술 스택

- Python 3.10+
- Streamlit
- OpenAI API (gpt-5-mini)
- Pillow (이미지 처리)
- Base64 Encoding
- dotenv (환경변수 관리)



---

##  5. 프로젝트 구조

project/    
│   
├── app.py                 # 메인 Streamlit 앱    
├── requirements.txt       # 패키지 목록    
├── .env (로컬용)         # API Key 저장    
├── README.md              # 프로젝트 설명    

---

## 6. 실행 방법

### 1 저장소 클론

git clone <repository-url>
cd project-folder

### 2 패키지 설치

pip install -r requirements.txt

### 3 환경 변수 설정 (.env)

프로젝트 루트에 `.env` 파일 생성 후 아래 작성:

OPENAI_API_KEY=본인의_API_KEY

### 4 실행

streamlit run app.py

---

##  7. 배포 링크

 https://codeit-project-gk46kjufbjwgxeau8zsnr6.streamlit.app/

 https://www.pinkluna.shop 
( 2026.04.27 SSL발급 진행중 )

## 서비스 전체 구조

본 서비스는 다음과 같은 구조로 배포되어 있습니다.

 사용자 (브라우저)   
        │    
        ▼   
 pinkluna.shop (커스텀 도메인)    
        │   
        ▼   
 DNS (가비아)   
        │   
        ▼   
 Streamlit Cloud (Frontend + Backend)   
        │   
        ├── 이미지 업로드 처리 (Pillow)   
        ├── UI (Streamlit)    
        │   
        ▼   
 OpenAI API (GPT-5-mini)    
        │   
        ├── 이미지 분석 (상품 특징 추출)    
        └── 광고 문구 생성    
        │   
        ▼   
 결과 반환 (상품 설명 + 광고 카피 3개)    
        │   
        ▼   
사용자 화면 출력    


---  

##  8. 서비스 특징

- 이미지 기반 자동 광고 생성
- 브랜드 톤 선택 가능
- 즉시 결과 확인 가능한 실시간 서비스
- 소상공인 맞춤형 마케팅 자동화

---

##  9. 평가 기준 대응

| 항목 | 설명 |
|------|------|
| 정확도 | 이미지 특징을 기반으로 광고 문구 생성 |
| 일관성 | 선택한 스타일에 따라 문구 톤 유지 |
| 사용성 | 간단한 업로드만으로 결과 생성 |
| UX | 직관적인 Streamlit 인터페이스 |
| 제어 가능성 | 스타일 선택 기능 제공 |

---

##  10. 향후 개선 방향

- 🎨 AI 이미지 생성 기능 추가 (Stable Diffusion / ControlNet)
- 📱 SNS 자동 포맷 생성 (인스타/쇼츠)
- 🧾 상세페이지 자동 생성 기능
- 🗂 생성 결과 저장 및 히스토리 기능
- 🛍 쇼핑몰 연동 기능 확장

---

##  11. 개발 후기

본 프로젝트를 통해 생성형 AI를 실제 서비스 형태로 구현하는 경험을 할 수 있었습니다.

특히 OpenAI API를 활용하여 이미지 분석과 텍스트 생성을 결합함으로써, 단순 모델 사용을 넘어 실제 서비스 구조 설계 경험을 얻었습니다.

또한 Streamlit을 활용한 빠른 웹 서비스 배포를 통해 AI 모델을 실제 사용자에게 제공하는 전체 흐름을 이해할 수 있었습니다.

---

##  12. 결론

PINKLUNA AI Marketing Studio는  
이미지 한 장으로 광고 콘텐츠를 자동 생성하는 AI 마케팅 도구로서,  

소상공인의 콘텐츠 제작 부담을 줄이고 실질적인 마케팅 효율 향상을 목표로 합니다.
