# The Coupon Code
# Description:
# Your online store likes to give out coupons for special occasions. Some customers try to cheat the system by entering
# invalid codes or using expired coupons.
# Write a function called checkCoupon which verifies that a coupon code is valid and not expired.
#
# A coupon is no more valid on the day AFTER the expiration date. All dates will be passed as strings
# in this format: "MONTH DATE, YEAR".

import datetime

def check_coupon(entered_code, correct_code, current_date, expiration_date):
    strptime = datetime.datetime.strptime
    format = "%B %d, %Y"
    return strptime(current_date, format) <= strptime(expiration_date, format) and\
                             entered_code is correct_code

import unittest
class teste30(unittest.TestCase):
    def test_ex30(self):
            self.assertEqual(check_coupon('123','123','September 5, 2014','October 1, 2014'), True)
            self.assertEqual(check_coupon('123a','123','September 5, 2014','October 1, 2014'), False)