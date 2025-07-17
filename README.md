
# K-AgriVision: AI Vision for Autonomous Livestock Farming

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.9+](https://img.shields.io/badge/python-3.9+-blue.svg)](https://www.python.org/downloads/release/python-390/)
[![status](https://img.shields.io/badge/status-Proof_of_Concept-orange.svg)](https://github.com/hwkim3330/K-AgriVision)
[![제안자](https://img.shields.io/badge/제안자-김현우(KETI)-brightgreen.svg)](https://github.com/hwkim3330)

> **"축산업의 미래는 '더 많은' 데이터가 아닌, '더 깊은' 통찰력에 있습니다."**
>
> 본 프로젝트는 제3회 스마트축산 AI 경진대회 출품작으로, AI 비전 기술을 통해 가축의 건강, 환경, 생산성을 통합 관리하여 **'자율 운영 농장(Autonomous Farm)'**을 구현하는 핵심 알고리즘을 제안합니다.

---

<br>

## 📜 Table of Contents (목차)

1.  [**Problem Statement (문제 정의)**](#1-problem-statement-문제-정의-데이터의-섬)
2.  [**Core Solution (핵심 솔루션)**](#2-core-solution-핵심-솔루션-ai-비전-모든-것을-보는-눈)
3.  [**System Architecture (시스템 아키텍처)**](#3-system-architecture-시스템-아키텍처-엣지와-클라우드의-협업)
4.  [**Key Features & Prototype (주요 기능 및 프로토타입)**](#4-key-features--prototype-주요-기능-및-프로토타입)
5.  [**Technical Deep Dive (기술 상세)**](#5-technical-deep-dive-기술-상세)
6.  [**Development Roadmap (개발 로드맵)**](#6-development-roadmap-개발-로드맵)
7.  [**Getting Started (프로젝트 실행)**](#7-getting-started-프로젝트-실행)

<br>

---

## 1. Problem Statement (문제 정의): 데이터의 섬

현재 스마트 축산 기술은 사양, 환경, 생산 관리 솔루션이 개별적으로 존재하여 **'데이터의 섬(Data Silo)'**에 갇혀 있습니다.

| 문제점 | 한계 |
| :--- | :--- |
| **분절된 데이터** | 가축의 질병이 발생해도 그 원인이 환경 문제인지, 개체 간 스트레스 문제인지 통합 분석이 불가능합니다. |
| **단순 모니터링** | 대부분의 솔루션은 과거와 현재의 데이터를 보여줄 뿐, 미래를 '예측'하고 선제적으로 '대응'하지 못합니다. |
| **사후 대응 중심** | 문제가 발생한 후에야 인지하고 조치하므로, 이미 경제적 손실은 발생한 상태입니다. |

<br>

---

## 2. Core Solution (핵심 솔루션): AI 비전, 모든 것을 보는 눈

저희는 축사 내 카메라를 **'모든 것을 보는 눈(The All-Seeing Eye)'**으로 활용하여, 분절된 데이터를 하나의 유기적인 인사이트로 통합합니다.


*<p align="center">AI 비전을 통한 통합 관리의 선순환 구조</p>*

1.  **정밀 사양관리 (Precision Livestock Farming):** 개별 가축의 미세 행동(기침, 파행, 섭식 시간)을 24시간 비접촉 모니터링하여 질병 및 스트레스 징후를 조기 예측합니다.
2.  **지능형 환경개선 (Intelligent Environment Control):** 가축의 분포(밀집도)와 바닥 오염도를 영상으로 분석하여 악취 및 유해가스 발생 가능성을 예측하고, 최적의 환경 제어를 유도합니다.
3.  **데이터 기반 생산관리 (Data-Driven Production):** 개체별 건강 데이터를 성장 이력과 결합, 정밀한 증체량 예측과 최적 출하 시점 산출로 농가 수익성을 극대화합니다.

<br>

---

## 3. System Architecture (시스템 아키텍처): 엣지와 클라우드의 협업

**실시간 분석은 엣지(Edge)에서, 심층 학습은 클라우드(Cloud)에서** 수행하는 효율적인 하이브리드 구조를 채택하여 즉각적인 대응과 지속적인 모델 고도화를 동시에 달성합니다.


*<p align="center">하이브리드 아키텍처 데이터 흐름도</p>*

| 컴포넌트 | 역할 | 주요 기술 |
| :--- | :--- | :--- |
| **Edge Device** | 실시간 영상 처리, 객체 탐지/추적, 긴급 알림 생성 | NVIDIA Jetson, YOLOv8, DeepSORT, ONNX Runtime |
| **Cloud Platform** | 데이터 저장/관리, AI 모델 심층 학습, 통합 분석, 대시보드 제공 | AWS/GCP/Azure, S3, Docker, Kubernetes, Pytorch |
| **User Interface** | 데이터 시각화, 인사이트 제공, 원격 제어 | Web (React/Vue), Mobile (Flutter) |

<br>

---

## 4. Key Features & Prototype (주요 기능 및 프로토타입)

| 기능 | 설명 | 프로토타입 예시 (대시보드 UI) |
| :--- | :--- | :--- |
| **통합 관제 대시보드** | 농장의 모든 핵심 지표를 한눈에 파악하고, 문제 발생 시 즉각적으로 인지할 수 있습니다. |  |
| **고위험군 개체 자동 선별** | AI가 질병, 스트레스 징후를 보이는 개체를 자동 선별하여 리스트업하고, 농장주의 집중 관리를 유도합니다. |  |
| **환경 위험도 맵핑** | 축사 평면도 위에 과밀, 고온, 악취 위험 구역을 히트맵 형태로 시각화하여 직관적인 환경 개선을 돕습니다. |  |

<br>

---

## 5. Technical Deep Dive (기술 상세)

본 프로젝트의 핵심 기술은 아래와 같은 파이프라인으로 구성됩니다.

```python
def k_agrivision_pipeline(video_stream):
    """
    K-AgriVision의 핵심 분석 파이프라인 의사코드
    """
    
    # --- 1. 엣지 컴퓨팅: 실시간 분석 ---
    # 개별 프레임에서 객체(가축) 탐지 및 추적
    detected_objects = object_detection_and_tracking(video_stream) # (YOLOv8 + DeepSORT)
    
    # 각 객체의 행동을 실시간으로 분류 (경량 모델)
    realtime_actions = realtime_action_classification(detected_objects) # (MobileNetV3)
    
    # 긴급 상황(예: 쓰러짐) 발생 시 즉시 알림 전송
    check_and_send_emergency_alert(realtime_actions)
    
    # 메타데이터를 클라우드로 전송
    send_metadata_to_cloud(detected_objects, realtime_actions)
    
    
    # --- 2. 클라우드 컴퓨팅: 심층 분석 (주기적 실행) ---
    # 저장된 메타데이터를 바탕으로 심층 행동 분석
    in_depth_actions = deep_behavior_analysis(metadata_from_edge) # (3D-CNN, Transformer)
    
    # 건강 이상 징후 예측 (시계열 분석)
    health_anomalies = health_anomaly_detection(in_depth_actions) # (LSTM)
    
    # 환경 데이터와 연계하여 원인 추론
    root_cause = root_cause_analysis(health_anomalies, environment_data)
    
    # 생산성 예측 모델 업데이트
    update_productivity_model(health_anomalies, growth_data)
    
    # 최종 분석 결과를 대시보드에 업데이트
    update_dashboard(root_cause, productivity_forecast)
    
    return "Analysis Complete. Dashboard Updated."
```

<br>

---

## 6. Development Roadmap (개발 로드맵)

본 제안은 단발성 출품이 아닌, 실제 산업에 기여하기 위한 장기적인 비전을 가지고 있습니다.

| 단계 | 기간 | 주요 목표 | 상태 |
| :--- | :--- | :--- | :--- |
| **Phase 1** | ~ 2025.Q4 | **기반 모델 구축 (PoC)** <br/> - 핵심 행동 분류 모델 개발 <br/> - 프로토타입 대시보드 구현 | 🟩 **진행 중** |
| **Phase 2**| ~ 2026.Q2 | **멀티모달 AI & 디지털 트윈** <br/> - 음향 분석 기술 융합 <br/> - 시뮬레이션 가능한 디지털 트윈 구축 | ⬜️ 계획 |
| **Phase 3**| ~ 2027 | **자율 운영 농장 실증** <br/> - 강화학습 기반 자율 운영 에이전트 개발 <br/> - 협력 농가 실증 테스트 | ⬜️ 계획 |

<br>

---

## 7. Getting Started (프로젝트 실행)

본 프로젝트의 코드는 하나의 파이썬 파일로 통합되어 있으며, 아래와 같이 간단히 실행해볼 수 있습니다.

#### 환경 설정
```bash
# 1. 저장소 복제
git clone https://github.com/hwkim3330/K-AgriVision.git
cd K-AgriVision

# 2. 가상환경 생성 및 활성화
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# 3. 필수 라이브러리 설치
pip install opencv-python numpy torch torchvision
```

#### 시뮬레이션 실행
아래 명령어를 실행하면, `main.py` 파일이 가상의 영상 스트림을 처리하는 과정을 시뮬레이션하고 결과를 출력합니다.
```bash
python main.py
```
 
