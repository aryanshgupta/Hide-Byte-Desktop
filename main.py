from tkinter import Canvas, IntVar, Scrollbar, StringVar, Tk, Frame, font, filedialog
from components.btn import Btn
from components.file_chooser import FileChooser
from components.inputfield import InputField
from components.navbar import NavBar
from components.selection_btn import SelectionBtn
from components.show_label import ShowLabel
from components.textfield import TextField

darkBgColor = "#222021"
ligthBgColor = "#282828"
fgColor = "#cccccc"


def showPage(frame: Frame) -> None:
    frame.tkraise()


def encode():
    print(plainFileChooser.fileFullPath)
    print(plainTextInput.getValue())
    print(keySizeSelection.value.get())
    print(secretKeyInput1.inputField.getValue())
    print(coverImageChooser.fileFullPath)


def decode():
    print(stegoObjectChooser.fileFullPath)
    print(secretKeyInput2.getValue())
    print(originalMessageFormat.value.get())
    print(originalFileExtension.getValue())


root = Tk()
root.title("Stego Image Creator | Project")
root.iconbitmap("assets/images/favicon.ico")
root.geometry("490x625")
root.minsize(490, 625)
root.configure(bg=darkBgColor)
root.resizable(False, True)

defaultFont = font.nametofont("TkDefaultFont")
defaultFont.configure(family="Poppins", size=12)
root.option_add("*Font", defaultFont)

root.rowconfigure(0, weight=1)
root.columnconfigure(0, weight=1)

homeFrame = Frame(root)
encodeFrame = Frame(root)
decodeFrame = Frame(root)

for frame in (homeFrame, encodeFrame, decodeFrame):
    frame.grid(row=0, column=0, sticky="nsew")

# ================================================================== HOME ==================================================================
encodeOpBtn = Btn(
    window=homeFrame,
    fileName="encode.png",
    isExpanded=True,
    fillBy="both",
)
encodeOpBtn.btn.config(command=lambda: showPage(encodeFrame))

decodeOpBtn = Btn(
    window=homeFrame,
    fileName="decode.png",
    isExpanded=True,
    fillBy="both",
)
decodeOpBtn.btn.config(command=lambda: showPage(decodeFrame))

# ================================================================== ENCODE ==================================================================
enBottomScroller = Scrollbar(encodeFrame)
enBottomScroller.pack(side="right", fill="y")

enTopFrame = Frame(encodeFrame, bg=darkBgColor)
enTopFrame.pack(fill="x")

enBottomMainFrame = Frame(encodeFrame)
enBottomMainFrame.pack(expand=True, fill="both")

enBottomCanvas = Canvas(
    enBottomMainFrame,
    bg=darkBgColor,
    bd=0,
    highlightthickness=0,
)
enBottomCanvas.pack(expand=True, fill="both")
enBottomCanvas.config(yscrollcommand=enBottomScroller.set)
enBottomCanvas.bind(
    "<Configure>",
    lambda e: enBottomCanvas.config(scrollregion=enBottomCanvas.bbox("all"), ),
)

enBottomScroller.config(command=enBottomCanvas.yview)

enBottomFrame = Frame(enBottomCanvas, bg=darkBgColor)
enBottomCanvas.create_window((0, 0), window=enBottomFrame, anchor="nw")

# ------- encode top frame -------

navbar1 = NavBar(window=enTopFrame, title="Encode")
navbar1.back.btn.config(command=lambda: showPage(homeFrame))

# ------- encode bottom frame -------

plainFileChooser = FileChooser(
    window=enBottomFrame,
    dialogTitle="Select a plain file",
    title="Choose plain file:",
    fileImageName="file.png",
    fileTypes=(("All Files", "*.*"), ),
)

# -----

ShowLabel(
    window=enBottomFrame,
    text="OR",
    style=("Poppins", 12, font.BOLD),
    vAlign="n",
    marginY=(20, 0),
)

# -----

plainTextInput = TextField(
    window=enBottomFrame,
    title="Enter plain text:",
    height=3,
    width=46,
    align="top",
)

# -----

keySizeSelection = SelectionBtn(
    window=enBottomFrame,
    title="Select key size in bytes:",
    options=["16", "24", "32"],
)

# -----

secretKeyInput1 = InputField(
    window=enBottomFrame,
    title="Enter secret key:",
    stringSize=lambda: keySizeSelection.value.get(),
)

# -----

coverImageChooser = FileChooser(
    window=enBottomFrame,
    title="Choose cover image:",
    fileImageName="image.png",
    dialogTitle="Select a cover image",
    marginY=(18, 0),
    fileTypes=(
        ("JPEG", "*.jpg;*.jpeg"),
        ("PNG", "*.png"),
    ),
)

# -----

encodeBtn = Btn(window=enBottomFrame, fileName="encode-btn.png", marginY=18)
encodeBtn.btn.config(command=encode)

# ================================================================== DECODE ==================================================================
deBottomScroller = Scrollbar(decodeFrame)
deBottomScroller.pack(side="right", fill="y")

deTopFrame = Frame(decodeFrame, bg=darkBgColor)
deTopFrame.pack(fill="x")

deBottomMainFrame = Frame(decodeFrame)
deBottomMainFrame.pack(expand=True, fill="both")

deBottomCanvas = Canvas(
    deBottomMainFrame,
    bg=darkBgColor,
    bd=0,
    highlightthickness=0,
)
deBottomCanvas.pack(expand=True, fill="both")
deBottomCanvas.config(yscrollcommand=deBottomScroller.set)
deBottomCanvas.bind(
    "<Configure>",
    lambda e: deBottomCanvas.config(scrollregion=deBottomCanvas.bbox("all"), ),
)

deBottomScroller.config(command=deBottomCanvas.yview)

deBottomFrame = Frame(deBottomCanvas, bg=darkBgColor)
deBottomCanvas.create_window((0, 0), window=deBottomFrame, anchor="nw")

# ------- decode top frame -------

navbar2 = NavBar(window=deTopFrame, title="Decode")
navbar2.back.btn.config(command=lambda: showPage(homeFrame))

# ------- decode bottom frame -------

stegoObjectChooser = FileChooser(
    window=deBottomFrame,
    dialogTitle="Select a stego object",
    title="Choose stego object:",
    fileImageName="image.png",
    fileTypes=(
        ("JPEG", "*.jpg;*.jpeg"),
        ("PNG", "*.png"),
    ),
)

# -----

secretKeyInput2 = TextField(
    window=deBottomFrame,
    title="Enter secret key:",
    width=46,
    align="top",
    marginY=(18, 0),
)

# -----

originalMessageFormat = SelectionBtn(
    window=deBottomFrame,
    title="Select original message format:",
    options=["Text", "File"],
)

# -----

originalFileExtension = TextField(
    window=deBottomFrame,
    title="Enter original file extension:",
    width=46,
    align="top",
)

# -----

decodeBtn = Btn(window=deBottomFrame, fileName="decode-btn.png", marginY=18)
decodeBtn.btn.config(command=decode)

showPage(homeFrame)
root.mainloop()
