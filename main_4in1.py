# import imageio
#
# imageio.plugins.ffmpeg.download()
# # import win_unicode_console
#
# win_unicode_console.enable()
import sys, os
from PyQt5.QtCore import *
from PyQt5.QtWidgets import (QWidget, QPushButton, QLineEdit, QLabel,QTextEdit,
                             QApplication, QFileDialog,QProgressBar)
from moviepy.video.io.VideoFileClip import VideoFileClip
from run4in1_video_cut import run4in1,run4in1_thread
from PyQt5.QtGui import QTextCursor

import threading
import multiprocessing


class Stream(QObject):
    """Redirects console output to text widget."""
    newText = pyqtSignal(str)

    def write(self, text):
        self.newText.emit(str(text))

class login(QWidget):
    def __init__(self):
        super(login, self).__init__()
        self.initUI()
        self.is_running = 0 # 0没在运行；1在运行
        self.save_file_names = [] #要执行的视频文件list
        # self.t1
        # Custom output stream.
        sys.stdout = Stream(newText=self.onUpdateText)

    def onUpdateText(self, text):
        """Write console output to text widget."""
        cursor = self.textEdit.textCursor()
        cursor.movePosition(QTextCursor.End)
        cursor.insertText(text)
        self.textEdit.setTextCursor(cursor)
        self.textEdit.ensureCursorVisible()

    def closeEvent(self, event):
        """Shuts down application on close."""
        # Return stdout to defaults.
        sys.stdout = sys.__stdout__
        super().closeEvent(event)

    def initUI(self):
        # 源文件选择按钮和选择编辑框
        self.source_btn = QPushButton('选择源文件', self)
        self.source_btn.move(30, 30)
        self.source_btn.resize(90, 30)
        self.source_btn.clicked.connect(self.select_source)
        self.source_le = QLineEdit(self)
        self.source_le.move(150, 30)
        self.source_le.resize(450, 30)

        # 存储文件选择按钮和选择编辑框
        self.target_btn = QPushButton('选择保存路径', self)
        self.target_btn.move(30, 90)
        self.target_btn.resize(90, 30)
        self.target_btn.clicked.connect(self.select_target)
        self.target_le = QLineEdit(self)
        self.target_le.move(150, 90)
        self.target_le.resize(450, 30)

        # 保存按钮，调取数据增加函数等
        self.save_btn = QPushButton('开始', self)
        self.save_btn.move(30, 210)
        self.save_btn.resize(140, 30)
        self.save_btn.clicked.connect(self.addNum)

        # 执行成功返回值显示位置设置
        self.result_le = QLabel(self)
        self.result_le.move(30, 270)
        self.result_le.resize(340, 30)

        self.progressBar = QProgressBar(self)
        self.progressBar.setGeometry(QRect(250, 210, 361, 23))
        self.progressBar.setProperty("value", 0)
        self.progressBar.setObjectName("progressBar")

        self.textEdit = QTextEdit(self, readOnly=True)
        self.textEdit.setGeometry(QRect(30, 300, 500, 200))
        self.textEdit.setObjectName("textEdit")

        # 整体界面设置
        self.setGeometry(400, 400, 800, 600)
        self.setWindowTitle('视频剪切')  # 设置界面标题名
        self.show()

    # 打开的视频文件名称
    def select_source(self):
        open_dic = "C:/Users/29125/PycharmProjects/video4in1"
        self.targets, fileType = QFileDialog.getOpenFileNames(self, "选择源文件", open_dic)
        self.source_le.setText(str(self.targets))

        if len(self.targets) >0:
            print('选择了待处理的视频数量：', len(self.targets))
        # target, fileType = QFileDialog.getSaveFileName(self, "选择保存路径", self.source_le.text())
        self.save_file_names = []
        for target in self.targets:
            target_dir, target_file = os.path.split(target)
            target2 = os.path.join(target_dir, '4in1_'+ target_file)

            self.target_le.setText(target_dir)
            self.save_file_names.append(target2)
        # print(self.save_file_names)
    # 保存的视频文件名称，要写上后缀名
    def select_target(self):
        # target, fileType = QFileDialog.getSaveFileName(self, "选择保存路径", "C:/Users/29125/PycharmProjects/video4in1")
        open_dic = "C:/Users/29125/PycharmProjects/video4in1"
        target = QFileDialog.getExistingDirectory(self, "选择保存路径", self.target_le.text())
        self.target_le.setText(str(target))

    def addNum(self):
        print('执行操作的文件数量：',len(self.save_file_names))
        target = self.target_le.text().strip()  # 获取剪切后视频保存的文件夹

        if self.is_running ==0:
            self.t1 = threading.Thread(target=run4in1_thread,
                                              args=(self.targets, self.save_file_names,self.progressBar))
            # self.progressBar.setValue(i / len(result_ads) * 100)
            self.t1.is_alive()
            self.t1.start()
            self.is_running = 1
            self.save_btn.setText("中止")

        else:
            # self.t1.terminate()
            self.is_running = 0
            self.save_btn.setText("开始")
        # run4in1(source , target)

        # start_time = self.start_le.text().strip()  # 获取开始剪切时间
        # stop_time = self.stop_le.text().strip()  # 获取剪切的结束时间
        # video = VideoFileClip(source)  # 视频文件加载
        # video = video.subclip(int(start_time), int(stop_time))  # 执行剪切操作
        # video.to_videofile(target, fps=20, remove_temp=True)  # 输出文件
        # self.result_le.setText("ok!")  # 输出文件后界面返回OK
        # self.result_le.setStyleSheet("color:red;font-size:40px")  # 设置OK颜色为红色，大小为四十像素
        # self.result_le.setAlignment(Qt.AlignCenter)  # OK在指定框内居中



if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = login()
    sys.exit(app.exec_())