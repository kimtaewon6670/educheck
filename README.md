# EduCheck

객관식 문제은행 기반 학습 취약도 분석 및 맞춤형 문제 추천 시스템

---

## 1. 프로젝트 개요

EduCheck는 문제은행에 등록된 객관식 문제를 학습자가 풀고, 자동 채점 결과와 풀이 시간을 기반으로 학습자의 취약 영역을 분석하는 로컬 데스크톱 앱이다.

본 시스템은 어휘, 문법, 독해 유형의 문제 풀이 데이터를 수집하고, 정답률, 오답률, 평균 풀이 시간을 분석하여 취약 유형과 취약 세부단원을 도출한다. 이후 분석 결과를 바탕으로 취약 영역의 출제 비중을 높인 맞춤형 문제 세트를 제공한다.

외부 LLM API나 서버를 사용하지 않으며, 모든 문제 데이터와 학습 기록은 로컬 SQLite 데이터베이스에 저장된다.

---

## 2. 개발 목적

기존의 단순 문제 풀이 시스템은 사용자가 어떤 영역에서 취약한지 구체적으로 파악하기 어렵다.

본 프로젝트는 문제 풀이 결과를 단순 점수로만 제공하는 것이 아니라, 문제 유형, 세부단원, 난이도, 풀이 시간 데이터를 함께 분석하여 학습자가 어느 부분을 우선적으로 복습해야 하는지 확인할 수 있도록 한다.

이를 통해 학습자는 자신의 취약 영역을 파악하고, 시스템이 생성한 맞춤형 문제 세트를 통해 부족한 영역을 반복 학습할 수 있다.

---

## 3. 주요 기능

### 3.1 문제은행 관리 기능

- 객관식 문제 등록
- 문제 유형 설정
  - 어휘
  - 문법
  - 독해
- 세부단원 설정
- 난이도 설정
  - 쉬움
  - 보통
  - 어려움
- 보기 1~4번 입력
- 정답 설정
- 해설 입력
- 문제 목록 조회
- 문제 검색 및 필터링
- 문제 수정
- 문제 비활성화

---

### 3.2 학습자 진단 문제 풀이 기능

- 진단 문제 시작
- 난이도 선택
- 선택한 난이도 기준 문제 출제
- 어휘, 문법, 독해 유형이 균형 있게 포함된 문제 세트 생성
- 기본 10문제 제공
- 객관식 답안 선택
- 문제별 풀이 시간 측정
- 문제 제출

---

### 3.3 맞춤형 문제 풀이 기능

- 이전 풀이 기록 기반 맞춤형 문제 세트 생성
- 정답률이 낮은 문제 유형의 출제 비중 증가
- 오답률이 높은 세부단원의 출제 비중 증가
- 선택한 난이도 안에서 맞춤형 문제 생성
- 맞춤형 문제 풀이
- 추천 사유 표시

예시:

```text
문법 유형의 정답률이 가장 낮아 다음 문제 세트에서 문법 문제 비중을 높였습니다.
```

---

### 3.4 자동 채점 기능

- 학습자 답안과 정답 비교
- 정답 / 오답 판정
- 총 문항 수 계산
- 정답 수 계산
- 오답 수 계산
- 점수 계산
- 정답률 계산
- 문항별 채점 결과 표시
- 해설 제공

---

### 3.5 학습 기록 저장 기능

- 풀이 세션 저장
- 문항별 풀이 기록 저장
- 선택 답안 저장
- 정답 여부 저장
- 풀이 시간 저장
- 풀이 일시 저장
- 최근 풀이 결과 저장
- 이전 학습 기록 조회

---

### 3.6 학습 분석 기능

- 전체 정답률 분석
- 문제 유형별 정답률 / 오답률 분석
  - 어휘
  - 문법
  - 독해
- 세부단원별 정답률 / 오답률 분석
- 난이도별 정답률 분석
- 난이도 내 유형별 정답률 분석
- 평균 풀이 시간 분석
- 정답률과 오답률 기반 취약 영역 판단
- 취약 영역 TOP 3 추출

---

### 3.7 오답 복습 기능

- 오답 목록 조회
- 오답 다시 풀기
- 오답 재풀이 결과 저장
- 오답 회복률 확인

---

### 3.8 대시보드 기능

- 총 풀이 문제 수 표시
- 평균 정답률 표시
- 최근 점수 표시
- 취약 유형 TOP 3 표시
- 최근 점수 추이 그래프
- 유형별 분석 그래프
- 세부단원별 분석 그래프
- 추천 학습 방향 표시

---

### 3.9 학습 리포트 기능

- 풀이 결과 기반 리포트 생성
- 점수, 정답률, 취약 유형, 취약 세부단원 표시
- 추천 학습 방향 제공
- 템플릿 기반 피드백 문장 생성
- 외부 LLM API 미사용

---

## 4. 기술 스택

| 구분 | 기술 |
|---|---|
| Language | Python |
| UI / View | PySide6 |
| Database | SQLite |
| Data Analysis | pandas |
| Visualization | matplotlib |
| Architecture | MVC Pattern |
| Packaging | PyInstaller |
| Version Control | Git / GitHub |

---

## 5. 시스템 구조

본 프로젝트는 MVC 구조를 기반으로 개발한다.

```text
View
→ Controller
→ Service
→ Repository
→ SQLite DB
```

### 5.1 MVC 구성

| 구성요소 | 역할 |
|---|---|
| Model | 문제 데이터, 풀이 세션, 답안 기록, 분석 데이터 구조 관리 |
| View | PySide6 기반 화면 표시 및 사용자 입력 처리 |
| Controller | 사용자 요청 처리 및 기능 흐름 제어 |
| Service | 자동 채점, 학습 분석, 맞춤형 문제 세트 생성 등 핵심 로직 처리 |
| Repository | SQLite 데이터베이스 접근 및 CRUD 처리 |

---

## 6. 프로젝트 폴더 구조

```text
educheck/
│
├─ main.py
├─ requirements.txt
├─ README.md
│
├─ app/
│  ├─ models/
│  │  ├─ question_model.py
│  │  ├─ quiz_session_model.py
│  │  └─ answer_log_model.py
│  │
│  ├─ views/
│  │  ├─ main_window.py
│  │  ├─ dashboard_view.py
│  │  ├─ question_manage_view.py
│  │  ├─ quiz_view.py
│  │  ├─ result_view.py
│  │  ├─ analysis_view.py
│  │  └─ wrong_answer_view.py
│  │
│  ├─ controllers/
│  │  ├─ main_controller.py
│  │  ├─ question_controller.py
│  │  ├─ quiz_controller.py
│  │  ├─ analysis_controller.py
│  │  └─ wrong_answer_controller.py
│  │
│  ├─ services/
│  │  ├─ grading_service.py
│  │  ├─ analysis_service.py
│  │  ├─ recommendation_service.py
│  │  └─ report_service.py
│  │
│  ├─ repositories/
│  │  ├─ db.py
│  │  ├─ question_repository.py
│  │  ├─ quiz_session_repository.py
│  │  └─ answer_log_repository.py
│  │
│  └─ utils/
│     ├─ constants.py
│     ├─ validators.py
│     └─ chart_util.py
│
├─ data/
│  └─ .gitkeep
│
└─ docs/
   ├─ images/
   │  └─ dashboard_mockup.png
   ├─ requirements.md
   ├─ erd.md
   ├─ usecase.md
   ├─ sequence.md
   └─ test_case.md
```

---

## 7. 데이터베이스 주요 테이블

### 7.1 questions

문제은행 데이터를 저장하는 테이블이다.

| 컬럼 | 설명 |
|---|---|
| question_id | 문제 고유 ID |
| category | 문제 유형 |
| unit | 세부단원 |
| difficulty | 난이도 |
| question_text | 문제 내용 |
| option_1 | 보기 1 |
| option_2 | 보기 2 |
| option_3 | 보기 3 |
| option_4 | 보기 4 |
| correct_answer | 정답 |
| explanation | 해설 |
| is_active | 문제 활성화 여부 |
| created_at | 등록일 |

---

### 7.2 quiz_sessions

한 번의 문제 풀이 기록을 저장하는 테이블이다.

| 컬럼 | 설명 |
|---|---|
| session_id | 풀이 세션 ID |
| quiz_type | 진단 문제 / 맞춤형 문제 / 오답 복습 |
| difficulty | 선택 난이도 |
| started_at | 풀이 시작 시간 |
| ended_at | 풀이 종료 시간 |
| total_count | 전체 문항 수 |
| correct_count | 정답 수 |
| wrong_count | 오답 수 |
| score | 점수 |
| accuracy | 정답률 |

---

### 7.3 answer_logs

문항별 풀이 결과를 저장하는 테이블이다.

| 컬럼 | 설명 |
|---|---|
| answer_id | 답안 기록 ID |
| session_id | 풀이 세션 ID |
| question_id | 문제 ID |
| selected_answer | 학습자가 선택한 답 |
| correct_answer | 정답 |
| is_correct | 정답 여부 |
| solving_time | 풀이 시간 |
| answered_at | 답안 제출 시간 |

---

### 7.4 analysis_results

학습 분석 결과를 저장하는 테이블이다.

| 컬럼 | 설명 |
|---|---|
| analysis_id | 분석 결과 ID |
| analysis_type | 유형 / 세부단원 / 난이도 |
| target_name | 분석 대상 이름 |
| total_count | 풀이 문항 수 |
| correct_count | 정답 수 |
| wrong_count | 오답 수 |
| accuracy | 정답률 |
| wrong_rate | 오답률 |
| avg_solving_time | 평균 풀이 시간 |
| created_at | 분석 생성일 |

---

## 8. 맞춤형 문제 생성 방식

맞춤형 문제 세트는 학습자의 이전 풀이 기록을 기반으로 생성한다.

### 8.1 기본 진단 문제 세트

진단 문제는 선택한 난이도 안에서 어휘, 문법, 독해 유형이 균형 있게 포함되도록 구성한다.

예시:

| 유형 | 문제 수 |
|---|---:|
| 어휘 | 3 |
| 문법 | 4 |
| 독해 | 3 |

---

### 8.2 맞춤형 문제 세트

학습자의 정답률이 낮거나 오답률이 높은 유형의 문제 비중을 높여 다음 문제 세트를 구성한다.

예시:

| 분석 결과 | 다음 문제 구성 |
|---|---|
| 어휘 취약 | 어휘 6문제 / 문법 2문제 / 독해 2문제 |
| 문법 취약 | 어휘 2문제 / 문법 6문제 / 독해 2문제 |
| 독해 취약 | 어휘 2문제 / 문법 2문제 / 독해 6문제 |

---

## 9. 실행 방법

### 9.1 저장소 클론

```bash
git clone https://github.com/kimtaewon6670/educheck.git
cd educheck
```

---

### 9.2 가상환경 생성

```bash
python -m venv venv
```

---

### 9.3 가상환경 실행

Windows PowerShell 기준:

```bash
.\venv\Scripts\activate
```

---

### 9.4 패키지 설치

```bash
pip install -r requirements.txt
```

---

### 9.5 프로그램 실행

```bash
python main.py
```

---

## 10. requirements.txt

```txt
PySide6
pandas
matplotlib
```

---

## 11. 브랜치 전략

| 브랜치 | 용도 |
|---|---|
| main | 최종 제출용 안정 버전 |
| develop | 개발 통합 브랜치 |
| feature/ui | PySide6 화면 및 View 작업 |
| feature/core | DB, Controller, Service, 분석 로직 작업 |

---

## 12. 역할 분담

| 담당 | 역할 |
|---|---|
| UI 담당 | PySide6 화면 구현, 화면 전환, 문제 풀이 화면, 결과 화면, 대시보드 구현 |
| Core 담당 | SQLite DB 설계, 문제 CRUD, 자동 채점, 학습 분석, 맞춤형 문제 세트 생성 로직 구현 |

---

## 13. 개발 일정

| 주차 | 목표 |
|---|---|
| 1주차 | 프로젝트 구조 생성, DB 설계, 문제은행 관리 기능 구현 |
| 2주차 | 진단 문제 풀이, 자동 채점, 풀이 기록 저장 기능 구현 |
| 3주차 | 학습 분석, 맞춤형 문제 세트 생성, 대시보드, 오답 복습, 문서 정리 |

---

## 14. 제약사항

- 웹 서비스가 아닌 데스크톱 앱으로 구현한다.
- 인터넷 연결 없이 로컬 환경에서 실행 가능해야 한다.
- 외부 서버를 사용하지 않는다.
- ChatGPT, Gemini, Claude 등 외부 LLM API를 사용하지 않는다.
- API Key를 사용하지 않는다.
- 문제 데이터와 학습 기록은 SQLite 로컬 DB에 저장한다.
- 오픈소스 코드를 직접 복사하여 사용할 경우 전체 코드의 20% 이내로 제한한다.
- 정답률, 오답률, 평균 풀이 시간을 기반으로 취약 영역을 판단한다.
- 맞춤형 문제 세트 생성 알고리즘은 직접 구현한다.

---

## 15. 프로젝트 최종 목표

본 프로젝트의 최종 목표는 학습자의 문제 풀이 데이터를 기반으로 취약 유형과 취약 세부단원을 분석하고, 해당 영역을 중심으로 맞춤형 문제 세트를 제공하는 로컬 데스크톱 기반 에듀테크 시스템을 구현하는 것이다.
