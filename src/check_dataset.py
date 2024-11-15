 import os

def check_dataset_structure():
    """檢查數據集結構"""
    required_dirs = [
        'data/train/images',
        'data/train/labels',
        'data/val/images',
        'data/val/labels'
    ]
    
    for dir_path in required_dirs:
        full_path = os.path.join(os.getcwd(), dir_path)
        if not os.path.exists(full_path):
            print(f'錯誤: 目錄不存在 {full_path}')
            os.makedirs(full_path, exist_ok=True)
            print(f'已創建目錄 {full_path}')
        else:
            files = len([f for f in os.listdir(full_path) if os.path.isfile(os.path.join(full_path, f))])
            print(f'目錄 {dir_path} 存在，包含 {files} 個文件')

if __name__ == '__main__':
    check_dataset_structure()