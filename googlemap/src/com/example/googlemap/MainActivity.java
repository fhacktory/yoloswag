package com.example.googlemap;

import com.google.android.gms.common.ConnectionResult;
import com.google.android.gms.common.GooglePlayServicesUtil;
import com.google.android.gms.maps.CameraUpdateFactory;
import com.google.android.gms.maps.GoogleMap;
import com.google.android.gms.maps.SupportMapFragment;
import com.google.android.gms.maps.model.BitmapDescriptorFactory;
import com.google.android.gms.maps.model.Circle;
import com.google.android.gms.maps.model.CircleOptions;
import com.google.android.gms.maps.model.LatLng;
import com.google.android.gms.maps.model.MarkerOptions;
import com.google.android.gms.maps.model.Polyline;
import com.google.android.gms.maps.model.PolylineOptions;

import android.app.Dialog;
import android.content.Context;
import android.content.pm.ActivityInfo;
import android.content.res.Resources;
import android.graphics.Color;
import android.location.Criteria;
import android.location.Location;
import android.location.LocationListener;
import android.location.LocationManager;
import android.media.Ringtone;
import android.media.RingtoneManager;
import android.net.Uri;
import android.os.AsyncTask;
import android.os.Bundle;
import android.support.v4.app.FragmentActivity;
import android.view.View;
import android.view.View.OnClickListener;
import android.widget.ArrayAdapter;
import android.widget.Button;
import android.widget.EditText;
import android.widget.Spinner;
import android.widget.Toast;

import java.io.IOException;
import java.util.ArrayList;
import java.util.List;

import org.apache.http.HttpEntity;
import org.apache.http.HttpResponse;
import org.apache.http.NameValuePair;
import org.apache.http.client.ClientProtocolException;
import org.apache.http.client.HttpClient;
import org.apache.http.client.entity.UrlEncodedFormEntity;
import org.apache.http.client.methods.HttpPost;
import org.apache.http.impl.client.DefaultHttpClient;
import org.apache.http.message.BasicNameValuePair;
import org.apache.http.util.EntityUtils;
import org.json.JSONArray;
import org.json.JSONException;
import org.json.JSONObject;
 
public class MainActivity extends FragmentActivity  implements LocationListener {

	private GoogleMap		googleMap;
	private LocationManager locationManager;
	private ResumeChecker   resumeChecker;
	private ArrayList<ArrayList<Double>> 	listPos;
	private boolean			saveWay;
	private String			roadName;
	private String			urlPost;
	private String			urlGet;
	private PointOfView		currentPov = new PointOfView();
	
	public void displayText(String str)
	{
		Context context = getApplicationContext();
		CharSequence text = str;
		int duration = Toast.LENGTH_SHORT;

		Toast toast = Toast.makeText(context, text, duration);
		toast.show();
	}
	
	@Override
	protected void onCreate(final Bundle savedInstanceState)
	{
		  super.onCreate(savedInstanceState);
	      setContentView(R.layout.activity_main);
	      
	      saveWay = false;
	      listPos = new ArrayList<ArrayList<Double> >();
	      initButtons();
	      initLocationSystem();
	}
	  
	 private void addLines(LatLng pos1, LatLng pos2) {
		 PolylineOptions rectOptions = new PolylineOptions()
	        .add(pos1)
	        .add(pos2).color(Color.BLUE);
		 Polyline polyline = googleMap.addPolyline(rectOptions);
	 }
	
	private void initButtons()
	{
	    Button next = (Button)findViewById(R.id.PointOfView);
	    next.setBackgroundResource(R.drawable.poi);
	    next = (Button)findViewById(R.id.saveMovesBtn);
	    next.setBackgroundResource(R.drawable.start);

		
		findViewById(R.id.saveMovesBtn).setOnClickListener(clickListener);
		findViewById(R.id.PointOfView).setOnClickListener(clickListener);
	}
	
	private void initLocationSystem()
	{
		setRequestedOrientation(ActivityInfo.SCREEN_ORIENTATION_PORTRAIT);
		resumeChecker = ResumeChecker.getInstance();
	      int status = GooglePlayServicesUtil.isGooglePlayServicesAvailable(getBaseContext());
	      if (status != ConnectionResult.SUCCESS)
	        {
	            int requestCode = 10;
	            Dialog dialog = GooglePlayServicesUtil.getErrorDialog(status, this, requestCode);
	            dialog.show();
	        }
	        else
	        {	
	        	SupportMapFragment fm = (SupportMapFragment) getSupportFragmentManager().findFragmentById(R.id.map);

	            googleMap = fm.getMap();
	            googleMap.setMyLocationEnabled(true);

	            LocationManager locationManager = (LocationManager) getSystemService(LOCATION_SERVICE);
	            Criteria criteria = new Criteria();
	            String provider = locationManager.getBestProvider(criteria, true);
	            Location location = locationManager.getLastKnownLocation(provider);
	            if (location != null)
	            	onLocationChanged(location);
	            locationManager.requestLocationUpdates(provider, 1, 1, this);
	        }
	}
	
	@Override
	public void onLocationChanged(Location location) {
		double latitude = location.getLatitude();
		double longitude = location.getLongitude();
		LatLng latLng = new LatLng(latitude, longitude);
		
		currentPov.setLatitude(latitude);
		currentPov.setLongitude(longitude);
		googleMap.moveCamera(CameraUpdateFactory.newLatLng(latLng));
		googleMap.animateCamera(CameraUpdateFactory.zoomTo(15));
		if (saveWay)
		{
			ArrayList<Double> tmpPos = new ArrayList<Double>();
			tmpPos.add(latitude);
			tmpPos.add(longitude);
			listPos.add(tmpPos);
			for (int i = 0; listPos.size() > 2 && i < listPos.size(); ++i) {
				if (i == listPos.size() - 2)
					addLines(new LatLng(listPos.get(i).get(0), listPos.get(i).get(1)),
							new LatLng(listPos.get(i + 1).get(0), listPos.get(i + 1).get(1)));
			}
		}
	}
      
    //Global On click listener for all views
    final OnClickListener clickListener = new OnClickListener() {
        public void onClick(final View v) {
    		int keycode = v.getId();
    		if (keycode == R.id.saveMovesBtn)
    		{

    			Button btn = (Button)findViewById(R.id.saveMovesBtn);
    		    saveWay = (saveWay == true) ? false : true;
    			if (saveWay)
    				btn.setBackgroundResource(R.drawable.stop);
    			else
    				btn.setBackgroundResource(R.drawable.start);

    			Button povBtn = (Button) findViewById(R.id.PointOfView);    			
    			if (!saveWay)
    			{
    				confirmWithRoadName(v);
    			}
    			else
    			{
        			displayText("Press stop to send your road...");
    			}
    		}
    		else if (keycode == R.id.PointOfView)
    		{
    			createPOV();
    		}
        }
    };

    private void createPOV()
    {
    	Context context = this;	
		final Dialog dialog = new Dialog(context);
		dialog.setTitle("Please complete your P.o.I.");
		dialog.setContentView(R.layout.point_of_view);
		
		Spinner spinner = (Spinner)dialog.findViewById(R.id.povType);
		ArrayAdapter<CharSequence> adapter = ArrayAdapter.createFromResource(this,
				R.array.pov_array, android.R.layout.simple_spinner_item);
		adapter.setDropDownViewResource(android.R.layout.simple_spinner_dropdown_item);		 
		spinner.setAdapter(adapter);

		Button saveBtn = (Button) dialog.findViewById(R.id.savePov);
		Button cancelBtn = (Button) dialog.findViewById(R.id.cancelPov);
		saveBtn.setOnClickListener(new OnClickListener() {
			@Override
			public void onClick(View v) {
				Spinner spinner = (Spinner)dialog.findViewById(R.id.povType);
				String str = spinner.getSelectedItem().toString();

				EditText text = (EditText) dialog.findViewById(R.id.povTitle);
	    		currentPov.setTitle(text.getText().toString());
	    		text = (EditText) dialog.findViewById(R.id.povComment);
	    		currentPov.setComment(text.getText().toString());
	    		if (currentPov.getTitle().length() > 0 && 
	    			currentPov.getComment().length() > 0 &&
	    			currentPov.getLatitude() != null &&
	    			currentPov.getLongitude() != null)
	    		{
	    			currentPov.setType(str);
	    			createCustomMarker(new LatLng(currentPov.getLatitude(), currentPov.getLongitude()),
	    					currentPov.getTitle(), currentPov.getComment());
	    			sendNewPov();
	    			dialog.dismiss();
	    		}
	    		else if (currentPov.getLatitude() == null || currentPov.getLongitude() == null)
	    			displayText("You have not been located yet.");
	    		else
	    			displayText("You have to enter a point of interest name and comment.");
			}
		});
		cancelBtn.setOnClickListener(new OnClickListener() {
			@Override
			public void onClick(View v) {
    			displayText("P.o.I. deleted.");
    			dialog.dismiss();
			}
		});
		dialog.show();
    }
    
    private void createCustomMarker(LatLng latlng, String str, String opt)
    {
    	googleMap.addMarker(new MarkerOptions()
        .position(latlng)
        .title(str + " :" + opt));
    }

    
    private void confirmWithRoadName(final View v) {
		Context context = this;	
		final Dialog dialog = new Dialog(context);
		dialog.setTitle("Please enter road title");
		dialog.setContentView(R.layout.custom_dialog);
		
		Button saveBtn = (Button) dialog.findViewById(R.id.saveRoadTitle);
		Button cancelBtn = (Button) dialog.findViewById(R.id.cancelRoadSave);
		saveBtn.setOnClickListener(new OnClickListener() {
			@Override
			public void onClick(View v) {
	    		EditText text = (EditText) dialog.findViewById(R.id.roadTitle);
	    		if ((roadName = text.getText().toString()).length() > 0)
	    		{
	    			sendNewWay();
		    		dialog.dismiss();
	    		}
	    		else
	    			displayText("You have to enter a road name.");
			}
		});
		cancelBtn.setOnClickListener(new OnClickListener() {
			@Override
			public void onClick(View v) {
    			displayText("Road deleted.");
    			dialog.dismiss();
    			listPos.clear();
			}
		});
		dialog.show();
    }
    
    private void sendNewPov()
    {
		displayText("Sending data...");    			
    	String ret;
    	if ((ret = writeJSONPov()) == null)
    		displayText("You have to save something before sending it");
    	else
    	{
    		urlPost = "http://bi.tk:1337/poi";
    		sendData(ret);
    	}
    	currentPov.setTitle("");
    	currentPov.setComment("");
    }
    
    private void sendNewWay()
	{
		displayText("Sending data...");    			
    	String ret;
    	if ((ret = writeJSONWay()) == null)
    		displayText("You have to save something before sending it");    		
    	else
    	{
    		urlPost = "http://bi.tk:1337/upload";
    		sendData(ret);
    	}
    	listPos.clear();
	}
	
    private void sendData(String jsonString)
    {
    	AsynClassPostTool tool = new AsynClassPostTool();
    	tool.execute(jsonString);
   	} 

    private String writeJSONWay() {
   		try
   		{
   		  JSONObject mainObject = new JSONObject();
   		  mainObject.put("name", roadName);
   		  JSONArray tracksObject = new JSONArray();
 
		  for (int i = 0; i < listPos.size(); i++)
		  {
			  JSONArray posObject = new JSONArray();
			  posObject.put(listPos.get(i).get(0));
			  posObject.put(listPos.get(i).get(1));
			  tracksObject.put(posObject);
		  }
   	      mainObject.put("tracks", tracksObject);
       	  return mainObject.toString();
    	 }
    	 catch (JSONException e)
    	  {
    	  }
   		return null;
    } 

    private String writeJSONPov() {
   		try
   		{
   			JSONObject mainObject = new JSONObject();
   			mainObject.put("title", currentPov.getTitle());
   			mainObject.put("comment", currentPov.getTitle());
 		  
   			JSONArray posObject = new JSONArray();
   			posObject.put(currentPov.getLatitude());
   			posObject.put(currentPov.getLongitude());

   			mainObject.put("position", posObject);
   			mainObject.put("type", currentPov.getType());
   			return mainObject.toString();
    	 }
    	 catch (JSONException e)
    	  {
    	  }
   		return null;
    } 

	public void makeSound()
	{
		try {
			Uri notification = RingtoneManager.getDefaultUri(RingtoneManager.TYPE_NOTIFICATION);
			Ringtone r = RingtoneManager.getRingtone(getApplicationContext(), notification);
			r.play();
		} catch (Exception e) {
			e.printStackTrace();
		}
	}
	public void onWindowFocusChanged(boolean hasFocus)
	{
	}
	
	@Override
	public void onResume()
		{
	      super.onResume();	      
	      locationManager = (LocationManager) this.getSystemService(LOCATION_SERVICE);
	      if(locationManager.isProviderEnabled(LocationManager.GPS_PROVIDER))
	          followGPS();
	      resumeChecker.onActivityResumed();
	  }
	 
	  @Override
	  public void onPause() {
		  //unfollowGPS();
		  super.onPause();
	      resumeChecker.onActivityPaused();
	  }

	  @Override
	  public void onStop() {
		  //unfollowGPS();
		  super.onStop();
	  }

	  @Override
	  public void onDestroy()
	  {
		  unfollowGPS();
		  super.onDestroy();
	  }
	  
	  public void followGPS() {
		  locationManager.requestLocationUpdates(LocationManager.GPS_PROVIDER, 5000, 10, this);
	  }

	  public void unfollowGPS() {
	      locationManager.removeUpdates(this);
	  }

	  @Override
	  public void onProviderDisabled(final String provider) {
//		  if("gps".equals(provider))
//	          unfollowGPS();
	  }

	  @Override
	  public void onProviderEnabled(final String provider) {
	      if("gps".equals(provider))
	          followGPS();
	  }

	  @Override
	  public void onStatusChanged(String provider, int status, Bundle extras) {
			// TODO Auto-generated method stub
			
	  }
	  
	  public class AsynClassPostTool extends AsyncTask<String, Void, Void> {

		    private Exception exception;

		    protected Void doInBackground(String... jsonString) {	
					// Create a new HttpClient and Post Header
					HttpClient httpclient = new DefaultHttpClient();
			        HttpPost httppost = new HttpPost(urlPost);
		 
					try {
						// Add your data
						List<NameValuePair> nameValuePairs = new ArrayList<NameValuePair>();
						nameValuePairs.add(new BasicNameValuePair("json", jsonString[0]));
						httppost.setEntity(new UrlEncodedFormEntity(nameValuePairs));
		 
						 HttpResponse response = httpclient.execute(httppost);						 
					     HttpEntity entity = response.getEntity();
					     String json = EntityUtils.toString(entity);
					} catch (ClientProtocolException e) {
						// TODO Auto-generated catch block
					} catch (IOException e) {
						// TODO Auto-generated catch block
					}
		        Void tmp = null;
		        return tmp;
		    }
		    
		    protected void onPostExecute(){
			}
			protected void onProgressUpdate(){
			}

	}
}