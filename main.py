import time
import random
import argparse
from datetime import datetime

# --- ANSI 색상 코드 (터미널 출력을 더 보기 좋게 만듭니다) ---
class C:
    HEADER = '\033[95m'
    BLUE = '\033[94m'
    CYAN = '\033[96m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    END = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

# ==============================================================================
# 1. 엣지 컴퓨팅 시뮬레이션 (Edge Computing Simulation)
#   - 농장 현장에서 실시간으로 빠르게 처리되어야 하는 기능들입니다.
# ==============================================================================
class EdgeDevice:
    """농장에 설치된 엣지 디바이스를 시뮬레이션하는 클래스입니다."""
    def __init__(self, device_id):
        self.device_id = device_id
        self.livestock_db = {i: {'id': i, 'status': 'normal', 'behavior_history': []} for i in range(1, 11)}
        print(f"{C.GREEN}[Edge Init] 엣지 디바이스 '{self.device_id}'가 활성화되었습니다. 10마리의 가축을 추적합니다.{C.END}")

    def object_detection_and_tracking(self, frame_id):
        """
        [YOLOv8 + DeepSORT 역할]
        실시간 영상 프레임에서 가축을 탐지하고 ID를 부여하여 추적합니다.
        """
        print(f"\n--- Frame {frame_id}: 실시간 영상 분석 시작 ---")
        time.sleep(0.1)
        # 실제로는 여기서 각 가축의 위치(bbox)와 ID가 반환됩니다.
        detected_objects = list(self.livestock_db.values())
        print(f"{C.CYAN}[Edge L1] {len(detected_objects)}마리의 가축이 탐지 및 추적되었습니다.{C.END}")
        return detected_objects

    def realtime_action_classification(self, detected_objects):
        """
        [MobileNetV3 (경량 모델) 역할]
        탐지된 각 가축의 행동을 '서기', '눕기', '먹기', '기침', '쓰러짐' 등 간단한 카테고리로 분류합니다.
        """
        behaviors = ['standing', 'lying', 'eating']
        for obj in detected_objects:
            # 5% 확률로 비정상 행동(기침)을 시뮬레이션
            if random.random() < 0.05:
                action = 'coughing'
            # 1% 확률로 긴급 상황(쓰러짐)을 시뮬레이션
            elif random.random() < 0.01:
                action = 'fallen'
            else:
                action = random.choice(behaviors)
            
            obj['current_action'] = action
            obj['behavior_history'].append(action)
        print(f"{C.CYAN}[Edge L2] 각 개체의 실시간 행동이 분류되었습니다.{C.END}")
        return detected_objects

    def check_and_send_emergency_alert(self, analyzed_objects):
        """
        분석된 데이터에서 긴급 상황을 감지하고 즉시 알림을 생성합니다.
        """
        for obj in analyzed_objects:
            if obj['current_action'] == 'fallen':
                print(f"{C.RED}{C.BOLD}🚨 [긴급 알림] ID-{obj['id']} 가축이 쓰러졌습니다! 즉시 확인이 필요합니다!{C.END}")
    
    def send_metadata_to_cloud(self, analyzed_objects):
        """
        실시간 분석 결과를 클라우드로 전송합니다. 실제로는 JSON 형태로 API를 통해 전송됩니다.
        """
        metadata_packet = {
            'timestamp': datetime.now().isoformat(),
            'device_id': self.device_id,
            'data': [{'id': obj['id'], 'action': obj['current_action']} for obj in analyzed_objects]
        }
        print(f"{C.CYAN}[Edge L3] 분석 메타데이터를 클라우드로 전송합니다... (총 {len(metadata_packet['data'])}개){C.END}")
        return metadata_packet


# ==============================================================================
# 2. 클라우드 플랫폼 시뮬레이션 (Cloud Platform Simulation)
#   - 방대한 데이터를 저장하고, 복잡한 모델을 학습/분석하는 기능들입니다.
# ==============================================================================
class CloudPlatform:
    """클라우드 플랫폼을 시뮬레이션하는 클래스입니다."""
    def __init__(self):
        self.big_data_storage = []
        self.health_trends = {}
        print(f"\n{C.GREEN}[Cloud Init] 클라우드 플랫폼이 활성화되었습니다.{C.END}")

    def receive_and_store_data(self, metadata_packet):
        """
        엣지로부터 받은 데이터를 데이터 레이크(Big Data Storage)에 저장합니다.
        """
        self.big_data_storage.append(metadata_packet)
        print(f"{C.BLUE}[Cloud L1] 엣지로부터 메타데이터 수신 및 저장 완료. (총 {len(self.big_data_storage)}개 패킷 누적){C.END}")

    def run_deep_analysis(self):
        """
        [3D-CNN, Transformer 역할]
        주기적으로 저장된 데이터를 바탕으로 심층 분석을 수행합니다.
        예: 단순 '기침'이 아닌, '연속적인 마른 기침' 패턴을 분석합니다.
        """
        if len(self.big_data_storage) < 10:
            return None # 데이터가 충분하지 않으면 분석을 건너뜁니다.
        
        print(f"{C.BLUE}[Cloud L2] 누적된 데이터를 바탕으로 심층 분석 및 건강 이상 징후 예측을 시작합니다...{C.END}")
        time.sleep(0.5)

        # '기침' 행동이 단기간에 3번 이상 발생한 개체를 '고위험군'으로 분류
        cough_counts = {}
        for packet in self.big_data_storage[-10:]: # 최근 10개 데이터 분석
            for data in packet['data']:
                if data['action'] == 'coughing':
                    cough_counts[data['id']] = cough_counts.get(data['id'], 0) + 1
        
        high_risk_livestock = []
        for livestock_id, count in cough_counts.items():
            if count >= 2:
                self.health_trends[livestock_id] = 'respiratory_disease_symptom'
                high_risk_livestock.append(livestock_id)

        if high_risk_livestock:
            print(f"{C.YELLOW}[분석 결과] 고위험군 개체 발견: ID-{high_risk_livestock}. (사유: 호흡기 질환 의심){C.END}")
        else:
            print(f"{C.YELLOW}[분석 결과] 모든 개체의 건강 상태가 양호합니다.{C.END}")

    def update_dashboard(self):
        """
        분석된 최종 결과를 사용자가 보는 대시보드에 업데이트합니다.
        """
        print(f"{C.BLUE}[Cloud L3] 분석 결과를 대시보드에 업데이트합니다.{C.END}")


# ==============================================================================
# 3. 메인 실행 함수 (Main Execution Function)
# ==============================================================================
def run_simulation(duration_seconds):
    """지정된 시간 동안 전체 K-AgriVision 파이프라인 시뮬레이션을 실행합니다."""
    
    print(f"\n{C.HEADER}{C.BOLD}========== K-AgriVision 시뮬레이션 시작 (총 {duration_seconds}초) =========={C.END}")
    
    # 1. 시스템 초기화
    edge_device = EdgeDevice(device_id="Farm01-Edge01")
    cloud_platform = CloudPlatform()

    start_time = time.time()
    frame_count = 0
    
    # 2. 시뮬레이션 루프 실행
    while time.time() - start_time < duration_seconds:
        frame_count += 1
        
        # --- 엣지 파이프라인 ---
        detected_obj = edge_device.object_detection_and_tracking(frame_count)
        analyzed_obj = edge_device.realtime_action_classification(detected_obj)
        edge_device.check_and_send_emergency_alert(analyzed_obj)
        metadata = edge_device.send_metadata_to_cloud(analyzed_obj)
        
        # --- 클라우드 파이프라인 ---
        cloud_platform.receive_and_store_data(metadata)
        
        # 5 프레임마다 한 번씩 심층 분석 실행
        if frame_count % 5 == 0:
            cloud_platform.run_deep_analysis()
            cloud_platform.update_dashboard()

        time.sleep(0.5) # 실제 시간 흐름을 표현하기 위한 딜레이

    print(f"\n{C.HEADER}{C.BOLD}========== 시뮬레이션 종료 (총 {frame_count} 프레임 분석) =========={C.END}\n")


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="K-AgriVision: AI Vision for Autonomous Livestock Farming - Simulation")
    parser.add_argument('--duration', type=int, default=10, help='시뮬레이션을 실행할 시간(초)')
    args = parser.parse_args()
    
    run_simulation(args.duration)
