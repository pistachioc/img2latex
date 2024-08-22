import tkinter as tk
from io import BytesIO
from tkinter import filedialog, messagebox

import matplotlib.pyplot as plt
from PIL import Image, ImageTk

from pix2tex.cli import LatexOCR
from latex2img import latex2image

# Biến toàn cục để lưu hình ảnh và mã LaTeX
global_img = None
global_img_path = "result.png"
global_latex_code = None  # Mã LaTeX mặc định


def choose_image():
    """
    Choose an image to display

    :return: input image
    """
    global global_img
    file_path = filedialog.askopenfilename(filetypes=[("Image files", "*.jpg *.png")])
    if file_path:
        try:
            global_img = Image.open(file_path)
            max_width, max_height = 500, 500  # Kích thước tối đa
            img = global_img
            img.thumbnail((max_width, max_height))  # Thay đổi kích thước giữ tỷ lệ
            img_display = ImageTk.PhotoImage(img)
            canvas_image.create_image(0, 0, anchor="nw", image=img_display)
            canvas_image.image = img_display
            canvas_image.file_path = file_path
            canvas_image.config(scrollregion=canvas_image.bbox(tk.ALL))
            status_var.set(f"Đã mở: {file_path}")
        except Exception as e:
            messagebox.showerror("Error", f"Không thể mở hình ảnh: {e}")

def load_result_image(target_canvas):
    """
    Load result image and display it on the given canvas.

    :param target_canvas: The canvas to display the image on
    :return: result image
    """
    try:
        img = Image.open(global_img_path)
        max_width, max_height = 500, 500  # Kích thước tối đa
        img.thumbnail((max_width, max_height))  # Thay đổi kích thước giữ tỷ lệ
        img_display = ImageTk.PhotoImage(img)
        target_canvas.create_image(0, 0, anchor="nw", image=img_display)
        target_canvas.image = img_display
        target_canvas.file_path = global_img_path
        target_canvas.config(scrollregion=target_canvas.bbox(tk.ALL))
        status_var.set(f"Đã mở: {global_img_path}")
    except Exception as e:
        messagebox.showerror("Error", f"Không tồn tại kết quả: {e}")



def display_latex():
    """
    Display latex code and load the result image in the second canvas
    """
    global global_latex_code
    if global_img is None:
        messagebox.showwarning("Warning", "Chưa mở hình ảnh nào!")
        return

    latex_code = model(global_img)
    global_latex_code = latex_code

    render_latex_code = fr"""${latex_code}$"""

    img_result = latex2image(render_latex_code, image_name=global_img_path, image_size_in=(5, 1), fontsize=20, dpi=300)

    # Hiển thị LaTeX trên canvas thứ nhất
    fig, ax = plt.subplots()
    ax.text(0.5, 0.5, latex_code, fontsize=20, ha='center', va='center')
    ax.axis('off')

    # Thiết lập kích thước của hình ảnh LaTeX
    fig.set_size_inches(5, 2)

    buf = BytesIO()
    plt.savefig(buf, format='png', bbox_inches='tight')
    buf.seek(0)

    img = Image.open(buf)
    img_display = ImageTk.PhotoImage(img)
    canvas_latex.create_image(0, 0, anchor="nw", image=img_display)
    canvas_latex.image = img_display
    canvas_latex.config(scrollregion=canvas_latex.bbox(tk.ALL))
    status_var.set("Đã hiển thị mã LaTeX!")
    buf.close()
    plt.close(fig)

    # Hiển thị ảnh kết quả trong frame thứ 2
    load_result_image(canvas_latex_2)


def copy_latex():
    """
    Copy latex code

    :return: latex code
    """
    if global_latex_code:
        root.clipboard_clear()  # Xóa nội dung clipboard hiện tại
        root.clipboard_append(global_latex_code)  # Sao chép mã LaTeX vào clipboard
        root.update()  # Cập nhật clipboard ngay lập tức
        messagebox.showinfo("Thông báo", "Mã LaTeX đã được sao chép vào clipboard!")
    else:
        messagebox.showwarning("Warning", "Không có mã LaTeX nào để sao chép!")


# Tạo cửa sổ chính
root = tk.Tk()
root.title("Chuyển đổi hình ảnh sang mã LaTeX")
# root.state("zoomed")  # Đặt cửa sổ ở chế độ full màn hình (vừa với toàn màn hình)

# Thiết lập cửa sổ chiếm toàn bộ màn hình
root.geometry(f"{root.winfo_screenwidth()}x{root.winfo_screenheight()}+0+0")

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
button_open = tk.Button(frame_buttons, text="Chọn ảnh", command=choose_image, bg="#4CAF50", fg="white",
                        font=("Arial", 12, "bold"))
button_open.pack(pady=10, fill=tk.X)

# Button hiển thị kết quả LaTeX
button_convert = tk.Button(frame_buttons, text="Hiển thị LaTeX", command=display_latex, bg="#2196F3", fg="white",
                           font=("Arial", 12, "bold"))
button_convert.pack(pady=10, fill=tk.X)

# Button sao chép mã LaTeX
button_copy = tk.Button(frame_buttons, text="Sao chép LaTeX", command=copy_latex, bg="#FFC107", fg="black",
                        font=("Arial", 12, "bold"))
button_copy.pack(pady=10, fill=tk.X)

# Frame chứa canvas và thanh trượt cho hình ảnh gốc
frame_canvas_image = tk.Frame(frame_images)
frame_canvas_image.pack(pady=10, expand=True, fill=tk.BOTH)
label_image = tk.Label(frame_canvas_image, text="Hình ảnh gốc", bg="#1e1e1e", fg="white", font=("Arial", 12, "bold"))
label_image.pack(pady=5)

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
frame_canvas_latex.pack(side=tk.LEFT, padx=10, pady=10, expand=True, fill=tk.BOTH)

label_latex = tk.Label(frame_canvas_latex, text="Mã LaTeX", bg="#1e1e1e", fg="white", font=("Arial", 12, "bold"))
label_latex.pack(pady=5)

# Cửa sổ hiển thị kết quả LaTeX
canvas_latex = tk.Canvas(frame_canvas_latex, bg="#ffffff", relief=tk.RIDGE, borderwidth=3)
canvas_latex.pack(side=tk.LEFT, expand=True, fill=tk.BOTH)

# Thêm thanh trượt dọc và ngang cho kết quả LaTeX
scroll_y_latex = tk.Scrollbar(frame_canvas_latex, orient="vertical", command=canvas_latex.yview)
scroll_y_latex.pack(side="right", fill="y")
scroll_x_latex = tk.Scrollbar(frame_canvas_latex, orient="horizontal", command=canvas_latex.xview)
scroll_x_latex.pack(side="bottom", fill="x")
canvas_latex.configure(yscrollcommand=scroll_y_latex.set, xscrollcommand=scroll_x_latex.set)

# Tạo frame thứ hai giống như frame đầu tiên, đặt cạnh frame_canvas_latex
frame_canvas_latex_2 = tk.Frame(frame_images)
frame_canvas_latex_2.pack(side=tk.LEFT, padx=10, pady=10, expand=True, fill=tk.BOTH)

label_latex_2 = tk.Label(frame_canvas_latex_2, text="LaTex dự đoán sau khi Render", bg="#1e1e1e", fg="white", font=("Arial", 12, "bold"))
label_latex_2.pack(pady=5)

# Cửa sổ hiển thị kết quả LaTeX thứ hai
canvas_latex_2 = tk.Canvas(frame_canvas_latex_2, bg="#ffffff", relief=tk.RIDGE, borderwidth=3)
canvas_latex_2.pack(side=tk.LEFT, expand=True, fill=tk.BOTH)

# Thêm thanh trượt dọc và ngang cho kết quả LaTeX thứ hai
scroll_y_latex_2 = tk.Scrollbar(frame_canvas_latex_2, orient="vertical", command=canvas_latex_2.yview)
scroll_y_latex_2.pack(side="right", fill="y")
scroll_x_latex_2 = tk.Scrollbar(frame_canvas_latex_2, orient="horizontal", command=canvas_latex_2.xview)
scroll_x_latex_2.pack(side="bottom", fill="x")
canvas_latex_2.configure(yscrollcommand=scroll_y_latex_2.set, xscrollcommand=scroll_x_latex_2.set)

# Khởi tạo mô hình
model = LatexOCR()

# Chạy chương trình
root.mainloop()
