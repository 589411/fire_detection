# 建立基礎檢測器類別
class BaseDetector:
    def __init__(self, model_path, conf_threshold=0.4):
        self.model = YOLO(model_path)
        self.conf_threshold = conf_threshold
        self.output_dir = self._create_output_dirs()
        
    # 共用的基礎方法...

class FireDetector(BaseDetector):
    def __init__(self, model_path='path/to/fire_model.pt'):
        super().__init__(model_path)
        # 火災檢測特定設置...

class HelmetDetector(BaseDetector):
    def __init__(self, model_path='path/to/helmet_model.pt'):
        super().__init__(model_path)
        # 安全帽檢測特定設置... 