# -*- coding: utf-8 -*-

import os

import qrcode

from theme.color import ColorValueError
from theme.theme import Theme, InvalidThemeError


class QRCodeBuilder:
    """QRCode 생성"""

    def __init__(self):
        self._data = None
        self._img_path = None
        self._box_size = 0
        self._border = 0

        self._fill_color = ""
        self._background_color = ""

    def set_data(self, data):
        self._data = data
        return self

    def set_image_path(self, image_path):
        self._img_path = image_path
        return self

    def set_box_size(self, box_size):
        self._box_size = box_size
        return self

    def set_border(self, border):
        self._border = border
        return self

    def set_color(self, background_color="", fill_color=""):
        """색상을 변경한다."""
        self._background_color = background_color or self._background_color
        self._fill_color = fill_color or self._fill_color
        return self

    def set_theme(self, theme):
        """테마를 설정한다."""
        theme_table = {
            "GRAY": Theme.get_gray_theme,
            "GRAPE": Theme.get_grape_theme,
            "BLUE": Theme.get_blue_theme,
            "GREEN": Theme.get_green_theme,
            "ORANGE": Theme.get_orange_theme,
            "RED": Theme.get_red_theme,
            "VIOLET": Theme.get_violet_theme,
            "CYAN": Theme.get_cyan_theme,
            "LIME": Theme.get_lime_theme,
            "PINK": Theme.get_pink_theme,
            "INDIGO": Theme.get_indigo_theme,
            "TEAL": Theme.get_teal_theme,
            "YELLOW": Theme.get_yellow_theme
        }
        theme_method = theme_table.get(theme.upper(), None)
        if theme_method is None:
            raise InvalidThemeError("Invalid value for theme. <{}>".format(theme))

        color = theme_method()
        self._fill_color = color.fill_color
        self._background_color = color.background_color
        return self

    def build(self):
        if not self._background_color or not self._fill_color:
            raise ColorValueError("Required color. <{}, {}>".format(self._background_color, self._fill_color))

        if not self._data:
            raise ValueError("Required data.")

        self._box_size = self._box_size or 20
        self._border = self._border or 5
        self._img_path = self._img_path or os.path.abspath("./qrcode.png")

        name, ext = os.path.splitext(self._img_path)
        return self.__QRCode(
            self._img_path, ext[1:],
            self._data,
            self._box_size, self._border,
            self._background_color, self._fill_color)

    class __QRCode:
        def __init__(self, img_path, img_format, data, box_size, border, background_color, fill_color):
            self._img_path = img_path
            self._img_format = img_format
            self._data = data
            self._box_size = box_size
            self._border = border
            self._background_color = background_color
            self._fill_color = fill_color

        def save_img(self):
            qr = qrcode.QRCode(
                version=1,
                error_correction=qrcode.constants.ERROR_CORRECT_L,
                box_size=self._box_size,
                border=self._border
            )
            qr.add_data(self._data)
            qr.make(fit=True)
            img = qr.make_image(fill_color=self._fill_color, back_color=self._background_color)

            if os.path.exists(self._img_path):
                os.remove(self._img_path)

            dir_name = os.path.abspath(os.path.dirname(self._img_path))
            if not os.path.exists(dir_name):
                os.makedirs(dir_name)

            img.save(self._img_path, self._img_format)
