from hijri_converter import Hijri, Gregorian
from dates_list import gregorian_dates, tahsel_dates, rafaa_dates


Hijri_dates = ['06/09/1442',
               '29/08/1442',
               '29/08/1442',
               '23/08/1442',
               '23/08/1442',
               '19/08/1442',
               '18/08/1442',
               '17/08/1442',
               '17/08/1442',
               '02/08/1442',
               '01/08/1442',
               '01/08/1442',
               '18/07/1442',
               '18/07/1442',
               '13/07/1442',
               '13/07/1442',
               '11/07/1442',
               '10/07/1442',
               '10/07/1442',
               '10/07/1442',
               '10/07/1442',
               '10/07/1442',
               '10/07/1442',
               '09/07/1442',
               '09/07/1442', ]

def convert_from_hijri_to_gregorian():
    for d in Hijri_dates:
        # new = d.split('/')[::-1]
        new = d.split('/')
        # print(new)
        new_list = list(map(int, new))
        g = Hijri(new_list[2], new_list[1], new_list[0]).to_gregorian()
        print(g)

# Convert a Hijri date to Gregorian
# g = Hijri(1403, 2, 17).to_gregorian()

# Convert a Gregorian date to Hijri
# h = Gregorian(1982, 12, 2).to_hijri()

# print(g)
# print(h)

def convert_from_gregorian_to_hijri(dates):
    for d in dates:
        new = d.split('/')
        new_list = list(map(int, new))
        h = Gregorian(new_list[0], new_list[1], new_list[2]).to_hijri()
        print(h)



convert_from_gregorian_to_hijri(rafaa_dates)