from ultralytics import YOLO
import os
from pathlib import Path

def train_model():
    # 確保使用正確的數據配置文件
    data_yaml = os.path.abspath('data/data.yaml')
    if not os.path.exists(data_yaml):
        raise FileNotFoundError(f"找不到數據配置文件: {data_yaml}")
    
    # 初始化模型
    model = YOLO('yolov8n.yaml')
    
    # 訓練參數
    params = {
        'data': data_yaml,
        'epochs': 100,
        'imgsz': 640,
        'batch': 16,
        'device': 0,  # GPU
        'name': 'fire_detection',
        'exist_ok': True
    }
    
    # 開始訓練
    try:
        results = model.train(**params)
        print("訓練完成!")
        return results
    except Exception as e:
        print(f"訓練過程中發生錯誤: {str(e)}")
        return None

if __name__ == '__main__':
    train_model()