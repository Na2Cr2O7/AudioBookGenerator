import pdfplumber
import stdcpp as std
class istream:
    def __init__(self, fn):
        self.o=open(fn,'a',encoding='utf-8')
    def __lshift__(self, s):
        self.o.write(s)
        return self
    def __del__(self):
        self.o.close()
    def close(self):
        self.o.close()
    def flush(self):
        self.o.flush()
import os

def extractPDF(pdfPath):
    allText = ""
    with pdfplumber.open(pdfPath) as pdf:
        for page in pdf.pages:
            text = page.extract_text()
            allText += text
        
        for idx, image in enumerate(pdf.images):
            #std.cout <<image['stream'].get_data()<<std.endl
            with open(f"image{idx}.png", "wb") as f:
                f.write(image['stream'].get_data())
    return allText
if __name__ == "__main__":
    import sys
    import tqdm
    if len(sys.argv)<2:
        print("ExtractPDF.py <pdf路径或目录>")
        raise SystemExit
    std.cout << "结果输出到output.txt" << std.endl
    iss=istream("output.txt")
    pdfPaths = sys.argv[1:]
    for path in tqdm.tqdm(pdfPaths):
        if os.path.isdir(path):
            for file in tqdm.tqdm(os.listdir(path)):
                if file.endswith(".pdf"):
                    pdfPath = os.path.join(path, file)
                    allText = extractPDF(pdfPath)
                    iss << allText
                    
                    
        else:
            allText = extractPDF(path)
            iss << allText
