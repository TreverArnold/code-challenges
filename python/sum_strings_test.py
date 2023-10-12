from sum_strings import sum_strings


# I can't figure out how to truly test this with the scale of digits it was meant for
# So these are just general operation tests, not to the full extent of the codes capabilities
def test_sum_strings():
    assert sum_strings("0", "0") == "0"
    assert sum_strings("0", "1") == "1"
    assert sum_strings("1", "0") == "1"
    assert sum_strings("0", "0001") == "1"
    assert sum_strings("0001", "0") == "1"
    assert (
        sum_strings(
            "29347578239455263045820972983465064376572634875623456902634950620346570623465473092634659238476056705460827650643756732452345723945906578623045786243857423607276854237348576092436",
            "979046723590348756923465203465023467526347652934876580237465782634856743259326457862834657896348756846798651663864861823641182364819643126438091263480123646123854165874651046543650134567237562430561640656",
        )
        == "979046723590348756923465232812601706981610698755849563702530159207491618882783360497785278242919380312271744298524100299697887825647293770194823715825847592030432788920437290401073741844091799779137733092"
    )