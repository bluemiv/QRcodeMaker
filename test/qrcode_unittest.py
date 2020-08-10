# -*- coding: utf-8 -*-

import unittest

import qrcode_maker


class QRCodeUnitTest(unittest.TestCase):

    @classmethod
    def setUp(cls) -> None:
        cls.url = r"https://memostack.tistory.com/"

    def test_custom_color_build(self):
        builder = qrcode_maker.QRCodeBuilder()
        qr = builder.set_data(self.url).set_image_path("../result/normal_qrcode.png").set_color("white",
                                                                                                "black").build()
        qr.save_img()

        qr = builder.set_image_path("../result/border_qrcode.png").set_border(30).build()
        qr.save_img()

        builder = qrcode_maker.QRCodeBuilder()
        qr = builder.set_data(self.url).set_image_path("../result/box_size_qrcode.png").set_box_size(30).set_color(
            "white", "black").build()
        qr.save_img()

    def test_theme_build(self):
        builder = qrcode_maker.QRCodeBuilder()
        qr = builder.set_data(self.url).set_image_path("../result/red_qrcode.png").set_theme("red").build()
        qr.save_img()

        qr = builder.set_image_path("../result/blue_qrcode.png").set_theme("blue").build()
        qr.save_img()

        qr = builder.set_image_path("../result/gray_qrcode.png").set_theme("gray").build()
        qr.save_img()

        qr = builder.set_image_path("../result/grape_qrcode.png").set_theme("grape").build()
        qr.save_img()

        qr = builder.set_image_path("../result/green_qrcode.png").set_theme("green").build()
        qr.save_img()

        qr = builder.set_image_path("../result/orange_qrcode.png").set_theme("orange").build()
        qr.save_img()

        qr = builder.set_image_path("../result/violet_qrcode.png").set_theme("violet").build()
        qr.save_img()

        qr = builder.set_image_path("../result/cyan_qrcode.png").set_theme("cyan").build()
        qr.save_img()

        qr = builder.set_image_path("../result/lime_qrcode.png").set_theme("lime").build()
        qr.save_img()

        qr = builder.set_image_path("../result/pink_qrcode.png").set_theme("pink").build()
        qr.save_img()

        qr = builder.set_image_path("../result/indigo_qrcode.png").set_theme("indigo").build()
        qr.save_img()

        qr = builder.set_image_path("../result/teal_qrcode.png").set_theme("teal").build()
        qr.save_img()

        qr = builder.set_image_path("../result/yellow_qrcode.png").set_theme("yellow").build()
        qr.save_img()


if __name__ == "__main__":
    unittest.main()
