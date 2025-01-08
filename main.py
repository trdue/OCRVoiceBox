import pytesseract
from PIL import Image
from gtts import gTTS
import os

# Tesseract OCRエンジンのパスを設定
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
# pytesseract.pytesseract.tesseract_cmd = '/usr/local/bin/tesseract'  # macOS/Linuxの場合

# OCRを実行して画像からテキストを抽出する関数
def extract_text_from_image(image_path):
    # 画像を開く
    image = Image.open(image_path)
    # OCRを実行してテキストを抽出
    text = pytesseract.image_to_string(image, lang='jpn')
    text = text.replace('\n', ' ')
    text = text.replace('\r', ' ')
    return text

# テキストを音声に変換する関数
def text_to_speech(text, output_file):
    # gTTSを使ってテキストを音声に変換
    tts = gTTS(text=text, lang='ja')
    # 音声ファイルを保存
    tts.save(output_file)

# メイン関数
def main(image_path, output_audio_file):
    # 画像からテキストを抽出
    extracted_text = extract_text_from_image(image_path)
    print("Extracted Text:")
    print(extracted_text)

    # 抽出したテキストを音声に変換
    text_to_speech(extracted_text, output_audio_file)
    print(f"Audio file saved as {output_audio_file}")

# プログラムのエントリーポイント
if __name__ == "__main__":
    # 画像ファイルのパス
    image_path = "./img/XXX.jpg"
    # 出力する音声ファイルのパス
    output_audio_file = "text/XXX.mp3"

    # メイン関数を実行
    main(image_path, output_audio_file)
