import tkinter as tk
from time import strftime

class DigitalClock:
    def __init__(self, root):
        self.root = root
        self.root.title("可放大缩小的数字时钟")
        self.root.geometry("800x300")
        self.root.configure(bg="black")
        
        # 初始字体大小
        self.font_size = 72
        
        # 创建时钟标签
        self.time_label = tk.Label(
            root, 
            font=('ds-digital', self.font_size, 'bold'),
            background='black',
            foreground='white'
        )
        self.time_label.pack(anchor='center', expand=1)
        
        # 创建放大和缩小按钮
        self.control_frame = tk.Frame(root, bg="black")
        self.control_frame.pack(pady=10)
        
        self.zoom_in_button = tk.Button(
            self.control_frame,
            text="放大 +",
            command=self.zoom_in,
            bg="black",
            fg="white",
            padx=10
        )
        self.zoom_in_button.pack(side=tk.LEFT, padx=5)
        
        self.zoom_out_button = tk.Button(
            self.control_frame,
            text="缩小 -",
            command=self.zoom_out,
            bg="black",
            fg="white",
            padx=10
        )
        self.zoom_out_button.pack(side=tk.RIGHT, padx=5)
        
        # 开始更新时间
        self.update_time()
    
    def update_time(self):
        """更新时间显示"""
        current_time = strftime('%H:%M:%S')
        self.time_label.config(text=current_time)
        self.root.after(1000, self.update_time)
    
    def zoom_in(self):
        """放大字体"""
        self.font_size += 5
        self.time_label.config(font=('ds-digital', self.font_size, 'bold'))
    
    def zoom_out(self):
        """缩小字体"""
        if self.font_size > 10:
            self.font_size -= 5
            self.time_label.config(font=('ds-digital', self.font_size, 'bold'))

if __name__ == "__main__":
    root = tk.Tk()
    digital_clock = DigitalClock(root)
    root.mainloop()