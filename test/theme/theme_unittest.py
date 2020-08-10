# -*- coding: utf-8 -*-

import unittest

from theme.theme import Theme


class ThemeUnitTest(unittest.TestCase):

    def test_get_theme(self):
        color = Theme.get_blue_theme()
        self.assertEqual("#1C7ED6", color.fill_color)
        self.assertEqual("#E7F5FF", color.background_color)

        color = Theme.get_red_theme()
        self.assertEqual("#FA5252", color.fill_color)
        self.assertEqual("#FFF5F5", color.background_color)

        color = Theme.get_cyan_theme()
        self.assertEqual("#1098AD", color.fill_color)
        self.assertEqual("#E3FAFC", color.background_color)

        color = Theme.get_grape_theme()
        self.assertEqual("#AE3EC9", color.fill_color)
        self.assertEqual("#F8F0FC", color.background_color)

        color = Theme.get_gray_theme()
        self.assertEqual("#495057", color.fill_color)
        self.assertEqual("#F8F9FA", color.background_color)

        color = Theme.get_green_theme()
        self.assertEqual("#37B24D", color.fill_color)
        self.assertEqual("#EBFBEE", color.background_color)

        color = Theme.get_indigo_theme()
        self.assertEqual("#4263EB", color.fill_color)
        self.assertEqual("#EDF2FF", color.background_color)

        color = Theme.get_lime_theme()
        self.assertEqual("#74B816", color.fill_color)
        self.assertEqual("#F4FCE3", color.background_color)

        color = Theme.get_orange_theme()
        self.assertEqual("#F76707", color.fill_color)
        self.assertEqual("#FFF4E6", color.background_color)

        color = Theme.get_pink_theme()
        self.assertEqual("#D6336C", color.fill_color)
        self.assertEqual("#FFF0F6", color.background_color)

        color = Theme.get_teal_theme()
        self.assertEqual("#0CA678", color.fill_color)
        self.assertEqual("#E6FCF5", color.background_color)

        color = Theme.get_violet_theme()
        self.assertEqual("#7048E8", color.fill_color)
        self.assertEqual("#F3F0FF", color.background_color)

        color = Theme.get_yellow_theme()
        self.assertEqual("#F59F00", color.fill_color)
        self.assertEqual("#FFF9DB", color.background_color)


if __name__ == "__main__":
    unittest.main()
