# -*- coding: utf-8 -*-

from . import color


class InvalidThemeError(RuntimeError):
    pass


class Theme:

    @staticmethod
    def get_blue_theme():
        builder = color.ColorBuilder()
        return builder.set_background_color("#e7f5ff").set_fill_color("#1c7ed6").build()

    @staticmethod
    def get_red_theme():
        builder = color.ColorBuilder()
        return builder.set_background_color("#fff5f5").set_fill_color("#fa5252").build()

    @staticmethod
    def get_gray_theme():
        builder = color.ColorBuilder()
        return builder.set_background_color("#f8f9fa").set_fill_color("#495057").build()

    @staticmethod
    def get_pink_theme():
        builder = color.ColorBuilder()
        return builder.set_background_color("#fff0f6").set_fill_color("#d6336c").build()

    @staticmethod
    def get_grape_theme():
        builder = color.ColorBuilder()
        return builder.set_background_color("#f8f0fc").set_fill_color("#ae3ec9").build()

    @staticmethod
    def get_violet_theme():
        builder = color.ColorBuilder()
        return builder.set_background_color("#f3f0ff").set_fill_color("#7048e8").build()

    @staticmethod
    def get_indigo_theme():
        builder = color.ColorBuilder()
        return builder.set_background_color("#edf2ff").set_fill_color("#4263eb").build()

    @staticmethod
    def get_cyan_theme():
        builder = color.ColorBuilder()
        return builder.set_background_color("#e3fafc").set_fill_color("#1098ad").build()

    @staticmethod
    def get_teal_theme():
        builder = color.ColorBuilder()
        return builder.set_background_color("#e6fcf5").set_fill_color("#0ca678").build()

    @staticmethod
    def get_green_theme():
        builder = color.ColorBuilder()
        return builder.set_background_color("#ebfbee").set_fill_color("#37b24d").build()

    @staticmethod
    def get_lime_theme():
        builder = color.ColorBuilder()
        return builder.set_background_color("#f4fce3").set_fill_color("#66a80f").build()

    @staticmethod
    def get_yellow_theme():
        builder = color.ColorBuilder()
        return builder.set_background_color("#fff9db").set_fill_color("#e67700").build()

    @staticmethod
    def get_orange_theme():
        builder = color.ColorBuilder()
        return builder.set_background_color("#fff4e6").set_fill_color("#f76707").build()
