import wx
import os
import random

def changemd5(filelist):
    for ffile in filelist:
        with open(ffile,'a') as f:
            if ffile != 'MD5CHANGERGUI.py':
                for i in range(1,random.randint(1,5)):
                    f.write(' ')

def listdir(path, list_name):
    for file in os.listdir(path):  
        file_path = os.path.join(path, file)  
        if os.path.isdir(file_path):  
            listdir(file_path, list_name)  
        else:  
            list_name.append(file_path)
    print(list_name)

file_list=''
dirname=''

class Frame(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self, None, title='MD5CHANGER_GUI', size=(571, 301),name='frame',style=541072896)
        self.mainwindow = wx.Panel(self)
        self.SetTransparent(250)
        self.mainwindow.SetOwnBackgroundColour((255, 255, 255, 255))
        self.Centre()
        self.btn_ok = wx.Button(self.mainwindow,size=(200, 60),pos=(70, 164),label='Start',name='button')
        self.btn_ok.Bind(wx.EVT_BUTTON,self.btn_ok_OnCLick)
        self.btn_exit = wx.Button(self.mainwindow,size=(200, 60),pos=(287, 164),label='Exit',name='button')
        self.btn_exit.Bind(wx.EVT_BUTTON,self.btn_exit_OnCLick)
        self.editbox1 = wx.TextCtrl(self.mainwindow,size=(251, 26),pos=(159, 98),value='',name='text',style=0)
        self.label1 = wx.StaticText(self.mainwindow,size=(118, 25),pos=(28, 99),label='File or Directory : ',name='staticText',style=2321)
        label1_Font = wx.Font(10,74,90,400,False,'Microsoft YaHei UI',-1)
        self.label1.SetFont(label1_Font)
        self.btn_file = wx.Button(self.mainwindow,size=(96, 90),pos=(426, 35),label='File Browser',name='button')
        btn_file_Font = wx.Font(10,70,90,400,False,'Microsoft YaHei UI',-1)
        self.btn_file.SetFont(btn_file_Font)
        self.btn_file.Bind(wx.EVT_BUTTON,self.btn_file_OnCLick)
        self.combobox1 = wx.ComboBox(self.mainwindow,value='Only Selected Files',pos=(159, 37),name='comboBox',choices=['Only Selected Files', 'All Files Under the Directory'],style=16)
        self.combobox1.SetSize((250, 27))
        combobox1_Font = wx.Font(10,74,90,400,False,'Microsoft YaHei UI',-1)
        self.combobox1.Bind(wx.EVT_COMBOBOX,self.combobox1_SeLIST)
        self.combobox1.SetFont(combobox1_Font)
        self.label2 = wx.StaticText(self.mainwindow,size=(99, 24),pos=(27, 41),label='Execute Way :',name='staticText',style=2321)
        label2_Font = wx.Font(10,74,90,400,False,'Microsoft YaHei UI',-1)
        self.label2.SetFont(label2_Font)
        self.label_cprt = wx.StaticText(self.mainwindow,size=(80, 24),pos=(474, 238),label='By.bGVveno=',name='staticText',style=2321)
        self.label_cprt.SetForegroundColour((255, 255, 255, 255))

    def combobox1_SeLIST(self,event):
        self.editbox1.SetValue('')
        
    def btn_ok_OnCLick(self,event):
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
                   

    def btn_exit_OnCLick(self,event):
        self.Destroy()
        exit()

    def btn_file_OnCLick(self,event):       
        if self.combobox1.GetValue() == 'Only Selected Files':
            filedlg=wx.FileDialog(self, message="Select Files", defaultDir='', defaultFile='', wildcard='*.*', style=wx.FD_MULTIPLE)
            if filedlg.ShowModal() == wx.ID_OK:
                global file_list
                file_list = filedlg.GetPaths()
                self.editbox1.SetValue(file_list[0])
                filedlg.Destroy()
        elif self.combobox1.GetValue() == 'All Files Under the Directory':
            dirdlg=wx.DirDialog(self, message="Select Directory", defaultPath='', style=0)
            if dirdlg.ShowModal() == wx.ID_OK:
                global dirname
                dirname = dirdlg.GetPath()
                self.editbox1.SetValue(dirname+"......")
                global templist
                templist=[]
                listdir(dirname,templist)
                dirdlg.Destroy()

    def btn_list_OnCLick(self,event):
        if self.combobox1.GetValue() == 'Only Selected Files':
            print(file_list)
            #self.Destroy()
        elif self.combobox1.GetValue() == 'All Files Under the Directory':
            print(templist)
            #self.Destroy()   

class myApp(wx.App):
    def  OnInit(self):
        self.frame = Frame()
        self.frame.Show(True)
        return True

if __name__ == '__main__':
    app = myApp()
    app.MainLoop()

