import os
import shutil
import random
from pathlib import Path

def split_dataset(train_ratio=0.8):
    print("開始分割數據集...")
    
    random.seed(42)
    
    train_images_dir = Path('data/train/images')
    train_images = list(train_images_dir.glob('*.jpg')) + \
                  list(train_images_dir.glob('*.jpeg')) + \
                  list(train_images_dir.glob('*.png'))
    
    total = len(train_images)
    val_size = int(total * (1 - train_ratio))
    
    print(f'總數據量: {total}')
    print(f'將移動 {val_size} 個文件到驗證集')
    
    val_images = random.sample(train_images, val_size)
    
    val_images_dir = Path('data/val/images')
    val_labels_dir = Path('data/val/labels')
    val_images_dir.mkdir(parents=True, exist_ok=True)
    val_labels_dir.mkdir(parents=True, exist_ok=True)
    
    moved_count = 0
    for img_path in val_images:
        try:
            img_name = img_path.name
            label_name = img_path.stem + '.txt'
            src_label_path = Path('data/train/labels') / label_name
            dst_img_path = val_images_dir / img_name
            dst_label_path = val_labels_dir / label_name
            
            shutil.move(str(img_path), str(dst_img_path))
            if src_label_path.exists():
                shutil.move(str(src_label_path), str(dst_label_path))
            
            moved_count += 1
            if moved_count % 100 == 0:
                print(f'已處理: {moved_count}/{val_size}')
                
        except Exception as e:
            print(f'移動文件時發生錯誤: {str(e)}')
    
    print("\n數據集分割完成!")
    print(f'訓練集圖片: {len(list(Path("data/train/images").glob("*.*")))}')
    print(f'驗證集圖片: {len(list(Path("data/val/images").glob("*.*")))}')

if __name__ == '__main__':
    split_dataset()