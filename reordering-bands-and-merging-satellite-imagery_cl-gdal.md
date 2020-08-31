#  Reordering bands and merging satellite imagery
Satellite imagery data is not necessarily RGB when you get it. Depending on the type of end product you want (true color, NIR, etc), you'll need to re-order the bands accordingly.
## Pre-requisites
There are a few assumptions for this guide:
- GDAL (if you ran [`things_setup.sh`](https://github.com/Quartz/how-we-make-things/blob/master/things_setup.sh) or via `brew install gdal`)
- GeoTIFF files you'd like to use for this process.
## Reorder bands
Satellite's capture data across discrete spectral bands. For our purposes, it helps to think of these bands as visible and non-visible wavelengths. When visualizing satellite data we're confined to only showing three bands at a time. Whatever the bands we want to use, they need to be rendered out to: Red, blue, green (RGB).

As a general rule of thumb, most instruments (say Landsat) order their bands from shortest to longest wavelengths. That means that the Landsat 8 three visible bands are: Blue, green, and red (BGR). To have them to be human readable when rendered in a browser or Photoshop, you'll need to flip the order from BGR to RGB.

We can do that with the command line program `gdal_translate` ([docs](https://gdal.org/programs/gdal_translate.html)).

```
gdal_translate your_sat_image.tif output.tif 
    -b 3 -b 2 -b 1 
    -co COMPRESS=DEFLATE -co PHOTOMETRIC=RGB
```

The `-b` flag represents our bands. The integer after is the destination of that band... so the first band (B) is going to the third position which would be B in RGB. We're really just swapping the position of the first and third band so it goes from BGR to RGB.

Those last two flags are "creation options" you can read more about them here. One is a type of creation, the other insures that our output file is in RGB color mode.

For a bunch of files, you can port this code into `python` or you can run a for loop in `shell`. 

Place all your imagery in a folder. Inside that folder run:

```
mkdir output
for tif in *.tif
do
    gdal_translate $tif output/output_$tif 
        -b 3 -b 2 -b 1 
        -co COMPRESS=DEFLATE -co PHOTOMETRIC=RGB
done
```

You should now have a folder full of reordered band imagery! 

### Futher reading
You don't just have to make RGB imagery! You can make what's called false-colored imagery as well... these types of images help us visualize environmental changes.

* Our very own David Yanofsky contrasting urban environment against vegetation in this [Hurricane Harvey example](https://qz.com/1064364/hurricane-harvey-houstons-flooding-made-worse-by-unchecked-urban-development-and-wetland-destruction/).
* False-color using the NIR band can also higlight loss or lack of vegetation as seen in [this example](https://qz.com/1461195/did-the-woosley-fire-disturb-a-nuclear-waste-site-california-says-no-and-a-group-of-doctors-say-yes/) on a wildfire in California.

## Merging satellite imagery

If you're trying to combine multiple captures of a region from the same collection, you might find GDAL's `gdal_merge` program useful.

You can achieve this simply by running:

```
gdal_merge.py 
    -of GTiff 
    -a_nodata 0
    -o merged_sat_image.tif
    image_1.tif image_2.tif image_3.tif 
    -co PHOTOMETRIC=RGB -co COMPRESS=DEFLATE
```

Most of this should look the same from the reordering bands section with a few exceptions. 

First, we're `-a_nodata` set to zero insures that the alpha masks of the other files are not part of this merge. The result would add black (no data) borders and not a seamless merge of imagery.

Second, we need to state each item we're merging to make the composite image. You'll notice we do this after the `-i` flag, where we list your tifs _ad nauseam_.

The output file will still have black borders, which I'll usually remove in a post-processing tool like Photoshop. In general, I'm handling color correction in that software to begin with, so it doesn't seem like a hassle to remove the borders from the output GeoTiff there.

### Further Reading
* Rob Simmon has an excellent primer on the GDAL programs `merge` and `translate` that you can read [here](https://medium.com/planet-stories/a-gentle-introduction-to-gdal-part-1-a3253eb96082).
* GDAL is written in Python and—as you might assume—[there are bindings](https://pypi.org/project/GDAL/) you can use if you're getting advanced with your usage.