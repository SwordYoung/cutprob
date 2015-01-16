#!/usr/bin/env python

if __name__ == "__main__":
    every = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 12, 14, 16, 18, 20, 24, 28, 32, 36, 40, 48, 56, 64, 72, 80, 96, 108, 120, 144, 168, 192, 216, 240, 288, 324, 360, 432, 504, 576, 648, 720, 864, 972, 1152, 1296, 1440, 1728, 2016, 2304, 2592, 2880, 3456, 3888, 4608, 5184, 5760, 6912, 8064, 9216, 10080, 11520, 12960, 14400, 17280, 19440, 23040, 25920, 28800, 34560, 40320, 46080, 50400, 57600, 64800, 72000, 86400, 97200, 103680, 116640, 138240, 155520, 172800, 207360, 241920, 276480, 302400, 345600, 388800, 432000, 518400, 583200, 622080, 699840, 829440, 933120, 1088640, 1209600, 1451520, 1693440, 1935360, 2116800, 2419200, 2721600, 3024000, 3628800, 4082400, 4354560, 4898880, 5806080, 6531840, 7620480, 8467200, 11612160, 13547520, 15482880, 16934400, 19353600, 21772800, 24192000, 29030400, 32659200, 34836480, 39191040, 46448640, 52254720, 60963840, 67737600, 92897280, 104509440, 121927680, 139345920, 152409600, 174182400, 195955200, 217728000, 261273600, 293932800, 313528320, 352719360, 418037760, 470292480, 548674560, 609638400, 836075520, 940584960, 1045094400, 1219276800, 1393459200, 1524096000, 1741824000, 1959552000, 2177280000, 2612736000, 2939328000, 3135283200, 3527193600, 4180377600, 4702924800, 5486745600, 6096384000, 8360755200, 9405849600, 10346434560, 11496038400, 13412044800, 15328051200, 16765056000, 19160064000, 21555072000, 23950080000, 28740096000, 32332608000, 34488115200, 38799129600, 45984153600, 51732172800, 60354201600, 67060224000, 91968307200, 100329062400, 112870195200, 124157214720, 137952460800, 160944537600, 183936614400, 201180672000, 229920768000, 258660864000, 287400960000, 344881152000, 387991296000, 413857382400, 465589555200, 551809843200, 620786073600, 724250419200, 804722688000, 1195587993600, 1304277811200, 1467312537600, 1614043791360, 1793381990400, 2092278988800, 2391175987200, 2615348736000, 2988969984000, 3362591232000, 3736212480000, 4483454976000, 5043886848000, 5380145971200, 6052664217600, 7173527961600, 8070218956800, 9415255449600, 10139505868800, 11266117632000, 16738231910400, 18259889356800, 20542375526400, 22596613079040, 25107347865600, 29291905843200, 33476463820800, 36614882304000, 41845579776000, 47076277248000, 52306974720000, 62768369664000, 70614415872000, 75322043596800, 84737299046400, 107602919424000, 121053284352000, 141228831744000, 152092588032000, 168991764480000, 251073478656000, 273898340352000, 308135632896000, 338949196185600, 376610217984000, 439378587648000, 502146957312000, 549223234560000, 627683696640000, 706144158720000, 784604620800000, 941525544960000, 1004293914624000, 1129830653952000, 1205152697548800, 1355796784742400, 1721646710784000, 1936852549632000, 2259661307904000, 2433481408512000, 2703868231680000, 4017175658496000, 4382373445632000, 4930170126336000, 5423187138969600, 6025763487744000, 7030057402368000, 8034351316992000, 8787571752960000, 10670622842880000, 12004450698240000, 13338278553600000, 16005934264320000, 17072996548608000, 19207121117184000, 20487595858329600, 23048545340620800, 29267994083328000, 32926493343744000, 38414242234368000, 41369183944704000, 45965759938560000, 68291986194432000, 74500348575744000, 83812892147712000, 92194181362483200, 108463742779392000, 126541033242624000, 144618323705856000, 158176291553280000, 192071211171840000, 216080112568320000, 240089013964800000, 288106816757760000, 307313937874944000, 345728180109312000, 368776725449932800, 414873816131174400, 526823893499904000, 592676880187392000, 691456360218624000, 744645311004672000, 827383678894080000]
    n = int(raw_input())

    for i in xrange(n):
        line = raw_input().strip()
        line = line.split(' ')
        l = int(line[0])
        r = int(line[1])
#        print "%d : %d" % (l, r)
        s = 0
        for t in every:
            if t >= l and t <= r:
                s += 1
        print s
