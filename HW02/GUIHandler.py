# -*-coding:utf-8-*-
import tkinter as tk
import tkinter.messagebox as msb
import Generator as sg
import numpy as np

class GUIHandler:
    def __init__(self):
        self.mtk = tk.Tk()
        self.mtk.wm_minsize(480, 480)
        self.mtk.resizable(0, 0)
        self.mtk.title('音訊產生器')
        self.ini_widges()
        self.count = 0
        self.generator = sg.SoundGenerator(16200, 1)

    def ini_widges(self):
        self.filename_inp = tk.Entry(self.mtk)
        self.filename_inp.grid(row=1, column=0, padx=10)

        self.outputfn_txt = tk.Label(self.mtk, text='輸出(匯入)檔名 : ').grid(row=0, column=0)

        self.sample_rate = tk.Entry(self.mtk).grid(row=1, column=2, padx=10)

        self.outputfn_txt = tk.Label(self.mtk, text='取樣率(預設:16200) : ').grid(row=0, column=2)

        self.btn_output = tk.Button(self.mtk, text='作業輸出(小蜜蜂雙聲道)', command=self.homeworkout)
        self.btn_output2 = tk.Button(self.mtk, text='作業輸出(頻率調製)', command=self.frehomeworkout)
        self.btn_output.grid(row=1, column=1, sticky='E', padx=10)
        self.btn_output2.grid(row=1, column=1, sticky='W', padx=10)

        self.btn_inputTxt = tk.Button(self.mtk, text='從txt匯入', command=self.inputTXT)
        self.btn_inputTxt.grid(row=2, column=0, pady=20)

        self.outputfn_txt = tk.Label(self.mtk, text='使用教學 : 請輸入 1 ~ 7(Do ~ Si)  0 為休止符 並輸入拍子數').grid(row=2, column=1, pady=40)

        self.outputfn_txt = tk.Label(self.mtk, text='音符(0~7) : ').grid(row=3, column=0, pady=40)

        self.chord = tk.Entry(self.mtk)
        self.chord.grid(row=4, column=0, padx=10)

        self.outputfn_txt = tk.Label(self.mtk, text='拍數 : ').grid(row=3, column=1)
        self.sec = tk.Entry(self.mtk)
        self.sec.grid(row=4, column=1, padx=10)

        self.btn_delete = tk.Button(self.mtk, text='刪除一個', command=self.btn_delete_handler).grid(row=4, column=2, padx=50, sticky='E')
        self.btn_sumit = tk.Button(self.mtk, text='增加', command=self.btn_sumit_handler).grid(row=4, column=2, sticky='W')

        self.outputfn_txt = tk.Label(self.mtk, text='當前樂譜 : ', wraplength=480)
        self.outputfn_txt.grid(row=5, column=0, pady=60, columnspan=4, sticky='W')

        self.btn_output = tk.Button(self.mtk, text='輸出檔案',command=self.btn_output_handler)
        self.btn_output.grid(row=6, column=1)
    def inputTXT(self):
        if self.filename_inp.get() is '':
            print('請打上輸出檔案名稱')
            msb._show('錯誤', '請打上txt檔案名稱(不須加.txt)')
        else:
            file_name = self.filename_inp.get()
            p = open(file_name+'.txt', 'r')
            if p is None:
                msb._show('錯誤', '請打上正確的txt檔案名稱(不須加.txt)')
                return
            inf = p.read()
            inf = inf.split(' ')
            print(inf)
            if inf[-1] is '':
                del inf[-1]
            try:
                for i, j in enumerate(inf):
                    inf[i] = list(map(int, j.split(',')))
            except ValueError:
                msb._show('錯誤', '音符只能輸入數字')
                return
            for i in inf:
                if i[0] < 0 or i[0] > 7:
                    msb._show('錯誤', '音符只能輸入(0~7)')
                    return
                elif i[1] <= 0 or i[1] > 4:
                    msb._show('錯誤', '拍數只能輸入數字(1~4)')
                    return
            print(inf)
            self.outputfn_txt.configure(text='當前樂譜 : ')
            self.generator.spectrum = inf
            for i, j in enumerate(inf):
                if i % 4 is 0:
                    self.outputfn_txt.configure(text=str(
                        self.outputfn_txt.cget('text')+'| '+self.generator.hzArr[inf[i][0]][0] + '-' + str(inf[i][1]) + ' '))
                else:
                    self.outputfn_txt.configure(text=str(
                        self.outputfn_txt.cget('text') + self.generator.hzArr[inf[i][0]][0] + '-' + str(inf[i][1]) + ' '))

    def btn_sumit_handler(self):
        if self.filename_inp.get() is '':
            print('請打上輸出檔案名稱')
            msb._show('錯誤', '請打上輸出檔案名稱')
        elif self.chord.get() is '':
            print('請輸入音符(0~7)')
            msb._show('錯誤', '請輸入音符(0~7)')
        elif self.sec.get() is '':
            print('請輸入拍子數')
            msb._show('錯誤', '請輸入拍子數')
        else:
            try:
                chord_m = int(self.chord.get())
            except ValueError:
                msb._show('錯誤', '音符只能輸入數字')
                return
            try:
                sec_m = int(self.sec.get())
                if sec_m <= 0 or sec_m > 4:
                    msb._show('錯誤', '拍數只能輸入數字(1~4)')
                    return
            except ValueError:
                msb._show('錯誤', '拍數只能輸入數字(1~4)')
                return
            if chord_m < 0 or chord_m > 7:
                msb._show('錯誤', '音符只能輸入(0~7)')
                return
            # print(self.outputfn_txt.cget('text'))

            # print(self.count % 4)
            if self.count % 4 is 0:
                self.outputfn_txt.configure(text=str(self.outputfn_txt.cget('text')+'| '+self.generator.hzArr[chord_m][0] + '-' + str(sec_m) + ' '))
            else:
                self.outputfn_txt.configure(text=str(
                    self.outputfn_txt.cget('text') + self.generator.hzArr[chord_m][0] + '-' + str(sec_m) + ' '))
            self.count += 1
            self.generator.spectrum.append([chord_m, sec_m])

    def btn_delete_handler(self):
        if len(self.outputfn_txt.cget('text')) is 7:
            msb._show('錯誤', '譜是空的')
        else:
            del self.generator.spectrum[-1]
            if self.count % 4 is 1:
                strr = self.outputfn_txt.cget('text')
                strr = strr[:-6]
            else:
                strr = self.outputfn_txt.cget('text')
                strr = strr[:-4]
            self.outputfn_txt.configure(text=strr)
            self.count -= 1

    def homeworkout(self):
        data = []
        data_low = []
        spec = [[5, 1], [3, 1], [3, 2], [4, 1], [2, 1], [2, 2], [1, 1], [2, 1], [3, 1], [4, 1], [5, 1], [5, 1], [5, 2], [5, 1], [3, 1], [3, 2], [4, 1], [2, 1], [2, 2],
                [1, 1], [3, 1], [5, 1], [5, 1], [3, 4], [2, 1], [2, 1], [2, 1], [2, 1], [2, 1], [3, 1], [4, 2], [3, 1], [3, 1], [3, 1], [3, 1], [3, 1], [4, 1], [5, 2],
                [5, 1], [3, 1], [3, 2], [4, 1], [2, 1], [2, 2], [1, 1], [3, 1], [5, 1], [5, 1], [1, 4]]
        for i in spec:
            data.extend(self.generator.generate_wave(i[0], i[1]))
            data_low.extend(self.generator.lowgenerate_wave(i[0], i[1]))
        for i, j in enumerate(data_low[:-25000]):
            data[i+25000] += data_low[i]
        data.extend(data_low[-25000:])
        self.generator.save_wave(np.array(data), 0)
        msb._show('成功', '輸出成功!')

    def frehomeworkout(self):
        data = []
        data_low = []
        spec = [[5, 1], [3, 1], [3, 2], [4, 1], [2, 1], [2, 2], [1, 1], [2, 1], [3, 1], [4, 1], [5, 1], [5, 1], [5, 2],
                [5, 1], [3, 1], [3, 2], [4, 1], [2, 1], [2, 2],
                [1, 1], [3, 1], [5, 1], [5, 1], [3, 4], [2, 1], [2, 1], [2, 1], [2, 1], [2, 1], [3, 1], [4, 2], [3, 1],
                [3, 1], [3, 1], [3, 1], [3, 1], [4, 1], [5, 2],
                [5, 1], [3, 1], [3, 2], [4, 1], [2, 1], [2, 2], [1, 1], [3, 1], [5, 1], [5, 1], [1, 4]]
        for i in spec:
            data.extend(self.generator.kappa(i[0], i[1], False))
            # data_low.extend(self.generator.kappa(i[0], i[1], True))
        # for i, j in enumerate(data_low[:-25000]):
        #     data[i + 25000] += data_low[i]
        # data.extend(data_low[-25000:])
        self.generator.save_wave(np.array(data), 1)
        msb._show('成功', '輸出成功!')

    def btn_output_handler(self):
        if self.filename_inp.get() is '':
            print('請輸出檔案名稱')
            msb._show('錯誤', '請打上輸出檔案名稱')
        else:
            data = []
            for i in self.generator.spectrum:
                data.extend(self.generator.generate_wave(i[0], i[1]))
            self.generator.save_w(np.array(data), self.filename_inp.get())
            p = open(self.filename_inp.get() + '.txt', 'w')
            for i in self.generator.spectrum:
                p.write(str(i[0])+','+str(i[1])+' ')
            msb._show('成功', '輸出成功!')











