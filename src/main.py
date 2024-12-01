def main():
    # 單獨使用
    fire_detector = FireDetector()
    fire_detector.detect_video()
    
    # 或同時使用
    helmet_detector = HelmetDetector()
    
    # 可以開啟多個視窗
    import threading
    
    threading.Thread(target=fire_detector.detect_video, args=(0,)).start()
    threading.Thread(target=helmet_detector.detect_video, args=(1,)).start() 