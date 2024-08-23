import sys
import os
from PySide2 import QtWidgets,QtCore,QtGui
from PySide2.QtWidgets import *
from PySide2.QtGui import *
from PySide2.QtCore import * 
import json
import subprocess
HEADERS = [
    "",
    "Project Name",
    "Project Version",
    "Project Folder Path",
    ]
CHECKBOX = 0
PROJECT_NAME = 1
PROJECT_VERSION = 2
PROJECT_PATH = 3

SVN_SETTING = {
    "svn": "C:/Program Files/TortoiseSVN/bin",
    "closOtion" : " /closeonend:0"
}

COPYRIGHT = "Copyright (C) Studio EON"
VERSION = "4.1"

class SVN(QWidget):
    def __init__(self):
        super().__init__()
        self.project_list = []
        self.project_names = []
        self.svn_action_information = []
        self.josn_information = {}
        self.public_list = []
        self.check_box_list = []
        self.test_bool = True
        self.users_path = os.path.expanduser('~')

        file_path = os.path.dirname(__file__)
        icon_path = str(file_path) + r"\icon"

        self.folder_icon_path = icon_path + r"\folder.png"
        self.setWindowIcon(QIcon(icon_path+r"\svn_icon.png"))

        self.setWindowTitle("SVN Action Tool")
        self.resize(850,450)
        self.Main_layout()
        self.Button_Click_Evnet()
        self.init_table_widget()

        

    def Work_project_list_layout(self):

        work_project_groupbox = QGroupBox()
        work_project_vbox = QVBoxLayout()
        work_project_hbox = QHBoxLayout()

        project_list_lb = QLabel("SVN Action Tool")
        self.work_project_add_button = QPushButton("Project ADD")
        self.work_project_delete_button = QPushButton("Project Delete")

        self.work_project_tablewidget = QTableWidget()
        self.work_project_tablewidget.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.work_project_tablewidget.setColumnCount(len(HEADERS))
        self.work_project_tablewidget.setHorizontalHeaderLabels(HEADERS)
        self.work_project_tablewidget.setColumnWidth(0, self.width()*1/30)
        self.work_project_tablewidget.setColumnWidth(1, self.width()*1/8)
        self.work_project_tablewidget.setColumnWidth(2, self.width()*1/8)
        self.work_project_tablewidget.horizontalHeader().setSectionResizeMode(3, QHeaderView.Stretch)

        work_project_hbox.addWidget(project_list_lb)
        work_project_hbox.addWidget(self.work_project_add_button)
        work_project_hbox.addWidget(self.work_project_delete_button)

        work_project_vbox.addLayout(work_project_hbox)
        work_project_vbox.addWidget(self.work_project_tablewidget)

        work_project_groupbox.setLayout(work_project_vbox)

        return work_project_groupbox


    def Public_project_list_layout(self):        
        tab1 = QTabWidget()
        public_project53_groupbox = QGroupBox()

        eon_set53_hbox = QHBoxLayout()
        eon_prj53_hbox = QHBoxLayout()
        eon_lib53_hbox = QHBoxLayout()
        public_project53_vbox = QVBoxLayout()
        ipx_prj53_hbox = QHBoxLayout()

        self.eon_set53_checkbox = QCheckBox()
        self.eon_set53_lb = QLabel("Eon Set53")
        self.eon_set53_lineedit = QLineEdit()
        self.eon_set53_lineedit.setReadOnly(True)
        self.eon_set53_button = QPushButton()
        self.eon_set53_button.setIconSize(QSize(20,20))
        self.eon_set53_button.setIcon(QIcon(self.folder_icon_path))

        self.eon_prj53_checkbox = QCheckBox()
        self.eon_prj53_lb = QLabel("Eon Prj53")
        self.eon_prj53_lineedit = QLineEdit()
        self.eon_prj53_lineedit.setReadOnly(True)
        self.eon_prj53_button = QPushButton()
        self.eon_prj53_button.setIconSize(QSize(20,20))
        self.eon_prj53_button.setIcon(QIcon(self.folder_icon_path))

        self.eon_lib53_checkbox = QCheckBox()
        self.eon_lib53_lb = QLabel("Eon Lib53")
        self.eon_lib53_lineedit = QLineEdit()
        self.eon_lib53_lineedit.setReadOnly(True)
        self.eon_lib53_button = QPushButton()
        self.eon_lib53_button.setIconSize(QSize(20,20))
        self.eon_lib53_button.setIcon(QIcon(self.folder_icon_path))

        self.ipx_prj53_checkbox = QCheckBox()
        self.ipx_prj53_lb = QLabel("IPX prj53")
        self.ipx_prj53_lineedit = QLineEdit()
        self.ipx_prj53_lineedit.setReadOnly(True)
        self.ipx_prj53_button = QPushButton()
        self.ipx_prj53_button.setIconSize(QSize(20,20))
        self.ipx_prj53_button.setIcon(QIcon(self.folder_icon_path))

        eon_set53_hbox.addWidget(self.eon_set53_checkbox)
        eon_set53_hbox.addWidget(self.eon_set53_lb)
        eon_set53_hbox.addWidget(self.eon_set53_lineedit)
        eon_set53_hbox.addWidget(self.eon_set53_button)

        eon_prj53_hbox.addWidget(self.eon_prj53_checkbox)
        eon_prj53_hbox.addWidget(self.eon_prj53_lb)
        eon_prj53_hbox.addWidget(self.eon_prj53_lineedit)
        eon_prj53_hbox.addWidget(self.eon_prj53_button)
    
        eon_lib53_hbox.addWidget(self.eon_lib53_checkbox)
        eon_lib53_hbox.addWidget(self.eon_lib53_lb)
        eon_lib53_hbox.addWidget(self.eon_lib53_lineedit)
        eon_lib53_hbox.addWidget(self.eon_lib53_button)

        ipx_prj53_hbox.addWidget(self.ipx_prj53_checkbox)
        ipx_prj53_hbox.addWidget(self.ipx_prj53_lb)
        ipx_prj53_hbox.addWidget(self.ipx_prj53_lineedit)
        ipx_prj53_hbox.addWidget(self.ipx_prj53_button)

        public_project53_vbox.addLayout(eon_set53_hbox)
        public_project53_vbox.addLayout(eon_prj53_hbox)
        public_project53_vbox.addLayout(eon_lib53_hbox)
        public_project53_vbox.addLayout(ipx_prj53_hbox)


        public_project53_groupbox.setLayout(public_project53_vbox)

        tab1.addTab(public_project53_groupbox,"5.3")

        return tab1


    def SVN_action_layout(self):
        svn_action_groupbox = QGroupBox()
        svn_button_hbox = QHBoxLayout()
        svn_action_vbox = QVBoxLayout()
        test_vbox = QHBoxLayout()

        self.svn_check_project_list = QLineEdit()
        self.svn_check_project_list.setReadOnly(True)
        svn_action_list_lb = QLabel("SVN 작업 리스트 목록")
        self.check_box_all = QPushButton("Select All")
        self.svn_mklink_button = QPushButton("Mklink")
        self.svn_cleanup_button = QPushButton("Cleanup")
        self.svn_update_button = QPushButton("Update")

        test_vbox.addWidget(svn_action_list_lb)
        test_vbox.addWidget(self.check_box_all)
        
        svn_button_hbox.addWidget(self.svn_mklink_button)
        svn_button_hbox.addWidget(self.svn_cleanup_button)
        svn_button_hbox.addWidget(self.svn_update_button)

        svn_action_vbox.addLayout(test_vbox)
        svn_action_vbox.addWidget(self.svn_check_project_list)
        svn_action_vbox.addLayout(svn_button_hbox)

        svn_action_groupbox.setLayout(svn_action_vbox)

        return svn_action_groupbox
    
    def About_Layout(self):
        about_layout_groupbox = QGroupBox()
        copyright_lb = QLabel(COPYRIGHT)
        version_lb = QLabel("V"+VERSION)
        about_layout = QHBoxLayout()

        about_layout.addWidget(copyright_lb)
        about_layout.addStretch()
        about_layout.addWidget(version_lb)

        about_layout_groupbox.setLayout(about_layout)
        
        return about_layout_groupbox

    def Main_layout(self):
        main_layout = QGridLayout(self)
        main_layout.addWidget(self.Work_project_list_layout(),0,0,1,2)
        main_layout.addWidget(self.Public_project_list_layout(),1,0)
        main_layout.addWidget(self.SVN_action_layout(),1,1)
        main_layout.addWidget(self.About_Layout(),2,0,1,2)


    def Button_Click_Evnet(self):

        self.work_project_add_button.clicked.connect(self.Table_ADD_Button_Click_Event)
        self.work_project_delete_button.clicked.connect(self.Table_Delete_Button_Click_Event)

        self.eon_set53_button.clicked.connect(lambda : self.Public_Button_Click_Event(self.eon_set53_lb,self.eon_set53_lineedit))
        self.eon_prj53_button.clicked.connect(lambda : self.Public_Button_Click_Event(self.eon_prj53_lb,self.eon_prj53_lineedit))
        self.eon_lib53_button.clicked.connect(lambda : self.Public_Button_Click_Event(self.eon_lib53_lb,self.eon_lib53_lineedit))

        self.ipx_prj53_button.clicked.connect(lambda : self.Public_Button_Click_Event(self.ipx_prj53_lb,self.ipx_prj53_lineedit))

        self.eon_set53_checkbox.pressed.connect(lambda : self.Public_CheckBox_Clicked(self.eon_set53_checkbox,self.eon_set53_lb,self.eon_set53_lineedit))
        self.eon_prj53_checkbox.pressed.connect(lambda : self.Public_CheckBox_Clicked(self.eon_prj53_checkbox,self.eon_prj53_lb,self.eon_prj53_lineedit))
        self.eon_lib53_checkbox.pressed.connect(lambda : self.Public_CheckBox_Clicked(self.eon_lib53_checkbox,self.eon_lib53_lb,self.eon_lib53_lineedit))

        self.ipx_prj53_checkbox.pressed.connect(lambda : self.Public_CheckBox_Clicked(self.ipx_prj53_checkbox,self.ipx_prj53_lb,self.ipx_prj53_lineedit))

        self.svn_mklink_button.clicked.connect(self.SVN_Mklink_Button_Click_Event)
        self.svn_cleanup_button.clicked.connect(self.SVN_Cleanup_Button_Click_Event)
        self.svn_update_button.clicked.connect(self.SVN_Update_Button_Click_Evnet)

        self.check_box_all.clicked.connect(self.Select_All)



    def init_table_widget(self):
        # ini파일을 읽어와서 widget이 실행하면 tablewidget에 값을 넣어준다.
        josn_file = "{}\\SVN_Action_Json.json".format(self.users_path)
        if os.path.isfile(josn_file):
            with open(josn_file) as jn:
                json_object = json.load(jn)
            
            try:
                for i in range(len(json_object["project"])):
                    project_name = json_object["project"][i]["project_name"]
                    project_version = json_object["project"][i]["project_version"]
                    project_path = json_object["project"][i]["project_path"]
                    
                    if not os.path.isfile(project_path +"/"+ project_name + ".uproject"):
                        continue

                    self.project_checkbox = QCheckBox(self)
                    self.work_project_tablewidget.insertRow(i)
                    self.work_project_tablewidget.setCellWidget(i,CHECKBOX,self.project_checkbox)
                    self.work_project_tablewidget.setItem(i,PROJECT_NAME,QTableWidgetItem(project_name))
                    self.work_project_tablewidget.setItem(i,PROJECT_VERSION,QTableWidgetItem(project_version))
                    self.work_project_tablewidget.setItem(i,PROJECT_PATH,QTableWidgetItem(project_path))
                    self.project_checkbox.pressed.connect(self.Project_CheckBox_Clicked)

                    self.project_list.append({"project_name":project_name,"project_path":project_path,"project_version":project_version})        
                
                for p in range(len(json_object["public_project"])):
                    public_project_name = json_object["public_project"][p]["project_name"]
                    public_project_path = json_object["public_project"][p]["project_path"]
                    public_project_version = json_object["public_project"][p]["project_version"]

                    if not os.path.isfile(public_project_path +"/"+ public_project_name + ".uproject"):
                        continue

                    if public_project_name == "eon_set53": self.eon_set53_lineedit.setText(public_project_path)
                    if public_project_name == "eon_lib53": self.eon_lib53_lineedit.setText(public_project_path)
                    if public_project_name == "eon_prj53": self.eon_prj53_lineedit.setText(public_project_path)
                    if public_project_name == "IPX_prj53": self.ipx_prj53_lineedit.setText(public_project_path)
                
                    
                    self.public_list.append({"project_name":public_project_name,"project_path":public_project_path,"project_version":public_project_version})  
            except:
                pass
        
        else:
            with open("{}\\SVN_Action_Json.json".format(self.users_path),"w") as jn:
                json.dump(self.josn_information,jn,sort_keys=True,indent=4)


    def Table_ADD_Button_Click_Event(self):
        # add 버튼 클릭시 폴더 선택 창이 나온 후 폴더를 선택하면 tablewidget에 선택한 폴더의 이름 주소를 넣어준다.
        project_folder_path=QFileDialog.getExistingDirectory(self)
        public_project_name = ["eon_set","eon_lib","eon_prj"]

        if project_folder_path:

            for i in public_project_name:
                if i in project_folder_path:
                    QMessageBox.information(self,"ㅎ.ㅎ","공용 프로젝트는 아래에 첨부 해주세요!")
                    return

            for file_in_folder in os.listdir(project_folder_path):
                if ".uproject" in file_in_folder:
                    project_file = project_folder_path +"/"+ file_in_folder 
                    self.project_checkbox = QCheckBox(self)

                    with open(project_file) as uproject:
                        unreal_version = json.load(uproject)
                        project_version = unreal_version["EngineAssociation"]

                    for i in self.project_list:
                        if i == {"project_name":file_in_folder.split(".uproject")[0],"project_path":project_folder_path,"project_version":project_version}:
                            QMessageBox.information(self,"메시지","이미 존재 합니다.")
                            return

                    rowcount = self.work_project_tablewidget.rowCount()
                    self.work_project_tablewidget.insertRow(rowcount)

                    self.work_project_tablewidget.setCellWidget(rowcount,CHECKBOX,self.project_checkbox)
                    self.work_project_tablewidget.setItem(rowcount,PROJECT_NAME,QTableWidgetItem(file_in_folder.split(".uproject")[0]))
                    self.work_project_tablewidget.setItem(rowcount,PROJECT_VERSION,QTableWidgetItem(project_version))
                    self.work_project_tablewidget.setItem(rowcount,PROJECT_PATH,QTableWidgetItem(project_folder_path))
                    
                    self.project_checkbox.pressed.connect(self.Project_CheckBox_Clicked)
                    self.project_list.append({"project_name":file_in_folder.split(".uproject")[0],"project_path":project_folder_path,"project_version":project_version})


        
    def Select_All(self):
        # public_checkBox_list = [self.eon_set_checkbox,self.eon_prj_checkbox,self.eon_lib_checkbox,self.eon_set52_checkbox,self.eon_prj52_checkbox,self.eon_lib52_checkbox,self.eon_set53_checkbox,self.eon_prj53_checkbox,self.eon_lib53_checkbox]
        # public_label_list = [self.eon_set_lb,self.eon_prj_lb,self.eon_lib_lb,self.eon_set52_lb,self.eon_prj52_lb,self.eon_lib52_lb,self.eon_set53_lb,self.eon_prj53_lb,self.eon_lib53_lb]
        # public_lineedit_list = [self.eon_set_lineedit,self.eon_prj_lineedit,self.eon_lib_lineedit,self.eon_set52_lineedit,self.eon_prj52_lineedit,self.eon_lib52_lineedit,self.eon_set53_lineedit,self.eon_prj53_lineedit,self.eon_lib53_lineedit]

        public_checkBox_list = [self.eon_set53_checkbox,self.eon_prj53_checkbox,self.eon_lib53_checkbox,self.ipx_prj53_checkbox]
        public_label_list = [self.eon_set53_lb,self.eon_prj53_lb,self.eon_lib53_lb,self.ipx_prj53_lb]
        public_lineedit_list = [self.eon_set53_lineedit,self.eon_prj53_lineedit,self.eon_lib53_lineedit,self.ipx_prj53_lineedit]

        self.svn_action_information = []
        self.svn_check_project_list.clear()
        self.project_names = []
        
        if self.test_bool:                
            for i in range(len(public_checkBox_list)):
                if public_lineedit_list[i].text():
                    public_checkBox_list[i].setChecked(True)

                    self.project_names.append(public_label_list[i].text())

                    public_project_path = public_lineedit_list[i].text()
                    public_project_name = public_lineedit_list[i].text().split("/")[-1]
                    
                    project_file = public_project_path +"/"+ public_project_name +".uproject"

                    with open(project_file) as uproject:
                        unreal_version = json.load(uproject)
                        project_version = unreal_version["EngineAssociation"]
                    
                    self.svn_action_information.append({"project_name":public_project_name,"project_path":public_project_path,"project_version":project_version})

                    self.svn_check_project_list.setText(''.join(str(element)+"," for element in self.project_names))


            for project_checkbox in range(self.work_project_tablewidget.rowCount()):
                self.work_project_tablewidget.cellWidget(project_checkbox,CHECKBOX).setChecked(True)

                project_name = self.work_project_tablewidget.item(project_checkbox,PROJECT_NAME).text()
                project_version = self.work_project_tablewidget.item(project_checkbox,PROJECT_VERSION).text()
                project_path = self.work_project_tablewidget.item(project_checkbox,PROJECT_PATH).text()

                self.project_names.append(project_name)
                self.svn_action_information.append({"project_name":project_name,"project_path":project_path,"project_version":project_version})
                self.svn_check_project_list.setText(''.join(str(element)+"," for element in self.project_names))

            self.test_bool = False

        else:
            for public_checkBox in public_checkBox_list:
                public_checkBox.setChecked(False)

            for project_checkbox in range(self.work_project_tablewidget.rowCount()):
                self.work_project_tablewidget.cellWidget(project_checkbox,CHECKBOX).setChecked(False)

            self.svn_action_information = []
            self.svn_check_project_list.clear()
            self.project_names = []
            self.test_bool = True
    

    def Table_Delete_Button_Click_Event(self):
        # delete 버튼 클릭시 호출 ( 선택한 row의 path값을 가져와 project_list에 remove 해준다)
        table_row = self.work_project_tablewidget.currentRow()
        
        if table_row >= 0:
            remove_project_name = self.work_project_tablewidget.item(table_row,PROJECT_NAME).text()
            remove_project_version = self.work_project_tablewidget.item(table_row,PROJECT_VERSION).text()
            remove_project_path = self.work_project_tablewidget.item(table_row,PROJECT_PATH).text()
            
            current_text = self.svn_check_project_list.text()
            try:
                if current_text:
                    remove_text = current_text.replace(remove_project_name+",","").strip()

                    self.svn_check_project_list.setText(remove_text)
                    self.svn_action_information.remove({"project_name":remove_project_name,"project_path":remove_project_path,"project_version":remove_project_version})
                    self.project_names.remove(remove_project_name)
            except:
                pass
            self.project_list.remove({"project_name":remove_project_name,"project_path":remove_project_path,"project_version":remove_project_version})
            self.work_project_tablewidget.removeRow(table_row)


    def Project_CheckBox_Clicked(self):
        table_row = self.work_project_tablewidget.currentRow()
        project_name = self.work_project_tablewidget.item(table_row,PROJECT_NAME).text()
        project_version = self.work_project_tablewidget.item(table_row,PROJECT_VERSION).text()
        project_path = self.work_project_tablewidget.item(table_row,PROJECT_PATH).text()

        #체크박스를 클릭 했을 때 false여서 추가 삭제 위치 변경함
        if self.work_project_tablewidget.cellWidget(table_row,CHECKBOX).isChecked():
            # 체크 아웃을 하면 LineEdit에 값을 없애준다.
            try:
                current_text = self.svn_check_project_list.text()
                remove_text = current_text.replace(project_name+",","").strip()

                self.svn_action_information.remove({"project_name":project_name,"project_path":project_path,"project_version":project_version})
                self.project_names.remove(project_name)
            except:
                pass
        else:
            #project table widget에 체크 박스를 클릭 하였을때 svn action 에 있는 LineEdit에 값을 넣어준다
            self.project_names.append(project_name)
            self.svn_action_information.append({"project_name":project_name,"project_path":project_path,"project_version":project_version})
            
        self.svn_check_project_list.setText(''.join(str(element)+"," for element in self.project_names))
            


    def Public_Button_Click_Event(self,project_label,project_lineedit):
        project_path = QFileDialog.getExistingDirectory(self)
        # public 프로젝트도 list에 넣어줘야 하니까 path 가져오는 걸로 값 만들어 줘야 할듯
        if project_path.split("/")[-1] == project_label.text().lower().replace(" ","_") or project_path.split("/")[-1] == "IPX_prj53":
            project_lineedit.setText(project_path)  
            project_name = project_path.split("/")[-1]
            project_file = project_path +"/"+ project_path.split("/")[-1] +".uproject"

            with open(project_file) as uproject:
                unreal_version = json.load(uproject)
                project_version = unreal_version["EngineAssociation"]

            self.public_list.append({"project_name":project_name,"project_path":project_path,"project_version":project_version})
        
        else:
            project_lineedit.setPlaceholderText("다시 입력해 주시요")


    def Public_CheckBox_Clicked(self,public_checkbox,public_label,public_lineedit):
        if public_lineedit.text():
            if public_checkbox.isChecked():
                
                # 체크 아웃을 하면 LineEdit에 값을 없애준다.
                current_text = self.svn_check_project_list.text()
                remove_text = current_text.replace(public_label.text()+",","").strip()

                public_project_name = public_lineedit.text().split("/")[-1]
                public_project_path = public_lineedit.text()

                project_file = public_project_path +"/"+ public_project_name +".uproject"

                with open(project_file) as uproject:
                    unreal_version = json.load(uproject)
                    project_version = unreal_version["EngineAssociation"]

                self.svn_check_project_list.setText(remove_text)
                try:
                    for i in self.svn_action_information:
                        if i == {"project_name":public_project_name,"project_path":public_project_path,"project_version":project_version}:
                            self.svn_action_information.remove({"project_name":public_project_name,"project_path":public_project_path,"project_version":project_version})
                    self.project_names.remove(public_label.text())
                except:
                    pass

            else:
                self.project_names.append(public_label.text())            

                public_project_name = public_lineedit.text().split("/")[-1]
                public_project_path = public_lineedit.text()
                
                project_file = public_project_path +"/"+ public_project_name +".uproject"

                with open(project_file) as uproject:
                    unreal_version = json.load(uproject)
                    project_version = unreal_version["EngineAssociation"]
                
                self.svn_action_information.append({"project_name":public_project_name,"project_path":public_project_path,"project_version":project_version})

                self.svn_check_project_list.setText(''.join(str(element)+"," for element in self.project_names))
            
                

    def SVN_Mklink_Button_Click_Event(self):
        cmd = []
        existence_count = 0
        failed_count = 0
        success_count = 0
        Administrator_count = 0
        failed_list = []
        Administrator_list = []
        text = ""
        eon_set53_path = ""
        eon_prj53_path = ""
        eon_lib53_path = ""
        ipx_prj53_path = ""
        
        if len(self.public_list) > 0:
            for p in range(len(self.public_list)):
                if self.public_list[p]["project_name"] == "eon_set53": eon_set53_path = self.public_list[p]["project_path"]
                elif self.public_list[p]["project_name"] == "eon_prj53": eon_prj53_path = self.public_list[p]["project_path"]
                elif self.public_list[p]["project_name"] == "eon_lib53": eon_lib53_path = self.public_list[p]["project_path"]
                elif self.public_list[p]["project_name"] == "IPX_prj53": ipx_prj53_path = self.public_list[p]["project_path"]

        else:
            QMessageBox.information(self,"메시지","공유 프로젝트를 추가 해주세요")
            return
        
        if len(self.svn_action_information) > 0:
            for i in range(len(self.svn_action_information)):
                project_version = self.svn_action_information[i]["project_version"]
                mklink_file_path = self.svn_action_information[i]["project_path"] + "/mklink.bat"
                
                if os.path.isfile(mklink_file_path):

                    if project_version == "5.3":
                        
                        if not eon_set53_path or not eon_prj53_path or not eon_lib53_path:
                            project_path = self.svn_action_information[i]["project_name"]
                            text += project_path + " "
                            continue

                        if "IPX_prj53" == self.svn_action_information[i]["project_name"] or "AS_ACES" == self.svn_action_information[i]["project_name"] or "gas1_ACES" == self.svn_action_information[i]["project_name"]:
                            # 연결하면 안되는 프로젝트
                            continue
                        
                        project_path = self.svn_action_information[i]["project_path"]

                        if self.svn_action_information[i]["project_name"] == "eon_prj53" or self.svn_action_information[i]["project_name"] == "eon_lib53":
                            MSPresets = "mklink /d " +"{}\Content\MSPresets {}\Content\MSPresets".format(project_path,eon_set53_path).replace("/","\\")
                            Master_mat = "mklink /d " +"{}\Content\Asset\Master_mat {}\Content\Asset\Master_mat".format(project_path,eon_set53_path).replace("/","\\")
                            Master_mat_5_3 = "mklink /d " +"{}\Content\Asset\Master_mat_5_3 {}\Content\Asset\Master_mat_5_3".format(project_path,eon_set53_path).replace("/","\\")
                            Setup = "mklink /d " +"{}\Content\Setup {}\Content\Setup".format(project_path,eon_set53_path).replace("/","\\")
                            Plugins = "mklink /d " +"{}\Plugins {}\Plugins".format(project_path,eon_set53_path).replace("/","\\")
                            cmd.append(MSPresets)
                            cmd.append(Master_mat)
                            cmd.append(Master_mat_5_3)
                            cmd.append(Setup)
                            cmd.append(Plugins)
                        
                        elif "IPX_" in self.svn_action_information[i]["project_name"] and "IPX_prj53" != self.svn_action_information[i]["project_name"]:
                            eon_city = "mklink /d " +"{}\Content\Asset\eon_city {}\Content\Asset\eon_city".format(project_path,ipx_prj53_path).replace("/","\\")
                            eon_nature = "mklink /d " + "{}\Content\Asset\eon_nature {}\Content\Asset\eon_nature".format(project_path,ipx_prj53_path).replace("/","\\")
                            eon_prj = "mklink /d " + "{}\Content\Asset\eon_prj {}\Content\Asset\eon_prj".format(project_path,ipx_prj53_path).replace("/","\\")
                            eon_vehicle = "mklink /d " + "{}\Content\Asset\eon_vehicle {}\Content\Asset\eon_vehicle".format(project_path,ipx_prj53_path).replace("/","\\")
                            fx = "mklink /d " + "{}\Content\Asset\FX {}\Content\Asset\FX".format(project_path,ipx_prj53_path).replace("/","\\")
                            Lighting = "mklink /d " + "{}\Content\Asset\Lighting {}\Content\Asset\Lighting".format(project_path,ipx_prj53_path).replace("/","\\")
                            Master_mat = "mklink /d " + "{}\Content\Asset\Master_mat {}\Content\Asset\Master_mat".format(project_path,ipx_prj53_path).replace("/","\\")
                            Master_mat_5_2 = "mklink /d " + "{}\Content\Asset\Master_mat_5_2 {}\Content\Asset\Master_mat_5_2".format(project_path,ipx_prj53_path).replace("/","\\")
                            skeletal = "mklink /d " + "{}\Content\Asset\skeletal {}\Content\Asset\skeletal".format(project_path,ipx_prj53_path).replace("/","\\")
                            Wade_Cloth_0015_Test = "mklink /d " + "{}\Content\Asset\Wade_Cloth_0015_Test {}\Content\Asset\Wade_Cloth_0015_Test".format(project_path,ipx_prj53_path).replace("/","\\")
                            MSPresets = "mklink /d " + "{}\Content\MSPresets {}\Content\MSPresets".format(project_path,ipx_prj53_path).replace("/","\\")
                            Setup = "mklink /d " + "{}\Content\Setup {}\Content\Setup".format(project_path,ipx_prj53_path).replace("/","\\")
                            CC_Rigs = "mklink /d " + "{}\Content\CC_Rigs {}\Content\CC_Rigs".format(project_path,ipx_prj53_path).replace("/","\\")
                            eon_bp_node = "mklink /d " + "{}\Plugins\EonBPnode {}\Plugins\EonBPnode".format(project_path,ipx_prj53_path).replace("/","\\")

                            cmd.append(eon_city)
                            cmd.append(eon_nature)
                            cmd.append(eon_prj)
                            cmd.append(eon_vehicle)
                            cmd.append(fx)
                            cmd.append(Lighting)
                            cmd.append(Master_mat)
                            cmd.append(Master_mat_5_2)
                            cmd.append(skeletal)
                            cmd.append(Wade_Cloth_0015_Test)
                            cmd.append(MSPresets)
                            cmd.append(Setup)
                            cmd.append(CC_Rigs)
                            cmd.append(eon_bp_node)


                        else:
                            MSPresets = "mklink /d " +"{}\Content\MSPresets {}\Content\MSPresets".format(project_path,eon_set53_path).replace("/","\\")
                            Master_mat = "mklink /d " +"{}\Content\Asset\Master_mat {}\Content\Asset\Master_mat".format(project_path,eon_set53_path).replace("/","\\")
                            Master_mat_5_3 = "mklink /d " +"{}\Content\Asset\Master_mat_5_3 {}\Content\Asset\Master_mat_5_3".format(project_path,eon_set53_path).replace("/","\\")
                            Setup = "mklink /d " +"{}\Content\Setup {}\Content\Setup".format(project_path,eon_set53_path).replace("/","\\")
                            EonBPnode = "mklink /d " +"{}\Plugins\EonBPnode {}\Plugins\EonBPnode".format(project_path,eon_set53_path).replace("/","\\")
                            HoudiniNiagara = "mklink /d " +"{}\Plugins\HoudiniNiagara {}\Plugins\HoudiniNiagara".format(project_path,eon_set53_path).replace("/","\\")
                            MoviePipelineDeadline = "mklink /d " +"{}\Plugins\MoviePipelineDeadline {}\Plugins\MoviePipelineDeadline".format(project_path,eon_set53_path).replace("/","\\")
                            Oceanology_Plugin = "mklink /d " +"{}\Plugins\Oceanology_Plugin {}\Plugins\Oceanology_Plugin".format(project_path,eon_set53_path).replace("/","\\")
                            RLPlugin = "mklink /d " +"{}\Plugins\RLPlugin {}\Plugins\RLPlugin".format(project_path,eon_set53_path).replace("/","\\")
                            SideFX_Labs = "mklink /d " +"{}\Plugins\SideFX_Labs {}\Plugins\SideFX_Labs".format(project_path,eon_set53_path).replace("/","\\")
                            UnrealDeadlineService = "mklink /d " +"{}/Plugins/UnrealDeadlineService {}/Plugins/UnrealDeadlineService".format(project_path,eon_set53_path).replace("/","\\")
                            eon_city = "mklink /d " +"{}\Content\Asset\eon_city {}\Content\Asset\eon_city".format(project_path,eon_lib53_path).replace("/","\\")
                            eon_nature = "mklink /d " +"{}\Content\Asset\eon_nature {}\Content\Asset\eon_nature".format(project_path,eon_lib53_path).replace("/","\\")
                            eon_vehicle = "mklink /d " +"{}\Content\Asset\eon_vehicle {}\Content\Asset\eon_vehicle".format(project_path,eon_lib53_path).replace("/","\\")
                            eon_ch = "mklink /d " +"{}\Content\Asset\eon_ch {}\Content\Asset\eon_ch".format(project_path,eon_lib53_path).replace("/","\\")
                            skeletal = "mklink /d " +"{}\Content\Asset\skeletal {}\Content\Asset\skeletal".format(project_path,eon_lib53_path).replace("/","\\")
                            fx = "mklink /d " +"{}\Content\Asset\FX {}\Content\Asset\FX".format(project_path,eon_lib53_path).replace("/","\\")
                            Lighting = "mklink /d " +"{}\Content\Asset\Lighting {}\Content\Asset\Lighting".format(project_path,eon_lib53_path).replace("/","\\")
                            eon_prj = "mklink /d " +"{}\Content\Asset\eon_prj {}\Content\Asset\eon_prj".format(project_path,eon_prj53_path).replace("/","\\")
                
                            cmd.append(MSPresets)
                            cmd.append(Master_mat)
                            cmd.append(Master_mat_5_3)
                            cmd.append(Setup)
                            cmd.append(EonBPnode)
                            cmd.append(HoudiniNiagara)
                            cmd.append(MoviePipelineDeadline)
                            cmd.append(Oceanology_Plugin)
                            cmd.append(RLPlugin)
                            cmd.append(SideFX_Labs)
                            cmd.append(UnrealDeadlineService)
                            cmd.append(eon_city)
                            cmd.append(eon_nature)
                            cmd.append(eon_vehicle)
                            cmd.append(eon_ch)
                            cmd.append(skeletal)
                            cmd.append(fx)
                            cmd.append(Lighting)
                            cmd.append(eon_prj)

            existence = ""#이미 있는거
            failed = "지정된 경로를 찾을 수 없습니다.\n" # 연구소
            amin = "이 작업을 수행할 수 있는 권한이 없습니다.\n"
            success = "" #
            
            if len(cmd) == 0:
                QMessageBox.information(self,"!","프로젝트 폴더에 Mklink 배치파일 없어서 종료합니다.")
                return  

            for i in cmd:
                result = subprocess.run(i, capture_output= True,text=True,shell=True)
                print(result)
                
                if result.stdout == existence: 
                    existence_count = existence_count + 1

                if result.stderr == amin:
                    Administrator_count = Administrator_count + 1
                    Administrator = i.split(" ")[2].replace("\\","/")
                    Administrator_list.append(Administrator)
                    
                elif result.stderr == failed: 
                    failed_count = failed_count + 1
                    failed = result.args.split(" ")[-2]
                    failed_list.append(failed)

                elif not result.stdout == success:
                    success_count = success_count + 1

            if failed_count > 0:
                QMessageBox.information(self,"오류","{}\n폴더의 주소가 오류가 있습니다. 확인 부탁드립니다.".format("\n".join(failed_list)))
                return            

            if text:                    
                QMessageBox.information(self,"메시지","성공 : {}개\n이미 링크 중 : {}개\n링크 연결을 완료 했습니다!\n< {} >\n해당 프로젝트는 링크 연결에 실패하였습니다.\n공유 프로젝트 주소가 있는지 확인 해주세요".format(success_count,existence_count,text))
                return
            
            if Administrator_count > 0:
                QMessageBox.information(self,"관리자 권한 필요","{} 링크하기 위해서는 관리자 권한이 필요합니다.".format(Administrator_list))
                return
            
            QMessageBox.information(self,"완료","성공 : {}개\n이미 링크 중 : {}개\n링크 연결을 완료 했습니다!".format(success_count,existence_count))
        
        else:
            QMessageBox.information(self,"추가","리스트 목록에 추가 해주세요")

    def SVN_Cleanup_Button_Click_Event(self):

        if len(self.svn_action_information) > 0:
            project_paths = []
            for i in range(len(self.svn_action_information)):
                project_paths.append(self.svn_action_information[i]["project_path"])
            cmd = "TortoiseProc.exe /command:cleanup  /path:{}".format("*".join(project_paths)) + SVN_SETTING["closOtion"]
            subprocess.Popen(cmd, shell=True)
        else:
            QMessageBox.information(self,"추가","리스트 목록에 추가 해주세요")

    def SVN_Update_Button_Click_Evnet(self):
        #project table widget에서 체크를 하면 값을 가져와서 업데이트를 한다.
        project_paths = []
        if len(self.svn_action_information) > 0:
            for i in range(len(self.svn_action_information)):
                project_paths.append(self.svn_action_information[i]["project_path"])
            cmd = "TortoiseProc.exe /command:update  /path:{}".format("*".join(project_paths)) + SVN_SETTING["closOtion"]
            self.result = subprocess.Popen(cmd, shell=True, text = True)
            
        else:
            QMessageBox.information(self,"추가","리스트 목록에 추가 해주세요")
            

    def closeEvent(self, event):
        #종료 이벤트 종료하면 tablewidget에 있는 값을 project_list에 저장하여 ini 파일에 저장
        public_project_duplicate_check = []
        self.josn_information["project"] = self.project_list
        
        for item in self.public_list:
            if item not in public_project_duplicate_check:
                public_project_duplicate_check.append(item)
        
        self.josn_information["public_project"] = public_project_duplicate_check

        with open("{}\\SVN_Action_Json.json".format(self.users_path),"w") as jn:
            json.dump(self.josn_information,jn,sort_keys=True,indent=4)


    

if __name__ == "__main__":
    app = QApplication(sys.argv)
    form = SVN()
    form.show()
    app.exec_()