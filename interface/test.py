import tkinter as tk

# Tạo cửa sổ chính
root = tk.Tk()
root.title("Frames with LaTeX")

# Tạo frame chính chứa cả hai frame
frame_images = tk.Frame(root)
frame_images.pack(expand=True, fill=tk.BOTH)

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

label_latex_2 = tk.Label(frame_canvas_latex_2, text="Mã LaTeX 2", bg="#1e1e1e", fg="white", font=("Arial", 12, "bold"))
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

# Khởi động giao diện
root.mainloop()
