import shutil
import os
from datetime import datetime

def backup_model():
    # 源文件路徑
    source_path = 'E:/runs/detect/fire_detection/weights/best.pt'
    
    # 創建備份目錄
    backup_dir = 'model_backup'
    os.makedirs(backup_dir, exist_ok=True)
    
    # 生成備份文件名（包含時間戳）
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    backup_path = f'{backup_dir}/best_{timestamp}.pt'
    
    # 複製文件
    shutil.copy2(source_path, backup_path)
    print(f'模型已備份到: {backup_path}')

if __name__ == '__main__':
    backup_model() 