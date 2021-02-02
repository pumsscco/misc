#!/bin/bash
mlogfilter mongodb.log.2017 --from May 06 --to Jun >mongodb.log.2017-05
mlogfilter mongodb.log.2017 --from Jun --to Jul >mongodb.log.2017-06
mlogfilter mongodb.log.2017 --from Jul --to Aug >mongodb.log.2017-07
mlogfilter mongodb.log.2017 --from Aug --to Sep >mongodb.log.2017-08
mlogfilter mongodb.log.2017 --from Sep --to Oct >mongodb.log.2017-09
mlogfilter mongodb.log.2017 --from Oct --to Nov >mongodb.log.2017-10
mlogfilter mongodb.log.2017 --from Nov --to Dec >mongodb.log.2017-11
mlogfilter mongodb.log.2017 --from Dec  >mongodb.log.2017-12
mlogfilter mongodb.log.2018 --from Jan --to Feb >mongodb.log.2018-01
mlogfilter mongodb.log.2018 --from Feb --to Mar >mongodb.log.2018-02
mlogfilter mongodb.log.2018 --from Mar --to Apr >mongodb.log.2018-03
mlogfilter mongodb.log.2018 --from Apr --to May >mongodb.log.2018-04
mlogfilter mongodb.log.2018 --from May --to Jun >mongodb.log.2018-05
mlogfilter mongodb.log.2018 --from Jun --to Jul >mongodb.log.2018-06
mlogfilter mongodb.log.2018 --from Jul --to Aug >mongodb.log.2018-07
mlogfilter mongodb.log.2018 --from Aug --to Sep >mongodb.log.2018-08
mlogfilter mongodb.log.2018 --from Sep --to Oct >mongodb.log.2018-09
mlogfilter mongodb.log.2018 --from Oct --to Nov >mongodb.log.2018-10
mlogfilter mongodb.log.2018 --from Nov --to Dec >mongodb.log.2018-11
mlogfilter mongodb.log.2018 --from Dec >mongodb.log.2018-12

