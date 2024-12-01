from ultralytics import YOLO
import cv2
import time
from pathlib import Path
from datetime import datetime
import os

class Detector:
    def __init__(self, model_path, conf_threshold=0.3):
        print(f"載入模型: {model_path}")
        self.model = YOLO(model_path)
        self.conf_threshold = conf_threshold
        self.output_dir = self._create_output_dirs()
        self.running = True
    
    def _create_output_dirs(self):
        """創建輸出目錄"""
        output_dir = Path('outputs')
        (output_dir / 'videos').mkdir(parents=True, exist_ok=True)
        (output_dir / 'images').mkdir(parents=True, exist_ok=True)
        return output_dir
    
    def detect_video(self):
        """視頻檢測"""
        cap = cv2.VideoCapture(0)
        if not cap.isOpened():
            print("無法打開攝像頭")
            return
        
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        output_path = str(self.output_dir / 'videos' / f'detection_{timestamp}.mp4')
        width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
        height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
        fps = int(cap.get(cv2.CAP_PROP_FPS))
        writer = cv2.VideoWriter(output_path, 
                               cv2.VideoWriter_fourcc(*'mp4v'), 
                               fps, (width, height))
        
        try:
            while cap.isOpened() and self.running:
                ret, frame = cap.read()
                if not ret:
                    break
                
                results = self.model.predict(
                    source=frame,
                    conf=self.conf_threshold,
                    iou=0.45,
                    show=True,
                    show_conf=True,
                    show_labels=True
                )
                
                writer.write(frame)
                
                # 添加檢測結果的輸出
                for r in results:
                    if len(r.boxes) > 0:
                        print(f"檢測到: {r.boxes.cls.tolist()}, 置信度: {r.boxes.conf.tolist()}")
                
                # 按 'q' 退出
                if cv2.waitKey(1) & 0xFF == ord('q'):
                    print("使用者按下 q 鍵，停止檢測")
                    break
                
        except KeyboardInterrupt:
            print("接收到中斷信號")
        
        finally:
            print("正在釋放資源...")
            self.running = False
            cap.release()
            writer.release()
            cv2.destroyAllWindows()
            print("檢測結束")

def main():
    while True:
        print("\n請選擇檢測類型：")
        print("1. 火災檢測")
        print("2. 安全帽檢測")
        print("3. 退出程式")
        
        choice = input("請輸入選項 (1/2/3): ")
        
        if choice == "1":
            detector = Detector(
                model_path='weights/fire_detection/best.pt',
                conf_threshold=0.3
            )
            print("開始火災檢測 (按 'q' 退出)")
            detector.detect_video()
            
        elif choice == "2":
            detector = Detector(
                model_path='weights/helmet_detection/best.pt',
                conf_threshold=0.3
            )
            print("開始安全帽檢測 (按 'q' 退出)")
            detector.detect_video()
            
        elif choice == "3":
            print("程式結束")
            break
            
        else:
            print("無效的選項，請重新選擇")

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print("\n程式被使用者中斷")
    finally:
        cv2.destroyAllWindows()