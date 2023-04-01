import model_dars

avto1 = model_dars.avto_info("GM","Malibu","Qora", "avto", 2022, "tekin")
model_dars.info_print(avto1)
avto2 = model_dars.avto_info("BMW", "M6", "oq", "mehanika", 2022, "bepul")
model_dars.info_print(avto2)

import model_dars as m
avto1 = m.avto_info("GM", "Malibu", "Qora", "Avtomat", 2022, "bepul")
m.info_print(avto1)


import model_dars as a
avto1 = a.avto_kirit()
for avto in avto1:
    a.info_print(avto)
    
# from model_dars import avto_info, info_print
# avto = avto_info("GM", "Malibu", "Qora", "avtomat", 2022, "bepul")
# info_print(avto1)    


# from model_dars import avto_info as info, info_print as iprint
# avto1 = ("GM", "Malibu", "Qora", "avtomat", 2020, 40000)
# iprint(avto1)

# from model_dars import *
# avto1 = avto_info("GM", "Malibu", "Qora", "Avtomat", 2022, "bepul")
# info_print(avto1)













































