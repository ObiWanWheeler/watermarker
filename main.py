from tkinter import Tk, filedialog, PhotoImage, Canvas, Button, Entry, messagebox
from PIL import Image, ImageDraw


file = None
img = None


def water_mark_image(watermark_text):
    global file
    global img
    if file and watermark_text:
        out_path = file[::-1].replace(".", "-watermarked."[::-1], 1)[::-1]
        image = Image.open(file)
        editable = ImageDraw.Draw(image)
        width, height = image.size
        editable.text((height/2 - len(watermark_text), height/2), watermark_text, fill=(39, 30, 40, 128))
        image.save(out_path)
        img = PhotoImage(file=rf"{out_path}")
        canvas.create_image(100, 112, image=img)
    else:
        messagebox.showwarning(title="Oops...", message="You forgot to specify an image or a watermark!")


def select_image():
    global file
    global img
    file = filedialog.askopenfilename(initialdir="/Pictures", title="Select a picture",
                                      filetypes=[("Image Files", ".jpg .png")])
    img = PhotoImage(file=rf"{file}")
    canvas.create_image(100, 112, image=img)


window = Tk()
window.title("Watermarker")
window.minsize(width=200, height=500)
window.maxsize(width=400, height=700)
window.config(padx=100, pady=100)

canvas = Canvas(width=200, height=224, highlightthickness=0)
canvas.grid(column=1, row=1, padx=10, pady=20)
select_image_btn = Button(width=10, height=2, text="Select Image", command=select_image)
select_image_btn.grid(column=1, row=2, padx=10, pady=10)
watermark_entry = Entry()
watermark_entry.grid(column=1, row=3, padx=10, pady=10)
watermark_btn = Button(width=20, height=2, text="Watermark",
                       command=lambda: water_mark_image(watermark_text=watermark_entry.get()))
watermark_btn.grid(column=1, row=4, padx=10, pady=10)

window.mainloop()
