# Making a public lands explorer map

[View the map here](https://publiclands.evanapplegate.com) • [Repo](https://github.com/evanapplegate/fed_lands_selloff)

_For 3D view on mobile two-finger drag up and down, for 3D view on desktop two-finger/middle mouse button click and drag. Population data via ORNL LandScan._

I never made interactive maps before machine learning coding tools. It’s now incredibly easy to style your map, add a UI, and deploy it to millions.

Making an attractive slippy map is exponentially harder than styling a jpg. You must design 23 discrete maps, from z0 global to z22 building-level, and each has to look good individually and fit together in transitions. Mapbox and MapLibre are a huge boon: you get fine control over styling and you can even kludge together good lighting for hillshades (Jonni Walker is a [master of this](https://api.mapbox.com/styles/v1/jonniwalker/cm73c1jsw003u01r3b89be4ez.html?title=view&access_token=pk.eyJ1Ijoiam9ubml3YWxrZXIiLCJhIjoiY2loeG82cWplMDA4N3cxa3MzZXU2N2JpYSJ9.H6vPKI0UKLv733mSCXh2Lw&zoomwheel=true&fresh=true#10.87/38.5654/-109.2833/51.8/58)).

Though my editorial mapping days are behind me, the news prompted me to make this map in late June 2025: Senate Republicans [tacked onto the reconciliation bill](https://www.energy.senate.gov/services/files/DF7B7FBE-9866-4B69-8ACA-C661A4F18096) a plan for “mandatory disposal” of 0.5% of western public lands managed by the Forest Service and Bureau of Land Management. 

The goal: let locals manage their neighboring lands and to “address local housing needs.” There are many orphaned BLM/FS parcels adjoining cities in the mountain west that could be put to better use if the municipalities could build on them.

Notwithstanding that the limiting reagent for housing in western states is definitely not access to land (it’s regulation, zoning, and incumbent homeowners), the plan is too blunt an instrument to achieve that goal. 

Getting 0.5% of western public lands off the federal books may be the first step in enclosing a uniquely American commons. Public lands are terra who-gives-a-████. Anyone can hike, camp, off-road, shoot, hunt, fish, maybe get some money out of them through timber and mineral leases. No country today (least of all the U.S.) would set aside massive tracts of beautiful lands for all to enjoy *ad libitum*.

GIS analyst Phil Hartger at [The Wilderness Society](https://www.wilderness.org/articles/media-resources/250-million-acres-public-lands-eligible-sale-senr-bill) subtracted excluded/protected lands from extant FS and BLM admin boundaries, leaving [what could be sold if the plan went through](https://www.dropbox.com/scl/fo/smwyjbbwr9ie5qg3dtuzd/AP10gfeav1spzd-mPAL-k1E?rlkey=q055x4j4kxf29giajlmw11m93&e=1&dl=0). 

He displayed his layers on an ArcGIS Online map, but I’m a [cartographer](https://evanapplegate.com) so I wanted to gild the lily.

## Stack
- IDE: Cursor + Claude 4 Sonnet
- Frontend: HTML/CSS/JS, maps rendered with MapLibre GL JS (an open source alternative to Mapbox GL JS) 
- Map Data: [Protomaps](https://protomaps.com/) PMTiles: these let you serve tiles via range requests from a single file, making tiled maps orders of magnitude cheaper to host.  
- Backend: Node.js + Express
- Deployment: Heroku  

## Data
I wanted these layers on the map:
- All FS lands
- FS lands exposed to sale
- All BLM lands
- BLM lands exposed to sale
- National Forest names
    - I asked Cursor + Claude 4 Sonnet + OGR to convert the above gov- and NGO-supplied shapefiles to geojson, then tippecanoe to convert them to PMTiles.
- Areas where people actually lived (to test the thesis of this plan)
    - I grabbed ORNL LandScan data (1km gridded population estimates for the U.S.), wiped the pixels where fewer then ten people lived, OGR’d the raster into a polygon, ran it through tippecanoe to make PMTiles, then made a little crosshatch PNG to symbolize it.

## Design
I needed a cute basemap so I forked Amy Lee Walton’s [Cali Terrain Mapbox style](https://blog.mapbox.com/mapbox-cali-terrain-style-bea8cd410523), wiped the hillshade, and made it greener (my experience with CA NFs is scrubby and green, and I prefer to remember the green.) I added other Mapbox basemaps (satellite, outdoors, light and dark) in a picker.

One of my favorite things about MapLibre is its ability to render 3D terrain in the browser with WebGL. I pointed it at free AWS Terrarium tiles, added a “pick your z” exaggeration slider, and now you can see the steep parts.

I wanted to use Mapbox GL JS because it offers a beautiful globe projection, but it doesn’t support PMTiles; dealbreaker, my hosting bill would’ve been astronomical if the map got any traction and I wasn’t serving tiles from a flat file.

## Frontend
Thank you Claude for the HTML/CSS/JS, it added layer toggles and menus to let the user pick their fills/strokes/opacities.

## Backend
The PMTiles went into a Cloudflare R2 bucket; no egress fees, which makes hosting this type of thing absurdly cheap.

The whole thing is run on a Node.js + Express server, deployed via Heroku (feels cheap and easy? Is there a better way to do thi?) which set up SSL, pointed it at my subdomain, and it’s done: vector PMTiles + a minimal server + static hosting via Cloudflare = a pretty fast, scalable web map.