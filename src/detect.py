from ultralytics import YOLO
import cv2
import time
from pathlib import Path
from datetime import datetime
import os

class FireDetector:
    def __init__(self, 
                 model_path='E:/runs/detect/fire_detection/weights/best.pt',
                 conf_threshold=0.25):
        self.model = YOLO(model_path)
        self.conf_threshold = conf_threshold
        self.output_dir = self._create_output_dirs()
    
    def _create_output_dirs(self):
        """創建輸出目錄"""
        output_dir = Path('outputs')
        (output_dir / 'videos').mkdir(parents=True, exist_ok=True)
        (output_dir / 'images').mkdir(parents=True, exist_ok=True)
        return output_dir
    
    def _get_timestamp(self):
        """獲取時間戳"""
        return datetime.now().strftime("%Y%m%d_%H%M%S")
    
    def detect_video(self, source='0', save_video=True):
        """視頻火災檢測"""
        cap = cv2.VideoCapture(source if source != '0' else 0)
        
        # 設置視頻保存
        if save_video:
            timestamp = self._get_timestamp()
            output_path = str(self.output_dir / 'videos' / f'detection_{timestamp}.mp4')
            width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
            height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
            fps = int(cap.get(cv2.CAP_PROP_FPS))
            writer = cv2.VideoWriter(output_path, 
                                   cv2.VideoWriter_fourcc(*'mp4v'), 
                                   fps, (width, height))
        
        while cap.isOpened():
            ret, frame = cap.read()
            if not ret:
                break
            
            # 進行檢測
            results = self.model.predict(
                source=frame,
                conf=self.conf_threshold,
                show=True
            )
            
            # 保存檢測到火災的幀
            for r in results:
                if len(r.boxes) > 0:  # 如果檢測到火災
                    timestamp = self._get_timestamp()
                    img_path = str(self.output_dir / 'images' / f'fire_{timestamp}.jpg')
                    cv2.imwrite(img_path, frame)
            
            # 保存視頻
            if save_video:
                writer.write(frame)
            
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
        
        cap.release()
        if save_video:
            writer.release()
        cv2.destroyAllWindows()

def main():
    detector = FireDetector()
    detector.detect_video(save_video=True)

if __name__ == '__main__':
    main()