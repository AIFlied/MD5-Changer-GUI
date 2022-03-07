################
# Version 0.01 #
################

import wx
import os
import random

def changemd5(filelist):
    for ffile in filelist:
        with open(ffile,'a') as f:
            for i in range(1,random.randint(2,5)):
                f.write(' ')

def listdir(path, list_name):
    for file in os.listdir(path):  
        file_path = os.path.join(path, file)  
        if os.path.isdir(file_path):  
            listdir(file_path, list_name)  
        else:  
            list_name.append(file_path)

file_list=''
dirname=''

class Frame(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self, None, title='MD5CHANGER_GUI', size=(593, 280),name='frame',style=541072896)
        self.mainwindow = wx.Panel(self)
        self.SetTransparent(250)
        self.mainwindow.SetOwnBackgroundColour((255, 255, 255, 255))
        self.Centre()
        self.btn_ok = wx.Button(self.mainwindow,size=(200, 60),pos=(71, 148),label='Start',name='button')
        btn_ok_FOnt = wx.Font(11,70,90,400,False,'Microsoft YaHei UI',-1)
        self.btn_ok.SetFont(btn_ok_FOnt)
        self.btn_ok.Bind(wx.EVT_BUTTON,self.btn_ok_ONClicK)
        self.btn_exit = wx.Button(self.mainwindow,size=(200, 60),pos=(302, 148),label='Exit',name='button')
        btn_exit_FOnt = wx.Font(11,70,90,400,False,'Microsoft YaHei UI',-1)
        self.btn_exit.SetFont(btn_exit_FOnt)
        self.btn_exit.Bind(wx.EVT_BUTTON,self.btn_exit_ONClicK)
        self.editbox1 = wx.TextCtrl(self.mainwindow,size=(270, 26),pos=(171, 87),value='',name='text',style=0)
        self.label1 = wx.StaticText(self.mainwindow,size=(133, 25),pos=(28, 89),label='Files or Dir Address : ',name='staticText',style=2321)
        label1_FOnt = wx.Font(10,74,90,400,False,'Microsoft YaHei UI',-1)
        self.label1.SetFont(label1_FOnt)
        self.btn_file = wx.Button(self.mainwindow,size=(103, 80),pos=(457, 35),label='File Browser',name='button')
        btn_file_FOnt = wx.Font(11,74,90,400,False,'Microsoft YaHei UI',-1)
        self.btn_file.SetFont(btn_file_FOnt)
        self.btn_file.Bind(wx.EVT_BUTTON,self.btn_file_ONClicK)
        self.combobox1 = wx.ComboBox(self.mainwindow,value='Only Selected Files',pos=(172, 37),name='comboBox',choices=['Only Selected Files', 'All Files Under the Directory'],style=16)
        self.combobox1.SetSize((268, 27))
        combobox1_FOnt = wx.Font(10,74,90,400,False,'Microsoft YaHei UI',-1)
        self.combobox1.SetFont(combobox1_FOnt)
        self.label2 = wx.StaticText(self.mainwindow,size=(124, 24),pos=(22, 41),label='Execution Mode :',name='staticText',style=2321)
        self.label2.SetForegroundColour('red')
        label2_FOnt = wx.Font(10,74,90,400,False,'Microsoft YaHei UI',-1)
        self.label2.SetFont(label2_FOnt)
        self.label_cprt = wx.StaticText(self.mainwindow,size=(80, 24),pos=(474, 238),label='By.bGVveno=',name='staticText',style=2321)
        self.label_cprt.SetForegroundColour((255, 255, 255, 255))

    def combobox1_CHOOSELISTITEM(self,event):
        self.editbox1.SetValue('')
        
    def btn_ok_ONClicK(self,event):
        if self.combobox1.GetValue() == 'Only Selected Files':
            changemd5(file_list)
            toastone = wx.MessageDialog(self,message="Complete!!",caption="Message",style= wx.YES_DEFAULT | wx.ICON_QUESTION)
            if toastone.ShowModal() == wx.ID_YES:  
                toastone.Destroy()  
                      
        elif self.combobox1.GetValue() == 'All Files Under the Directory':
            changemd5(templist)
            toastone = wx.MessageDialog(self,message="Complete!!",caption="Message",style= wx.YES_DEFAULT | wx.ICON_QUESTION)
            if toastone.ShowModal() == wx.ID_YES:  
                toastone.Destroy() 
                   

    def btn_exit_ONClicK(self,event):
        self.Destroy()
        exit()

    def btn_file_ONClicK(self,event):       
        if self.combobox1.GetValue() == 'Only Selected Files':
            filedlg=wx.FileDialog(self, message="Select Files", defaultDir='', defaultFile='', wildcard='*.*', style=wx.FD_MULTIPLE)
            if filedlg.ShowModal() == wx.ID_OK:
                global file_list
                file_list = filedlg.GetPaths()
                filelistall=""
                for i in file_list:
                    filelistall=filelistall+i
                self.editbox1.SetValue(filelistall)
                filedlg.Destroy()
        elif self.combobox1.GetValue() == 'All Files Under the Directory':
            dirdlg=wx.DirDialog(self, message="Select Directory", defaultPath='', style=0)
            if dirdlg.ShowModal() == wx.ID_OK:
                global dirname
                dirname = dirdlg.GetPath()
                self.editbox1.SetValue(dirname)
                global templist
                templist=[]
                listdir(dirname,templist)
                dirdlg.Destroy()

class myApp(wx.App):
    def  OnInit(self):
        self.frame = Frame()
        self.frame.Show(True)
        return True

if __name__ == '__main__':
    app = myApp()
    app.MainLoop()
