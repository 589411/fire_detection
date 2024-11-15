import os
import shutil
from pathlib import Path

def setup_dataset():
    """設置數據集目錄結構並檢查數據"""
    # 設置基礎路徑
    base_dir = Path('data')
    
    # 創建必要的目錄
    directories = [
        base_dir / 'train' / 'images',
        base_dir / 'train' / 'labels',
        base_dir / 'val' / 'images',
        base_dir / 'val' / 'labels'
    ]
    
    # 創建目錄
    for dir_path in directories:
        dir_path.mkdir(parents=True, exist_ok=True)
        print(f'檢查目錄: {dir_path}')
        
        # 檢查目錄中的文件
        files = list(dir_path.glob('*.*'))
        print(f'目錄 {dir_path} 中有 {len(files)} 個文件')
        
        # 如果是圖片目錄，檢查圖片格式
        if 'images' in str(dir_path):
            image_files = [f for f in files if f.suffix.lower() in ('.jpg', '.jpeg', '.png')]
            print(f'其中有 {len(image_files)} 個圖片文件')
            
            # 顯示一些示例文件名
            if image_files:
                print('示例文件:', [f.name for f in image_files[:3]])

def create_data_yaml():
    """創建數據集配置文件"""
    yaml_content = f"""
path: {os.path.abspath('data')}  # 數據集根目錄
train: train/images  # 訓練集圖片相對路徑
val: val/images      # 驗證集圖片相對路徑
nc: 1                # 類別數量
names: ['fire']      # 類別名稱
    """.strip()
    
    yaml_path = Path('data') / 'data.yaml'
    yaml_path.write_text(yaml_content)
    print(f'\n創建配置文件: {yaml_path}')
    print('配置文件內容:')
    print(yaml_content)

if __name__ == '__main__':
    setup_dataset()
    create_data_yaml()