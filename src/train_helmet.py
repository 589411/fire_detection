from ultralytics import YOLO
import os
from pathlib import Path

def train_helmet_model():
    # 獲取項目根目錄
    root_dir = Path(__file__).parent.parent
    
    # 確保目錄存在
    weights_dir = root_dir / 'weights'
    weights_dir.mkdir(exist_ok=True)
    
    # 載入基礎模型
    model = YOLO('yolov8n.pt')
    
    # 使用絕對路徑
    data_yaml = str(root_dir / 'datasets/helmet/helmet_data.yaml')
    
    # 開始訓練
    results = model.train(
        data=data_yaml,
        epochs=100,
        imgsz=640,
        batch=16,
        name='helmet_detection',
        project=str(weights_dir)
    )

if __name__ == '__main__':
    train_helmet_model() 