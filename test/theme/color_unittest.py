# -*- coding: utf-8 -*-

import unittest

from theme.color import ColorBuilder, ColorValueError


class ColorBuilderUnitTest(unittest.TestCase):

    @classmethod
    def setUp(cls) -> None:
        pass

    def test_color_builder(self):
        builder = ColorBuilder()
        color = builder.set_fill_color("white").set_background_color("black").build()
        self.assertEqual("BLACK", color.background_color)
        self.assertEqual("WHITE", color.fill_color)

        color = builder.set_fill_color("#aaaddd").set_background_color("#cccfff").build()
        self.assertEqual("#CCCFFF", color.background_color)
        self.assertEqual("#AAADDD", color.fill_color)

        color = builder.set_background_color("blue").set_fill_color("#afafaf").build()
        self.assertEqual("BLUE", color.background_color)
        self.assertEqual("#AFAFAF", color.fill_color)

        self.assertRaises(ColorValueError, builder.set_background_color("test").set_fill_color("#afafaf").build)

        self.assertRaises(ColorValueError, builder.set_background_color("red").set_fill_color("#1a").build)

        self.assertRaises(ColorValueError, builder.set_background_color("").set_fill_color("black").build)
        self.assertRaises(ColorValueError, builder.set_background_color("yellow").set_fill_color("").build)

        self.assertRaises(ColorValueError, builder.set_fill_color("black").set_background_color("#sdsdsdsd").build)


if __name__ == "__main__":
    unittest.main()
