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

file_list=''
dirname=''


class Frame(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self, None, title='MD5CHANGER_GUI', size=(571, 301),name='frame',style=541072896)
        self.mainwindow = wx.Panel(self)
        self.SetTransparent(250)
        self.mainwindow.SetOwnBackgroundColour((255, 255, 255, 255))
        self.Centre()
        self.btn_ok = wx.Button(self.mainwindow,size=(200, 60),pos=(65, 164),label='Start',name='button')
        self.btn_ok.Bind(wx.EVT_BUTTON,self.btn_ok_OnCLick)
        self.btn_exit = wx.Button(self.mainwindow,size=(200, 60),pos=(296, 164),label='Exit',name='button')
        self.btn_exit.Bind(wx.EVT_BUTTON,self.btn_exit_OnCLick)
        self.editbox1 = wx.TextCtrl(self.mainwindow,size=(314, 26),pos=(159, 98),value='',name='text',style=0)
        self.label1 = wx.StaticText(self.mainwindow,size=(118, 25),pos=(28, 99),label='File or Directory : ',name='staticText',style=2321)
        label1_Font = wx.Font(10,70,90,400,False,'Microsoft YaHei UI',-1)
        self.label1.SetFont(label1_Font)
        self.btn_file = wx.Button(self.mainwindow,size=(37, 28),pos=(480, 97),label='[<<]',name='button')
        self.btn_file.Bind(wx.EVT_BUTTON,self.btn_file_OnCLick)
        self.combobox1 = wx.ComboBox(self.mainwindow,value='Only Selected Files',pos=(159, 37),name='comboBox',choices=['Only Selected Files', 'All Files Under the Directory and Sub-dirs'],style=16)
        self.combobox1.SetSize((314, 27))
        self.label2 = wx.StaticText(self.mainwindow,size=(99, 24),pos=(27, 41),label='Execute Way :',name='staticText',style=2321)
        label2_Font = wx.Font(10,70,90,400,False,'Microsoft YaHei UI',-1)
        self.label2.SetFont(label2_Font)
        #self.btn_list = wx.Button(self.mainwindow,size=(167, 30),pos=(350, 36),label='List All Files',name='button')
        #self.btn_list.Bind(wx.EVT_BUTTON,self.btn_list_OnCLick)
        self.label_cprt = wx.StaticText(self.mainwindow,size=(80, 24),pos=(474, 238),label='By.bGVveno=',name='staticText',style=2321)
        self.label_cprt.SetForegroundColour((255, 255, 255, 255))

    def btn_ok_OnCLick(self,event):
        if self.combobox1.GetValue() == 'Only Selected Files':
            changemd5(file_list)
            #self.Destroy()
        elif self.combobox1.GetValue() == 'All Files Under the Directory and Sub-dirs':
            changemd5(templist)
            #self.Destroy()        

    def btn_exit_OnCLick(self,event):
        self.Destroy()
        exit()

    def btn_file_OnCLick(self,event):       
        if self.combobox1.GetValue() == 'Only Selected Files':
            filedlg=wx.FileDialog(self, message="Select Files", defaultDir='', defaultFile='', wildcard='*.*', style=wx.FD_MULTIPLE)
            if filedlg.ShowModal() == wx.ID_OK:
                global file_list
                file_list = filedlg.GetPaths()
                self.editbox1.SetValue(file_list[0]+"......")
                filedlg.Destroy()
        elif self.combobox1.GetValue() == 'All Files Under the Directory and Sub-dirs':
            dirdlg=wx.DirDialog(self, message="Select Directory", defaultPath='', style=0)
            if dirdlg.ShowModal() == wx.ID_OK:
                global dirname
                dirname = dirdlg.GetPath()
                self.editbox1.SetValue(dirname+"......")
                global templist
                templist=[]
                listdir(dirname,templist)
                dirdlg.Destroy()
                print(templist)

    #def btn_list_OnCLick(self,event):
    #    print(file_list)

class myApp(wx.App):
    def  OnInit(self):
        self.frame = Frame()
        self.frame.Show(True)
        return True

if __name__ == '__main__':
    app = myApp()
    app.MainLoop()

