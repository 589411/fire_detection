import shutil
from pathlib import Path
import time
from datetime import datetime
import os

class ModelBackup:
    def __init__(self):
        self.root_dir = Path(__file__).parent.parent
        self.models = {
            'fire': self.root_dir / 'weights' / 'fire_detection' / 'best.pt',
            'helmet': self.root_dir / 'weights' / 'helmet_detection' / 'best.pt'
        }
        self.backup_dir = self.root_dir / 'backup_weights'
        
    def create_backup(self):
        # 創建備份目錄
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        backup_path = self.backup_dir / timestamp
        backup_path.mkdir(parents=True, exist_ok=True)
        
        # 備份每個模型
        for name, model_path in self.models.items():
            if model_path.exists():
                # 創建帶時間戳的備份文件名
                backup_file = backup_path / f"{name}_best_{timestamp}.pt"
                shutil.copy2(model_path, backup_file)
                print(f"已備份 {name} 模型到: {backup_file}")
            else:
                print(f"警告: 找不到 {name} 模型文件: {model_path}")
        
        # 保留最近5個備份
        self._cleanup_old_backups()
    
    def _cleanup_old_backups(self, keep_num=5):
        """清理舊的備份，只保留最近的 keep_num 個"""
        if self.backup_dir.exists():
            backups = sorted(self.backup_dir.iterdir(), key=lambda x: x.stat().st_mtime)
            if len(backups) > keep_num:
                for old_backup in backups[:-keep_num]:
                    shutil.rmtree(old_backup)
                    print(f"已刪除舊備份: {old_backup}")

def main():
    backup = ModelBackup()
    backup.create_backup()

if __name__ == '__main__':
    main() 