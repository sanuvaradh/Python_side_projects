package module3;

import java.awt.Component;
import java.util.ArrayList;
import java.util.List;

//Processing library
import processing.core.PApplet;

//Unfolding libraries
import de.fhpotsdam.unfolding.UnfoldingMap;
import de.fhpotsdam.unfolding.marker.Marker;
import de.fhpotsdam.unfolding.data.PointFeature;
import de.fhpotsdam.unfolding.marker.SimplePointMarker;
import de.fhpotsdam.unfolding.providers.Google;
import de.fhpotsdam.unfolding.providers.MBTilesMapProvider;
import de.fhpotsdam.unfolding.utils.MapUtils;

//Parsing library
import parsing.ParseFeed;

/** EarthquakeCityMap
 * An application with an interactive map displaying earthquake data
 * based on live feed from http://earthquake.usgs.gov
 * Developed as part of 'Object Oriented programming in Java' MOOC from UC SanDiego
 * */
public class EarthquakeCityMap extends PApplet {

	// Loading world map
	private UnfoldingMap map;
	
	//feed with magnitude 1.0+ Earthquakes in the past 7 days
	private String earthquakesURL = "http://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/1.0_week.atom";
	
	public void setup() {
		
	    size(950, 600, OPENGL);		
            map = new UnfoldingMap(this, 200, 50, 700, 500, new Google.GoogleMapProvider());//Set dimensions for map display		
	    map.zoomToLevel(2);
	    MapUtils.createDefaultEventDispatcher(this, map);	
			
	    // List to populate with new SimplePointMarkers
	    List<Marker> markers = new ArrayList<Marker>();

	    //collect properties for each earthquake
	    List<PointFeature> earthquakes = ParseFeed.parseEarthquake(this, earthquakesURL);	    	   
	    for (PointFeature pf:earthquakes)
	    {	    	
	    	map.addMarker(createMarker(pf));// add a marker for this earthquake 	
	    }	    		    	
	    
	}
		
	// Helper method that takes in an earthquake feature and 
	// returns a SimplePointMarker for that earthquake
	private SimplePointMarker createMarker(PointFeature feature)
	{
		
		SimplePointMarker s= new SimplePointMarker(feature.getLocation());
		Object magObj = feature.getProperty("magnitude");
    	        float mag=Float.parseFloat(magObj.toString());
		
    		if(mag<4.0)
    		{
    			s.setColor(color(0,0,255));// color:Blue for low magnitudes
    			s.setRadius(4);// small size marker
    		}
    		else if(mag>5.0)
    		{
    			s.setColor(color(255,0,0));//color Red for High magnitudes
    			s.setRadius(10);// big sized marker
    		}
    		else
    		{
    			s.setColor(color(255,255,0));//color yellow for moderate magnitude
    			s.setRadius(7); // medium sized marker
    		}
    	
		return s;
	}
	
	
	public void draw() 
	{
		background(10);
		map.draw();
	}

}
