import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image, ImageTk
import matplotlib.pyplot as plt
from io import BytesIO

def open_image():
    file_path = filedialog.askopenfilename(
        filetypes=[("Image files", "*.jpg *.png")]
    )
    if file_path:
        try:
            img = Image.open(file_path)
            img_display = ImageTk.PhotoImage(img)
            canvas_image.create_image(0, 0, anchor="nw", image=img_display)
            canvas_image.image = img_display
            canvas_image.file_path = file_path  # Lưu đường dẫn vào canvas
            canvas_image.config(scrollregion=canvas_image.bbox(tk.ALL))
            status_var.set(f"Đã mở: {file_path}")
        except Exception as e:
            messagebox.showerror("Error", f"Không thể mở hình ảnh: {e}")

def display_latex():
    # Mã LaTeX mẫu
    latex_code = r"$x=1/2$"
    
    # tạo hình ảnh từ mã LaTeX
    fig, ax = plt.subplots()
    ax.text(0.5, 0.5, latex_code, fontsize=20, ha='center', va='center')
    ax.axis('off')

    # lưu hình ảnh vào bộ nhớ
    buf = BytesIO()
    plt.savefig(buf, format='png')
    buf.seek(0)
    
    # hiển thị hình ảnh trên giao diện Tkinter
    img = Image.open(buf)
    img_display = ImageTk.PhotoImage(img)
    canvas_latex.create_image(0, 0, anchor="nw", image=img_display)
    canvas_latex.image = img_display
    canvas_latex.config(scrollregion=canvas_latex.bbox(tk.ALL))
    status_var.set("Đã hiển thị mã LaTeX!")
    buf.close()
    plt.close(fig)

# Tạo cửa sổ chính
root = tk.Tk()
root.title("Chuyển đổi hình ảnh sang mã LaTeX")
root.geometry("800x600")
root.config(bg="#282828")

# Tạo thanh trạng thái
status_var = tk.StringVar()
status_bar = tk.Label(root, textvariable=status_var, relief=tk.SUNKEN, anchor='w', bg="#444444", fg="white")
status_bar.pack(side=tk.BOTTOM, fill=tk.X)
status_var.set("Sẵn sàng")

# Frame chứa các nút
frame_buttons = tk.Frame(root, bg="#333333", padx=10, pady=10)
frame_buttons.pack(side=tk.LEFT, fill=tk.Y)

# Frame chứa các cửa sổ hiển thị hình ảnh và mã LaTeX
frame_images = tk.Frame(root, bg="#1e1e1e", padx=10, pady=10)
frame_images.pack(side=tk.RIGHT, expand=True, fill=tk.BOTH)

# Button chọn ảnh
button_open = tk.Button(frame_buttons, text="Chọn ảnh", command=open_image, bg="#4CAF50", fg="white", font=("Arial", 12, "bold"))
button_open.pack(pady=10, fill=tk.X)

# Button hiển thị kết quả LaTeX
button_convert = tk.Button(frame_buttons, text="Hiển thị LaTeX", command=display_latex, bg="#2196F3", fg="white", font=("Arial", 12, "bold"))
button_convert.pack(pady=10, fill=tk.X)

# Frame chứa canvas và thanh trượt cho hình ảnh gốc
frame_canvas_image = tk.Frame(frame_images)
frame_canvas_image.pack(pady=10, expand=True, fill=tk.BOTH)

# Cửa sổ hiển thị hình ảnh gốc
canvas_image = tk.Canvas(frame_canvas_image, bg="#ffffff", relief=tk.RIDGE, borderwidth=3)
canvas_image.pack(side=tk.LEFT, expand=True, fill=tk.BOTH)

# Thêm thanh trượt dọc và ngang cho hình ảnh gốc
scroll_y_image = tk.Scrollbar(frame_canvas_image, orient="vertical", command=canvas_image.yview)
scroll_y_image.pack(side="right", fill="y")
scroll_x_image = tk.Scrollbar(frame_canvas_image, orient="horizontal", command=canvas_image.xview)
scroll_x_image.pack(side="bottom", fill="x")
canvas_image.configure(yscrollcommand=scroll_y_image.set, xscrollcommand=scroll_x_image.set)

# Frame chứa canvas để hiển thị kết quả LaTeX
frame_canvas_latex = tk.Frame(frame_images)
frame_canvas_latex.pack(pady=10, expand=True, fill=tk.BOTH)

# Cửa sổ hiển thị kết quả LaTeX
canvas_latex = tk.Canvas(frame_canvas_latex, bg="#ffffff", relief=tk.RIDGE, borderwidth=3)
canvas_latex.pack(side=tk.LEFT, expand=True, fill=tk.BOTH)

# Thêm thanh trượt dọc và ngang cho kết quả LaTeX
scroll_y_latex = tk.Scrollbar(frame_canvas_latex, orient="vertical", command=canvas_latex.yview)
scroll_y_latex.pack(side="right", fill="y")
scroll_x_latex = tk.Scrollbar(frame_canvas_latex, orient="horizontal", command=canvas_latex.xview)
scroll_x_latex.pack(side="bottom", fill="x")
canvas_latex.configure(yscrollcommand=scroll_y_latex.set, xscrollcommand=scroll_x_latex.set)

# Chạy chương trình
root.mainloop()
