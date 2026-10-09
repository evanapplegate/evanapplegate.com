# My least favorite ten thousand words

To finish a cartography & GIS masters degree at UW-Madison I had to make a map that required

1) "Basic command line" levels of computer literacy

2) A guess at the physical phenomena that a grid of numbers expressing some radiometric quantity concerning earth’s surface or atmosphere purported to relate to

I failed, I spent like ~200 hours of work across months, emailing, searching
wandering around the space sciences engineering center laptop in hand. Had to
abandon original topic re: "relationship between earth’s surface brightness
and earth’s atmospheric-terrestrial energy balance," which was good,
because I knew nothing and couldn’t even make an educated guess. Gross
scales, coarse materials, a ~3600x7200 grid of numbers was supposed to tell
me about THE WHOLE PLANET EARTH’S exchange of photons? C’mon

My notes file below, may you understand something called "White Sky Albedo" better than I did 


lmao i can’t even remember what I’m supposed to do! this shit hieroglyphics!


**Environmental Research Letters -** check their formats, you’ll cut it down, put the rest in SI.


**Latest questions**


- why don’t I just use class 13 from the albedo LUM and skip the euclidian allocation/nearest neighbor part?
“Since the LUMs include albedo and BRDF statistics for each IGBP class for all possible locations, they can be used to generate albedo maps for projected land cover”



- “Since the LUMs include albedo and BRDF statistics for each IGBP class for all possible locations, they can be used to generate albedo maps for projected land cover”

**mutlu meeting 3/29**


- forcing calc is in realm of possibility, so you’re okay on that

- recommends keeping track of LC through the whole process, but can just do it post-facto; after you get your final RF map for the 3 classes, overlay with original LC map and just see what coincides. you’ll have to do it once per month and then the +/- std dev but that’s still easier than keeping track of each class I think? I have 17 classes x 3 OG rasters x 12 months x 12 1 sigma x 12 1-sigma. but wait will I have to do that anyway post-facto?
you want to be able to say “for the 25%+ class, tk converted from boreal forest, tk from desert, etc.) you dont need the std dev since all we care about is the previous LC, right?



- you want to be able to say “for the 25%+ class, tk converted from boreal forest, tk from desert, etc.) you dont need the std dev since all we care about is the previous LC, right?

- use these probability classes
25%+ - least conservative
50%+ - medium conservative
75%+ - most conservative



1. 25%+ - least conservative

1. 50%+ - medium conservative

1. 75%+ - most conservative

- ghimire, soden papers can help with the vocabulary for your intro and lit review.

**outstanding questions**


- The forcing calc
Ghimire’s was forcing per unit area = (Δmonthly WSA x shell’s WSA kernel) + (Δmonthly BSA x shell’s BSA kernel)
Mine is: forcing per unit area = (((Δ WSA x fraction WSA) x WSA kernel ) + ((Δ BSA x fraction BSA) x BSA kernel)))
we use the fractions because we dont know the contributions. because kernels have both BSA and WSA, we separate their contributions.


what does my final number even mean? Summing all the cells for the segment “cells that are 100% likely to become urban in the future), I got WSA term = 6.4 and BSA term = 12.6. Divided by the number of cells (24,588) yields 0.000774 average per cell. so this makes sense, can only go up.
Do I need to keep track of albedo change by original LC class?
document how it’s geographically varying; how it matters from LC > to current urban
do a flowchart
find two contrasting cases; boreal forest converting to urban vs. desert converting to urban.
proximity is king here; they bloom out from current cities


change to **3 classes,** each probability class has RF, + std dev, - std dev. whiskers and error bars at the end.
25+; separate into discrete LC rasters?
land cover class 1
land cover class 2
land cover class 3


50+
75+


**do LC change post-facto! as long as you keep the 3 classes, then**
why more BSA? kernels isolate land surface component only, so less atmo effects overall, and less WSA effects.
read more ghimire and shell to see why that is, goes in the explanatory.


just keep track of what you did to each file.
bring the maps, then we’ll pick out what we want to present.



- Ghimire’s was forcing per unit area = (Δmonthly WSA x shell’s WSA kernel) + (Δmonthly BSA x shell’s BSA kernel)

- Mine is: forcing per unit area = (((Δ WSA x fraction WSA) x WSA kernel ) + ((Δ BSA x fraction BSA) x BSA kernel)))
we use the fractions because we dont know the contributions. because kernels have both BSA and WSA, we separate their contributions.



- we use the fractions because we dont know the contributions. because kernels have both BSA and WSA, we separate their contributions.

- what does my final number even mean? Summing all the cells for the segment “cells that are 100% likely to become urban in the future), I got WSA term = 6.4 and BSA term = 12.6. Divided by the number of cells (24,588) yields 0.000774 average per cell. so this makes sense, can only go up.

- Do I need to keep track of albedo change by original LC class?
document how it’s geographically varying; how it matters from LC > to current urban
do a flowchart
find two contrasting cases; boreal forest converting to urban vs. desert converting to urban.
proximity is king here; they bloom out from current cities



- document how it’s geographically varying; how it matters from LC > to current urban

- do a flowchart

- find two contrasting cases; boreal forest converting to urban vs. desert converting to urban.

- proximity is king here; they bloom out from current cities

- change to **3 classes,** each probability class has RF, + std dev, - std dev. whiskers and error bars at the end.
25+; separate into discrete LC rasters?
land cover class 1
land cover class 2
land cover class 3


50+
75+



- 25+; separate into discrete LC rasters?
land cover class 1
land cover class 2
land cover class 3



- land cover class 1

- land cover class 2

- land cover class 3

- 50+

- 75+

- **do LC change post-facto! as long as you keep the 3 classes, then**

- why more BSA? kernels isolate land surface component only, so less atmo effects overall, and less WSA effects.
read more ghimire and shell to see why that is, goes in the explanatory.



- read more ghimire and shell to see why that is, goes in the explanatory.

- just keep track of what you did to each file.

- bring the maps, then we’ll pick out what we want to present.

**Pure data tasks**


- get albedo rasters into something easily readable: converted to tiff, stripped out water since I don’t care, bands = IGBP classes now. **CHECK**
Lower file size using extract by mask? nah I need the extents to match all the way around, the damn euclidian allocations won’t stand for that. but heyyy I can clip everything by the same shapefile right, then set extents to match the kernels? gonna try that, it’ll make this way faster.
when you get an actual good file, can use this to clip by shapefile: gdalwarp -of GTiff -dstnodata 0 -ot Int16 -te -180 -90 180 90 -cutline arc_dissolved.shp -cl arc_dissolved -crop_to_cutline BSA_Aug_mean.tif albedo_cropped3.tiff --config GDAL_CACHEMAX 2048 -multi
*well that works but it’s incredibly slow AND it only cuts down filesize from 800mb to 500mb. Not worth the time or extent fuckery. nixed!*





- Lower file size using extract by mask? nah I need the extents to match all the way around, the damn euclidian allocations won’t stand for that. but heyyy I can clip everything by the same shapefile right, then set extents to match the kernels? gonna try that, it’ll make this way faster.

- when you get an actual good file, can use this to clip by shapefile: gdalwarp -of GTiff -dstnodata 0 -ot Int16 -te -180 -90 180 90 -cutline arc_dissolved.shp -cl arc_dissolved -crop_to_cutline BSA_Aug_mean.tif albedo_cropped3.tiff --config GDAL_CACHEMAX 2048 -multi
*well that works but it’s incredibly slow AND it only cuts down filesize from 800mb to 500mb. Not worth the time or extent fuckery. nixed!*



- *well that works but it’s incredibly slow AND it only cuts down filesize from 800mb to 500mb. Not worth the time or extent fuckery. nixed!*

- New categories **CHECK**
25%+ - value is 25
50%+ - value is 50
75%+ - value is 75
extant - value is 101
this did it: gdal_calc.py --calc "A*(A==101)" --format GTiff --type UInt16 --NoDataValue 0 -A input.tif --A_band 1 --outfile output.tif
and to get the extents right: gdalwarp -ot Int16 -te -180 -90 180 90 75_and_up.tif 75_and_up2.tif





- 25%+ - value is 25

- 50%+ - value is 50

- 75%+ - value is 75

- extant - value is 101
this did it: gdal_calc.py --calc "A*(A==101)" --format GTiff --type UInt16 --NoDataValue 0 -A input.tif --A_band 1 --outfile output.tif
and to get the extents right: gdalwarp -ot Int16 -te -180 -90 180 90 75_and_up.tif 75_and_up2.tif



- this did it: gdal_calc.py --calc "A*(A==101)" --format GTiff --type UInt16 --NoDataValue 0 -A input.tif --A_band 1 --outfile output.tif

- and to get the extents right: gdalwarp -ot Int16 -te -180 -90 180 90 75_and_up.tif 75_and_up2.tif

- extant class 13 albedo; hey assign_albedos.py works, if you can get it to read what you like you can get this done lickety split
I mean i could do this pretty easily with batch scripting or gdal_calc as a subprocess, but it keeps throwing an error about "ERROR 1: TIFFOpen:: No such file or directory”. with a final "AttributeError: 'NoneType' object has no attribute ‘SetGeoTransform’.” so I dunno? If this worked it would be great!
sys.executable will always point to canopy, no matter terminal or canopy. so that may explain it? god canopy fucked my life up.
*this is taking guneralps current cities and assigning class 13 albedos from each of the following files. just a loop with band math, man.*


extant city with WSA, 12 months
extant city with WSA, 12 months + 1std dev
extant city with WSA, 12 months - 1std dev
extant city with BSA, 12 months
extant city with BSA, 12 months + 1std dev
extant city with BSA, 12 months - 1std dev



- I mean i could do this pretty easily with batch scripting or gdal_calc as a subprocess, but it keeps throwing an error about "ERROR 1: TIFFOpen:: No such file or directory”. with a final "AttributeError: 'NoneType' object has no attribute ‘SetGeoTransform’.” so I dunno? If this worked it would be great!
sys.executable will always point to canopy, no matter terminal or canopy. so that may explain it? god canopy fucked my life up.
*this is taking guneralps current cities and assigning class 13 albedos from each of the following files. just a loop with band math, man.*



- sys.executable will always point to canopy, no matter terminal or canopy. so that may explain it? god canopy fucked my life up.

- *this is taking guneralps current cities and assigning class 13 albedos from each of the following files. just a loop with band math, man.*

- extant city with WSA, 12 months

- extant city with WSA, 12 months + 1std dev

- extant city with WSA, 12 months - 1std dev

- extant city with BSA, 12 months

- extant city with BSA, 12 months + 1std dev

- extant city with BSA, 12 months - 1std dev

- euclidian allocation maps, arc cant read or write multiband tiffs for this function so going to get all these.
[ ]  
*this is taking what you just did up there, and using euclidian alloc to amoeba those values out. can batch it or use arcpy, probably going to batch it.*


extant city with WSA, 12 months
extant city with WSA, 12 months + 1std dev
extant city with WSA, 12 months - 1std dev
extant city with BSA, 12 months
extant city with BSA, 12 months + 1std dev
extant city with BSA, 12 months - 1std dev



- [ ]  
*this is taking what you just did up there, and using euclidian alloc to amoeba those values out. can batch it or use arcpy, probably going to batch it.*



- *this is taking what you just did up there, and using euclidian alloc to amoeba those values out. can batch it or use arcpy, probably going to batch it.*

- extant city with WSA, 12 months

- extant city with WSA, 12 months + 1std dev

- extant city with WSA, 12 months - 1std dev

- extant city with BSA, 12 months

- extant city with BSA, 12 months + 1std dev

- extant city with BSA, 12 months - 1std dev

- Assign %-chance pixels to extant’s albedos
Schneider’s 2001 data has all the LC classes! Seto’s data is in goode homolosine, schneiders provided in the same; maybe if I resample in the exact same way while NOT changing projection, I can see if schneider’s urban class is co-incident with seto’s if so, then the rest should match up. they both used goode homolosine! .msked.bip is the one you want
setting both layer CRS to the custom proj "+proj=igh +a=6371007.181 +b=6371007.181 +units=m +no_defs” gets them nicely co-incident. resampling with gdal_warp and tr -5000, default nearest neighbor, gets VERY close to their data! going to try it again with Arc.
Arc time: arc is a fucking moron, the .hdr cant have .bip on the end too. so match filenames exactly and it’ll read the dataset. 10.1's authalic sphere rounds the axes measurements to 6371007.181?
seto comes in as "GCS_MODIS_sphere," which must be why I had to fix it up in QGIS. defined schneider’s projection in arc to match seto’s, which had a decimal sphere called "GCS_MODIS_Sphere" that arc had never heard of.
resample without class 13 extraction first, match cell size to seto, use as snap raster: **perfect** **match on extant urban pixels, even the little scattered fucks. Yes!! can just fill in the isolated inland zero/waters and we’ll be good?
better to throw out any seto pixels that coincide with old-LC water, or fill in the waters on my old-LC layer with nearest neighbor? I assume seto had a water mask, but probably one that threw out single water pixels? or wasn’t accounted for? either:
don’t use any pixels that overlap water in the calc
find which seto pixels overlap water, extract them, use them as nibble mask? I’d tally up the # of seto-overlaps-water pixels just to see how many there are.
result: threw out 340 pixels out of an original total of 251,479, 0.001%, so i aint worried




schneider nodatas: 253, 254, 255. water is 0, 17.


reprojected both to WGS84, using native goofy decimal degree resolution and just typing in 0.05deg. all still overlapped nicely.


[http://chris35wills.github.io/python-gdal-raster-io/](http://chris35wills.github.io/python-gdal-raster-io/) and [http://geoinformaticstutorial.blogspot.co.uk/2012/09/reading-raster-data-with-python-and-gdal.html](http://geoinformaticstutorial.blogspot.co.uk/2012/09/reading-raster-data-with-python-and-gdal.html) for ENVI and python?
split ALL non-extant pixels in seto file (1-100% chance) into land cover? but they cant encode more than one number? use arithmetic?
1-25 - 100
26-50 - 200
then add to LC raster one at a time
then get python to say
see value 109?
fetch albedo value from an albedo file, picking the right band
replace that value/write to a new file?
LORDY this will suck, like 300 gigs of files at the end!
waitaminit: store as multiband tiffs! mean, + std dev, - std dev = 3 bands. one for each month.




I have 3 rasters. The following has to be repeated for each:
Assign a value to each of them using raster calc; they overlay with a land cover map, so assign the class of whatever they overlay to each pixel.
Assign albedo value by reading from another file, which has one band per land cover class.
Say a pixel from the first step is now land cover class 5; the script looks in an albedo file, opens band 5, then replaces the pixel’s current value with whatever it overlays in the albedo file.
Repeat this 12x for 12 months of data, then +1 std deviation, then -1 std deviation.
There are 12 months of albedo data, so this happens over the 12 albedo rasters.
Then **+1** standard deviation value, which is collected from another raster with the same setup as the albedo raster (i.e. script would open this raster, find the value in band 5, add this value to the current raster, then save as a new value in a new band) Repeat 12 times, once for each month.
Then **1** standard deviation, same process as above, once per month for a total of 12.
So (12 months of data) + (12 months of +1 std dev data) + (12 months of -1 std dev data) = 36 outputs written across 12 3-band rasters.




Assign a new albedo value by reading from another file.
If a pixel is land cover class 5, or 7, or 1, or whatever, it doesn’t matter this time; the script looks in a different albedo file then replaces the pixel’s current value with whatever it overlays and writes a new raster.
Repeat this 12x for 12 months of data, then +1 std deviation, then -1 std deviation.
There are 12 months of albedo data, so this happens over the 12 albedo separate rasters.
Then **+1** standard deviation, which is collected from another raster with the same setup as the albedo raster (i.e. script would open this raster, find the pixel in band 13, replace the value of the current pixel, then save as a new raster.) Repeat 12 times, once for each month.
Then **1** standard deviation, same process as above, once per month for a total of 12.
So (12 months of data) + (12 months of +1 std dev data) + (12 months of -1 std dev data) = 36 outputs written across 12 3-band rasters




Generate a new set of rasters, a simple subtraction: the difference the between the old-land-cover albedo value and the new-land-cover albedo value.
Same thing as above: (12 months of data) + (12 months of +1 std dev data) + (12 months of -1 std dev data) = 36 outputs across 12 3-band rasters
:moneybag: Looking for someone located anywhere + good at geo-python raster stuff to help me automate a raster processing task with GDAL and python. Basically band math over a few dozen files, likely a day or two’s work for someone competent, but I only have like a week to do it and I stink at python. Offering $750 to help me put together some scripts and parse the results into something I can play with, message me for deets or evandapplegate@gmail.com, please pass along to anyone who might be interested. :moneybag:







- Schneider’s 2001 data has all the LC classes! Seto’s data is in goode homolosine, schneiders provided in the same; maybe if I resample in the exact same way while NOT changing projection, I can see if schneider’s urban class is co-incident with seto’s if so, then the rest should match up. they both used goode homolosine! .msked.bip is the one you want

- setting both layer CRS to the custom proj "+proj=igh +a=6371007.181 +b=6371007.181 +units=m +no_defs” gets them nicely co-incident. resampling with gdal_warp and tr -5000, default nearest neighbor, gets VERY close to their data! going to try it again with Arc.
Arc time: arc is a fucking moron, the .hdr cant have .bip on the end too. so match filenames exactly and it’ll read the dataset. 10.1's authalic sphere rounds the axes measurements to 6371007.181?
seto comes in as "GCS_MODIS_sphere," which must be why I had to fix it up in QGIS. defined schneider’s projection in arc to match seto’s, which had a decimal sphere called "GCS_MODIS_Sphere" that arc had never heard of.
resample without class 13 extraction first, match cell size to seto, use as snap raster: **perfect** **match on extant urban pixels, even the little scattered fucks. Yes!! can just fill in the isolated inland zero/waters and we’ll be good?
better to throw out any seto pixels that coincide with old-LC water, or fill in the waters on my old-LC layer with nearest neighbor? I assume seto had a water mask, but probably one that threw out single water pixels? or wasn’t accounted for? either:
don’t use any pixels that overlap water in the calc
find which seto pixels overlap water, extract them, use them as nibble mask? I’d tally up the # of seto-overlaps-water pixels just to see how many there are.
result: threw out 340 pixels out of an original total of 251,479, 0.001%, so i aint worried




schneider nodatas: 253, 254, 255. water is 0, 17.


reprojected both to WGS84, using native goofy decimal degree resolution and just typing in 0.05deg. all still overlapped nicely.



- Arc time: arc is a fucking moron, the .hdr cant have .bip on the end too. so match filenames exactly and it’ll read the dataset. 10.1's authalic sphere rounds the axes measurements to 6371007.181?

- seto comes in as "GCS_MODIS_sphere," which must be why I had to fix it up in QGIS. defined schneider’s projection in arc to match seto’s, which had a decimal sphere called "GCS_MODIS_Sphere" that arc had never heard of.

- resample without class 13 extraction first, match cell size to seto, use as snap raster: **perfect** **match on extant urban pixels, even the little scattered fucks. Yes!! can just fill in the isolated inland zero/waters and we’ll be good?
better to throw out any seto pixels that coincide with old-LC water, or fill in the waters on my old-LC layer with nearest neighbor? I assume seto had a water mask, but probably one that threw out single water pixels? or wasn’t accounted for? either:
don’t use any pixels that overlap water in the calc
find which seto pixels overlap water, extract them, use them as nibble mask? I’d tally up the # of seto-overlaps-water pixels just to see how many there are.
result: threw out 340 pixels out of an original total of 251,479, 0.001%, so i aint worried




schneider nodatas: 253, 254, 255. water is 0, 17.



- better to throw out any seto pixels that coincide with old-LC water, or fill in the waters on my old-LC layer with nearest neighbor? I assume seto had a water mask, but probably one that threw out single water pixels? or wasn’t accounted for? either:
don’t use any pixels that overlap water in the calc
find which seto pixels overlap water, extract them, use them as nibble mask? I’d tally up the # of seto-overlaps-water pixels just to see how many there are.
result: threw out 340 pixels out of an original total of 251,479, 0.001%, so i aint worried





- don’t use any pixels that overlap water in the calc

- find which seto pixels overlap water, extract them, use them as nibble mask? I’d tally up the # of seto-overlaps-water pixels just to see how many there are.
result: threw out 340 pixels out of an original total of 251,479, 0.001%, so i aint worried



- result: threw out 340 pixels out of an original total of 251,479, 0.001%, so i aint worried

- schneider nodatas: 253, 254, 255. water is 0, 17.

- reprojected both to WGS84, using native goofy decimal degree resolution and just typing in 0.05deg. all still overlapped nicely.

- [http://chris35wills.github.io/python-gdal-raster-io/](http://chris35wills.github.io/python-gdal-raster-io/) and [http://geoinformaticstutorial.blogspot.co.uk/2012/09/reading-raster-data-with-python-and-gdal.html](http://geoinformaticstutorial.blogspot.co.uk/2012/09/reading-raster-data-with-python-and-gdal.html) for ENVI and python?

- split ALL non-extant pixels in seto file (1-100% chance) into land cover? but they cant encode more than one number? use arithmetic?
1-25 - 100
26-50 - 200
then add to LC raster one at a time
then get python to say
see value 109?
fetch albedo value from an albedo file, picking the right band
replace that value/write to a new file?
LORDY this will suck, like 300 gigs of files at the end!
waitaminit: store as multiband tiffs! mean, + std dev, - std dev = 3 bands. one for each month.





- 1-25 - 100

- 26-50 - 200

- then add to LC raster one at a time

- then get python to say
see value 109?
fetch albedo value from an albedo file, picking the right band
replace that value/write to a new file?
LORDY this will suck, like 300 gigs of files at the end!
waitaminit: store as multiband tiffs! mean, + std dev, - std dev = 3 bands. one for each month.



- see value 109?

- fetch albedo value from an albedo file, picking the right band

- replace that value/write to a new file?

- LORDY this will suck, like 300 gigs of files at the end!

- waitaminit: store as multiband tiffs! mean, + std dev, - std dev = 3 bands. one for each month.

- I have 3 rasters. The following has to be repeated for each:
Assign a value to each of them using raster calc; they overlay with a land cover map, so assign the class of whatever they overlay to each pixel.
Assign albedo value by reading from another file, which has one band per land cover class.
Say a pixel from the first step is now land cover class 5; the script looks in an albedo file, opens band 5, then replaces the pixel’s current value with whatever it overlays in the albedo file.
Repeat this 12x for 12 months of data, then +1 std deviation, then -1 std deviation.
There are 12 months of albedo data, so this happens over the 12 albedo rasters.
Then **+1** standard deviation value, which is collected from another raster with the same setup as the albedo raster (i.e. script would open this raster, find the value in band 5, add this value to the current raster, then save as a new value in a new band) Repeat 12 times, once for each month.
Then **1** standard deviation, same process as above, once per month for a total of 12.
So (12 months of data) + (12 months of +1 std dev data) + (12 months of -1 std dev data) = 36 outputs written across 12 3-band rasters.




Assign a new albedo value by reading from another file.
If a pixel is land cover class 5, or 7, or 1, or whatever, it doesn’t matter this time; the script looks in a different albedo file then replaces the pixel’s current value with whatever it overlays and writes a new raster.
Repeat this 12x for 12 months of data, then +1 std deviation, then -1 std deviation.
There are 12 months of albedo data, so this happens over the 12 albedo separate rasters.
Then **+1** standard deviation, which is collected from another raster with the same setup as the albedo raster (i.e. script would open this raster, find the pixel in band 13, replace the value of the current pixel, then save as a new raster.) Repeat 12 times, once for each month.
Then **1** standard deviation, same process as above, once per month for a total of 12.
So (12 months of data) + (12 months of +1 std dev data) + (12 months of -1 std dev data) = 36 outputs written across 12 3-band rasters




Generate a new set of rasters, a simple subtraction: the difference the between the old-land-cover albedo value and the new-land-cover albedo value.
Same thing as above: (12 months of data) + (12 months of +1 std dev data) + (12 months of -1 std dev data) = 36 outputs across 12 3-band rasters
:moneybag: Looking for someone located anywhere + good at geo-python raster stuff to help me automate a raster processing task with GDAL and python. Basically band math over a few dozen files, likely a day or two’s work for someone competent, but I only have like a week to do it and I stink at python. Offering $750 to help me put together some scripts and parse the results into something I can play with, message me for deets or evandapplegate@gmail.com, please pass along to anyone who might be interested. :moneybag:





- Assign a value to each of them using raster calc; they overlay with a land cover map, so assign the class of whatever they overlay to each pixel.

- Assign albedo value by reading from another file, which has one band per land cover class.
Say a pixel from the first step is now land cover class 5; the script looks in an albedo file, opens band 5, then replaces the pixel’s current value with whatever it overlays in the albedo file.
Repeat this 12x for 12 months of data, then +1 std deviation, then -1 std deviation.
There are 12 months of albedo data, so this happens over the 12 albedo rasters.
Then **+1** standard deviation value, which is collected from another raster with the same setup as the albedo raster (i.e. script would open this raster, find the value in band 5, add this value to the current raster, then save as a new value in a new band) Repeat 12 times, once for each month.
Then **1** standard deviation, same process as above, once per month for a total of 12.
So (12 months of data) + (12 months of +1 std dev data) + (12 months of -1 std dev data) = 36 outputs written across 12 3-band rasters.





- Say a pixel from the first step is now land cover class 5; the script looks in an albedo file, opens band 5, then replaces the pixel’s current value with whatever it overlays in the albedo file.

- Repeat this 12x for 12 months of data, then +1 std deviation, then -1 std deviation.
There are 12 months of albedo data, so this happens over the 12 albedo rasters.
Then **+1** standard deviation value, which is collected from another raster with the same setup as the albedo raster (i.e. script would open this raster, find the value in band 5, add this value to the current raster, then save as a new value in a new band) Repeat 12 times, once for each month.
Then **1** standard deviation, same process as above, once per month for a total of 12.
So (12 months of data) + (12 months of +1 std dev data) + (12 months of -1 std dev data) = 36 outputs written across 12 3-band rasters.



- There are 12 months of albedo data, so this happens over the 12 albedo rasters.

- Then **+1** standard deviation value, which is collected from another raster with the same setup as the albedo raster (i.e. script would open this raster, find the value in band 5, add this value to the current raster, then save as a new value in a new band) Repeat 12 times, once for each month.

- Then **1** standard deviation, same process as above, once per month for a total of 12.

- So (12 months of data) + (12 months of +1 std dev data) + (12 months of -1 std dev data) = 36 outputs written across 12 3-band rasters.

- Assign a new albedo value by reading from another file.
If a pixel is land cover class 5, or 7, or 1, or whatever, it doesn’t matter this time; the script looks in a different albedo file then replaces the pixel’s current value with whatever it overlays and writes a new raster.
Repeat this 12x for 12 months of data, then +1 std deviation, then -1 std deviation.
There are 12 months of albedo data, so this happens over the 12 albedo separate rasters.
Then **+1** standard deviation, which is collected from another raster with the same setup as the albedo raster (i.e. script would open this raster, find the pixel in band 13, replace the value of the current pixel, then save as a new raster.) Repeat 12 times, once for each month.
Then **1** standard deviation, same process as above, once per month for a total of 12.
So (12 months of data) + (12 months of +1 std dev data) + (12 months of -1 std dev data) = 36 outputs written across 12 3-band rasters





- If a pixel is land cover class 5, or 7, or 1, or whatever, it doesn’t matter this time; the script looks in a different albedo file then replaces the pixel’s current value with whatever it overlays and writes a new raster.

- Repeat this 12x for 12 months of data, then +1 std deviation, then -1 std deviation.
There are 12 months of albedo data, so this happens over the 12 albedo separate rasters.
Then **+1** standard deviation, which is collected from another raster with the same setup as the albedo raster (i.e. script would open this raster, find the pixel in band 13, replace the value of the current pixel, then save as a new raster.) Repeat 12 times, once for each month.
Then **1** standard deviation, same process as above, once per month for a total of 12.
So (12 months of data) + (12 months of +1 std dev data) + (12 months of -1 std dev data) = 36 outputs written across 12 3-band rasters



- There are 12 months of albedo data, so this happens over the 12 albedo separate rasters.

- Then **+1** standard deviation, which is collected from another raster with the same setup as the albedo raster (i.e. script would open this raster, find the pixel in band 13, replace the value of the current pixel, then save as a new raster.) Repeat 12 times, once for each month.

- Then **1** standard deviation, same process as above, once per month for a total of 12.

- So (12 months of data) + (12 months of +1 std dev data) + (12 months of -1 std dev data) = 36 outputs written across 12 3-band rasters

- Generate a new set of rasters, a simple subtraction: the difference the between the old-land-cover albedo value and the new-land-cover albedo value.
Same thing as above: (12 months of data) + (12 months of +1 std dev data) + (12 months of -1 std dev data) = 36 outputs across 12 3-band rasters
:moneybag: Looking for someone located anywhere + good at geo-python raster stuff to help me automate a raster processing task with GDAL and python. Basically band math over a few dozen files, likely a day or two’s work for someone competent, but I only have like a week to do it and I stink at python. Offering $750 to help me put together some scripts and parse the results into something I can play with, message me for deets or evandapplegate@gmail.com, please pass along to anyone who might be interested. :moneybag:



- Same thing as above: (12 months of data) + (12 months of +1 std dev data) + (12 months of -1 std dev data) = 36 outputs across 12 3-band rasters
:moneybag: Looking for someone located anywhere + good at geo-python raster stuff to help me automate a raster processing task with GDAL and python. Basically band math over a few dozen files, likely a day or two’s work for someone competent, but I only have like a week to do it and I stink at python. Offering $750 to help me put together some scripts and parse the results into something I can play with, message me for deets or evandapplegate@gmail.com, please pass along to anyone who might be interested. :moneybag:

- could this be done with vector? Then I’d only have to generate one file per each of the probability classes, but then how to move albedo values in the raster > values in their own column in the points? and then how to do changes/subtraction?

What are you looking to end up with?


- Euclidian allocation - 12 files, probably composed from individuals since I don’t think arcgis lets you write to multi-band tiffs. or do it with composite bands...
January
mean albedo in band 1
+1 std dev in band 2
1 std dev in band 3


Feb
Mar
Apri
May
June
July
Aug
Sep
Oct
Nov
Dec



- January
mean albedo in band 1
+1 std dev in band 2
1 std dev in band 3



- mean albedo in band 1

- +1 std dev in band 2

- 1 std dev in band 3

- Feb

- Mar

- Apri

- May

- June

- July

- Aug

- Sep

- Oct

- Nov

- Dec

- Old-LC files: 3 probabilities x 15 land cover classes x 12 months x 3 values (mean, +1 sigma, -1 sigma) x .103gb per raster = 167 gigs
25%+
land cover class 1
January
mean albedo in band 1
+1 std dev in band 2
1 std dev in band 3


Feb
Mar
Apri
May
June
July
Aug
Sep
Oct
Nov
Dec


Class 2
Class 3
Class 4
Class 5
Class 6
Class 7
Class 8
Class 9
Class 10
Class 11
Class 12
Class 14
Class 15
Class 16


50%+
75%+



- 25%+
land cover class 1
January
mean albedo in band 1
+1 std dev in band 2
1 std dev in band 3


Feb
Mar
Apri
May
June
July
Aug
Sep
Oct
Nov
Dec


Class 2
Class 3
Class 4
Class 5
Class 6
Class 7
Class 8
Class 9
Class 10
Class 11
Class 12
Class 14
Class 15
Class 16



- land cover class 1
January
mean albedo in band 1
+1 std dev in band 2
1 std dev in band 3


Feb
Mar
Apri
May
June
July
Aug
Sep
Oct
Nov
Dec



- January
mean albedo in band 1
+1 std dev in band 2
1 std dev in band 3



- mean albedo in band 1

- +1 std dev in band 2

- 1 std dev in band 3

- Feb

- Mar

- Apri

- May

- June

- July

- Aug

- Sep

- Oct

- Nov

- Dec

- Class 2

- Class 3

- Class 4

- Class 5

- Class 6

- Class 7

- Class 8

- Class 9

- Class 10

- Class 11

- Class 12

- Class 14

- Class 15

- Class 16

- 50%+

- 75%+

- New-LC (now urban) files: 3 probabilities x 12 months x 3 values (mean, +1 sigma, -1 sigma) x .130gb = 14 gigs
25%+
January
mean albedo in band 1
+1 std dev in band 2
1 std dev in band 3




50%+
75%+



- 25%+
January
mean albedo in band 1
+1 std dev in band 2
1 std dev in band 3





- January
mean albedo in band 1
+1 std dev in band 2
1 std dev in band 3



- mean albedo in band 1

- +1 std dev in band 2

- 1 std dev in band 3

- 50%+

- 75%+

- Difference files: 3 probabilities x 12 months x 3 values (mean, +1 sigma, -1 sigma) x .130gb = 14 gigs
25%+
January
mean albedo in band 1
+1 std dev in band 2
1 std dev in band 3




50%+
75%+



- 25%+
January
mean albedo in band 1
+1 std dev in band 2
1 std dev in band 3





- January
mean albedo in band 1
+1 std dev in band 2
1 std dev in band 3



- mean albedo in band 1

- +1 std dev in band 2

- 1 std dev in band 3

- 50%+

- 75%+

:moneybag: Looking for someone located anywhere + good at geo-python raster stuff to help me automate a raster processing task with GDAL and python. It’s basically band math over a few dozen files, likely a day or two’s work for someone competent, but I only have like a week to do it and I stink at python. Offering $750 to help me put together a script and parse the results into something I can play with; message me for deets. :moneybag:


**python fuckery**


- /Library/Frameworks/GDAL.framework/Versions shows I have 1.11, running the gdalinfo in the “program” folder there says i have 1.11.4 AND it supports HDF4.
man it really hates quotes in your paths, if you try to call this to/from any paths with quotes it wont work. anyway this works: /Library/Frameworks/GDAL.framework/Versions/1.11/Programs/gdal_translate -of GTiff HDF4_EOS:EOS_GRID:"MCD12Q1.A2001001.h21v06.051.2014287163907.hdf":MOD12Q1:"Land_Cover_Type_1" test.tiff
to run a bash script from the terminal: sh your_script.sh
okay we’re going to test resample with MCD12Q1.A2001001.h20v06.051.2014287163707, which is over egypt. seeing if resampling to 0.05 deg matches up with their shit, then I can mosaic the rest.
testing in arc: loads nice in arcgis, which is a change. anyway reprojecting the 3707 tile to seto’s GCS and resampling, no go. ditto with taking the projected file and running nearest neighbor and majority resample from the toolbox.
they said in the SI they extracted the urban pixels then resampled: extracted class 13 from the reprojected file > then resample, no joy on any resample method. its closer though! typing in 5000 no diff than using seto as cell size, makes sense.
how about extracting, resampling, then reprojecting? slightly diff results from using seto as snap raster, but they wouldnt have done that since they, you know, did this first. so proceeding using unsnapped. okay so far the closest is extracted first, then reprojected, then nearest neighbor, using seto as snap raster.
majority is way too generous, cubic and bilinear identical. im stumped, can’t get the extant city pixels to match up.
maybe its because they said "circa 2000," and im using 2001? this data got a revise in 2016, waybackmachine says the 005 was last there in 2012. MCD12Q1.005 is what I need to replicate this and I have MCD12Q1.051. Asked USGS, maybe I can get it from someone else?






they come out with "+proj=sinu +lon_0=0 +x_0=0 +y_0=0 +a=6371007.181 +b=6371007.181 +units=m +no_defs”



- man it really hates quotes in your paths, if you try to call this to/from any paths with quotes it wont work. anyway this works: /Library/Frameworks/GDAL.framework/Versions/1.11/Programs/gdal_translate -of GTiff HDF4_EOS:EOS_GRID:"MCD12Q1.A2001001.h21v06.051.2014287163907.hdf":MOD12Q1:"Land_Cover_Type_1" test.tiff
to run a bash script from the terminal: sh your_script.sh
okay we’re going to test resample with MCD12Q1.A2001001.h20v06.051.2014287163707, which is over egypt. seeing if resampling to 0.05 deg matches up with their shit, then I can mosaic the rest.
testing in arc: loads nice in arcgis, which is a change. anyway reprojecting the 3707 tile to seto’s GCS and resampling, no go. ditto with taking the projected file and running nearest neighbor and majority resample from the toolbox.
they said in the SI they extracted the urban pixels then resampled: extracted class 13 from the reprojected file > then resample, no joy on any resample method. its closer though! typing in 5000 no diff than using seto as cell size, makes sense.
how about extracting, resampling, then reprojecting? slightly diff results from using seto as snap raster, but they wouldnt have done that since they, you know, did this first. so proceeding using unsnapped. okay so far the closest is extracted first, then reprojected, then nearest neighbor, using seto as snap raster.
majority is way too generous, cubic and bilinear identical. im stumped, can’t get the extant city pixels to match up.
maybe its because they said "circa 2000," and im using 2001? this data got a revise in 2016, waybackmachine says the 005 was last there in 2012. MCD12Q1.005 is what I need to replicate this and I have MCD12Q1.051. Asked USGS, maybe I can get it from someone else?







- to run a bash script from the terminal: sh your_script.sh

- okay we’re going to test resample with MCD12Q1.A2001001.h20v06.051.2014287163707, which is over egypt. seeing if resampling to 0.05 deg matches up with their shit, then I can mosaic the rest.
testing in arc: loads nice in arcgis, which is a change. anyway reprojecting the 3707 tile to seto’s GCS and resampling, no go. ditto with taking the projected file and running nearest neighbor and majority resample from the toolbox.
they said in the SI they extracted the urban pixels then resampled: extracted class 13 from the reprojected file > then resample, no joy on any resample method. its closer though! typing in 5000 no diff than using seto as cell size, makes sense.
how about extracting, resampling, then reprojecting? slightly diff results from using seto as snap raster, but they wouldnt have done that since they, you know, did this first. so proceeding using unsnapped. okay so far the closest is extracted first, then reprojected, then nearest neighbor, using seto as snap raster.
majority is way too generous, cubic and bilinear identical. im stumped, can’t get the extant city pixels to match up.
maybe its because they said "circa 2000," and im using 2001? this data got a revise in 2016, waybackmachine says the 005 was last there in 2012. MCD12Q1.005 is what I need to replicate this and I have MCD12Q1.051. Asked USGS, maybe I can get it from someone else?





- testing in arc: loads nice in arcgis, which is a change. anyway reprojecting the 3707 tile to seto’s GCS and resampling, no go. ditto with taking the projected file and running nearest neighbor and majority resample from the toolbox.

- they said in the SI they extracted the urban pixels then resampled: extracted class 13 from the reprojected file > then resample, no joy on any resample method. its closer though! typing in 5000 no diff than using seto as cell size, makes sense.
how about extracting, resampling, then reprojecting? slightly diff results from using seto as snap raster, but they wouldnt have done that since they, you know, did this first. so proceeding using unsnapped. okay so far the closest is extracted first, then reprojected, then nearest neighbor, using seto as snap raster.
majority is way too generous, cubic and bilinear identical. im stumped, can’t get the extant city pixels to match up.
maybe its because they said "circa 2000," and im using 2001? this data got a revise in 2016, waybackmachine says the 005 was last there in 2012. MCD12Q1.005 is what I need to replicate this and I have MCD12Q1.051. Asked USGS, maybe I can get it from someone else?



- how about extracting, resampling, then reprojecting? slightly diff results from using seto as snap raster, but they wouldnt have done that since they, you know, did this first. so proceeding using unsnapped. okay so far the closest is extracted first, then reprojected, then nearest neighbor, using seto as snap raster.

- majority is way too generous, cubic and bilinear identical. im stumped, can’t get the extant city pixels to match up.

- maybe its because they said "circa 2000," and im using 2001? this data got a revise in 2016, waybackmachine says the 005 was last there in 2012. MCD12Q1.005 is what I need to replicate this and I have MCD12Q1.051. Asked USGS, maybe I can get it from someone else?

- they come out with "+proj=sinu +lon_0=0 +x_0=0 +y_0=0 +a=6371007.181 +b=6371007.181 +units=m +no_defs”

- /Users/traveler/Library/Enthought/Canopy_64bit/User/bin has a gdalinfo in there, that says i have 2.0.1. Anything I do in the terminal or in canopy will use 2.0.1, which can’t access HDF. So I gotta find a way to access 1.11? downgrade? gonna try

- [http://gis.stackexchange.com/questions/140398/mosaicking-and-projecting-modis-land-cover-data-mcd12q1](http://gis.stackexchange.com/questions/140398/mosaicking-and-projecting-modis-land-cover-data-mcd12q1)

**Questions for Jeff**


A = urban pixels


B = “future” urban pixels


C = albedo


D = standard deviation of albedos in C


- this is band math; just adding and subtracting. reclassify.

- same as in 579 lab, basically; to uptake albedo values, reclassify to 0, then add what’s underneath on the albedo values to.

- try this in Arc modelbuilder, grab the python script, then make a loop to just do it with your multiple inputs. out. jeff says build your workflow in modelbuilder and literally just loop over your stuff.

you use GDAL on HDF4? NOPE


Good packages? ever use rasterio? NOPE


**General software tips**


- Ugh arc exports all in ADF if you don’t tell it TIFF. or you can make 20MB tiffs to make this easier.

- QGIS Raster > landscape ecology > statistics can tell you how much of each pixel, just put 1 for cell size

- gdal_calc: set nodata = 0 means “when you’re all done, and you see a 0, that’s nodata"

- processing > results viewer to show stuff that got ouput to html, as in raster statistics

- you can run gdal_XXX.py scripts you download from anywhere as long as you put python in front of them and the full path. you cant just put em with the rest of the gdal python scripts in library/frameworks etc because of permissions I guess. so stash them where you need them and call with python and the full path from terminal.
here’s the path: /Library/Frameworks/GDAL.framework/Versions/1.11/Programs/



- here’s the path: /Library/Frameworks/GDAL.framework/Versions/1.11/Programs/

- r.report will give you a histo, if its not outputting raw text you have to make it save to a path that has no spaces.

- you’ll get incorrect min/max values no matter what you use to calc the stats (python gdal bindings, command line, GRASS, etc…) unless you run a gdal_translate with “-stats" first; this creates a new tif with the stats re-calc’d and embedded in the file.
gdal_hist gives a dumbass output with cumulative values and everything’s rounded to hell, maybe multiplying all the values would help but python is just rounding shit to death
r.report gives more precise output, but in awful formats. what’s with all the pipes???



- gdal_hist gives a dumbass output with cumulative values and everything’s rounded to hell, maybe multiplying all the values would help but python is just rounding shit to death

- r.report gives more precise output, but in awful formats. what’s with all the pipes???

- settings > custom CRS for new projeciton

- gdalwarp -tr 5000 5000 = target cell size 5000x5000 (meters)

- ogr2ogr is fucked because it doesnt have spatialite =/, cant use -dialect sqlite

- insanely stupid workflow for deleting those overlap-water pixels: extract all water pixels, find overlap with seto data, set all seto data to same value, convert seto data to vector, SAGA’s polygon dissolve, then clip raster by mask layer

- store everything on the external, but do the conversions on the native HDD. the write speed sucks ass. IO sucks too so you cant really stream stuff into QGIS.

- NameChanger for batch renaming

- remember in python to pick what band you want from the albedo files, you kept getting that array-dimension error because it read the whole 16 band file instead of just band 13 (urban)

- IGBP classes
1 Evergreen Needleleaf forest
2 Evergreen Broadleaf forest
3 Deciduous Needleleaf forest
4 Deciduous Broadleaf forest
5 Mixed forest 6 Closed shrublands
7 Open shrublands 8 Woody savannas
9 Savannas
10 Grasslands
11 Permanent wetlands
12 Croplands
13 Urban and built-up
14 Cropland/Natural vegetation mosaic
15 Snow and ice
16 Barren or sparsely vegetated



- 1 Evergreen Needleleaf forest

- 2 Evergreen Broadleaf forest

- 3 Deciduous Needleleaf forest

- 4 Deciduous Broadleaf forest

- 5 Mixed forest 6 Closed shrublands

- 7 Open shrublands 8 Woody savannas

- 9 Savannas

- 10 Grasslands

- 11 Permanent wetlands

- 12 Croplands

- 13 Urban and built-up

- 14 Cropland/Natural vegetation mosaic

- 15 Snow and ice

- 16 Barren or sparsely vegetated

- I have to do the following 12 times, 1 for each month:
Reclassify urban raster into categories - might have to make these more unique if I’m going to assign by old albedo?
used SAGA “reclassify grid values"


[ ]  
0 - no chance of becoming urban
1 - 1 to 25% chance
2 - 26 to 50% chance
3 - 51 to 75% chance
4 - 76-99% chance
5 - 100% chance
10 - extant cities as of 2000-2001


Let’s see what previous LC is like!
got different pixel values for each %-urban layer. every pixel in 1-25% is “1,” every pixel in 25-50% is “2,” etc. raster calc + the previous LC file, which is all IGBP categories = a whole bunch of new values in your raster.
Take this new raster, run simple stats on it (like with the LC toolbox) and there you have it: how many pixels of each probability category have a chance to become urban.
an issue here: remember how this 0.05 deg LC file doesnt match up perfectly? well, the extant cities of course dont match up to class 13 in this LC file. so this is fucked without that real LC since I need class 13 of the previous LC file to align *exactly* with the extant cities in guneralp’s data. So, again, come back to this. This will only really work if I get guneralp’s data or take all those HDFs > merge em all > resample to 0.05 deg > see if this resampling has the same extant-city LC as guneralp’s original shitty MODIS-sphere projection. if not, what the fuck!




Overlay extant urban pixels, future urban pixels, and albedo data
Urban probability pixels take on the values of what they overlap in the albedo file.
but this already sucks; gdal_calc in batch mode won’t work if the extents are different. r.mapcalculator doesnt work.
for some reason raster calculator in QGIS does it fine and doesn’t bitch about extents. but I can’t automate that. maybe it’s calling a different gdal???
use this? [http://gdal-calculations.googlecode.com/svn-history/r55/trunk/lib/gdal_calculations/gdal_calculate.py](http://gdal-calculations.googlecode.com/svn-history/r55/trunk/lib/gdal_calculations/gdal_calculate.py)
[http://gis.stackexchange.com/questions/122581/using-qgsrastercalculator](http://gis.stackexchange.com/questions/122581/using-qgsrastercalculator) or call QGIS’s raster calc with python?
**set an albedo layer’s pixels to 0 with the raster calc, then take your urban % layer + that new empty layer, there, you have a new layer with the perfect extent. THEN you can batch process gdal_calc either from QGIS or command line. the layer is called “just for setting extent”. Remember: the albedo files are monthly averages 2001-2010.**
I think I need to mass-extract band 13 from the albedo files, otherwise this is going to take fucking forever and take all the room on my hard drive
[gdal_calc.py](http://gdal_calc.py/)
A urban_100_new_extent.tif --A_band 1 -B albedo_test.tif --B_band 13 --calc="(A+B)" --outfile=out2.tiff --type=“UInt16"
^^^ this works, try to automate this somehow.


Calcs with UInt16 outputs, set nodata to 0. There are no 0 albedo spots on earth, man. check the histos. Then you can batch em again on standard devs, plus and minus. **But I need to know the prior LC** so I can assign the correct albedo; notice how the albedo files have different bands? these tests only used class 13. you gotta match those to each prior LC; so you have to find the prior LC for each of the % chance rasters, then conditionally re-assign their pixel values to the matching band in the albedo file.
Going to skip most of this part and start testing my assignments of the extant albedos to my %-chance pixels.
extant + BSA *DONE* **(A-10)+B**
extant + WSA *DONE*
extant BSA + std dev
extant WSA - std dev
100% chance + BSA *JUST TESTING THIS FOR APRIL BSA + WSA, THIS NEEDS ACTUAL ALBEDO VALUES FROM THE LC - DONE* **(A-5)+B**
100% chance + WSA *DONE*
100% chance BSA + std dev
100% chance WSA - std dev
75-99% chance + BSA **(A-4)+B**
75-99% chance + WSA
75-99% chance BSA + std dev
75-99% chance BSA - std dev
50-75% chance + BSA **(A-3)+B**
50-75% chance + WSA
50-75% chance BSA + std dev
50-75% chance BSA - std dev
25-50% chance + BSA
25-50% chance + WSA
25-50% chance BSA + std dev
25-50% chance WSA - std dev
1-25% chance + BSA
1-25% chance + WSA
1-25% chance BSA + std dev
1-25% chance WSA - std dev


That sorts out the *before* albedo; so you can say “for pixels with a 50-75% chance of becoming urban by 2030, the aggregate albedo change as they became urban was TK.”






% chance pixels take on the value of the *nearest* *pixel* in the “extant albedo” layer (can I do IDW or something too? what’s good when you know nothing except spatial auto = weak as hell?)
well I’m coming up empty on doing this purely in raster, but it works if you convert everything to points first using "grid values to points" (SAGA tool in QGIS)
vector in QGIS: [http://gis.stackexchange.com/questions/11377/how-to-join-attributes-from-nearest-point-in-qgis](http://gis.stackexchange.com/questions/11377/how-to-join-attributes-from-nearest-point-in-qgis) distance analysis with this method takes 10 mins just to calculate, then you have to join and change the ID values from strings to reals with the field calc, then back to raster? this sucks! it takes fucking forever!


raster in QGIS: no idea
raster in arcgis: old guy on SE says "I think you’ll have to convert [extant] to points anyway. Next step do euclidian allocation to these points. Con(~IsNull(“100%-chance-layer"),"allocation)). Use lookup to convert results into floats."
[ ]  
the Euclidian allocation tool seems to work, makes voronois, but takes 5 mins each, do it for both extant WSA and BSA, can script with ArcPy too [http://pro.arcgis.com/en/pro-app/tool-reference/spatial-analyst/euclidean-allocation.htm](http://pro.arcgis.com/en/pro-app/tool-reference/spatial-analyst/euclidean-allocation.htm)
Then do this in raster calc, put what you want to reassign in the middle, then the nearest-neighbor albedo fill that you just generated outside: Con(~IsNull("reassign test\100_chance_wsa_Apr.tif"),"reassign test\ws_apr.tif")
This gets you the WSA and BSA of the extant cities re-assigned to the 100%-chance pixels.


Record change in the % chance pixels as they change, can do this in QGIS






Okay, assignment happens with Euclidan allocation, now to actually calculate the forcing. Forcing has 3 terms: WSA/BSA albedo from IGBP dataset (assigned to the pixels for extant, 100%, 75%, etc), kernels from shell, then the fraction from MERRA Forcing. Delta WSA *change in kernel + delta BSA* change in kernel. Shell’s 3-deg kernels aren’t separated into white- and black-sky, but Mutlu’s MERRA reanalysis data separates white-sky and black-sky albedo. coarse but doesn’t matter, includes relative fractions of direct vs. diffuse insolation (interacting with atmo vs. no atmo impact, i.e. white-sky vs. black-sky). includes direct (BSA) map and diffuse (WSA) map, and every pixel has 12 values (1 per month, so pick #4 for april since that’s what we’re testing here). numbers range from 0-100, remember they’re fractions that need to be multiplied by...something, the kernels?
those merra things from mutlu: band 4 from diffuse + band 4 from direct = 1. remember, they’re fractions. They’re 32-bit data with stupid cell sizes. may have to resample.
Shell’s kernels: albedo_sw_monthly.nc is total-sky (I guess white sky?), 12 files one per month, but its extents are all fucked and it aint aligned. UGH
I dont know why it only works this way but: get the netcdf into QGIS by dragging > right click save as a tiff, no translate or nothin, then do the below warp on it
gdalwarp --config CENTER_LONG 0 -overwrite -t_srs "+proj=longlat +ellps=WGS84 +datum=WGS84 +no_defs" -wo SOURCE_EXTRA=1000 -of GTiff "/Users/traveler/Dropbox/school stuff/766/doing thesis/outputs/getting shell kernels out of netCDF/april_to_tiff_WSA_kernel.tif" "/Users/traveler/Dropbox/school stuff/766/doing thesis/outputs/getting shell kernels out of netCDF/april_to_tiff_recentering_2.tif” gets it into the right centering
yields 1.25deg resolution, do “file + just_to_set_extent” in raster calc to match resolution and extents to other data; now it’s resampled to match the albedo data. has nodata along top, right, bottom, but shouldnt mess with stuff too bad. *instead of the raster calc trick, I should be able to resample and set extents with gdal_translate or gdal_warp right??? oh well*
gdalinfo NETCDF:/Users/traveler/Dropbox/school\ stuff/766/doing\ thesis/data/CAM\ kernels\ from\ Shell\ 2008/albedo_sw_monthly.nc:monkernel well monkernel is the sub-dataset, but it cant directly access bands from here with another colon. dunno how to dig deeper, the documentation says to use gdal_translate but guh??


she says "The unit in the albedo file is wrong [gdalinfo for the .nc file says W/m&2/K] . It should be w/m^2/(0.01 increase in fractional albedo). That is, the kernel corresponds to an increase of 0.01 in the albedo (though it maxes out a 1).” So “watts per square meter per 0.01 increase in albedo.” area x change = total change in RF.
which makes total sense, they’re all negative values; "over *this* pixel, dropping albedo by 0.01 means a -1.whatever change in watts per square meter of RF.” I guess since the kernels describe the *change in forcing per unit change of albedo, this method doesn’t need insolation/SSRD.* But then again since it’s only changes, it doesnt make for absolutes. Zhai 2014 says for absolutes you need SSRD/insolation.
where do mutlu’s fractions come in? let’s talk through what I have, using april data and 100%-chance expansion pixels only
WSA for 100%-chance land *before* it changes
BSA for 100%-chance land *before* it changes
WSA for 100%-chance land *after* it changes in like 30 years
BSA for 100%-chance land *after* it changes in like 30 years
why the hell did I do extant albedo? I guess I need that for current forcing, but I dunno how to even calculate that since I need insolation apparently!
and what the fucking cock was I talking about with “change in kernel,” the kernel values dont change!
Okay the *expansion* *probability* pixels have changes in albedo since they went from previous LC > urban, class 13 albedo. I mean theoretically, I still haven’t generated/received the previous LC map yet. ANYWAY those have changes, and changes are good shit. **✓**
**(((Δ WSA** **x fraction WSA)** **x WSA kernel )** **+ ((Δ BSA** **x fraction BSA)** **x BSA kernel))) x total area = forcing change as all that stuff moves from previous LC to urban. I think this might be it!**
Ghimire: monthly forcing = (Δmonthly WSA x shell’s WSA kernel) + (Δmonthly BSA x shell’s BSA kernel)
he didn’t do fractions, should I?


unit shuffle:
the kernel is watts/sq meter/0.01 increase in fractional albedo. That is, the kernel corresponds to an increase of 0.01 in the albedo. So “watts per square meter per 0.01 increase in albedo.” does that even apply to decreasing albedo?
since the fractions are spatial: make a ΔWSA and a ΔBSA calc, multiply by 0.001 since that’s the albedo scale factor. i guess we’re back to 32 bit floats
then multiply THOSE by the the fraction WSA and fraction BSA
then, finally, multiply those by the kernel data to see what each Δ in albedo means for RF.
albedo goes down, yields a negative value. negative value * neg kernel value = a positive forcing effect, since low albedo means that many more watts/sq meter getting absorbed?
albedo goes up, yields a positive value. positive value * neg kernel value = negative forcing effect, since high albedo means more watts/sq meter getting reflected?


Used “raster layer statistics” in toolbox to sum them, cumbersome but works, py can definitely do this.
as in all things, the histos might be more interesting than the sums; the albedo*kernel files show whether, on balance, there’s more positive or negative forcing
well there’s a lot on either side of zero, with the vast majority not increasing or decreasing much at all. duh. not a lot of fat tails


WSA sum for april: 6.42119546358
BSA sum for april: 12.6113679784
whole lot more black sky according to the WSA/BSA fraction histos, who knew? why is that?? what the hell is black sky albedo???
that yields 19.03256344 for total change in forcing per square meter, over the entire earth’s worth of 100%-chance urban land, for April. dividing that by the number of 100%-chance-to-become-urban pixels, 24,588, yields 0.000774 bump in RF per cell. fucking tiny. but, you know, that makes sense since 1) urban land area is tiny in general 2) ghimire says it took 305 years of anthro LC change to get a watts/m^2 drop of -0.16. so this is a drop in a bucket of a drop in a bucket. hahaha this result SUCKS but hey, you knew it’d be small stuff


After that you have to calculate how much area you have covered by those pixels. they’re in geographic coordinates; converting to something with meters necessarily changes the number of cells; that’s not good. I guess it wont really matter if you reproject it the same way each time? So going to do it with world sinusoidal, seems simple enough "+proj=sinu +lon_0=0 +x_0=0 +y_0=0 +datum=WGS84 +units=m +no_defs"
so that has 20,721 pixels, each pixel 5,564.11m on a side, or 30,959,320.0921 square meters. that’s 641,508,071,628.404 square meters total in the 100%-chance-of-becoming-urban class, or 641,508 sq km, or 247,687 square miles. that’s reasonable compared to the 1.2m square kilometers of TOTAL “any chance at all” land reported by Seto 2012.



















1. Reclassify urban raster into categories - might have to make these more unique if I’m going to assign by old albedo?
used SAGA “reclassify grid values"



1. used SAGA “reclassify grid values"

1. [ ]  
0 - no chance of becoming urban
1 - 1 to 25% chance
2 - 26 to 50% chance
3 - 51 to 75% chance
4 - 76-99% chance
5 - 100% chance
10 - extant cities as of 2000-2001



- 0 - no chance of becoming urban

- 1 - 1 to 25% chance

- 2 - 26 to 50% chance

- 3 - 51 to 75% chance

- 4 - 76-99% chance

- 5 - 100% chance

- 10 - extant cities as of 2000-2001

1. Let’s see what previous LC is like!
got different pixel values for each %-urban layer. every pixel in 1-25% is “1,” every pixel in 25-50% is “2,” etc. raster calc + the previous LC file, which is all IGBP categories = a whole bunch of new values in your raster.
Take this new raster, run simple stats on it (like with the LC toolbox) and there you have it: how many pixels of each probability category have a chance to become urban.
an issue here: remember how this 0.05 deg LC file doesnt match up perfectly? well, the extant cities of course dont match up to class 13 in this LC file. so this is fucked without that real LC since I need class 13 of the previous LC file to align *exactly* with the extant cities in guneralp’s data. So, again, come back to this. This will only really work if I get guneralp’s data or take all those HDFs > merge em all > resample to 0.05 deg > see if this resampling has the same extant-city LC as guneralp’s original shitty MODIS-sphere projection. if not, what the fuck!





- got different pixel values for each %-urban layer. every pixel in 1-25% is “1,” every pixel in 25-50% is “2,” etc. raster calc + the previous LC file, which is all IGBP categories = a whole bunch of new values in your raster.

- Take this new raster, run simple stats on it (like with the LC toolbox) and there you have it: how many pixels of each probability category have a chance to become urban.
an issue here: remember how this 0.05 deg LC file doesnt match up perfectly? well, the extant cities of course dont match up to class 13 in this LC file. so this is fucked without that real LC since I need class 13 of the previous LC file to align *exactly* with the extant cities in guneralp’s data. So, again, come back to this. This will only really work if I get guneralp’s data or take all those HDFs > merge em all > resample to 0.05 deg > see if this resampling has the same extant-city LC as guneralp’s original shitty MODIS-sphere projection. if not, what the fuck!



- an issue here: remember how this 0.05 deg LC file doesnt match up perfectly? well, the extant cities of course dont match up to class 13 in this LC file. so this is fucked without that real LC since I need class 13 of the previous LC file to align *exactly* with the extant cities in guneralp’s data. So, again, come back to this. This will only really work if I get guneralp’s data or take all those HDFs > merge em all > resample to 0.05 deg > see if this resampling has the same extant-city LC as guneralp’s original shitty MODIS-sphere projection. if not, what the fuck!

1. Overlay extant urban pixels, future urban pixels, and albedo data

1. Urban probability pixels take on the values of what they overlap in the albedo file.
but this already sucks; gdal_calc in batch mode won’t work if the extents are different. r.mapcalculator doesnt work.
for some reason raster calculator in QGIS does it fine and doesn’t bitch about extents. but I can’t automate that. maybe it’s calling a different gdal???
use this? [http://gdal-calculations.googlecode.com/svn-history/r55/trunk/lib/gdal_calculations/gdal_calculate.py](http://gdal-calculations.googlecode.com/svn-history/r55/trunk/lib/gdal_calculations/gdal_calculate.py)
[http://gis.stackexchange.com/questions/122581/using-qgsrastercalculator](http://gis.stackexchange.com/questions/122581/using-qgsrastercalculator) or call QGIS’s raster calc with python?
**set an albedo layer’s pixels to 0 with the raster calc, then take your urban % layer + that new empty layer, there, you have a new layer with the perfect extent. THEN you can batch process gdal_calc either from QGIS or command line. the layer is called “just for setting extent”. Remember: the albedo files are monthly averages 2001-2010.**
I think I need to mass-extract band 13 from the albedo files, otherwise this is going to take fucking forever and take all the room on my hard drive
[gdal_calc.py](http://gdal_calc.py/)
A urban_100_new_extent.tif --A_band 1 -B albedo_test.tif --B_band 13 --calc="(A+B)" --outfile=out2.tiff --type=“UInt16"
^^^ this works, try to automate this somehow.


Calcs with UInt16 outputs, set nodata to 0. There are no 0 albedo spots on earth, man. check the histos. Then you can batch em again on standard devs, plus and minus. **But I need to know the prior LC** so I can assign the correct albedo; notice how the albedo files have different bands? these tests only used class 13. you gotta match those to each prior LC; so you have to find the prior LC for each of the % chance rasters, then conditionally re-assign their pixel values to the matching band in the albedo file.
Going to skip most of this part and start testing my assignments of the extant albedos to my %-chance pixels.
extant + BSA *DONE* **(A-10)+B**
extant + WSA *DONE*
extant BSA + std dev
extant WSA - std dev
100% chance + BSA *JUST TESTING THIS FOR APRIL BSA + WSA, THIS NEEDS ACTUAL ALBEDO VALUES FROM THE LC - DONE* **(A-5)+B**
100% chance + WSA *DONE*
100% chance BSA + std dev
100% chance WSA - std dev
75-99% chance + BSA **(A-4)+B**
75-99% chance + WSA
75-99% chance BSA + std dev
75-99% chance BSA - std dev
50-75% chance + BSA **(A-3)+B**
50-75% chance + WSA
50-75% chance BSA + std dev
50-75% chance BSA - std dev
25-50% chance + BSA
25-50% chance + WSA
25-50% chance BSA + std dev
25-50% chance WSA - std dev
1-25% chance + BSA
1-25% chance + WSA
1-25% chance BSA + std dev
1-25% chance WSA - std dev


That sorts out the *before* albedo; so you can say “for pixels with a 50-75% chance of becoming urban by 2030, the aggregate albedo change as they became urban was TK.”







- but this already sucks; gdal_calc in batch mode won’t work if the extents are different. r.mapcalculator doesnt work.
for some reason raster calculator in QGIS does it fine and doesn’t bitch about extents. but I can’t automate that. maybe it’s calling a different gdal???
use this? [http://gdal-calculations.googlecode.com/svn-history/r55/trunk/lib/gdal_calculations/gdal_calculate.py](http://gdal-calculations.googlecode.com/svn-history/r55/trunk/lib/gdal_calculations/gdal_calculate.py)
[http://gis.stackexchange.com/questions/122581/using-qgsrastercalculator](http://gis.stackexchange.com/questions/122581/using-qgsrastercalculator) or call QGIS’s raster calc with python?
**set an albedo layer’s pixels to 0 with the raster calc, then take your urban % layer + that new empty layer, there, you have a new layer with the perfect extent. THEN you can batch process gdal_calc either from QGIS or command line. the layer is called “just for setting extent”. Remember: the albedo files are monthly averages 2001-2010.**
I think I need to mass-extract band 13 from the albedo files, otherwise this is going to take fucking forever and take all the room on my hard drive
[gdal_calc.py](http://gdal_calc.py/)
A urban_100_new_extent.tif --A_band 1 -B albedo_test.tif --B_band 13 --calc="(A+B)" --outfile=out2.tiff --type=“UInt16"
^^^ this works, try to automate this somehow.


Calcs with UInt16 outputs, set nodata to 0. There are no 0 albedo spots on earth, man. check the histos. Then you can batch em again on standard devs, plus and minus. **But I need to know the prior LC** so I can assign the correct albedo; notice how the albedo files have different bands? these tests only used class 13. you gotta match those to each prior LC; so you have to find the prior LC for each of the % chance rasters, then conditionally re-assign their pixel values to the matching band in the albedo file.
Going to skip most of this part and start testing my assignments of the extant albedos to my %-chance pixels.
extant + BSA *DONE* **(A-10)+B**
extant + WSA *DONE*
extant BSA + std dev
extant WSA - std dev
100% chance + BSA *JUST TESTING THIS FOR APRIL BSA + WSA, THIS NEEDS ACTUAL ALBEDO VALUES FROM THE LC - DONE* **(A-5)+B**
100% chance + WSA *DONE*
100% chance BSA + std dev
100% chance WSA - std dev
75-99% chance + BSA **(A-4)+B**
75-99% chance + WSA
75-99% chance BSA + std dev
75-99% chance BSA - std dev
50-75% chance + BSA **(A-3)+B**
50-75% chance + WSA
50-75% chance BSA + std dev
50-75% chance BSA - std dev
25-50% chance + BSA
25-50% chance + WSA
25-50% chance BSA + std dev
25-50% chance WSA - std dev
1-25% chance + BSA
1-25% chance + WSA
1-25% chance BSA + std dev
1-25% chance WSA - std dev


That sorts out the *before* albedo; so you can say “for pixels with a 50-75% chance of becoming urban by 2030, the aggregate albedo change as they became urban was TK.”





- for some reason raster calculator in QGIS does it fine and doesn’t bitch about extents. but I can’t automate that. maybe it’s calling a different gdal???
use this? [http://gdal-calculations.googlecode.com/svn-history/r55/trunk/lib/gdal_calculations/gdal_calculate.py](http://gdal-calculations.googlecode.com/svn-history/r55/trunk/lib/gdal_calculations/gdal_calculate.py)
[http://gis.stackexchange.com/questions/122581/using-qgsrastercalculator](http://gis.stackexchange.com/questions/122581/using-qgsrastercalculator) or call QGIS’s raster calc with python?
**set an albedo layer’s pixels to 0 with the raster calc, then take your urban % layer + that new empty layer, there, you have a new layer with the perfect extent. THEN you can batch process gdal_calc either from QGIS or command line. the layer is called “just for setting extent”. Remember: the albedo files are monthly averages 2001-2010.**
I think I need to mass-extract band 13 from the albedo files, otherwise this is going to take fucking forever and take all the room on my hard drive
[gdal_calc.py](http://gdal_calc.py/)
A urban_100_new_extent.tif --A_band 1 -B albedo_test.tif --B_band 13 --calc="(A+B)" --outfile=out2.tiff --type=“UInt16"
^^^ this works, try to automate this somehow.


Calcs with UInt16 outputs, set nodata to 0. There are no 0 albedo spots on earth, man. check the histos. Then you can batch em again on standard devs, plus and minus. **But I need to know the prior LC** so I can assign the correct albedo; notice how the albedo files have different bands? these tests only used class 13. you gotta match those to each prior LC; so you have to find the prior LC for each of the % chance rasters, then conditionally re-assign their pixel values to the matching band in the albedo file.
Going to skip most of this part and start testing my assignments of the extant albedos to my %-chance pixels.
extant + BSA *DONE* **(A-10)+B**
extant + WSA *DONE*
extant BSA + std dev
extant WSA - std dev
100% chance + BSA *JUST TESTING THIS FOR APRIL BSA + WSA, THIS NEEDS ACTUAL ALBEDO VALUES FROM THE LC - DONE* **(A-5)+B**
100% chance + WSA *DONE*
100% chance BSA + std dev
100% chance WSA - std dev
75-99% chance + BSA **(A-4)+B**
75-99% chance + WSA
75-99% chance BSA + std dev
75-99% chance BSA - std dev
50-75% chance + BSA **(A-3)+B**
50-75% chance + WSA
50-75% chance BSA + std dev
50-75% chance BSA - std dev
25-50% chance + BSA
25-50% chance + WSA
25-50% chance BSA + std dev
25-50% chance WSA - std dev
1-25% chance + BSA
1-25% chance + WSA
1-25% chance BSA + std dev
1-25% chance WSA - std dev


That sorts out the *before* albedo; so you can say “for pixels with a 50-75% chance of becoming urban by 2030, the aggregate albedo change as they became urban was TK.”



- use this? [http://gdal-calculations.googlecode.com/svn-history/r55/trunk/lib/gdal_calculations/gdal_calculate.py](http://gdal-calculations.googlecode.com/svn-history/r55/trunk/lib/gdal_calculations/gdal_calculate.py)

- [http://gis.stackexchange.com/questions/122581/using-qgsrastercalculator](http://gis.stackexchange.com/questions/122581/using-qgsrastercalculator) or call QGIS’s raster calc with python?

- **set an albedo layer’s pixels to 0 with the raster calc, then take your urban % layer + that new empty layer, there, you have a new layer with the perfect extent. THEN you can batch process gdal_calc either from QGIS or command line. the layer is called “just for setting extent”. Remember: the albedo files are monthly averages 2001-2010.**

- I think I need to mass-extract band 13 from the albedo files, otherwise this is going to take fucking forever and take all the room on my hard drive

- [gdal_calc.py](http://gdal_calc.py/)
A urban_100_new_extent.tif --A_band 1 -B albedo_test.tif --B_band 13 --calc="(A+B)" --outfile=out2.tiff --type=“UInt16"
^^^ this works, try to automate this somehow.



- A urban_100_new_extent.tif --A_band 1 -B albedo_test.tif --B_band 13 --calc="(A+B)" --outfile=out2.tiff --type=“UInt16"

- ^^^ this works, try to automate this somehow.

- Calcs with UInt16 outputs, set nodata to 0. There are no 0 albedo spots on earth, man. check the histos. Then you can batch em again on standard devs, plus and minus. **But I need to know the prior LC** so I can assign the correct albedo; notice how the albedo files have different bands? these tests only used class 13. you gotta match those to each prior LC; so you have to find the prior LC for each of the % chance rasters, then conditionally re-assign their pixel values to the matching band in the albedo file.

- Going to skip most of this part and start testing my assignments of the extant albedos to my %-chance pixels.
extant + BSA *DONE* **(A-10)+B**
extant + WSA *DONE*
extant BSA + std dev
extant WSA - std dev
100% chance + BSA *JUST TESTING THIS FOR APRIL BSA + WSA, THIS NEEDS ACTUAL ALBEDO VALUES FROM THE LC - DONE* **(A-5)+B**
100% chance + WSA *DONE*
100% chance BSA + std dev
100% chance WSA - std dev
75-99% chance + BSA **(A-4)+B**
75-99% chance + WSA
75-99% chance BSA + std dev
75-99% chance BSA - std dev
50-75% chance + BSA **(A-3)+B**
50-75% chance + WSA
50-75% chance BSA + std dev
50-75% chance BSA - std dev
25-50% chance + BSA
25-50% chance + WSA
25-50% chance BSA + std dev
25-50% chance WSA - std dev
1-25% chance + BSA
1-25% chance + WSA
1-25% chance BSA + std dev
1-25% chance WSA - std dev



- extant + BSA *DONE* **(A-10)+B**

- extant + WSA *DONE*

- extant BSA + std dev

- extant WSA - std dev

- 100% chance + BSA *JUST TESTING THIS FOR APRIL BSA + WSA, THIS NEEDS ACTUAL ALBEDO VALUES FROM THE LC - DONE* **(A-5)+B**

- 100% chance + WSA *DONE*

- 100% chance BSA + std dev

- 100% chance WSA - std dev

- 75-99% chance + BSA **(A-4)+B**

- 75-99% chance + WSA

- 75-99% chance BSA + std dev

- 75-99% chance BSA - std dev

- 50-75% chance + BSA **(A-3)+B**

- 50-75% chance + WSA

- 50-75% chance BSA + std dev

- 50-75% chance BSA - std dev

- 25-50% chance + BSA

- 25-50% chance + WSA

- 25-50% chance BSA + std dev

- 25-50% chance WSA - std dev

- 1-25% chance + BSA

- 1-25% chance + WSA

- 1-25% chance BSA + std dev

- 1-25% chance WSA - std dev

- That sorts out the *before* albedo; so you can say “for pixels with a 50-75% chance of becoming urban by 2030, the aggregate albedo change as they became urban was TK.”

1. % chance pixels take on the value of the *nearest* *pixel* in the “extant albedo” layer (can I do IDW or something too? what’s good when you know nothing except spatial auto = weak as hell?)
well I’m coming up empty on doing this purely in raster, but it works if you convert everything to points first using "grid values to points" (SAGA tool in QGIS)
vector in QGIS: [http://gis.stackexchange.com/questions/11377/how-to-join-attributes-from-nearest-point-in-qgis](http://gis.stackexchange.com/questions/11377/how-to-join-attributes-from-nearest-point-in-qgis) distance analysis with this method takes 10 mins just to calculate, then you have to join and change the ID values from strings to reals with the field calc, then back to raster? this sucks! it takes fucking forever!


raster in QGIS: no idea
raster in arcgis: old guy on SE says "I think you’ll have to convert [extant] to points anyway. Next step do euclidian allocation to these points. Con(~IsNull(“100%-chance-layer"),"allocation)). Use lookup to convert results into floats."
[ ]  
the Euclidian allocation tool seems to work, makes voronois, but takes 5 mins each, do it for both extant WSA and BSA, can script with ArcPy too [http://pro.arcgis.com/en/pro-app/tool-reference/spatial-analyst/euclidean-allocation.htm](http://pro.arcgis.com/en/pro-app/tool-reference/spatial-analyst/euclidean-allocation.htm)
Then do this in raster calc, put what you want to reassign in the middle, then the nearest-neighbor albedo fill that you just generated outside: Con(~IsNull("reassign test\100_chance_wsa_Apr.tif"),"reassign test\ws_apr.tif")
This gets you the WSA and BSA of the extant cities re-assigned to the 100%-chance pixels.


Record change in the % chance pixels as they change, can do this in QGIS







- well I’m coming up empty on doing this purely in raster, but it works if you convert everything to points first using "grid values to points" (SAGA tool in QGIS)
vector in QGIS: [http://gis.stackexchange.com/questions/11377/how-to-join-attributes-from-nearest-point-in-qgis](http://gis.stackexchange.com/questions/11377/how-to-join-attributes-from-nearest-point-in-qgis) distance analysis with this method takes 10 mins just to calculate, then you have to join and change the ID values from strings to reals with the field calc, then back to raster? this sucks! it takes fucking forever!



- vector in QGIS: [http://gis.stackexchange.com/questions/11377/how-to-join-attributes-from-nearest-point-in-qgis](http://gis.stackexchange.com/questions/11377/how-to-join-attributes-from-nearest-point-in-qgis) distance analysis with this method takes 10 mins just to calculate, then you have to join and change the ID values from strings to reals with the field calc, then back to raster? this sucks! it takes fucking forever!

- raster in QGIS: no idea

- raster in arcgis: old guy on SE says "I think you’ll have to convert [extant] to points anyway. Next step do euclidian allocation to these points. Con(~IsNull(“100%-chance-layer"),"allocation)). Use lookup to convert results into floats."
[ ]  
the Euclidian allocation tool seems to work, makes voronois, but takes 5 mins each, do it for both extant WSA and BSA, can script with ArcPy too [http://pro.arcgis.com/en/pro-app/tool-reference/spatial-analyst/euclidean-allocation.htm](http://pro.arcgis.com/en/pro-app/tool-reference/spatial-analyst/euclidean-allocation.htm)
Then do this in raster calc, put what you want to reassign in the middle, then the nearest-neighbor albedo fill that you just generated outside: Con(~IsNull("reassign test\100_chance_wsa_Apr.tif"),"reassign test\ws_apr.tif")
This gets you the WSA and BSA of the extant cities re-assigned to the 100%-chance pixels.


Record change in the % chance pixels as they change, can do this in QGIS





- [ ]  
the Euclidian allocation tool seems to work, makes voronois, but takes 5 mins each, do it for both extant WSA and BSA, can script with ArcPy too [http://pro.arcgis.com/en/pro-app/tool-reference/spatial-analyst/euclidean-allocation.htm](http://pro.arcgis.com/en/pro-app/tool-reference/spatial-analyst/euclidean-allocation.htm)
Then do this in raster calc, put what you want to reassign in the middle, then the nearest-neighbor albedo fill that you just generated outside: Con(~IsNull("reassign test\100_chance_wsa_Apr.tif"),"reassign test\ws_apr.tif")
This gets you the WSA and BSA of the extant cities re-assigned to the 100%-chance pixels.


Record change in the % chance pixels as they change, can do this in QGIS



- the Euclidian allocation tool seems to work, makes voronois, but takes 5 mins each, do it for both extant WSA and BSA, can script with ArcPy too [http://pro.arcgis.com/en/pro-app/tool-reference/spatial-analyst/euclidean-allocation.htm](http://pro.arcgis.com/en/pro-app/tool-reference/spatial-analyst/euclidean-allocation.htm)

- Then do this in raster calc, put what you want to reassign in the middle, then the nearest-neighbor albedo fill that you just generated outside: Con(~IsNull("reassign test\100_chance_wsa_Apr.tif"),"reassign test\ws_apr.tif")
This gets you the WSA and BSA of the extant cities re-assigned to the 100%-chance pixels.



- This gets you the WSA and BSA of the extant cities re-assigned to the 100%-chance pixels.

- Record change in the % chance pixels as they change, can do this in QGIS

1. Okay, assignment happens with Euclidan allocation, now to actually calculate the forcing. Forcing has 3 terms: WSA/BSA albedo from IGBP dataset (assigned to the pixels for extant, 100%, 75%, etc), kernels from shell, then the fraction from MERRA Forcing. Delta WSA *change in kernel + delta BSA* change in kernel. Shell’s 3-deg kernels aren’t separated into white- and black-sky, but Mutlu’s MERRA reanalysis data separates white-sky and black-sky albedo. coarse but doesn’t matter, includes relative fractions of direct vs. diffuse insolation (interacting with atmo vs. no atmo impact, i.e. white-sky vs. black-sky). includes direct (BSA) map and diffuse (WSA) map, and every pixel has 12 values (1 per month, so pick #4 for april since that’s what we’re testing here). numbers range from 0-100, remember they’re fractions that need to be multiplied by...something, the kernels?
those merra things from mutlu: band 4 from diffuse + band 4 from direct = 1. remember, they’re fractions. They’re 32-bit data with stupid cell sizes. may have to resample.
Shell’s kernels: albedo_sw_monthly.nc is total-sky (I guess white sky?), 12 files one per month, but its extents are all fucked and it aint aligned. UGH
I dont know why it only works this way but: get the netcdf into QGIS by dragging > right click save as a tiff, no translate or nothin, then do the below warp on it
gdalwarp --config CENTER_LONG 0 -overwrite -t_srs "+proj=longlat +ellps=WGS84 +datum=WGS84 +no_defs" -wo SOURCE_EXTRA=1000 -of GTiff "/Users/traveler/Dropbox/school stuff/766/doing thesis/outputs/getting shell kernels out of netCDF/april_to_tiff_WSA_kernel.tif" "/Users/traveler/Dropbox/school stuff/766/doing thesis/outputs/getting shell kernels out of netCDF/april_to_tiff_recentering_2.tif” gets it into the right centering
yields 1.25deg resolution, do “file + just_to_set_extent” in raster calc to match resolution and extents to other data; now it’s resampled to match the albedo data. has nodata along top, right, bottom, but shouldnt mess with stuff too bad. *instead of the raster calc trick, I should be able to resample and set extents with gdal_translate or gdal_warp right??? oh well*
gdalinfo NETCDF:/Users/traveler/Dropbox/school\ stuff/766/doing\ thesis/data/CAM\ kernels\ from\ Shell\ 2008/albedo_sw_monthly.nc:monkernel well monkernel is the sub-dataset, but it cant directly access bands from here with another colon. dunno how to dig deeper, the documentation says to use gdal_translate but guh??


she says "The unit in the albedo file is wrong [gdalinfo for the .nc file says W/m&2/K] . It should be w/m^2/(0.01 increase in fractional albedo). That is, the kernel corresponds to an increase of 0.01 in the albedo (though it maxes out a 1).” So “watts per square meter per 0.01 increase in albedo.” area x change = total change in RF.
which makes total sense, they’re all negative values; "over *this* pixel, dropping albedo by 0.01 means a -1.whatever change in watts per square meter of RF.” I guess since the kernels describe the *change in forcing per unit change of albedo, this method doesn’t need insolation/SSRD.* But then again since it’s only changes, it doesnt make for absolutes. Zhai 2014 says for absolutes you need SSRD/insolation.
where do mutlu’s fractions come in? let’s talk through what I have, using april data and 100%-chance expansion pixels only
WSA for 100%-chance land *before* it changes
BSA for 100%-chance land *before* it changes
WSA for 100%-chance land *after* it changes in like 30 years
BSA for 100%-chance land *after* it changes in like 30 years
why the hell did I do extant albedo? I guess I need that for current forcing, but I dunno how to even calculate that since I need insolation apparently!
and what the fucking cock was I talking about with “change in kernel,” the kernel values dont change!
Okay the *expansion* *probability* pixels have changes in albedo since they went from previous LC > urban, class 13 albedo. I mean theoretically, I still haven’t generated/received the previous LC map yet. ANYWAY those have changes, and changes are good shit. **✓**
**(((Δ WSA** **x fraction WSA)** **x WSA kernel )** **+ ((Δ BSA** **x fraction BSA)** **x BSA kernel))) x total area = forcing change as all that stuff moves from previous LC to urban. I think this might be it!**
Ghimire: monthly forcing = (Δmonthly WSA x shell’s WSA kernel) + (Δmonthly BSA x shell’s BSA kernel)
he didn’t do fractions, should I?


unit shuffle:
the kernel is watts/sq meter/0.01 increase in fractional albedo. That is, the kernel corresponds to an increase of 0.01 in the albedo. So “watts per square meter per 0.01 increase in albedo.” does that even apply to decreasing albedo?
since the fractions are spatial: make a ΔWSA and a ΔBSA calc, multiply by 0.001 since that’s the albedo scale factor. i guess we’re back to 32 bit floats
then multiply THOSE by the the fraction WSA and fraction BSA
then, finally, multiply those by the kernel data to see what each Δ in albedo means for RF.
albedo goes down, yields a negative value. negative value * neg kernel value = a positive forcing effect, since low albedo means that many more watts/sq meter getting absorbed?
albedo goes up, yields a positive value. positive value * neg kernel value = negative forcing effect, since high albedo means more watts/sq meter getting reflected?


Used “raster layer statistics” in toolbox to sum them, cumbersome but works, py can definitely do this.
as in all things, the histos might be more interesting than the sums; the albedo*kernel files show whether, on balance, there’s more positive or negative forcing
well there’s a lot on either side of zero, with the vast majority not increasing or decreasing much at all. duh. not a lot of fat tails


WSA sum for april: 6.42119546358
BSA sum for april: 12.6113679784
whole lot more black sky according to the WSA/BSA fraction histos, who knew? why is that?? what the hell is black sky albedo???
that yields 19.03256344 for total change in forcing per square meter, over the entire earth’s worth of 100%-chance urban land, for April. dividing that by the number of 100%-chance-to-become-urban pixels, 24,588, yields 0.000774 bump in RF per cell. fucking tiny. but, you know, that makes sense since 1) urban land area is tiny in general 2) ghimire says it took 305 years of anthro LC change to get a watts/m^2 drop of -0.16. so this is a drop in a bucket of a drop in a bucket. hahaha this result SUCKS but hey, you knew it’d be small stuff


After that you have to calculate how much area you have covered by those pixels. they’re in geographic coordinates; converting to something with meters necessarily changes the number of cells; that’s not good. I guess it wont really matter if you reproject it the same way each time? So going to do it with world sinusoidal, seems simple enough "+proj=sinu +lon_0=0 +x_0=0 +y_0=0 +datum=WGS84 +units=m +no_defs"
so that has 20,721 pixels, each pixel 5,564.11m on a side, or 30,959,320.0921 square meters. that’s 641,508,071,628.404 square meters total in the 100%-chance-of-becoming-urban class, or 641,508 sq km, or 247,687 square miles. that’s reasonable compared to the 1.2m square kilometers of TOTAL “any chance at all” land reported by Seto 2012.

















- those merra things from mutlu: band 4 from diffuse + band 4 from direct = 1. remember, they’re fractions. They’re 32-bit data with stupid cell sizes. may have to resample.

- Shell’s kernels: albedo_sw_monthly.nc is total-sky (I guess white sky?), 12 files one per month, but its extents are all fucked and it aint aligned. UGH
I dont know why it only works this way but: get the netcdf into QGIS by dragging > right click save as a tiff, no translate or nothin, then do the below warp on it
gdalwarp --config CENTER_LONG 0 -overwrite -t_srs "+proj=longlat +ellps=WGS84 +datum=WGS84 +no_defs" -wo SOURCE_EXTRA=1000 -of GTiff "/Users/traveler/Dropbox/school stuff/766/doing thesis/outputs/getting shell kernels out of netCDF/april_to_tiff_WSA_kernel.tif" "/Users/traveler/Dropbox/school stuff/766/doing thesis/outputs/getting shell kernels out of netCDF/april_to_tiff_recentering_2.tif” gets it into the right centering
yields 1.25deg resolution, do “file + just_to_set_extent” in raster calc to match resolution and extents to other data; now it’s resampled to match the albedo data. has nodata along top, right, bottom, but shouldnt mess with stuff too bad. *instead of the raster calc trick, I should be able to resample and set extents with gdal_translate or gdal_warp right??? oh well*
gdalinfo NETCDF:/Users/traveler/Dropbox/school\ stuff/766/doing\ thesis/data/CAM\ kernels\ from\ Shell\ 2008/albedo_sw_monthly.nc:monkernel well monkernel is the sub-dataset, but it cant directly access bands from here with another colon. dunno how to dig deeper, the documentation says to use gdal_translate but guh??


she says "The unit in the albedo file is wrong [gdalinfo for the .nc file says W/m&2/K] . It should be w/m^2/(0.01 increase in fractional albedo). That is, the kernel corresponds to an increase of 0.01 in the albedo (though it maxes out a 1).” So “watts per square meter per 0.01 increase in albedo.” area x change = total change in RF.
which makes total sense, they’re all negative values; "over *this* pixel, dropping albedo by 0.01 means a -1.whatever change in watts per square meter of RF.” I guess since the kernels describe the *change in forcing per unit change of albedo, this method doesn’t need insolation/SSRD.* But then again since it’s only changes, it doesnt make for absolutes. Zhai 2014 says for absolutes you need SSRD/insolation.
where do mutlu’s fractions come in? let’s talk through what I have, using april data and 100%-chance expansion pixels only
WSA for 100%-chance land *before* it changes
BSA for 100%-chance land *before* it changes
WSA for 100%-chance land *after* it changes in like 30 years
BSA for 100%-chance land *after* it changes in like 30 years
why the hell did I do extant albedo? I guess I need that for current forcing, but I dunno how to even calculate that since I need insolation apparently!
and what the fucking cock was I talking about with “change in kernel,” the kernel values dont change!
Okay the *expansion* *probability* pixels have changes in albedo since they went from previous LC > urban, class 13 albedo. I mean theoretically, I still haven’t generated/received the previous LC map yet. ANYWAY those have changes, and changes are good shit. **✓**
**(((Δ WSA** **x fraction WSA)** **x WSA kernel )** **+ ((Δ BSA** **x fraction BSA)** **x BSA kernel))) x total area = forcing change as all that stuff moves from previous LC to urban. I think this might be it!**
Ghimire: monthly forcing = (Δmonthly WSA x shell’s WSA kernel) + (Δmonthly BSA x shell’s BSA kernel)
he didn’t do fractions, should I?


unit shuffle:
the kernel is watts/sq meter/0.01 increase in fractional albedo. That is, the kernel corresponds to an increase of 0.01 in the albedo. So “watts per square meter per 0.01 increase in albedo.” does that even apply to decreasing albedo?
since the fractions are spatial: make a ΔWSA and a ΔBSA calc, multiply by 0.001 since that’s the albedo scale factor. i guess we’re back to 32 bit floats
then multiply THOSE by the the fraction WSA and fraction BSA
then, finally, multiply those by the kernel data to see what each Δ in albedo means for RF.
albedo goes down, yields a negative value. negative value * neg kernel value = a positive forcing effect, since low albedo means that many more watts/sq meter getting absorbed?
albedo goes up, yields a positive value. positive value * neg kernel value = negative forcing effect, since high albedo means more watts/sq meter getting reflected?


Used “raster layer statistics” in toolbox to sum them, cumbersome but works, py can definitely do this.
as in all things, the histos might be more interesting than the sums; the albedo*kernel files show whether, on balance, there’s more positive or negative forcing
well there’s a lot on either side of zero, with the vast majority not increasing or decreasing much at all. duh. not a lot of fat tails


WSA sum for april: 6.42119546358
BSA sum for april: 12.6113679784
whole lot more black sky according to the WSA/BSA fraction histos, who knew? why is that?? what the hell is black sky albedo???
that yields 19.03256344 for total change in forcing per square meter, over the entire earth’s worth of 100%-chance urban land, for April. dividing that by the number of 100%-chance-to-become-urban pixels, 24,588, yields 0.000774 bump in RF per cell. fucking tiny. but, you know, that makes sense since 1) urban land area is tiny in general 2) ghimire says it took 305 years of anthro LC change to get a watts/m^2 drop of -0.16. so this is a drop in a bucket of a drop in a bucket. hahaha this result SUCKS but hey, you knew it’d be small stuff


After that you have to calculate how much area you have covered by those pixels. they’re in geographic coordinates; converting to something with meters necessarily changes the number of cells; that’s not good. I guess it wont really matter if you reproject it the same way each time? So going to do it with world sinusoidal, seems simple enough "+proj=sinu +lon_0=0 +x_0=0 +y_0=0 +datum=WGS84 +units=m +no_defs"
so that has 20,721 pixels, each pixel 5,564.11m on a side, or 30,959,320.0921 square meters. that’s 641,508,071,628.404 square meters total in the 100%-chance-of-becoming-urban class, or 641,508 sq km, or 247,687 square miles. that’s reasonable compared to the 1.2m square kilometers of TOTAL “any chance at all” land reported by Seto 2012.















- I dont know why it only works this way but: get the netcdf into QGIS by dragging > right click save as a tiff, no translate or nothin, then do the below warp on it

- gdalwarp --config CENTER_LONG 0 -overwrite -t_srs "+proj=longlat +ellps=WGS84 +datum=WGS84 +no_defs" -wo SOURCE_EXTRA=1000 -of GTiff "/Users/traveler/Dropbox/school stuff/766/doing thesis/outputs/getting shell kernels out of netCDF/april_to_tiff_WSA_kernel.tif" "/Users/traveler/Dropbox/school stuff/766/doing thesis/outputs/getting shell kernels out of netCDF/april_to_tiff_recentering_2.tif” gets it into the right centering

- yields 1.25deg resolution, do “file + just_to_set_extent” in raster calc to match resolution and extents to other data; now it’s resampled to match the albedo data. has nodata along top, right, bottom, but shouldnt mess with stuff too bad. *instead of the raster calc trick, I should be able to resample and set extents with gdal_translate or gdal_warp right??? oh well*
gdalinfo NETCDF:/Users/traveler/Dropbox/school\ stuff/766/doing\ thesis/data/CAM\ kernels\ from\ Shell\ 2008/albedo_sw_monthly.nc:monkernel well monkernel is the sub-dataset, but it cant directly access bands from here with another colon. dunno how to dig deeper, the documentation says to use gdal_translate but guh??



- gdalinfo NETCDF:/Users/traveler/Dropbox/school\ stuff/766/doing\ thesis/data/CAM\ kernels\ from\ Shell\ 2008/albedo_sw_monthly.nc:monkernel well monkernel is the sub-dataset, but it cant directly access bands from here with another colon. dunno how to dig deeper, the documentation says to use gdal_translate but guh??

- she says "The unit in the albedo file is wrong [gdalinfo for the .nc file says W/m&2/K] . It should be w/m^2/(0.01 increase in fractional albedo). That is, the kernel corresponds to an increase of 0.01 in the albedo (though it maxes out a 1).” So “watts per square meter per 0.01 increase in albedo.” area x change = total change in RF.
which makes total sense, they’re all negative values; "over *this* pixel, dropping albedo by 0.01 means a -1.whatever change in watts per square meter of RF.” I guess since the kernels describe the *change in forcing per unit change of albedo, this method doesn’t need insolation/SSRD.* But then again since it’s only changes, it doesnt make for absolutes. Zhai 2014 says for absolutes you need SSRD/insolation.
where do mutlu’s fractions come in? let’s talk through what I have, using april data and 100%-chance expansion pixels only
WSA for 100%-chance land *before* it changes
BSA for 100%-chance land *before* it changes
WSA for 100%-chance land *after* it changes in like 30 years
BSA for 100%-chance land *after* it changes in like 30 years
why the hell did I do extant albedo? I guess I need that for current forcing, but I dunno how to even calculate that since I need insolation apparently!
and what the fucking cock was I talking about with “change in kernel,” the kernel values dont change!
Okay the *expansion* *probability* pixels have changes in albedo since they went from previous LC > urban, class 13 albedo. I mean theoretically, I still haven’t generated/received the previous LC map yet. ANYWAY those have changes, and changes are good shit. **✓**
**(((Δ WSA** **x fraction WSA)** **x WSA kernel )** **+ ((Δ BSA** **x fraction BSA)** **x BSA kernel))) x total area = forcing change as all that stuff moves from previous LC to urban. I think this might be it!**
Ghimire: monthly forcing = (Δmonthly WSA x shell’s WSA kernel) + (Δmonthly BSA x shell’s BSA kernel)
he didn’t do fractions, should I?


unit shuffle:
the kernel is watts/sq meter/0.01 increase in fractional albedo. That is, the kernel corresponds to an increase of 0.01 in the albedo. So “watts per square meter per 0.01 increase in albedo.” does that even apply to decreasing albedo?
since the fractions are spatial: make a ΔWSA and a ΔBSA calc, multiply by 0.001 since that’s the albedo scale factor. i guess we’re back to 32 bit floats
then multiply THOSE by the the fraction WSA and fraction BSA
then, finally, multiply those by the kernel data to see what each Δ in albedo means for RF.
albedo goes down, yields a negative value. negative value * neg kernel value = a positive forcing effect, since low albedo means that many more watts/sq meter getting absorbed?
albedo goes up, yields a positive value. positive value * neg kernel value = negative forcing effect, since high albedo means more watts/sq meter getting reflected?


Used “raster layer statistics” in toolbox to sum them, cumbersome but works, py can definitely do this.
as in all things, the histos might be more interesting than the sums; the albedo*kernel files show whether, on balance, there’s more positive or negative forcing
well there’s a lot on either side of zero, with the vast majority not increasing or decreasing much at all. duh. not a lot of fat tails


WSA sum for april: 6.42119546358
BSA sum for april: 12.6113679784
whole lot more black sky according to the WSA/BSA fraction histos, who knew? why is that?? what the hell is black sky albedo???
that yields 19.03256344 for total change in forcing per square meter, over the entire earth’s worth of 100%-chance urban land, for April. dividing that by the number of 100%-chance-to-become-urban pixels, 24,588, yields 0.000774 bump in RF per cell. fucking tiny. but, you know, that makes sense since 1) urban land area is tiny in general 2) ghimire says it took 305 years of anthro LC change to get a watts/m^2 drop of -0.16. so this is a drop in a bucket of a drop in a bucket. hahaha this result SUCKS but hey, you knew it’d be small stuff


After that you have to calculate how much area you have covered by those pixels. they’re in geographic coordinates; converting to something with meters necessarily changes the number of cells; that’s not good. I guess it wont really matter if you reproject it the same way each time? So going to do it with world sinusoidal, seems simple enough "+proj=sinu +lon_0=0 +x_0=0 +y_0=0 +datum=WGS84 +units=m +no_defs"
so that has 20,721 pixels, each pixel 5,564.11m on a side, or 30,959,320.0921 square meters. that’s 641,508,071,628.404 square meters total in the 100%-chance-of-becoming-urban class, or 641,508 sq km, or 247,687 square miles. that’s reasonable compared to the 1.2m square kilometers of TOTAL “any chance at all” land reported by Seto 2012.













- which makes total sense, they’re all negative values; "over *this* pixel, dropping albedo by 0.01 means a -1.whatever change in watts per square meter of RF.” I guess since the kernels describe the *change in forcing per unit change of albedo, this method doesn’t need insolation/SSRD.* But then again since it’s only changes, it doesnt make for absolutes. Zhai 2014 says for absolutes you need SSRD/insolation.

- where do mutlu’s fractions come in? let’s talk through what I have, using april data and 100%-chance expansion pixels only
WSA for 100%-chance land *before* it changes
BSA for 100%-chance land *before* it changes
WSA for 100%-chance land *after* it changes in like 30 years
BSA for 100%-chance land *after* it changes in like 30 years
why the hell did I do extant albedo? I guess I need that for current forcing, but I dunno how to even calculate that since I need insolation apparently!
and what the fucking cock was I talking about with “change in kernel,” the kernel values dont change!
Okay the *expansion* *probability* pixels have changes in albedo since they went from previous LC > urban, class 13 albedo. I mean theoretically, I still haven’t generated/received the previous LC map yet. ANYWAY those have changes, and changes are good shit. **✓**
**(((Δ WSA** **x fraction WSA)** **x WSA kernel )** **+ ((Δ BSA** **x fraction BSA)** **x BSA kernel))) x total area = forcing change as all that stuff moves from previous LC to urban. I think this might be it!**
Ghimire: monthly forcing = (Δmonthly WSA x shell’s WSA kernel) + (Δmonthly BSA x shell’s BSA kernel)
he didn’t do fractions, should I?


unit shuffle:
the kernel is watts/sq meter/0.01 increase in fractional albedo. That is, the kernel corresponds to an increase of 0.01 in the albedo. So “watts per square meter per 0.01 increase in albedo.” does that even apply to decreasing albedo?
since the fractions are spatial: make a ΔWSA and a ΔBSA calc, multiply by 0.001 since that’s the albedo scale factor. i guess we’re back to 32 bit floats
then multiply THOSE by the the fraction WSA and fraction BSA
then, finally, multiply those by the kernel data to see what each Δ in albedo means for RF.
albedo goes down, yields a negative value. negative value * neg kernel value = a positive forcing effect, since low albedo means that many more watts/sq meter getting absorbed?
albedo goes up, yields a positive value. positive value * neg kernel value = negative forcing effect, since high albedo means more watts/sq meter getting reflected?


Used “raster layer statistics” in toolbox to sum them, cumbersome but works, py can definitely do this.
as in all things, the histos might be more interesting than the sums; the albedo*kernel files show whether, on balance, there’s more positive or negative forcing
well there’s a lot on either side of zero, with the vast majority not increasing or decreasing much at all. duh. not a lot of fat tails


WSA sum for april: 6.42119546358
BSA sum for april: 12.6113679784
whole lot more black sky according to the WSA/BSA fraction histos, who knew? why is that?? what the hell is black sky albedo???
that yields 19.03256344 for total change in forcing per square meter, over the entire earth’s worth of 100%-chance urban land, for April. dividing that by the number of 100%-chance-to-become-urban pixels, 24,588, yields 0.000774 bump in RF per cell. fucking tiny. but, you know, that makes sense since 1) urban land area is tiny in general 2) ghimire says it took 305 years of anthro LC change to get a watts/m^2 drop of -0.16. so this is a drop in a bucket of a drop in a bucket. hahaha this result SUCKS but hey, you knew it’d be small stuff


After that you have to calculate how much area you have covered by those pixels. they’re in geographic coordinates; converting to something with meters necessarily changes the number of cells; that’s not good. I guess it wont really matter if you reproject it the same way each time? So going to do it with world sinusoidal, seems simple enough "+proj=sinu +lon_0=0 +x_0=0 +y_0=0 +datum=WGS84 +units=m +no_defs"
so that has 20,721 pixels, each pixel 5,564.11m on a side, or 30,959,320.0921 square meters. that’s 641,508,071,628.404 square meters total in the 100%-chance-of-becoming-urban class, or 641,508 sq km, or 247,687 square miles. that’s reasonable compared to the 1.2m square kilometers of TOTAL “any chance at all” land reported by Seto 2012.











- WSA for 100%-chance land *before* it changes

- BSA for 100%-chance land *before* it changes

- WSA for 100%-chance land *after* it changes in like 30 years

- BSA for 100%-chance land *after* it changes in like 30 years
why the hell did I do extant albedo? I guess I need that for current forcing, but I dunno how to even calculate that since I need insolation apparently!
and what the fucking cock was I talking about with “change in kernel,” the kernel values dont change!
Okay the *expansion* *probability* pixels have changes in albedo since they went from previous LC > urban, class 13 albedo. I mean theoretically, I still haven’t generated/received the previous LC map yet. ANYWAY those have changes, and changes are good shit. **✓**
**(((Δ WSA** **x fraction WSA)** **x WSA kernel )** **+ ((Δ BSA** **x fraction BSA)** **x BSA kernel))) x total area = forcing change as all that stuff moves from previous LC to urban. I think this might be it!**
Ghimire: monthly forcing = (Δmonthly WSA x shell’s WSA kernel) + (Δmonthly BSA x shell’s BSA kernel)
he didn’t do fractions, should I?


unit shuffle:
the kernel is watts/sq meter/0.01 increase in fractional albedo. That is, the kernel corresponds to an increase of 0.01 in the albedo. So “watts per square meter per 0.01 increase in albedo.” does that even apply to decreasing albedo?
since the fractions are spatial: make a ΔWSA and a ΔBSA calc, multiply by 0.001 since that’s the albedo scale factor. i guess we’re back to 32 bit floats
then multiply THOSE by the the fraction WSA and fraction BSA
then, finally, multiply those by the kernel data to see what each Δ in albedo means for RF.
albedo goes down, yields a negative value. negative value * neg kernel value = a positive forcing effect, since low albedo means that many more watts/sq meter getting absorbed?
albedo goes up, yields a positive value. positive value * neg kernel value = negative forcing effect, since high albedo means more watts/sq meter getting reflected?


Used “raster layer statistics” in toolbox to sum them, cumbersome but works, py can definitely do this.
as in all things, the histos might be more interesting than the sums; the albedo*kernel files show whether, on balance, there’s more positive or negative forcing
well there’s a lot on either side of zero, with the vast majority not increasing or decreasing much at all. duh. not a lot of fat tails


WSA sum for april: 6.42119546358
BSA sum for april: 12.6113679784
whole lot more black sky according to the WSA/BSA fraction histos, who knew? why is that?? what the hell is black sky albedo???
that yields 19.03256344 for total change in forcing per square meter, over the entire earth’s worth of 100%-chance urban land, for April. dividing that by the number of 100%-chance-to-become-urban pixels, 24,588, yields 0.000774 bump in RF per cell. fucking tiny. but, you know, that makes sense since 1) urban land area is tiny in general 2) ghimire says it took 305 years of anthro LC change to get a watts/m^2 drop of -0.16. so this is a drop in a bucket of a drop in a bucket. hahaha this result SUCKS but hey, you knew it’d be small stuff


After that you have to calculate how much area you have covered by those pixels. they’re in geographic coordinates; converting to something with meters necessarily changes the number of cells; that’s not good. I guess it wont really matter if you reproject it the same way each time? So going to do it with world sinusoidal, seems simple enough "+proj=sinu +lon_0=0 +x_0=0 +y_0=0 +datum=WGS84 +units=m +no_defs"
so that has 20,721 pixels, each pixel 5,564.11m on a side, or 30,959,320.0921 square meters. that’s 641,508,071,628.404 square meters total in the 100%-chance-of-becoming-urban class, or 641,508 sq km, or 247,687 square miles. that’s reasonable compared to the 1.2m square kilometers of TOTAL “any chance at all” land reported by Seto 2012.









- why the hell did I do extant albedo? I guess I need that for current forcing, but I dunno how to even calculate that since I need insolation apparently!

- and what the fucking cock was I talking about with “change in kernel,” the kernel values dont change!

- Okay the *expansion* *probability* pixels have changes in albedo since they went from previous LC > urban, class 13 albedo. I mean theoretically, I still haven’t generated/received the previous LC map yet. ANYWAY those have changes, and changes are good shit. **✓**
**(((Δ WSA** **x fraction WSA)** **x WSA kernel )** **+ ((Δ BSA** **x fraction BSA)** **x BSA kernel))) x total area = forcing change as all that stuff moves from previous LC to urban. I think this might be it!**
Ghimire: monthly forcing = (Δmonthly WSA x shell’s WSA kernel) + (Δmonthly BSA x shell’s BSA kernel)
he didn’t do fractions, should I?


unit shuffle:
the kernel is watts/sq meter/0.01 increase in fractional albedo. That is, the kernel corresponds to an increase of 0.01 in the albedo. So “watts per square meter per 0.01 increase in albedo.” does that even apply to decreasing albedo?
since the fractions are spatial: make a ΔWSA and a ΔBSA calc, multiply by 0.001 since that’s the albedo scale factor. i guess we’re back to 32 bit floats
then multiply THOSE by the the fraction WSA and fraction BSA
then, finally, multiply those by the kernel data to see what each Δ in albedo means for RF.
albedo goes down, yields a negative value. negative value * neg kernel value = a positive forcing effect, since low albedo means that many more watts/sq meter getting absorbed?
albedo goes up, yields a positive value. positive value * neg kernel value = negative forcing effect, since high albedo means more watts/sq meter getting reflected?


Used “raster layer statistics” in toolbox to sum them, cumbersome but works, py can definitely do this.
as in all things, the histos might be more interesting than the sums; the albedo*kernel files show whether, on balance, there’s more positive or negative forcing
well there’s a lot on either side of zero, with the vast majority not increasing or decreasing much at all. duh. not a lot of fat tails


WSA sum for april: 6.42119546358
BSA sum for april: 12.6113679784
whole lot more black sky according to the WSA/BSA fraction histos, who knew? why is that?? what the hell is black sky albedo???
that yields 19.03256344 for total change in forcing per square meter, over the entire earth’s worth of 100%-chance urban land, for April. dividing that by the number of 100%-chance-to-become-urban pixels, 24,588, yields 0.000774 bump in RF per cell. fucking tiny. but, you know, that makes sense since 1) urban land area is tiny in general 2) ghimire says it took 305 years of anthro LC change to get a watts/m^2 drop of -0.16. so this is a drop in a bucket of a drop in a bucket. hahaha this result SUCKS but hey, you knew it’d be small stuff


After that you have to calculate how much area you have covered by those pixels. they’re in geographic coordinates; converting to something with meters necessarily changes the number of cells; that’s not good. I guess it wont really matter if you reproject it the same way each time? So going to do it with world sinusoidal, seems simple enough "+proj=sinu +lon_0=0 +x_0=0 +y_0=0 +datum=WGS84 +units=m +no_defs"
so that has 20,721 pixels, each pixel 5,564.11m on a side, or 30,959,320.0921 square meters. that’s 641,508,071,628.404 square meters total in the 100%-chance-of-becoming-urban class, or 641,508 sq km, or 247,687 square miles. that’s reasonable compared to the 1.2m square kilometers of TOTAL “any chance at all” land reported by Seto 2012.







- **(((Δ WSA** **x fraction WSA)** **x WSA kernel )** **+ ((Δ BSA** **x fraction BSA)** **x BSA kernel))) x total area = forcing change as all that stuff moves from previous LC to urban. I think this might be it!**

- Ghimire: monthly forcing = (Δmonthly WSA x shell’s WSA kernel) + (Δmonthly BSA x shell’s BSA kernel)
he didn’t do fractions, should I?



- he didn’t do fractions, should I?

- unit shuffle:
the kernel is watts/sq meter/0.01 increase in fractional albedo. That is, the kernel corresponds to an increase of 0.01 in the albedo. So “watts per square meter per 0.01 increase in albedo.” does that even apply to decreasing albedo?
since the fractions are spatial: make a ΔWSA and a ΔBSA calc, multiply by 0.001 since that’s the albedo scale factor. i guess we’re back to 32 bit floats
then multiply THOSE by the the fraction WSA and fraction BSA
then, finally, multiply those by the kernel data to see what each Δ in albedo means for RF.
albedo goes down, yields a negative value. negative value * neg kernel value = a positive forcing effect, since low albedo means that many more watts/sq meter getting absorbed?
albedo goes up, yields a positive value. positive value * neg kernel value = negative forcing effect, since high albedo means more watts/sq meter getting reflected?


Used “raster layer statistics” in toolbox to sum them, cumbersome but works, py can definitely do this.
as in all things, the histos might be more interesting than the sums; the albedo*kernel files show whether, on balance, there’s more positive or negative forcing
well there’s a lot on either side of zero, with the vast majority not increasing or decreasing much at all. duh. not a lot of fat tails


WSA sum for april: 6.42119546358
BSA sum for april: 12.6113679784
whole lot more black sky according to the WSA/BSA fraction histos, who knew? why is that?? what the hell is black sky albedo???
that yields 19.03256344 for total change in forcing per square meter, over the entire earth’s worth of 100%-chance urban land, for April. dividing that by the number of 100%-chance-to-become-urban pixels, 24,588, yields 0.000774 bump in RF per cell. fucking tiny. but, you know, that makes sense since 1) urban land area is tiny in general 2) ghimire says it took 305 years of anthro LC change to get a watts/m^2 drop of -0.16. so this is a drop in a bucket of a drop in a bucket. hahaha this result SUCKS but hey, you knew it’d be small stuff


After that you have to calculate how much area you have covered by those pixels. they’re in geographic coordinates; converting to something with meters necessarily changes the number of cells; that’s not good. I guess it wont really matter if you reproject it the same way each time? So going to do it with world sinusoidal, seems simple enough "+proj=sinu +lon_0=0 +x_0=0 +y_0=0 +datum=WGS84 +units=m +no_defs"
so that has 20,721 pixels, each pixel 5,564.11m on a side, or 30,959,320.0921 square meters. that’s 641,508,071,628.404 square meters total in the 100%-chance-of-becoming-urban class, or 641,508 sq km, or 247,687 square miles. that’s reasonable compared to the 1.2m square kilometers of TOTAL “any chance at all” land reported by Seto 2012.





- the kernel is watts/sq meter/0.01 increase in fractional albedo. That is, the kernel corresponds to an increase of 0.01 in the albedo. So “watts per square meter per 0.01 increase in albedo.” does that even apply to decreasing albedo?

- since the fractions are spatial: make a ΔWSA and a ΔBSA calc, multiply by 0.001 since that’s the albedo scale factor. i guess we’re back to 32 bit floats

- then multiply THOSE by the the fraction WSA and fraction BSA

- then, finally, multiply those by the kernel data to see what each Δ in albedo means for RF.
albedo goes down, yields a negative value. negative value * neg kernel value = a positive forcing effect, since low albedo means that many more watts/sq meter getting absorbed?
albedo goes up, yields a positive value. positive value * neg kernel value = negative forcing effect, since high albedo means more watts/sq meter getting reflected?



- albedo goes down, yields a negative value. negative value * neg kernel value = a positive forcing effect, since low albedo means that many more watts/sq meter getting absorbed?

- albedo goes up, yields a positive value. positive value * neg kernel value = negative forcing effect, since high albedo means more watts/sq meter getting reflected?

- Used “raster layer statistics” in toolbox to sum them, cumbersome but works, py can definitely do this.
as in all things, the histos might be more interesting than the sums; the albedo*kernel files show whether, on balance, there’s more positive or negative forcing
well there’s a lot on either side of zero, with the vast majority not increasing or decreasing much at all. duh. not a lot of fat tails


WSA sum for april: 6.42119546358
BSA sum for april: 12.6113679784
whole lot more black sky according to the WSA/BSA fraction histos, who knew? why is that?? what the hell is black sky albedo???
that yields 19.03256344 for total change in forcing per square meter, over the entire earth’s worth of 100%-chance urban land, for April. dividing that by the number of 100%-chance-to-become-urban pixels, 24,588, yields 0.000774 bump in RF per cell. fucking tiny. but, you know, that makes sense since 1) urban land area is tiny in general 2) ghimire says it took 305 years of anthro LC change to get a watts/m^2 drop of -0.16. so this is a drop in a bucket of a drop in a bucket. hahaha this result SUCKS but hey, you knew it’d be small stuff



- as in all things, the histos might be more interesting than the sums; the albedo*kernel files show whether, on balance, there’s more positive or negative forcing
well there’s a lot on either side of zero, with the vast majority not increasing or decreasing much at all. duh. not a lot of fat tails



- well there’s a lot on either side of zero, with the vast majority not increasing or decreasing much at all. duh. not a lot of fat tails

- WSA sum for april: 6.42119546358

- BSA sum for april: 12.6113679784

- whole lot more black sky according to the WSA/BSA fraction histos, who knew? why is that?? what the hell is black sky albedo???

- that yields 19.03256344 for total change in forcing per square meter, over the entire earth’s worth of 100%-chance urban land, for April. dividing that by the number of 100%-chance-to-become-urban pixels, 24,588, yields 0.000774 bump in RF per cell. fucking tiny. but, you know, that makes sense since 1) urban land area is tiny in general 2) ghimire says it took 305 years of anthro LC change to get a watts/m^2 drop of -0.16. so this is a drop in a bucket of a drop in a bucket. hahaha this result SUCKS but hey, you knew it’d be small stuff

- After that you have to calculate how much area you have covered by those pixels. they’re in geographic coordinates; converting to something with meters necessarily changes the number of cells; that’s not good. I guess it wont really matter if you reproject it the same way each time? So going to do it with world sinusoidal, seems simple enough "+proj=sinu +lon_0=0 +x_0=0 +y_0=0 +datum=WGS84 +units=m +no_defs"
so that has 20,721 pixels, each pixel 5,564.11m on a side, or 30,959,320.0921 square meters. that’s 641,508,071,628.404 square meters total in the 100%-chance-of-becoming-urban class, or 641,508 sq km, or 247,687 square miles. that’s reasonable compared to the 1.2m square kilometers of TOTAL “any chance at all” land reported by Seto 2012.



- so that has 20,721 pixels, each pixel 5,564.11m on a side, or 30,959,320.0921 square meters. that’s 641,508,071,628.404 square meters total in the 100%-chance-of-becoming-urban class, or 641,508 sq km, or 247,687 square miles. that’s reasonable compared to the 1.2m square kilometers of TOTAL “any chance at all” land reported by Seto 2012.

**D-fense - monday morning**


- Rob: monday May 2 or weds May 4

- Mutlu: monday May 2 before 3:30, 12:30-3pm

- Annemarie: monday May 2

March 25 - friday morning meet with Mutlu


April 18 - draft due to Mutlu


May 2 - defense


**Arc time**


- I dont have enough space on bootcamp to get all 40 gigs worth of data uncompressed. so lets try it and then do it on a lab computer. or get an external HDD? might be hella slow...

- albedo data files need headers, theyre in the FTP

- use snap raster in environment settings > processing extent > snap raster to get things aligned. to do so in QGIS: [http://gis.stackexchange.com/questions/159525/rasterization-of-point-vector-in-qgis-how-to-align-the-resulting-raster-to-an-e?rq=1](http://gis.stackexchange.com/questions/159525/rasterization-of-point-vector-in-qgis-how-to-align-the-resulting-raster-to-an-e?rq=1)

- need to throw out any pixels that went from water > urban since the MODIS LC stuff isnt perfectly coincident? man coastal cities get totally screwed in this analysis, they dont have before-LC. i mean naturally guneralp’s data wont be perfectly co-incident with MODIS right? different datasets? but cmon man its in MODIS-SPHERE while *actual* MODIS data is in some goofed up clarkes whatever the fuck ellipsoid? what the hell!

- okay guneralp and seto got their just raw coastlines and pixel arrangement from schneider et al, right?
this 11 year old thread makes it seem like its a mistake and nobody uses that stupid ass clarkes sphere? [http://forums.esri.com/Thread.asp?c=93&f=984&t=152042](http://forums.esri.com/Thread.asp?c=93&f=984&t=152042)
i mean I could nibble out all water, but is that defensible?



- this 11 year old thread makes it seem like its a mistake and nobody uses that stupid ass clarkes sphere? [http://forums.esri.com/Thread.asp?c=93&f=984&t=152042](http://forums.esri.com/Thread.asp?c=93&f=984&t=152042)

- i mean I could nibble out all water, but is that defensible?

- D-MODIS sphere is guneralp’s datum? what the hell is that?
WGS spheroid \/
6378137 , 298.257223563
6378206.4, 294.9786982138982,
clarke spheroid /\ EPSG 4008



- WGS spheroid \/

- 6378137 , 298.257223563

- 6378206.4, 294.9786982138982,

- clarke spheroid /\ EPSG 4008

- schneiders original 500m LC map resampled to 0.05 deg with nearest neighbor is definitely more generous

- what guneralp said:
*All data used in Goode’s Homolosine Equal-Area , spatial resolution of the maps is 5 km. Year 2000 urban map is (MODIS) land-cover product v5, resample the global urban land-cover map to 5-km resolution from its native resolution of 463 m.* So you can get what they used, MCD12Q1.051, from [http://e4ftl01.cr.usgs.gov/MOTA/](http://e4ftl01.cr.usgs.gov/MOTA/)
[Global forecasts of urban expansion to 2030 and direct impacts on biodiversity and carbon pools](http://e4ftl01.cr.usgs.gov/MOTA/MCD12Q1.051/) but they’re all chunked up so you’d have to download, mosaic, reproject. I think it’s 28 gigs...
schneiders 500m LC map: they did it themselves from a shitload of raw modis data; maybe their [http://iopscience.iop.org/article/10.1088/1748-9326/4/4/044003/fulltext/](http://iopscience.iop.org/article/10.1088/1748-9326/4/4/044003/fulltext/)
MCD12C1.051 is 0.05 deg, which matches our current resolution, but doesnt match up to land/water that guneralp used. They apparently grabbed the 500m then resampled + reprojected to goode’s homolosine equal area. [https://lpdaac.usgs.gov/dataset_discovery/modis/modis_products_table/mcd12c1](https://lpdaac.usgs.gov/dataset_discovery/modis/modis_products_table/mcd12c1)


*ignore: Land cover: We convert the VMAP0 vector-based land cover product (19) to raster, reprojected it to Goode’s Homolosine, and resample to 5 km. The reason we use VMAP0 product instead of MODIS v5 as we did for urban extent is that URBANMOD requires the initial data of the land cover to be simulated to be colocated with data from the driver maps. Although the initial urban extent map overlays with the other three driver maps, this would not be the case for the land cover driver map had we used MODIS v5 product to create it.*



- *All data used in Goode’s Homolosine Equal-Area , spatial resolution of the maps is 5 km. Year 2000 urban map is (MODIS) land-cover product v5, resample the global urban land-cover map to 5-km resolution from its native resolution of 463 m.* So you can get what they used, MCD12Q1.051, from [http://e4ftl01.cr.usgs.gov/MOTA/](http://e4ftl01.cr.usgs.gov/MOTA/)

- [Global forecasts of urban expansion to 2030 and direct impacts on biodiversity and carbon pools](http://e4ftl01.cr.usgs.gov/MOTA/MCD12Q1.051/) but they’re all chunked up so you’d have to download, mosaic, reproject. I think it’s 28 gigs...
schneiders 500m LC map: they did it themselves from a shitload of raw modis data; maybe their [http://iopscience.iop.org/article/10.1088/1748-9326/4/4/044003/fulltext/](http://iopscience.iop.org/article/10.1088/1748-9326/4/4/044003/fulltext/)
MCD12C1.051 is 0.05 deg, which matches our current resolution, but doesnt match up to land/water that guneralp used. They apparently grabbed the 500m then resampled + reprojected to goode’s homolosine equal area. [https://lpdaac.usgs.gov/dataset_discovery/modis/modis_products_table/mcd12c1](https://lpdaac.usgs.gov/dataset_discovery/modis/modis_products_table/mcd12c1)



- schneiders 500m LC map: they did it themselves from a shitload of raw modis data; maybe their [http://iopscience.iop.org/article/10.1088/1748-9326/4/4/044003/fulltext/](http://iopscience.iop.org/article/10.1088/1748-9326/4/4/044003/fulltext/)

- MCD12C1.051 is 0.05 deg, which matches our current resolution, but doesnt match up to land/water that guneralp used. They apparently grabbed the 500m then resampled + reprojected to goode’s homolosine equal area. [https://lpdaac.usgs.gov/dataset_discovery/modis/modis_products_table/mcd12c1](https://lpdaac.usgs.gov/dataset_discovery/modis/modis_products_table/mcd12c1)

- *ignore: Land cover: We convert the VMAP0 vector-based land cover product (19) to raster, reprojected it to Goode’s Homolosine, and resample to 5 km. The reason we use VMAP0 product instead of MODIS v5 as we did for urban extent is that URBANMOD requires the initial data of the land cover to be simulated to be colocated with data from the driver maps. Although the initial urban extent map overlays with the other three driver maps, this would not be the case for the land cover driver map had we used MODIS v5 product to create it.*

**pass for earthdata: Radartime1!**


**The Plan**


1. I have 0.05 degree snow-free shortwave black-sky and white-sky albedo for all IGBP land cover categories, in monthly means (Jan, Feb, March etc.) and standard deviations for each month. Do all analyses month-by-month.
*okay first get all the data aligned, i dont know where this 0.49 deg bullshit came up but everything needs to be in WGS84 and 0.05 deg res. Going to try this in arc, see how far it goes. NOTE: this snaps well.*



- *okay first get all the data aligned, i dont know where this 0.49 deg bullshit came up but everything needs to be in WGS84 and 0.05 deg res. Going to try this in arc, see how far it goes. NOTE: this snaps well.*

1. Take the albedo data’s class 13 (urban/built-up) white-sky and black-sky albedos, assign them to currently-urban pixels found in Guneralp’s 0.05 degree “where cities are now and where they will be in 2030” data (Guneralp’s currently-urban pixels are derived from Schneider 2009, just resampled to 0.05 degrees).

1. Now we have white-sky and black-sky albedos for all existing cities.

1. Assign current albedos to “likely to become urban by 2030” pixels; the pixel values range from 1%-100% probability of becoming urban.
5 categories: 1-25%, 25-50%, 50-75%, 75-99%, 100%
Most of these high-likelihood (100% chance) pixels touch current urban areas, so can use nearest neighbor to assign the albedos of current urban areas to the new pixels. The literature says that the “spreading pancake” model of urban development explains a good portion of expansion patterns, so the albedo values should stay pretty consistent on the edges of urban expansion.
Can tweak the assigned albedo values using the standard deviations for the currently-urban pixels.



- 5 categories: 1-25%, 25-50%, 50-75%, 75-99%, 100%

- Most of these high-likelihood (100% chance) pixels touch current urban areas, so can use nearest neighbor to assign the albedos of current urban areas to the new pixels. The literature says that the “spreading pancake” model of urban development explains a good portion of expansion patterns, so the albedo values should stay pretty consistent on the edges of urban expansion.

- Can tweak the assigned albedo values using the standard deviations for the currently-urban pixels.

1. These “likely to become urban by 2030” pixels also have their own a) current land cover categories and b) current albedo values.
Find albedo change as they move from their old land cover (*need 0.05 deg MODIS IGBP land cover map:* [http://e4ftl01.cr.usgs.gov/MOTA/MCD12C1.051/2012.01.01/MCD12C1.A2012001.051.2013178154403.hdf](http://e4ftl01.cr.usgs.gov/MOTA/MCD12C1.051/2012.01.01/MCD12C1.A2012001.051.2013178154403.hdf) download, [https://lpdaac.usgs.gov/about/news_archive/modisterra_land_cover_types_yearly_l3_global_005deg_cmg_mod12c1](https://lpdaac.usgs.gov/about/news_archive/modisterra_land_cover_types_yearly_l3_global_005deg_cmg_mod12c1) and [https://lpdaac.usgs.gov/dataset_discovery/modis/modis_products_table/mcd12c1](https://lpdaac.usgs.gov/dataset_discovery/modis/modis_products_table/mcd12c1) references it has this idiot ass crs "+proj=longlat +ellps=clrk66 +no_defs”, my gdal cant do HDF4, I dont know what the fuck!!!! reprojecting shifts shit all around and I hate it. can I just change the ellipse??) + associated old albedo --> new urban land cover + new associated albedo?
this is going to be a real nightmare if Guneralp does not cough up his original… (hint: he totally does not check his email)



- Find albedo change as they move from their old land cover (*need 0.05 deg MODIS IGBP land cover map:* [http://e4ftl01.cr.usgs.gov/MOTA/MCD12C1.051/2012.01.01/MCD12C1.A2012001.051.2013178154403.hdf](http://e4ftl01.cr.usgs.gov/MOTA/MCD12C1.051/2012.01.01/MCD12C1.A2012001.051.2013178154403.hdf) download, [https://lpdaac.usgs.gov/about/news_archive/modisterra_land_cover_types_yearly_l3_global_005deg_cmg_mod12c1](https://lpdaac.usgs.gov/about/news_archive/modisterra_land_cover_types_yearly_l3_global_005deg_cmg_mod12c1) and [https://lpdaac.usgs.gov/dataset_discovery/modis/modis_products_table/mcd12c1](https://lpdaac.usgs.gov/dataset_discovery/modis/modis_products_table/mcd12c1) references it has this idiot ass crs "+proj=longlat +ellps=clrk66 +no_defs”, my gdal cant do HDF4, I dont know what the fuck!!!! reprojecting shifts shit all around and I hate it. can I just change the ellipse??) + associated old albedo --> new urban land cover + new associated albedo?

- this is going to be a real nightmare if Guneralp does not cough up his original… (hint: he totally does not check his email)

1. Calculate change in forcing from all this albedo change
Forcing = change in white-sky albedo *change in kernel + change in black-sky albedo* change in kernel. Shell’s 3 degree kernels aren’t separated into white- and black-sky, but I have it written down from a previous meeting to “use Ghimire’s 2.5 degree data with 'share white-sky albedo' and 'share black-sky albedo’ for every spot on earth, multiply those fractions by Shell’s kernels.” Did you have Ghimire’s data somewhere? I emailed him last year but didn’t get real far...
this has 12 months of data, so keep everything monthly? Or another annual average?





- Forcing = change in white-sky albedo *change in kernel + change in black-sky albedo* change in kernel. Shell’s 3 degree kernels aren’t separated into white- and black-sky, but I have it written down from a previous meeting to “use Ghimire’s 2.5 degree data with 'share white-sky albedo' and 'share black-sky albedo’ for every spot on earth, multiply those fractions by Shell’s kernels.” Did you have Ghimire’s data somewhere? I emailed him last year but didn’t get real far...
this has 12 months of data, so keep everything monthly? Or another annual average?



- this has 12 months of data, so keep everything monthly? Or another annual average?

1. Deliverables:
Uncertainty estimates? what’s a good way to go about this? +/- 1 standard dev GOOD
Table with which “before” land cover classes will switch to urban/built-up by 2030? GOOD
Table with “before” albedos and “after” albedos? GOOD
Range of radiative forcing change? *youd get 1 global value with +/- uncertainty around it (expansion will cause tk watts of RF)*
Maps- means, variations, uncertainty



- Uncertainty estimates? what’s a good way to go about this? +/- 1 standard dev GOOD

- Table with which “before” land cover classes will switch to urban/built-up by 2030? GOOD

- Table with “before” albedos and “after” albedos? GOOD

- Range of radiative forcing change? *youd get 1 global value with +/- uncertainty around it (expansion will cause tk watts of RF)*

- Maps- means, variations, uncertainty

**mutlu meeting from India:**


- do everything by month. but final results will include annual averages of all this shit.

- remember to +/- 1 standard deviations for all these!

- for guneralp’s likely-urban pixels: use different probability thresholds, this could be 25%, 50%, hell any arbitrary numbers. we want to have a lot of stuff for the final tables; we’re tweaking a lot of variables. fuzzy! so pick a few/do it continuously even. if you figure that shit out.

- kernels: he has MERRA reanalysis data, mix of climate models and observation, separates white-sky and black-sky albedo. coarse but doesn’t matter, includes relative fractions of direct vs. diffuse insolation (interacting with atmo vs. no atmo impact). came up with direct & diffuse fraction for each month; direct (BSA) map and diffuse (WSA) map, and every pixel has 12 values (1 per month). numbers range from 0-100. instead of ghimire, use this. these are only fractions! also remember to do +/- 1 standard deviation.
forcing has 3 terms: white/black sky albedo from IGBP dataset, kernels from shell, fraction from MERRA



- forcing has 3 terms: white/black sky albedo from IGBP dataset, kernels from shell, fraction from MERRA

- get all the data, generate bunch of results with these, remember all your scenarios.

**Questions for mutlu**


- this a good LC dataset for “Before urban”? [https://lpdaac.usgs.gov/about/news_archive/modisterra_land_cover_types_yearly_l3_global_005deg_cmg_mod12c1](https://lpdaac.usgs.gov/about/news_archive/modisterra_land_cover_types_yearly_l3_global_005deg_cmg_mod12c1)

**Latest meeting**


**1. reclassify ca. 2001 urban extent data**


- current schema: Global Urban Extent (class 13), including land (class 1) and water (class 0). Also global IGBP Land Cover Map (classes 1-17), including urban extent (class 13) . so it matches up to IGBP
actually do we need to do this? The albedo data is 0.05 deg, the predicted urban extent data is 0.05 deg, which includes extant urban areas at 0.05 deg *derived from Schneider 2001*. so why tf would I bother with Schneider 2001?



- actually do we need to do this? The albedo data is 0.05 deg, the predicted urban extent data is 0.05 deg, which includes extant urban areas at 0.05 deg *derived from Schneider 2001*. so why tf would I bother with Schneider 2001?

**2. intersect with new albedo dataset with IGBP categories - really we’re forgetting about the actual albedo measurements. This has it already baked in.**


- separated out guneralp 101 pixels (extant 2001 urban areas per Schneider 2009) with raster calc, then converted to 16bit signed to match the bsa shortwave april data, then raster calcd like so: guneralp*0 + albedo_band_13 (since 13 is the urban one), then you get a 32 bit tiff with albedos assigned to the extant city pixels.
next up
average all WSA and BSA files?
("hierarchical_albedo_igbp_0.05.bsa_shortwave.Jan@13" +
"hierarchical_albedo_igbp_0.05.bsa_shortwave.Feb@13" +
"hierarchical_albedo_igbp_0.05.bsa_shortwave.Mar@13" +
"hierarchical_albedo_igbp_0.05.bsa_shortwave.Apr@13" +
"hierarchical_albedo_igbp_0.05.bsa_shortwave.May@13" +
"hierarchical_albedo_igbp_0.05.bsa_shortwave.Jun@13" +
"hierarchical_albedo_igbp_0.05.bsa_shortwave.Jul@13" +
"hierarchical_albedo_igbp_0.05.bsa_shortwave.Aug@13" +
"hierarchical_albedo_igbp_0.05.bsa_shortwave.Sep@13" +
"hierarchical_albedo_igbp_0.05.bsa_shortwave.Oct@13" +
"hierarchical_albedo_igbp_0.05.bsa_shortwave.Nov@13" +
"hierarchical_albedo_igbp_0.05.bsa_shortwave.Dec@13") / 12 works, but is that the correct way of doing this?


use the std dev somehow? I have no idea
assign potential-expansion pixels
took guneralp original, saved out 100-class, now have certain-expansion pixels and extant-city pixels with albedo values. how to assign the current albedo values to their new neighbors?
gdal_calc.py doesnt fucking work, throws an “image not found” error







- next up
average all WSA and BSA files?
("hierarchical_albedo_igbp_0.05.bsa_shortwave.Jan@13" +
"hierarchical_albedo_igbp_0.05.bsa_shortwave.Feb@13" +
"hierarchical_albedo_igbp_0.05.bsa_shortwave.Mar@13" +
"hierarchical_albedo_igbp_0.05.bsa_shortwave.Apr@13" +
"hierarchical_albedo_igbp_0.05.bsa_shortwave.May@13" +
"hierarchical_albedo_igbp_0.05.bsa_shortwave.Jun@13" +
"hierarchical_albedo_igbp_0.05.bsa_shortwave.Jul@13" +
"hierarchical_albedo_igbp_0.05.bsa_shortwave.Aug@13" +
"hierarchical_albedo_igbp_0.05.bsa_shortwave.Sep@13" +
"hierarchical_albedo_igbp_0.05.bsa_shortwave.Oct@13" +
"hierarchical_albedo_igbp_0.05.bsa_shortwave.Nov@13" +
"hierarchical_albedo_igbp_0.05.bsa_shortwave.Dec@13") / 12 works, but is that the correct way of doing this?


use the std dev somehow? I have no idea
assign potential-expansion pixels
took guneralp original, saved out 100-class, now have certain-expansion pixels and extant-city pixels with albedo values. how to assign the current albedo values to their new neighbors?
gdal_calc.py doesnt fucking work, throws an “image not found” error





- average all WSA and BSA files?
("hierarchical_albedo_igbp_0.05.bsa_shortwave.Jan@13" +
"hierarchical_albedo_igbp_0.05.bsa_shortwave.Feb@13" +
"hierarchical_albedo_igbp_0.05.bsa_shortwave.Mar@13" +
"hierarchical_albedo_igbp_0.05.bsa_shortwave.Apr@13" +
"hierarchical_albedo_igbp_0.05.bsa_shortwave.May@13" +
"hierarchical_albedo_igbp_0.05.bsa_shortwave.Jun@13" +
"hierarchical_albedo_igbp_0.05.bsa_shortwave.Jul@13" +
"hierarchical_albedo_igbp_0.05.bsa_shortwave.Aug@13" +
"hierarchical_albedo_igbp_0.05.bsa_shortwave.Sep@13" +
"hierarchical_albedo_igbp_0.05.bsa_shortwave.Oct@13" +
"hierarchical_albedo_igbp_0.05.bsa_shortwave.Nov@13" +
"hierarchical_albedo_igbp_0.05.bsa_shortwave.Dec@13") / 12 works, but is that the correct way of doing this?



- ("hierarchical_albedo_igbp_0.05.bsa_shortwave.Jan@13" +

- "hierarchical_albedo_igbp_0.05.bsa_shortwave.Feb@13" +

- "hierarchical_albedo_igbp_0.05.bsa_shortwave.Mar@13" +

- "hierarchical_albedo_igbp_0.05.bsa_shortwave.Apr@13" +

- "hierarchical_albedo_igbp_0.05.bsa_shortwave.May@13" +

- "hierarchical_albedo_igbp_0.05.bsa_shortwave.Jun@13" +

- "hierarchical_albedo_igbp_0.05.bsa_shortwave.Jul@13" +

- "hierarchical_albedo_igbp_0.05.bsa_shortwave.Aug@13" +

- "hierarchical_albedo_igbp_0.05.bsa_shortwave.Sep@13" +

- "hierarchical_albedo_igbp_0.05.bsa_shortwave.Oct@13" +

- "hierarchical_albedo_igbp_0.05.bsa_shortwave.Nov@13" +

- "hierarchical_albedo_igbp_0.05.bsa_shortwave.Dec@13") / 12 works, but is that the correct way of doing this?

- use the std dev somehow? I have no idea

- assign potential-expansion pixels
took guneralp original, saved out 100-class, now have certain-expansion pixels and extant-city pixels with albedo values. how to assign the current albedo values to their new neighbors?
gdal_calc.py doesnt fucking work, throws an “image not found” error



- took guneralp original, saved out 100-class, now have certain-expansion pixels and extant-city pixels with albedo values. how to assign the current albedo values to their new neighbors?

- gdal_calc.py doesnt fucking work, throws an “image not found” error

**3. figure out how to assign new albedo values! GIS problem, requires lit review and a defensible method**


- 2/11 - chat with Zhu
well, you’re making a shitload of assumptions, so the best hting to do would just go by spatial autocorrelation. try tobler’s ’72 paper and the 2004 AAG conference proceedings; they even had a paper on urban settings. you can reason this out instead of citing; really the new urban pixels is of similar cover to the stuff before it (tk cite) and thus you can just average the adjacent already-urban stuff.
two pixels over and up from the new unknown one, weight the closer ones more than the far, assign the average to the new pixel.
“connectivity analysis” to determine which are closest and which are far
so now, according to mutlu, just test it out; assigning the stuff shouldnt be that hard. you have the data; try a test run.



- well, you’re making a shitload of assumptions, so the best hting to do would just go by spatial autocorrelation. try tobler’s ’72 paper and the 2004 AAG conference proceedings; they even had a paper on urban settings. you can reason this out instead of citing; really the new urban pixels is of similar cover to the stuff before it (tk cite) and thus you can just average the adjacent already-urban stuff.

- two pixels over and up from the new unknown one, weight the closer ones more than the far, assign the average to the new pixel.

- “connectivity analysis” to determine which are closest and which are far

- so now, according to mutlu, just test it out; assigning the stuff shouldnt be that hard. you have the data; try a test run.

- there’s new albedo data IGBP LC cover categories, includes 13 urban land; so it has monthly avg albedo composites. so a single value instead of having to average 10 years worth of data. 2000-2010, same as before, we’re using this, no GEE needed!
all urban pixels co-incident with annemaries, at 5km res, same as guneralp!
think he’s talking about [http://modis.gsfc.nasa.gov/sci_team/meetings/201304/presentations/plenary/masek.pdf](http://modis.gsfc.nasa.gov/sci_team/meetings/201304/presentations/plenary/masek.pdf)



- all urban pixels co-incident with annemaries, at 5km res, same as guneralp!

- think he’s talking about [http://modis.gsfc.nasa.gov/sci_team/meetings/201304/presentations/plenary/masek.pdf](http://modis.gsfc.nasa.gov/sci_team/meetings/201304/presentations/plenary/masek.pdf)

- take schneider ca. 2001 urban LC map
reclassify it to 0-1, 13 goes to 1, everything else goes to 0
downsample to 0.05deg resolution (appx 5km as guneralp)
"MODIS does not use the "Normal Sphere (r=6370997) but 6371007.181” same as schneider, same as all MODIS shit
also guneralp’s “existing urban areas” are taken from schneider anyway?


GDAL warp -tr 0.05 0.05, EPSG4326 input and output srs, -r average, -ot float 32 bit



- reclassify it to 0-1, 13 goes to 1, everything else goes to 0

- downsample to 0.05deg resolution (appx 5km as guneralp)
"MODIS does not use the "Normal Sphere (r=6370997) but 6371007.181” same as schneider, same as all MODIS shit
also guneralp’s “existing urban areas” are taken from schneider anyway?



- "MODIS does not use the "Normal Sphere (r=6370997) but 6371007.181” same as schneider, same as all MODIS shit

- also guneralp’s “existing urban areas” are taken from schneider anyway?

- GDAL warp -tr 0.05 0.05, EPSG4326 input and output srs, -r average, -ot float 32 bit

- get Seto-guneralp data into same config as schneider - [https://web.archive.org/web/20141110212613/http://bguneralp.tamu.edu/](https://web.archive.org/web/20141110212613/http://bguneralp.tamu.edu/) the real download site got killed but its still up here
for some idiotic reason it came as "+proj=longlat +a=6371007 +b=0 +no_defs”. used "gdal_translate -a_nodata 255 -a_srs "+proj=igh +R=6371007 +no_defs”” on the goode-homolosine data they provided, this just assigns it the correct projection. Then warped to WGS84 while keeping the nodata value, nearest neighbor resampling.
so the workflow: dump ESRI GRID folder into QGIS > save as a TIFF > assign its bad SRS to it with translate > convert to WGS84 with warp
using nearest neighbor when you convert to WGS84 is most conservative, but leaves a lot of shit uncovered; that notch in chicago for a lot of nodata over japan. can use other resampling methods but then you’re just introducing error.
since schneider comes in goodes too (albeit of course with fucked up projection info on the .bip, what the hell), pulling the exact same -a_srs trick except with 6371007.181 on the schneider bip and overlaying with the properly-assigned-projection guneralp data yields much better alignment on chicago and japan; basically no processing here except assigning the correct projection.
so goode + goode makes a right, but that leaves the albedo data i’d have to reproject…if i can get guneralp to cough up a WGS84, would make my life hella easier. asked him.





- for some idiotic reason it came as "+proj=longlat +a=6371007 +b=0 +no_defs”. used "gdal_translate -a_nodata 255 -a_srs "+proj=igh +R=6371007 +no_defs”” on the goode-homolosine data they provided, this just assigns it the correct projection. Then warped to WGS84 while keeping the nodata value, nearest neighbor resampling.

- so the workflow: dump ESRI GRID folder into QGIS > save as a TIFF > assign its bad SRS to it with translate > convert to WGS84 with warp

- using nearest neighbor when you convert to WGS84 is most conservative, but leaves a lot of shit uncovered; that notch in chicago for a lot of nodata over japan. can use other resampling methods but then you’re just introducing error.

- since schneider comes in goodes too (albeit of course with fucked up projection info on the .bip, what the hell), pulling the exact same -a_srs trick except with 6371007.181 on the schneider bip and overlaying with the properly-assigned-projection guneralp data yields much better alignment on chicago and japan; basically no processing here except assigning the correct projection.
so goode + goode makes a right, but that leaves the albedo data i’d have to reproject…if i can get guneralp to cough up a WGS84, would make my life hella easier. asked him.



- so goode + goode makes a right, but that leaves the albedo data i’d have to reproject…if i can get guneralp to cough up a WGS84, would make my life hella easier. asked him.

- then intersect with the new albedo dataset, (its in WGS84), do it for all 12 months, at BSA and WSA. so 24 times total. at the very end, you’d have 24 values: observed monthly BSA, observed monthly WSA

- now intersect with guneralp map, which dictates where NEW urban pixels will appear. but how do we assign new albedo values to these pixels? nearest neighbor? average? what’s a defensible GIS method of assigning new values to neighboring pixels? Something that makes sense in terms of land cover change. Guneralp could have a method? Predictive land cover change?
get averages + std devs for contiguous currently-urban pixels. then generate new maps where you have diff methods of assigning new albedo values:
mean assigned to new value
+std dev assigned to new values
std dev assigned to new values
also do it randomly!
contiguous urban pixel albedos, grab an albedo value out of a hat, assign it to the new pixel.







- get averages + std devs for contiguous currently-urban pixels. then generate new maps where you have diff methods of assigning new albedo values:
mean assigned to new value
+std dev assigned to new values
std dev assigned to new values
also do it randomly!
contiguous urban pixel albedos, grab an albedo value out of a hat, assign it to the new pixel.





- mean assigned to new value

- +std dev assigned to new values

- std dev assigned to new values

- also do it randomly!
contiguous urban pixel albedos, grab an albedo value out of a hat, assign it to the new pixel.



- contiguous urban pixel albedos, grab an albedo value out of a hat, assign it to the new pixel.

- after that’s done you have a future albedo map. also know the albedo CHANGE of each pixel since that new albedo dataset has BSA + WSA albedo values for every single pixel and LC type! which is great since you know the OLD LC type and can say “eat into forest, tk albedo change, eat into desert, tk albedo change"
[ ]  
forcing = change in WS albedo *change in kernel + change in BS albedo* change in kernel. but shell’s kernels aren’t separated into WSA and BSA.
Ghimire used a coarse 2.5deg reanalysis dataset that has “share WSA” and “share BSA” for every spot on earth; take shell’s kernels and multiply by those WSA and BSA fractions.
this has 12 months of data, so keep everything monthly


repeat this with ANOTHER set of kernels, the one shell linked to but 404’d; Mutlu has these, so you can get em when the time comes





- [ ]  
forcing = change in WS albedo *change in kernel + change in BS albedo* change in kernel. but shell’s kernels aren’t separated into WSA and BSA.
Ghimire used a coarse 2.5deg reanalysis dataset that has “share WSA” and “share BSA” for every spot on earth; take shell’s kernels and multiply by those WSA and BSA fractions.
this has 12 months of data, so keep everything monthly


repeat this with ANOTHER set of kernels, the one shell linked to but 404’d; Mutlu has these, so you can get em when the time comes



- forcing = change in WS albedo *change in kernel + change in BS albedo* change in kernel. but shell’s kernels aren’t separated into WSA and BSA.

- Ghimire used a coarse 2.5deg reanalysis dataset that has “share WSA” and “share BSA” for every spot on earth; take shell’s kernels and multiply by those WSA and BSA fractions.
this has 12 months of data, so keep everything monthly



- this has 12 months of data, so keep everything monthly

- repeat this with ANOTHER set of kernels, the one shell linked to but 404’d; Mutlu has these, so you can get em when the time comes

latest meeting:


white-sky modis albedo differences t1 - white-sky modis albedo differences t2


same thing for black-sky MODIS albedo


total sky = white sky = includes atmo effects


clear sky = black sky = removes atmo effects


negative values for all these files means that surface albedo in that area


- maybe a positive absorbs energy

- negative values = more reflection of energy back into space

- get the albedo differences between date1=2000 and date2=2010, just use GEE

- jan 2000 jan 2010, feb 2000 feb 2010

- earlier - later or later - earlier? check ghimire

- use GEE, then mask out the ca. 2000 urban extent

- annemarie might have 2010 extent, i know i can get 2000. ask annemarie for year 2000 again

**Meeting**


- 2030 city extent predictions are 5km res, coarse, is that still valid?
if the RF signal from albedo is totally lost at the global level, you could do it on a smaller scale.
radloff has 2100-growth proj for urban areas in the US only
just concentrate on current cities, see the current spatial variation over the current urban extent



- if the RF signal from albedo is totally lost at the global level, you could do it on a smaller scale.

- radloff has 2100-growth proj for urban areas in the US only

- just concentrate on current cities, see the current spatial variation over the current urban extent

- also my solar radiation data is 14km res (0.125 deg), so does it matter if I use 1km albedo data instead of 500m? because 1km albedo is already loaded in google earth engine and thats waaay easier
insolation data can be coarse. climatology = you averaged all julys.
500m preferred for mapmaking; can you email simon *__* to ask if he can ingest 500m?
but you can use the 1km to get the WSA and BSA coefficients as a start, let’s test with that. scale up with 500m.
do even more in GEE: test it on a small area of ca. 2000 extent. one of the climate data sets in GEE has solar radiation, too.


**fuck the SSRD, just use the 3x3 deg kernels**



- insolation data can be coarse. climatology = you averaged all julys.

- 500m preferred for mapmaking; can you email simon *__* to ask if he can ingest 500m?

- but you can use the 1km to get the WSA and BSA coefficients as a start, let’s test with that. scale up with 500m.
do even more in GEE: test it on a small area of ca. 2000 extent. one of the climate data sets in GEE has solar radiation, too.



- do even more in GEE: test it on a small area of ca. 2000 extent. one of the climate data sets in GEE has solar radiation, too.

- **fuck the SSRD, just use the 3x3 deg kernels**

- white and black sky albedo is bewildering me; zhai 2014 used white sky for "Radiative forcing over China due to albedo change caused by land cover change during 1990–2010"
Ghimire 2014, crystal schaaf if the colleague. write barden ghimire, tell him youre trying to calculate some RF, we’re trying to use radia
try kernel approach. they used Shell et al paper; i cant figure out how you derived those from shell. “how do you get those coefficients used in the radiative kernels, Kws and Kbs? are they spatial or constant?” if you get those, you may be able to skip the insolation step.
he sent me to [http://people.oregonstate.edu/~shellk/kernel.html](http://people.oregonstate.edu/~shellk/kernel.html), downloaded CAM kernels (community atmo model),
CDO usage in terminal: /Users/traveler/Applications/CDO/bin/cdo   , also check the documentation
has water vapor, surface temp, CO2, albedo, and planck? what’s planck?


the kernels seem to be in daily steps stedda monthly, likely a mistake. changed with settaxis to monthly.
3x3 deg data, clear sky and cloudy-sky albedo. dunno if its white or black sky tho???
"The unit in the albedo file is wrong. It should be w/m^2/(0.01 increase in fractional albedo). That is, the kernel corresponds to an increase of 0.01 in the albedo (though it maxes out a 1)."
Shell sez:
CAM3_albedo_sw_kernel.nc and CAM3_albedo_sw_clr_kernel.nc are effects of surface albedo on total-sky and clear-sky albedos
and each includes both diffuse and direct effects (black and white sky, shortwave and longwave)


**just download 2000-2010 BS and WS albedo, 1km data on GEE, do jan 2010-jan 2000, feb 2010-feb 2000 etc, mask over with ca. 2001 urban extents**




PV paper assumes a constant “shortwave radiation absorbed by atmo;” we think shell et al 2008 and thus ghimire 2014 had a spatially-varying term.
if this goes nowhere, THEN continue with ECMWF data.



- Ghimire 2014, crystal schaaf if the colleague. write barden ghimire, tell him youre trying to calculate some RF, we’re trying to use radia

- try kernel approach. they used Shell et al paper; i cant figure out how you derived those from shell. “how do you get those coefficients used in the radiative kernels, Kws and Kbs? are they spatial or constant?” if you get those, you may be able to skip the insolation step.
he sent me to [http://people.oregonstate.edu/~shellk/kernel.html](http://people.oregonstate.edu/~shellk/kernel.html), downloaded CAM kernels (community atmo model),
CDO usage in terminal: /Users/traveler/Applications/CDO/bin/cdo   , also check the documentation
has water vapor, surface temp, CO2, albedo, and planck? what’s planck?


the kernels seem to be in daily steps stedda monthly, likely a mistake. changed with settaxis to monthly.
3x3 deg data, clear sky and cloudy-sky albedo. dunno if its white or black sky tho???
"The unit in the albedo file is wrong. It should be w/m^2/(0.01 increase in fractional albedo). That is, the kernel corresponds to an increase of 0.01 in the albedo (though it maxes out a 1)."
Shell sez:
CAM3_albedo_sw_kernel.nc and CAM3_albedo_sw_clr_kernel.nc are effects of surface albedo on total-sky and clear-sky albedos
and each includes both diffuse and direct effects (black and white sky, shortwave and longwave)


**just download 2000-2010 BS and WS albedo, 1km data on GEE, do jan 2010-jan 2000, feb 2010-feb 2000 etc, mask over with ca. 2001 urban extents**





- he sent me to [http://people.oregonstate.edu/~shellk/kernel.html](http://people.oregonstate.edu/~shellk/kernel.html), downloaded CAM kernels (community atmo model),
CDO usage in terminal: /Users/traveler/Applications/CDO/bin/cdo   , also check the documentation
has water vapor, surface temp, CO2, albedo, and planck? what’s planck?


the kernels seem to be in daily steps stedda monthly, likely a mistake. changed with settaxis to monthly.
3x3 deg data, clear sky and cloudy-sky albedo. dunno if its white or black sky tho???
"The unit in the albedo file is wrong. It should be w/m^2/(0.01 increase in fractional albedo). That is, the kernel corresponds to an increase of 0.01 in the albedo (though it maxes out a 1)."
Shell sez:
CAM3_albedo_sw_kernel.nc and CAM3_albedo_sw_clr_kernel.nc are effects of surface albedo on total-sky and clear-sky albedos
and each includes both diffuse and direct effects (black and white sky, shortwave and longwave)


**just download 2000-2010 BS and WS albedo, 1km data on GEE, do jan 2010-jan 2000, feb 2010-feb 2000 etc, mask over with ca. 2001 urban extents**



- CDO usage in terminal: /Users/traveler/Applications/CDO/bin/cdo   , also check the documentation
has water vapor, surface temp, CO2, albedo, and planck? what’s planck?



- has water vapor, surface temp, CO2, albedo, and planck? what’s planck?

- the kernels seem to be in daily steps stedda monthly, likely a mistake. changed with settaxis to monthly.

- 3x3 deg data, clear sky and cloudy-sky albedo. dunno if its white or black sky tho???

- "The unit in the albedo file is wrong. It should be w/m^2/(0.01 increase in fractional albedo). That is, the kernel corresponds to an increase of 0.01 in the albedo (though it maxes out a 1)."

- Shell sez:
CAM3_albedo_sw_kernel.nc and CAM3_albedo_sw_clr_kernel.nc are effects of surface albedo on total-sky and clear-sky albedos
and each includes both diffuse and direct effects (black and white sky, shortwave and longwave)



- CAM3_albedo_sw_kernel.nc and CAM3_albedo_sw_clr_kernel.nc are effects of surface albedo on total-sky and clear-sky albedos

- and each includes both diffuse and direct effects (black and white sky, shortwave and longwave)

- **just download 2000-2010 BS and WS albedo, 1km data on GEE, do jan 2010-jan 2000, feb 2010-feb 2000 etc, mask over with ca. 2001 urban extents**

- PV paper assumes a constant “shortwave radiation absorbed by atmo;” we think shell et al 2008 and thus ghimire 2014 had a spatially-varying term.

- if this goes nowhere, THEN continue with ECMWF data.

- *let’s make this work over one pixel. 2000 albedo is .1, 2010 albedo is .5, what’s the RF change? if we can get the equation to work, then we can scale it up.*
[ ]  
global urban now
global urban then
expansion of forcing data





- [ ]  
global urban now
global urban then
expansion of forcing data



- global urban now

- global urban then

- expansion of forcing data

**The plan so far**


- not going to worry about maxent so far: just do the albedo part

- ca. 2000 city extent = 500m **need from annemaries**

- ca. 2030 city extent = 5km **in hand**

- albedo = 500m/1km **can grab manually at 500m, what a drag, or GEE has 1km loaded already**

- radiative kernels = 3deg resolution **coarse as hell**

- SSRD = 0.125 deg/14km at equator. zhai used 0.75 deg, so who cares (0.75 GRIB data is just as much of a pain in the ass as netCDF, so lets go higher res)
take 10 years of MODIS albedo data, average 10 years of june, 10 years of july, etc. Also take std devs of those. End up with 24x global albedo maps.
remember to use floating point data, watch your scaling factors
advice from jeff
GDAL info : will tell you info about netcdf, what’s in there, the size and res and projection. then do another GDAL info on the variables within the netcdf, variable names and stuff.
write GDAL translate command based on that metadata info.
use jeff’s script to convert netCDF to ascii with a matlab script, loop through with python, convert to geotiff and average them. then you have a geotiff for each day and an average.


"White-sky is the bihemispherical reflectance under conditions of isotropic illumination, so it has the angular dependency removed. Black-sky is the directional hemispherical reflectance computed at local solar noon.” [http://modis-atmos.gsfc.nasa.gov/ALBEDO/faq.html](http://modis-atmos.gsfc.nasa.gov/ALBEDO/faq.html)
directional hemispherical reflectance (black-sky albedo) and the bihemispherical reflectance under isotropic illumination (white-sky albedo)


Google Earth Engine Developers is the user group
1 arc minute = 1.8km, 30 arc seconds = 1km, 1 degree = 111km
[http://e4ftl01.cr.usgs.gov/MOTA/](http://e4ftl01.cr.usgs.gov/MOTA/) al MCD43 data in ftp form if you want to get your curl on
[https://lpdaac.usgs.gov/dataset_discovery/modis/modis_products_table](https://lpdaac.usgs.gov/dataset_discovery/modis/modis_products_table) main products table
[https://lpdaac.usgs.gov/dataset_discovery/modis/modis_products_table/mcd43b3](https://lpdaac.usgs.gov/dataset_discovery/modis/modis_products_table/mcd43b3) 1km albedo, zhai used this with the QA flags at [https://lpdaac.usgs.gov/dataset_discovery/modis/modis_products_table/mcd43b2](https://lpdaac.usgs.gov/dataset_discovery/modis/modis_products_table/mcd43b2), which
[https://lpdaac.usgs.gov/dataset_discovery/modis/modis_products_table/mcd43a3](https://lpdaac.usgs.gov/dataset_discovery/modis/modis_products_table/mcd43a3) 500m albedo


[https://www.umb.edu/spectralmass/terra_aqua_modis/v006/mcd43a3_albedo_product](https://www.umb.edu/spectralmass/terra_aqua_modis/v006/mcd43a3_albedo_product) another description
[http://gis.stackexchange.com/questions/39279/mcd43a3-modis-products](http://gis.stackexchange.com/questions/39279/mcd43a3-modis-products) someone else hassling with this data
[http://hdfeos.org/zoo/index_openLPDAAC_Examples.php](http://hdfeos.org/zoo/index_openLPDAAC_Examples.php) process MCD with python and GDAL; try the MCD43C1 example towards the top. guy doing same thing, remember to filter out fill values and convert to float [http://hdfeos.org/forums/showthread.php?t=534](http://hdfeos.org/forums/showthread.php?t=534)
to start modis reproj tool GUI: navigate to folder in downloads in terminal, get into MRT/bin, type ./ModisTool. or just go in the damn folder and click “ModisTool"


insolation
the insolation data used in nemet is 1x1 deg; EWCF SSRD is 0.75 deg GRIB or 0.125 deg netCDF, [http://gewex-srb.larc.nasa.gov](http://gewex-srb.larc.nasa.gov/) gewex SRB/SSE from NASA is 1x1 deg
use step 3, grab both 0 and 12 time periods for anne to average





- take 10 years of MODIS albedo data, average 10 years of june, 10 years of july, etc. Also take std devs of those. End up with 24x global albedo maps.
remember to use floating point data, watch your scaling factors
advice from jeff
GDAL info : will tell you info about netcdf, what’s in there, the size and res and projection. then do another GDAL info on the variables within the netcdf, variable names and stuff.
write GDAL translate command based on that metadata info.
use jeff’s script to convert netCDF to ascii with a matlab script, loop through with python, convert to geotiff and average them. then you have a geotiff for each day and an average.


"White-sky is the bihemispherical reflectance under conditions of isotropic illumination, so it has the angular dependency removed. Black-sky is the directional hemispherical reflectance computed at local solar noon.” [http://modis-atmos.gsfc.nasa.gov/ALBEDO/faq.html](http://modis-atmos.gsfc.nasa.gov/ALBEDO/faq.html)
directional hemispherical reflectance (black-sky albedo) and the bihemispherical reflectance under isotropic illumination (white-sky albedo)


Google Earth Engine Developers is the user group
1 arc minute = 1.8km, 30 arc seconds = 1km, 1 degree = 111km
[http://e4ftl01.cr.usgs.gov/MOTA/](http://e4ftl01.cr.usgs.gov/MOTA/) al MCD43 data in ftp form if you want to get your curl on
[https://lpdaac.usgs.gov/dataset_discovery/modis/modis_products_table](https://lpdaac.usgs.gov/dataset_discovery/modis/modis_products_table) main products table
[https://lpdaac.usgs.gov/dataset_discovery/modis/modis_products_table/mcd43b3](https://lpdaac.usgs.gov/dataset_discovery/modis/modis_products_table/mcd43b3) 1km albedo, zhai used this with the QA flags at [https://lpdaac.usgs.gov/dataset_discovery/modis/modis_products_table/mcd43b2](https://lpdaac.usgs.gov/dataset_discovery/modis/modis_products_table/mcd43b2), which
[https://lpdaac.usgs.gov/dataset_discovery/modis/modis_products_table/mcd43a3](https://lpdaac.usgs.gov/dataset_discovery/modis/modis_products_table/mcd43a3) 500m albedo


[https://www.umb.edu/spectralmass/terra_aqua_modis/v006/mcd43a3_albedo_product](https://www.umb.edu/spectralmass/terra_aqua_modis/v006/mcd43a3_albedo_product) another description
[http://gis.stackexchange.com/questions/39279/mcd43a3-modis-products](http://gis.stackexchange.com/questions/39279/mcd43a3-modis-products) someone else hassling with this data
[http://hdfeos.org/zoo/index_openLPDAAC_Examples.php](http://hdfeos.org/zoo/index_openLPDAAC_Examples.php) process MCD with python and GDAL; try the MCD43C1 example towards the top. guy doing same thing, remember to filter out fill values and convert to float [http://hdfeos.org/forums/showthread.php?t=534](http://hdfeos.org/forums/showthread.php?t=534)
to start modis reproj tool GUI: navigate to folder in downloads in terminal, get into MRT/bin, type ./ModisTool. or just go in the damn folder and click “ModisTool"



- remember to use floating point data, watch your scaling factors

- advice from jeff
GDAL info : will tell you info about netcdf, what’s in there, the size and res and projection. then do another GDAL info on the variables within the netcdf, variable names and stuff.
write GDAL translate command based on that metadata info.
use jeff’s script to convert netCDF to ascii with a matlab script, loop through with python, convert to geotiff and average them. then you have a geotiff for each day and an average.



- GDAL info : will tell you info about netcdf, what’s in there, the size and res and projection. then do another GDAL info on the variables within the netcdf, variable names and stuff.

- write GDAL translate command based on that metadata info.

- use jeff’s script to convert netCDF to ascii with a matlab script, loop through with python, convert to geotiff and average them. then you have a geotiff for each day and an average.

- "White-sky is the bihemispherical reflectance under conditions of isotropic illumination, so it has the angular dependency removed. Black-sky is the directional hemispherical reflectance computed at local solar noon.” [http://modis-atmos.gsfc.nasa.gov/ALBEDO/faq.html](http://modis-atmos.gsfc.nasa.gov/ALBEDO/faq.html)
directional hemispherical reflectance (black-sky albedo) and the bihemispherical reflectance under isotropic illumination (white-sky albedo)



- directional hemispherical reflectance (black-sky albedo) and the bihemispherical reflectance under isotropic illumination (white-sky albedo)

- Google Earth Engine Developers is the user group

- 1 arc minute = 1.8km, 30 arc seconds = 1km, 1 degree = 111km

- [http://e4ftl01.cr.usgs.gov/MOTA/](http://e4ftl01.cr.usgs.gov/MOTA/) al MCD43 data in ftp form if you want to get your curl on

- [https://lpdaac.usgs.gov/dataset_discovery/modis/modis_products_table](https://lpdaac.usgs.gov/dataset_discovery/modis/modis_products_table) main products table
[https://lpdaac.usgs.gov/dataset_discovery/modis/modis_products_table/mcd43b3](https://lpdaac.usgs.gov/dataset_discovery/modis/modis_products_table/mcd43b3) 1km albedo, zhai used this with the QA flags at [https://lpdaac.usgs.gov/dataset_discovery/modis/modis_products_table/mcd43b2](https://lpdaac.usgs.gov/dataset_discovery/modis/modis_products_table/mcd43b2), which
[https://lpdaac.usgs.gov/dataset_discovery/modis/modis_products_table/mcd43a3](https://lpdaac.usgs.gov/dataset_discovery/modis/modis_products_table/mcd43a3) 500m albedo



- [https://lpdaac.usgs.gov/dataset_discovery/modis/modis_products_table/mcd43b3](https://lpdaac.usgs.gov/dataset_discovery/modis/modis_products_table/mcd43b3) 1km albedo, zhai used this with the QA flags at [https://lpdaac.usgs.gov/dataset_discovery/modis/modis_products_table/mcd43b2](https://lpdaac.usgs.gov/dataset_discovery/modis/modis_products_table/mcd43b2), which

- [https://lpdaac.usgs.gov/dataset_discovery/modis/modis_products_table/mcd43a3](https://lpdaac.usgs.gov/dataset_discovery/modis/modis_products_table/mcd43a3) 500m albedo

- [https://www.umb.edu/spectralmass/terra_aqua_modis/v006/mcd43a3_albedo_product](https://www.umb.edu/spectralmass/terra_aqua_modis/v006/mcd43a3_albedo_product) another description

- [http://gis.stackexchange.com/questions/39279/mcd43a3-modis-products](http://gis.stackexchange.com/questions/39279/mcd43a3-modis-products) someone else hassling with this data

- [http://hdfeos.org/zoo/index_openLPDAAC_Examples.php](http://hdfeos.org/zoo/index_openLPDAAC_Examples.php) process MCD with python and GDAL; try the MCD43C1 example towards the top. guy doing same thing, remember to filter out fill values and convert to float [http://hdfeos.org/forums/showthread.php?t=534](http://hdfeos.org/forums/showthread.php?t=534)

- to start modis reproj tool GUI: navigate to folder in downloads in terminal, get into MRT/bin, type ./ModisTool. or just go in the damn folder and click “ModisTool"

- insolation
the insolation data used in nemet is 1x1 deg; EWCF SSRD is 0.75 deg GRIB or 0.125 deg netCDF, [http://gewex-srb.larc.nasa.gov](http://gewex-srb.larc.nasa.gov/) gewex SRB/SSE from NASA is 1x1 deg
use step 3, grab both 0 and 12 time periods for anne to average



- the insolation data used in nemet is 1x1 deg; EWCF SSRD is 0.75 deg GRIB or 0.125 deg netCDF, [http://gewex-srb.larc.nasa.gov](http://gewex-srb.larc.nasa.gov/) gewex SRB/SSE from NASA is 1x1 deg

- use step 3, grab both 0 and 12 time periods for anne to average

- [ ]  
Overlay on top of current urban extent: Schneider’s ca. 2000 map
schneider might have an updated one, he’ll ask
seto/guneralp is at 5km res


Now you have current urban albedos. then take as much SSRD data as you have, do the same thing: 3 junes, 3 augusts, etc, etc. Take means and std. devs.
python time!


Overlay insolation on top of that.
check resolutions of all these


Using your good-as-hell defensible RF equation + your albedo measurements + your insolation, you can get RF. Bam, current RF.
Do all that shit above for guneralp’s 2030 map
there, take the difference, see how much less/more you get. voila!



- Overlay on top of current urban extent: Schneider’s ca. 2000 map
schneider might have an updated one, he’ll ask
seto/guneralp is at 5km res



- schneider might have an updated one, he’ll ask

- seto/guneralp is at 5km res

- Now you have current urban albedos. then take as much SSRD data as you have, do the same thing: 3 junes, 3 augusts, etc, etc. Take means and std. devs.
python time!



- python time!

- Overlay insolation on top of that.
check resolutions of all these



- check resolutions of all these

- Using your good-as-hell defensible RF equation + your albedo measurements + your insolation, you can get RF. Bam, current RF.

- Do all that shit above for guneralp’s 2030 map

- there, take the difference, see how much less/more you get. voila!

**other nuts and bolts**


- committee is mutlu, annemarie, rob or jack williams. ask rob first

- need to gather your committee at some point and show them something good

- For methods: check Zhai 2014, Schwaab 2014

- [http://ibis.colostate.edu/WebContent/WS/ColoradoView/TutorialsDownloads/A_Maxent_Model_v7.pdf](http://ibis.colostate.edu/WebContent/WS/ColoradoView/TutorialsDownloads/A_Maxent_Model_v7.pdf) maxent tutorial, has thresholding and converting ASCII to raster in arcgis

- uhh do i need to care about GDP and pop increases?

- how to restrict MaxEnt output to not go crazy?

- per Allison Thieme: make sure everything’s in ASCII grid, each run gets its own folder cuz MaxEnt tries to grab everything thats in the directory.

- high albedo = more radiation thrown back into the damn emptiness of space

- in Zhai 2014: RF change = negative SSRD * (albedo date 2 - albedo date 1). so a drop in albedo gets you a positive RF, a rise in albedo gets you a negative RF. if you just do it for one date, e. g. [http://www.acs.org/content/acs/en/climatescience/atmosphericwarming/climatsensitivity.html](http://www.acs.org/content/acs/en/climatescience/atmosphericwarming/climatsensitivity.html), you do something different:
ΔF = (1 – α)Save – εσTP^4
α = Earth’s albedo. a higher figure means you destroy more of the Save term, lowering the whole end of that equation
Save = average solar energy flux, 342 W·m–2
ε = effective emissivity of the planetary system
σ = Stefan-Boltzmann constant
TP = average planetary surface temperature.
If ΔF is zero, the energies are balanced, no warming or cooling.

- And according to: [http://my.net-link.net/~malexan/Climate-Model.htmInsolation](http://my.net-link.net/~malexan/Climate-Model.htmInsolation) (energy absorbed at earth’s surface) = 1/4 *solar constant* (1 - albedo)
solar constant = 1370 watts per square meter, which is hella much more than SSRD, so what gives?

- have SSRD netCDF data
get it for a full day: synoptic monthly means, time 0 and 12, add them together for each month"you can calculate the monthly means of daily forecast accumulations (for step 12) by adding together the synoptic monthly means at time 00, step 12 and time 12, step 12."
process to 3-year average of all that monthly shit
convert each band to tiff, raster calculator works, but you get negative values. how to relate the two I have no idea



1. get it for a full day: synoptic monthly means, time 0 and 12, add them together for each month"you can calculate the monthly means of daily forecast accumulations (for step 12) by adding together the synoptic monthly means at time 00, step 12 and time 12, step 12."

1. process to 3-year average of all that monthly shit

1. convert each band to tiff, raster calculator works, but you get negative values. how to relate the two I have no idea

- grab albedo data
process to same timeframe



1. process to same timeframe

- extract ca. 2000 urban extents

- use that as a mask on albedo and SSRD

- there, RF for 2000.

Calculating 1/2001 to 12/2002 mean SSRD:


("netcdf-atls00-a562cefde8a29a7288fa0b8b7f9413f7-PYotfi@1"+ "netcdf-atls00-a562cefde8a29a7288fa0b8b7f9413f7-PYotfi@2"+ "netcdf-atls00-a562cefde8a29a7288fa0b8b7f9413f7-PYotfi@3"+ "netcdf-atls00-a562cefde8a29a7288fa0b8b7f9413f7-PYotfi@4"+ "netcdf-atls00-a562cefde8a29a7288fa0b8b7f9413f7-PYotfi@5"+ "netcdf-atls00-a562cefde8a29a7288fa0b8b7f9413f7-PYotfi@6"+ "netcdf-atls00-a562cefde8a29a7288fa0b8b7f9413f7-PYotfi@7"+ "netcdf-atls00-a562cefde8a29a7288fa0b8b7f9413f7-PYotfi@8"+ "netcdf-atls00-a562cefde8a29a7288fa0b8b7f9413f7-PYotfi@9"+ " netcdf-atls00-a562cefde8a29a7288fa0b8b7f9413f7-PYotfi@10"+ "netcdf-atls00-a562cefde8a29a7288fa0b8b7f9413f7-PYotfi@11"+ "netcdf-atls00-a562cefde8a29a7288fa0b8b7f9413f7-PYotfi@12"+ "netcdf-atls00-a562cefde8a29a7288fa0b8b7f9413f7-PYotfi@13"+ "netcdf-atls00-a562cefde8a29a7288fa0b8b7f9413f7-PYotfi@14"+ "netcdf-atls00-a562cefde8a29a7288fa0b8b7f9413f7-PYotfi@15"+ "netcdf-atls00-a562cefde8a29a7288fa0b8b7f9413f7-PYotfi@16"+ "netcdf-atls00-a562cefde8a29a7288fa0b8b7f9413f7-PYotfi@17"+ "netcdf-atls00-a562cefde8a29a7288fa0b8b7f9413f7-PYotfi@18"+ "netcdf-atls00-a562cefde8a29a7288fa0b8b7f9413f7-PYotfi@19"+ "netcdf-atls00-a562cefde8a29a7288fa0b8b7f9413f7-PYotfi@21"+ "netcdf-atls00-a562cefde8a29a7288fa0b8b7f9413f7-PYotfi@22"+ "netcdf-atls00-a562cefde8a29a7288fa0b8b7f9413f7-PYotfi@23"+ "netcdf-atls00-a562cefde8a29a7288fa0b8b7f9413f7-PYotfi@24"+ "netcdf-atls00-a562cefde8a29a7288fa0b8b7f9413f7-PYotfi@25"+ "netcdf-atls00-a562cefde8a29a7288fa0b8b7f9413f7-PYotfi@26"+ "netcdf-atls00-a562cefde8a29a7288fa0b8b7f9413f7-PYotfi@27"+ "netcdf-atls00-a562cefde8a29a7288fa0b8b7f9413f7-PYotfi@28"+ "netcdf-atls00-a562cefde8a29a7288fa0b8b7f9413f7-PYotfi@29"+ "netcdf-atls00-a562cefde8a29a7288fa0b8b7f9413f7-PYotfi@30"+ "netcdf-atls00-a562cefde8a29a7288fa0b8b7f9413f7-PYotfi@31"+ "netcdf-atls00-a562cefde8a29a7288fa0b8b7f9413f7-PYotfi@32"+ "netcdf-atls00-a562cefde8a29a7288fa0b8b7f9413f7-PYotfi@33"+ "netcdf-atls00-a562cefde8a29a7288fa0b8b7f9413f7-PYotfi@34"+ "netcdf-atls00-a562cefde8a29a7288fa0b8b7f9413f7-PYotfi@35"+ "netcdf-atls00-a562cefde8a29a7288fa0b8b7f9413f7-PYotfi@36") / 36


- **NOTES FROM MUTLU***

- for MaxEnt: masking is important, try it on ONE urban area first, like in the uS before you go around the whole damn world.

- for RF calc: you dont need a climate model or any of that shit; you’re only interested in incoming solar radiation for that pixel; january, feb, same temporal span as your albedo MODIS, perturbed by a random value so you get variacne in there; cloudy, sunny, anything in between. use SSRD: Zhai 2014 used european SSRD [http://apps.ecmwf.int/datasets/data/interim-full-daily/](http://apps.ecmwf.int/datasets/data/interim-full-daily/) doesnt need insanely high temporal res or land-air-water interactions.

- Measure the albedo-linked RF from existing global urban areas; this is a GIS and modeling operation, basically.

- [ ]  
Download current albedo data: both Aqua + Terra Albedo 16-Day L3 Global 0.05Deg Climate Model Grid, 1/2000 to 1/2000, monthly data, processed to a 3-year average using both white sky albedo (includes contributions from atmospheric scattering) and black sky albedo (excludes those)
Apply over 2010 urban extent data: any MODIS albedo pixel that isn’t over one of these pixels aint an urban albedo value and can be discarded
converting this albedo to radiative forcing, now that’s a challenge. That involves a radiation and atmospheric model like Goddard Earth Observing System Model, Version 5, which incorporates incoming radiation + weather + land cover that you give it. An alternative would be to use “radiative kernels,” but I’ve read three descriptions and skimmed two papers and still couldn’t tell you exactly what it is.



- Download current albedo data: both Aqua + Terra Albedo 16-Day L3 Global 0.05Deg Climate Model Grid, 1/2000 to 1/2000, monthly data, processed to a 3-year average using both white sky albedo (includes contributions from atmospheric scattering) and black sky albedo (excludes those)

- Apply over 2010 urban extent data: any MODIS albedo pixel that isn’t over one of these pixels aint an urban albedo value and can be discarded

- converting this albedo to radiative forcing, now that’s a challenge. That involves a radiation and atmospheric model like Goddard Earth Observing System Model, Version 5, which incorporates incoming radiation + weather + land cover that you give it. An alternative would be to use “radiative kernels,” but I’ve read three descriptions and skimmed two papers and still couldn’t tell you exactly what it is.

- 

- Adapt the MaxEnt SDM to predict future urban expansion out to 2030 over a limited, area and if that works, extend it to the world. I don’t know how to get it to 2030 specifically, this is only a “potential” map.
Gather spatial data



- Gather spatial data

- [ ]  
[ ]  
Try it globally: used inputs from current gold standard, seto et al 2012
Current city extent: 2010 500m MODIS global urban land cover, Schneider et al 2014
Land cover: here’s water, where cities cant go, 500m global MODIS land cover
Population density over every damn inch of the world: Gridded Population of the World, version 3 (GPWv3), 2010, 5km res
Elevation and slope, because cities cant climb mountains, use to make a mask of where they cant go (big elevation differential between cells, threshold tbd): 90m Shuttle Radar Topography Mission Digital Elevation Model and 1km Global Land One-kilometer Base Elevation (GLOBE) Digital Elevation Model
Roads: VMAP0 from NGA, 1:1m scale


Try it regionally
Here’s where cities are now: % impervious USGS, 100% impervious as threshold
Land cover: NLCD 2011 land cover, here’s water, where cities cant go, 30m res
Population density: U.S. Census Grid, 2000 population, 1km res by Center for International Earth Science Information Network
Elevation and slope: NED 10m/ 1/3 arc second DEM
Roads: TIGER/LINE from U.S. census bureau




Feed into MaxEnt
Convert all city raster points to single lat/longs, which isn’t hard
Convert all “predictors”, the inputs, into .asc grid format
Mask out areas that have absurd elevation differences
Restrict outputs to contiguous pixels, since cities cant leapfrog. Do this before or after, preferably before but I’ll have to figure out how to do that
Threshold it to only output where its like 99.999% sure it can go because I’ve seen the outputs and they can get kinda, uh, generous
Might have to learn some simple scripting to get this to run multiple times without pointy clicky





- [ ]  
Try it globally: used inputs from current gold standard, seto et al 2012
Current city extent: 2010 500m MODIS global urban land cover, Schneider et al 2014
Land cover: here’s water, where cities cant go, 500m global MODIS land cover
Population density over every damn inch of the world: Gridded Population of the World, version 3 (GPWv3), 2010, 5km res
Elevation and slope, because cities cant climb mountains, use to make a mask of where they cant go (big elevation differential between cells, threshold tbd): 90m Shuttle Radar Topography Mission Digital Elevation Model and 1km Global Land One-kilometer Base Elevation (GLOBE) Digital Elevation Model
Roads: VMAP0 from NGA, 1:1m scale


Try it regionally
Here’s where cities are now: % impervious USGS, 100% impervious as threshold
Land cover: NLCD 2011 land cover, here’s water, where cities cant go, 30m res
Population density: U.S. Census Grid, 2000 population, 1km res by Center for International Earth Science Information Network
Elevation and slope: NED 10m/ 1/3 arc second DEM
Roads: TIGER/LINE from U.S. census bureau





- Try it globally: used inputs from current gold standard, seto et al 2012
Current city extent: 2010 500m MODIS global urban land cover, Schneider et al 2014
Land cover: here’s water, where cities cant go, 500m global MODIS land cover
Population density over every damn inch of the world: Gridded Population of the World, version 3 (GPWv3), 2010, 5km res
Elevation and slope, because cities cant climb mountains, use to make a mask of where they cant go (big elevation differential between cells, threshold tbd): 90m Shuttle Radar Topography Mission Digital Elevation Model and 1km Global Land One-kilometer Base Elevation (GLOBE) Digital Elevation Model
Roads: VMAP0 from NGA, 1:1m scale



1. Current city extent: 2010 500m MODIS global urban land cover, Schneider et al 2014

1. Land cover: here’s water, where cities cant go, 500m global MODIS land cover

1. Population density over every damn inch of the world: Gridded Population of the World, version 3 (GPWv3), 2010, 5km res

1. Elevation and slope, because cities cant climb mountains, use to make a mask of where they cant go (big elevation differential between cells, threshold tbd): 90m Shuttle Radar Topography Mission Digital Elevation Model and 1km Global Land One-kilometer Base Elevation (GLOBE) Digital Elevation Model

1. Roads: VMAP0 from NGA, 1:1m scale

- Try it regionally
Here’s where cities are now: % impervious USGS, 100% impervious as threshold
Land cover: NLCD 2011 land cover, here’s water, where cities cant go, 30m res
Population density: U.S. Census Grid, 2000 population, 1km res by Center for International Earth Science Information Network
Elevation and slope: NED 10m/ 1/3 arc second DEM
Roads: TIGER/LINE from U.S. census bureau



1. Here’s where cities are now: % impervious USGS, 100% impervious as threshold

1. Land cover: NLCD 2011 land cover, here’s water, where cities cant go, 30m res

1. Population density: U.S. Census Grid, 2000 population, 1km res by Center for International Earth Science Information Network

1. Elevation and slope: NED 10m/ 1/3 arc second DEM

1. Roads: TIGER/LINE from U.S. census bureau

- Feed into MaxEnt
Convert all city raster points to single lat/longs, which isn’t hard
Convert all “predictors”, the inputs, into .asc grid format
Mask out areas that have absurd elevation differences
Restrict outputs to contiguous pixels, since cities cant leapfrog. Do this before or after, preferably before but I’ll have to figure out how to do that
Threshold it to only output where its like 99.999% sure it can go because I’ve seen the outputs and they can get kinda, uh, generous
Might have to learn some simple scripting to get this to run multiple times without pointy clicky



- Convert all city raster points to single lat/longs, which isn’t hard

- Convert all “predictors”, the inputs, into .asc grid format

- Mask out areas that have absurd elevation differences

- Restrict outputs to contiguous pixels, since cities cant leapfrog. Do this before or after, preferably before but I’ll have to figure out how to do that

- Threshold it to only output where its like 99.999% sure it can go because I’ve seen the outputs and they can get kinda, uh, generous

- Might have to learn some simple scripting to get this to run multiple times without pointy clicky

- 

- Measure future albedo-linked RF resulting from expansion of global urban areas.
Compare the output to gold standard prediction map, see if its wildly different in degree of expansion
After the U.S. or global maxent output is done, take the tippy-top highest values, overlay over current 2000 urban areas, and do the modeling from step one this map. There, you have new RF values generated from MaxEnt, two firsts man! (lotta uncertainty here; why would the albedo of old be the albedo of the new? density? uhh set that aside)



- Compare the output to gold standard prediction map, see if its wildly different in degree of expansion

- After the U.S. or global maxent output is done, take the tippy-top highest values, overlay over current 2000 urban areas, and do the modeling from step one this map. There, you have new RF values generated from MaxEnt, two firsts man! (lotta uncertainty here; why would the albedo of old be the albedo of the new? density? uhh set that aside)

**Actually writing thesis**


1. Introduction
research question and significance - main goal is RF and albedo feedback. emissions accounted, surface albedo not so much
whast the global impact? water quality, heat island, health effects.
IPCC albedo change RF doesnt include urban areas
local-scale effects with albedo
UHI, health, green roofs and that nonsense




existing work, how this differs. 1-2 sentences on what they did.
what’s the gap in our knowledge (local scale is here, global is missing, and there’s gonna be lots of this)
overview of what I did; this is global, not local, and new methods here.



1. research question and significance - main goal is RF and albedo feedback. emissions accounted, surface albedo not so much
whast the global impact? water quality, heat island, health effects.
IPCC albedo change RF doesnt include urban areas
local-scale effects with albedo
UHI, health, green roofs and that nonsense





1. whast the global impact? water quality, heat island, health effects.

1. IPCC albedo change RF doesnt include urban areas

1. local-scale effects with albedo
UHI, health, green roofs and that nonsense



1. UHI, health, green roofs and that nonsense

1. existing work, how this differs. 1-2 sentences on what they did.

1. what’s the gap in our knowledge (local scale is here, global is missing, and there’s gonna be lots of this)

1. overview of what I did; this is global, not local, and new methods here.

1. Literature review
anthropogenic surface albedo change
ghimire and soden


albedo change and RF
albedo change as remedy
Gao - MODIS albedo product did it at 0.05



1. anthropogenic surface albedo change
ghimire and soden



1. ghimire and soden

1. albedo change and RF

1. albedo change as remedy

1. Gao - MODIS albedo product did it at 0.05

1. Methods
Data - describe each one.
took seto and guneralp, schneider 2001, reprojected both to WGS84
the albedo dataset; describe its provenance and how they did it


methodology
have the flow chart


science behind calculation



1. Data - describe each one.
took seto and guneralp, schneider 2001, reprojected both to WGS84
the albedo dataset; describe its provenance and how they did it



1. took seto and guneralp, schneider 2001, reprojected both to WGS84

1. the albedo dataset; describe its provenance and how they did it

1. methodology
have the flow chart



1. have the flow chart

1. science behind calculation

1. Results

1. Discussion

1. Conclusion

1. Works cited
