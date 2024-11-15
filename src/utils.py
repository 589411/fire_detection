import cv2
import numpy as np
from datetime import datetime
import os

def create_output_dirs():
    """創建輸出目錄"""
    dirs = ['outputs/images', 'outputs/videos', 'outputs/logs']
    for dir_path in dirs:
        os.makedirs(dir_path, exist_ok=True)
    return dirs

def get_timestamp():
    """獲取當前時間戳"""
    return datetime.now().strftime("%Y%m%d_%H%M%S")

def save_frame(frame, confidence, save_path='outputs/images'):
    """保存檢測到火災的圖片"""
    timestamp = get_timestamp()
    filename = f'fire_detected_{timestamp}_conf{confidence:.2f}.jpg'
    path = os.path.join(save_path, filename)
    cv2.imwrite(path, frame)
    return path

def log_detection(confidence, image_path, log_file='outputs/logs/detections.txt'):
    """記錄檢測結果"""
    timestamp = get_timestamp()
    with open(log_file, 'a', encoding='utf-8') as f:
        f.write(f'{timestamp} - 檢測到火災 - 置信度: {confidence:.2f} - 圖片: {image_path}\n')

def draw_info(frame, fps=0, confidence=0):
    """在圖片上繪製信息"""
    height, width = frame.shape[:2]
    
    # 添加FPS信息
    cv2.putText(frame, f'FPS: {fps:.1f}', 
                (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
    
    # 如果檢測到火災，添加警告
    if confidence > 0:
        warning_text = f'火災警告! 置信度: {confidence:.2f}'
        cv2.putText(frame, warning_text, 
                    (10, height - 20), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
    
    return frame