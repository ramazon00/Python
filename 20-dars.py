import avto_dars_mod
avto1=avto_dars_mod.avto_info("GM","Malibu","oq","avtomat",2022,40000)
avto_dars_mod.info_print(avto1)

import avto_dars_mod as a
avto1=a.avto_info("GM","Malibu","oq","avtomat",2022,40000)
a.info_print(avto1)


import avto_dars_mod as a

avto1=a.avto_kirit()
for avto in avto1:
    a.info_print(avto)



from avto_dars_mod import avto_info, info_print

avto1=avto_info("GM","Malibu","oq","avtomat",2022,40000)
info_print(avto1)

from avto_dars_mod import avto_info as ainfo, info_print as iprint
avto1=ainfo("GM","Malibu","kulrang","avtomat",2022,40000)
iprint(avto1)


from avto_dars_mod import*
avto1=avto_info("GM","Malibu","qora","avtomat",2022,40000)
info_print(avto1)