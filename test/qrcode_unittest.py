# -*- coding: utf-8 -*-

import unittest

import qrcode_maker


class QRCodeUnitTest(unittest.TestCase):

    @classmethod
    def setUp(cls) -> None:
        cls.url = r"https://memostack.tistory.com/"

    def test_custom_color_build(self):
        builder = qrcode_maker.QRCodeBuilder()
        qr = builder.set_data(self.url).set_image_path("../sample/normal_qrcode.png").set_color("white",
                                                                                                "black").build()
        qr.save_img()

        qr = builder.set_image_path("../sample/border_qrcode.png").set_border(30).build()
        qr.save_img()

        builder = qrcode_maker.QRCodeBuilder()
        qr = builder.set_data(self.url).set_image_path("../sample/box_size_qrcode.png").set_box_size(30).set_color(
            "white", "black").build()
        qr.save_img()

    def test_theme_build(self):
        builder = qrcode_maker.QRCodeBuilder()
        qr = builder.set_data(self.url).set_image_path("../sample/red_qrcode.png").set_theme("red").build()
        qr.save_img()

        qr = builder.set_image_path("../sample/blue_qrcode.png").set_theme("blue").build()
        qr.save_img()

        qr = builder.set_image_path("../sample/gray_qrcode.png").set_theme("gray").build()
        qr.save_img()

        qr = builder.set_image_path("../sample/grape_qrcode.png").set_theme("grape").build()
        qr.save_img()

        qr = builder.set_image_path("../sample/green_qrcode.png").set_theme("green").build()
        qr.save_img()

        qr = builder.set_image_path("../sample/orange_qrcode.png").set_theme("orange").build()
        qr.save_img()

        qr = builder.set_image_path("../sample/violet_qrcode.png").set_theme("violet").build()
        qr.save_img()

        qr = builder.set_image_path("../sample/cyan_qrcode.png").set_theme("cyan").build()
        qr.save_img()

        qr = builder.set_image_path("../sample/lime_qrcode.png").set_theme("lime").build()
        qr.save_img()

        qr = builder.set_image_path("../sample/pink_qrcode.png").set_theme("pink").build()
        qr.save_img()

        qr = builder.set_image_path("../sample/indigo_qrcode.png").set_theme("indigo").build()
        qr.save_img()

        qr = builder.set_image_path("../sample/teal_qrcode.png").set_theme("teal").build()
        qr.save_img()

        qr = builder.set_image_path("../sample/yellow_qrcode.png").set_theme("yellow").build()
        qr.save_img()


if __name__ == "__main__":
    unittest.main()
