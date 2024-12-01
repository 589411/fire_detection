from ultralytics import YOLO
import os

def train_fire_model():
    # 確保目錄存在
    os.makedirs('weights', exist_ok=True)
    
    # 載入基礎模型
    model = YOLO('yolov8n.pt')
    
    # 開始訓練
    results = model.train(
        data='datasets/fire/fire_data.yaml',
        epochs=100,
        imgsz=640,
        batch=16,
        name='fire_detection',
        project='weights'
    )

if __name__ == '__main__':
    train_fire_model() 