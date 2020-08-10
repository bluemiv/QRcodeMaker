# -*- coding: utf-8 -*-

import os

import qrcode


class QRCodeMaker:
    """QRCode 생성"""

    def __init__(self, data, img_path, box_size=20, border=5):
        assert data, "Required data"
        self._data = data
        self._img_path = img_path
        self._box_size = int(box_size) or 20
        self._border = int(border) or 5

        self._fill_color = "black"
        self._background_color = "white"

    def _get_img(self):
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=self._box_size,
            border=self._border
        )
        qr.add_data(self._data)
        qr.make(fit=True)

    def set_background_color(self, color):
        """색상을 변경한다."""
        pass

    def set_fill_color(self, color):
        pass

    def set_theme(self):
        """테마를 변경한다."""
        self._fill_color = None
        self._background_color = None

    def make(self):
        if os.path.exists(self._img_path):
            os.remove(self._img_path)
