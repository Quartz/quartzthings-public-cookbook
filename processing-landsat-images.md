# Creating your first satellite image

This tutorial shows you how to find, download, combine, and turn data captured by Landsat 8 into ready-for-publication images. You'll learn three ways to do this by using point and click tools, command line and Google Earth Engine.

[Best tutorial on using photoshop to process Landsat](https://earthobservatory.nasa.gov/blogs/elegantfigures/2013/10/22/how-to-make-a-true-color-landsat-8-image/)

[Best tutorial on using landsat util to process Landsat](https://www.developmentseed.org/blog/2014/08/29/landsat-util/)

[Best rundown of using satellites for journalism](https://gist.github.com/briantjacobs/ae5510ca84ef172b2f5f)

## First things first

You'll need:
* [Landsat Util](https://pythonhosted.org/landsat-util/installation.html)
* Photoshop

## Where does this data come from

These tools provide various ways to download Landsat scenes. I think Libra is the easiest to use.

* [Libra from Development Seed](https://libra.developmentseed.org)
* [Landsat Util](https://pythonhosted.org/landsat-util/)
* [Earth Explorer](https://earthexplorer.usgs.gov/)

## Point and click with photoshop

1. Open the three images in photoshop
  * You want the X_B2.tif X_B3.tif and X_B4.tif files 

2. Open the channels panel

3. Click the menu button on that panel and select "Merge Channels..."

4. Select "RGB Color" from mode, and keep channels at 3, click okay

5. Specify your channels 
  * Red: X_B4.tif
  * Green: X_B3.tif
  * Blue: X_B2.tif

  Click OK

6. Your image is really dark. Lighten it up by going to `Image > Adjustments > Levels`
  take the white carrot and drag it to the edge of the histogram, click okay

7. Open the layers panel, create a new Curves adjustment layer by clicking the half-filled circle button at the bottom of the panel.

8. Zoom to something that looks like it's white, click the white eye dropper in the panel, then click the white area perhaps a cloud or building roof.

9. In panel, select each channel from the RGB drop down, and drag the black carrot for each to the point on the histogram where the curve gets steep.

10. Switch back to the RGB view in the histogram and pull the middle of the white line up

Using this method will remove all of the geographic metadata from your image. [Here is a way to get it back](https://gis.stackexchange.com/a/108703) using the command line tool GDAL.

## On the command line with landsat-util

1. Open up the command line and navigate to the location that contains the folder of landsat images. (you want to be in the directory that contains the folder, not inside the folder itself)

2. run `landsat process [LANDSAT_ID] --pansharpen --bands 432` replacing LANDSAT_ID with your scene's id for instance: `landsat process LC08_L1TP_041036_20190122_20190122_01_RT --pansharpen --bands 432`

3. the output tells you where your file is located typically in your home directory inside of a folder at `landsat/processed/{landsat ID}`


## Using Google Earth Engine

1. Navigate to https://code.earthengine.google.com/

2. Create a new script

3. Pick a point you want to focus on by clicking on the map

4. Define your parameters

```javascript
var o = {
  start: ee.Date('2013-01-01'),
  finish: ee.Date('2019-03-09'),
  target: geometry,
  cloud_cover_lt: 0.8,
  bands:["B4", "B3", "B2"]
}
```

5. Load all of the landsat scenes

```javascript
var filteredCollection = ee.ImageCollection("LANDSAT/LC08/C01/T1_RT")
```

6. Filter to the one that is over your point

```javascript
var filteredCollection = ee.ImageCollection("LANDSAT/LC08/C01/T1_RT")
  .filterBounds(o.target)

```


7. Limit to those that have low cloud coverage

```javascript
var filteredCollection = ee.ImageCollection("LANDSAT/LC08/C01/T1_RT")
  .filterBounds(o.target)
  .filterMetadata("CLOUD_COVER", "less_than", o.cloud_cover_lt)
```

8. Limit to captures of during daylight

```javascript
var filteredCollection = ee.ImageCollection("LANDSAT/LC08/C01/T1_RT")
  .filterBounds(o.target)
  .filterMetadata("CLOUD_COVER", "less_than", o.cloud_cover_lt)
  .filterMetadata("SUN_ELEVATION", "greater_than", 0)
```

**Code Check** 
Right now your script should look like this
```javascript
var o = {
  start: ee.Date('2013-01-01'),
  finish: ee.Date('2019-03-09'),
  target: geometry,
  cloud_cover_lt: 0.8,
  bands:["B4", "B3", "B2"]
}

var filteredCollection = ee.ImageCollection("LANDSAT/LC08/C01/T1_RT")
  .filterBounds(o.target)
  .filterMetadata("CLOUD_COVER", "less_than", o.cloud_cover_lt)
  .filterMetadata("SUN_ELEVATION", "greater_than", 0)
```

**Okay back to it...** 

9. Pick the most recent scene of your collection

```javascript
var scene = ee.Image(filteredCollection.sort("DATE_ACQUIRED", false).first());
```

10. Set your parameters based on the data

You can do it this way by manually defining the extent of your data

```javascript
var params = {
  bands: o.bands,
  max: [10000,10000,10000],
  min: [1000,1000,1000]
}

```


More complexly you can try to do it automatically by programatically calculating the extent of the data in your target area

```javascript
var bandMax = filteredCollection.median()
    .reduceRegion({
      geometry: o.target,
      reducer: ee.Reducer.percentile([99]),
      scale: 60,
      tileScale: 16
    })
    
  var bandMin = filteredCollection.median()
    .reduceRegion({
      geometry: o.target,
      reducer: ee.Reducer.percentile([1]),
      scale: 60,
      tileScale: 16
    })


var params = {
  bands: o.bands,
  max: bandMax.values(o.bands).getInfo(),
  min: bandMin.values(o.bands).getInfo()
}

```

11. Plot your scene in the environment

```javascript
Map.addLayer(scene, params)
```

12. Save to your google drive as a jpeg

```javascript
var export_image = scene.visualize(params)

Export.image.toDrive({
    image: export_image,
    description: "my_scene_from_nicar",
    scale: 30,
    maxPixels: 240000000000
})
```

13. Click the "Run" button to exicute your code. In the "Tasks" panel clikc "Run" on the item created to begin the image export process.

Exporting images from Earth Engine can be slow. To speed it up, try drawing a shape on the map viewer and using it to crop with. Then update the export section to look a like this.

```javascript
var export_image = scene.visualize(params)

Export.image.toDrive({
    image: export_image,
    description: "my_scene_from_nicar",
    scale: 30,
    region: geometry, #make sure this matches the name of whatever shape you drew 
    maxPixels: 240000000000
})
```


## Now what?

These are some stories that have used Landsat imagery to various ends. Some simply make use of true-color images like we made here. Some combine bands that capture reflections that are invisible to humans to detect vegetation health or highlight land use.

* [The island Bangladesh is thinking of putting refugees on is hardly an island at all](https://qz.com/1075444/the-island-bangladesh-is-thinking-of-putting-refugees-is-hardly-an-island-at-all/) by Quartz
* [Who is the Wet Prince of Bel Air? Here are the likely culprits](https://www.revealnews.org/article/who-is-the-wet-prince-of-bel-air-here-are-the-likely-culprits/) by Reveal
* [Welcome to Fabulous Las Vegas: While supplies last](https://projects.propublica.org/las-vegas-growth-map/) by Propublica
* [A Rogue State Along Two Rivers](https://www.nytimes.com/interactive/2014/07/03/world/middleeast/syria-iraq-isis-rogue-state-along-two-rivers.html) by The New York Times

**[Sign Up for the Space Journos Slack](https://join.slack.com/t/space-journos/shared_invite/enQtNTcxMjkxMDA2Mjc0LWE3OGRkYTlkN2E5OWEyYTVmZmY0YTBjY2I2OGNjMjc1NGRmNTI2NGFkYjExMGI2ZjVmNmEyYzllOTAxNzczNDk)**

## Two Resources during breaking news events
[Digital Globe's Open Data](http://www.digitalglobe.com/opendata)
[Planet Disaster Data](https://www.planet.com/disasterdata/)

