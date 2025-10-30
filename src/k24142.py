import numpy as np
import cv2
from my_module.K24142.lecture05_camera_image_capture import MyVideoCapture

def lecture05_01():

    # カメラキャプチャ実行
    app = MyVideoCapture()
    app.run()

    # 画像をローカル変数に保存
    google_img : cv2.Mat = cv2.imread('images/google.png')
    capture_img : cv2.Mat = app.get_img()
    out_img : cv2.Mat = google_img

    g_hight, g_width, g_channel = google_img.shape
    c_hight, c_width, c_channel = capture_img.shape
    print(google_img.shape)
    print(capture_img.shape)

    for x in range(g_width):
        for y in range(g_hight):
            g, b, r = google_img[y, x]
            # もし白色(255,255,255)だったら置き換える
            if (b, g, r) == (255, 255, 255):
                out_img[y, x] = capture_img[int(y % c_hight), int(x % c_width)]

    # 書き込み処理
    out_path = 'output_images/lecture05_01_k24142.png'
    ok = cv2.imwrite(out_path, out_img)
    if ok:
        print(f'保存しました: {out_path}')
    else:
        print(f'保存に失敗しました: {out_path}')