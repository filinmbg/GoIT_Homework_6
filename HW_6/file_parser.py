import sys
from pathlib import Path

JPEG_IMAGES = []
JPG_IMAGES = []
PNG_IMAGES = []
SVG_IMAGES = []
AVI_VIDEO = []
MP4_VIDEO = []
MOV_VIDEO = []
MKV_VIDEO = []
DOC_DOCUMENTS = []
DOCX_DOCUMENTS = []
TXT_DOCUMENTS = []
PDF_DOCUMENTS = []
XLSX_DOCUMENTS = []
PPTX_DOCUMENTS = []
MP3_AUDIO = []
OGG_AUDIO = []
WAV_AUDIO = []
AMR_AUDIO = []
other = []
ARCHIVES = []

REGISTER_EXTENSION = {
    "JPEG": JPEG_IMAGES,
    "PNG": PNG_IMAGES,
    "JPG": JPG_IMAGES,
    "SVG": SVG_IMAGES,
    "AVI": AVI_VIDEO,
    "MP4": MP4_VIDEO,
    "MOV": MOV_VIDEO,
    "MKV": MKV_VIDEO,
    "DOC": DOC_DOCUMENTS,
    "DOCS": DOCX_DOCUMENTS,
    "TXT": TXT_DOCUMENTS,
    "PDF": PDF_DOCUMENTS,
    "XLSX": XLSX_DOCUMENTS,
    "PPTX": PPTX_DOCUMENTS,
    "MP3": MP3_AUDIO,
    "OGG": OGG_AUDIO,
    "WAV": WAV_AUDIO,
    "AMR": AMR_AUDIO,
    "ZIP": ARCHIVES,
    "GZ": ARCHIVES,
    "TAR": ARCHIVES,
}

FOLDERS = []
EXTENSION = set()
UNKNOWN = set()


def get_extension(filename: str) -> str:
    return Path(filename).suffix[1:].upper()


def scan(folder: Path) -> None:
    for item in folder.iterdir():
        if item.is_dir():
            if item.name not in (
                "archives",
                "video",
                "audio",
                "documents",
                "images",
                "other",
            ):
                FOLDERS.append(item)

                scan(item)
            continue

        ext = get_extension(item.name)
        fullname = folder / item.name
        if not ext:
            other.append(fullname)
        else:
            try:
                container = REGISTER_EXTENSION[ext]
                EXTENSION.add(ext)
                container.append(fullname)
            except KeyError:
                UNKNOWN.add(ext)
                other.append(fullname)


if __name__ == "__main__":
    folder_to_scan = sys.argv[1]
    print(f"Start in folder {folder_to_scan}")
    scan(Path(folder_to_scan))
    print(f"Images jpeg: {JPEG_IMAGES}")
    print(f"Images jpg: {JPG_IMAGES}")
    print(f"Images svg: {SVG_IMAGES}")
    print(f"Audio mp3: {MP3_AUDIO}")
    print(f"Archives: {ARCHIVES}")
    print(f"Images png: {PNG_IMAGES}")
    print(f"Video avi: {AVI_VIDEO}")
    print(f"Video mp4: {MP4_VIDEO}")
    print(f"Video mov: {MOV_VIDEO}")
    print(f"Video mkv: {MKV_VIDEO}")
    print(f"Documents doc: {DOC_DOCUMENTS}")
    print(f"Documents docx: {DOCX_DOCUMENTS}")
    print(f"Documents txt: {TXT_DOCUMENTS}")
    print(f"Documents pdf: {PDF_DOCUMENTS}")
    print(f"Documents xlsx: {XLSX_DOCUMENTS}")
    print(f"Documents pptx: {PPTX_DOCUMENTS}")
    print(f"Audio ogg: {OGG_AUDIO}")
    print(f"Audio wav: {WAV_AUDIO}")
    print(f"Audio amr: {AMR_AUDIO}")

    print(f"Types of files in folder: {EXTENSION}")
    print(f"Unknown files of types: {UNKNOWN}")
    print(f"other: {other}")

    print(FOLDERS)