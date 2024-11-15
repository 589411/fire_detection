import os
import glob

def find_model():
    print("開始搜索模型文件...")
    
    # 可能的路徑列表
    search_paths = [
        "E:/runs/detect/fire_detection/weights/best.pt",
        "E:/runs/detect/fire_detection/weights/last.pt",
        "E:/fire_detection/runs/detect/fire_detection/weights/best.pt",
        "E:/fire_detection/runs/detect/fire_detection/weights/last.pt",
        "E:/runs/train/fire_detection/weights/best.pt",
        "E:/runs/train/fire_detection/weights/last.pt",
        "E:/fire_detection/runs/train/fire_detection/weights/best.pt",
        "E:/fire_detection/runs/train/fire_detection/weights/last.pt"
    ]
    
    # 搜索每個可能的路徑
    for path in search_paths:
        if os.path.exists(path):
            print(f"\n找到模型文件！")
            print(f"路徑: {path}")
            print(f"文件大小: {os.path.getsize(path) / 1024 / 1024:.2f} MB")
            return path
    
    # 使用glob進行更廣泛的搜索
    print("\n開始進行全局搜索...")
    
    search_patterns = [
        "E:/**/*.pt",
        "E:/fire_detection/**/*.pt",
        "E:/runs/**/*.pt"
    ]
    
    for pattern in search_patterns:
        files = glob.glob(pattern, recursive=True)
        for file in files:
            print(f"\n找到權重文件：")
            print(f"路徑: {file}")
            print(f"文件大小: {os.path.getsize(file) / 1024 / 1024:.2f} MB")

if __name__ == "__main__":
    find_model()