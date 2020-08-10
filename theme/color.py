# -*- coding: utf-8 -*-

import re


class ColorValueError(RuntimeError):
    pass


class ColorBuilder:
    COLOR_LIST = ("black", "white", "red", "blue", "yellow")
    pattern = re.compile(r"^\#[a-zA-Z0-9]{6}$")

    def __init__(self):
        self._background_color = None
        self._fill_color = None

    def _is_color(self, color):
        return color and (color.lower() in self.COLOR_LIST or re.match(self.pattern, color))

    def set_background_color(self, color: str):
        self._background_color = color
        return self

    def set_fill_color(self, color: str):
        self._fill_color = color
        return self

    def build(self):
        if not self._is_color(self._background_color):
            raise ColorValueError("Invalid value for background color. <{}>".format(self._background_color))

        if not self._is_color(self._fill_color):
            raise ColorValueError("Invalid value for fill color. <{}>".format(self._fill_color))

        return self.Color(self._background_color.upper(), self._fill_color.upper())

    class Color:
        def __init__(self, background_color, fill_color):
            self._background_color = background_color
            self._fill_color = fill_color

        def __repr__(self):
            return "Background color: {}, Fill color: {}".format(self._background_color, self._fill_color)

        @property
        def background_color(self):
            return self._background_color

        @property
        def fill_color(self):
            return self._fill_color
