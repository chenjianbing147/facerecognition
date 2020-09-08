import datetime
import os
import threading
import time

import cv2
import face_recognition
import numpy as np
from PyQt5.QtGui import QImage, QPixmap
from PyQt5.QtWidgets import QMessageBox

from dboperate import DBOperate


class Display:
    def __init__(self, ui, mainWnd):
        self.ui = ui
        self.mainWnd = mainWnd
        self.db = DBOperate()

        # 默认视频源为相机
        self.doesCameraOpen = False

        # 信号槽设置，将按钮事件绑定到函数上
        ui.camera_button.clicked.connect(self.camera)
        ui.register_button.clicked.connect(self.register)
        ui.recognize_button.clicked.connect(self.recognize)

        # 创建一个关闭事件并设为未触发
        self.stopEvent = threading.Event()
        self.stopEvent.clear()

    def camera(self):
        if not self.doesCameraOpen:  # 摄像头未开启时点击启动摄像头
            self.cap = cv2.VideoCapture(0)
            self.cap.set(cv2.CAP_PROP_FPS, 60)

            # 创建视频显示线程
            self.th = threading.Thread(target=self.display)
            self.th.setDaemon(True)
            self.th.start()

            # 改变按钮文字
            self.ui.camera_button.setText('关闭摄像头')

            self.doesCameraOpen = True
            self.ui.register_button.setEnabled(True)
            self.ui.recognize_button.setEnabled(True)
        else:
            self.stopEvent.set()
            self.ui.camera_button.setText('开启摄像头')
            self.doesCameraOpen = False
            self.ui.register_button.setEnabled(False)
            self.ui.recognize_button.setEnabled(False)

    def display(self):
        while self.cap.isOpened():
            success, frame = self.cap.read()
            frame = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)
            img = QImage(frame.data, frame.shape[1], frame.shape[0], QImage.Format_RGB888)
            self.ui.video_label.setPixmap(QPixmap.fromImage(img))

            # 控制视频帧率
            cv2.waitKey(1000 // 30)

            # 判断关闭事件是否已触发
            if self.stopEvent.is_set():
                # 关闭事件置为未触发，清空显示label
                self.stopEvent.clear()
                self.ui.video_label.clear()
                break
        # 释放摄像头
        self.cap.release()

    # 每隔0.25秒保存1张视频帧，共保存4张，供保存人脸数据使用
    def save_four_img(self):
        for i in range(4):
            if self.cap.isOpened():
                success, frame = self.cap.read()
                path = r'./temp/'
                cv2.imwrite(path + str(i) + '.jpg', frame)
                time.sleep(0.25)

    # 保存1张人脸照片，供识别使用
    def save_one_img(self):
        success, frame = self.cap.read()
        cv2.imwrite(r'./temp/cap.jpg', frame)

    def delete_four_img(self):
        for i in range(4):
            path = r'./temp/' + str(i) + '.jpg'
            if os.path.exists(path):
                os.remove(path)

    def delete_one_img(self):
        path = r'./temp/cap.jpg'
        if os.path.exists(path):
            os.remove(path)

    # 将4张图片通过face_recognition转化为128维向量，并取平均值
    def img2vector(self):
        path = r'./temp/'
        vector = np.zeros(128)
        try:
            for i in range(4):
                img = face_recognition.load_image_file(path + str(i) + '.jpg')
                vector += face_recognition.face_encodings(img)[0]
            vector = vector / 4
            return True, vector
        except:
            QMessageBox.about(self.mainWnd, "录入失败", "未捕捉到人脸信息！")
            return False, vector

    def match_face(self, vector):
        try:
            student_list, vector_list = self.db.get_face_vector()
            print('point1')
            result = face_recognition.compare_faces(vector_list, vector)
            print('point2')
            if True in result:
                return True, student_list[result.index(True)]
            else:
                return False, []
        except:
            QMessageBox.about(self.mainWnd, "签到失败", "未捕捉到人脸信息！")
            return False, []

    def register(self):
        self.save_four_img()
        success, vector = list(self.img2vector())
        if not success:
            return
        name = self.ui.name_line.text()
        student_id = self.ui.id_line.text()
        self.delete_four_img()
        if len(name) * len(student_id) == 0:
            QMessageBox.about(self.mainWnd, "错误", "姓名与学号不得为空！")
        else:
            try:
                self.db.student_register(name, student_id, list(vector))
                QMessageBox.about(self.mainWnd, "提示", "录入成功!")
            except Exception:
                QMessageBox.about(self.mainWnd, "录入失败", "请检查姓名与学号是否填写正确！")

    def recognize(self):
        self.save_one_img()
        img = face_recognition.load_image_file(r'./temp/cap.jpg')
        self.delete_one_img()
        vector = face_recognition.face_encodings(img)[0]
        matched, result = self.match_face(vector)
        if matched:
            t = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            self.db.punch_in(t, result[1])
            QMessageBox.about(self.mainWnd, '签到成功',
                              '学生 ' + result[0] + ',学号 ' + result[1] + '\n已成功签到！时间' + t)
        else:
            QMessageBox.about(self.mainWnd, "签到失败", "未找到符合的人脸数据!")
