package com.example.googlemap;

public class PointOfView {
	private String _title;
	private String _comment;
	private Integer _type;
	private Double _latitude;
	private Double _longitude;
	
	public int getType()
	{
		return _type;
	}

	public void setType(String str)
	{
		 if (str.equals("Point of Interest"))
			_type = 0;
		 else if (str.equals("Point of View"))
			_type = 1;
		 else if (str.equals("Source"))
			_type = 2;
		 else if (str.equals("Watertap"))
			_type = 3;
		 else if (str.equals("Pass"))
			_type = 4;
		 else if (str.equals("Summit"))
			_type = 5;
		 else if (str.equals("Parking"))
			_type = 6;
		 else
			 _type = 0;
	}

		 
	public String getTitle()
	{
		return _title;
	}
	public void setTitle(String title)
	{
		_title = title;
	}
	
	public String getComment()
	{
		return _comment;
	}
	public void setComment(String comment)
	{
		_comment = comment;
	}
	
	public Double getLatitude()
	{
		return _latitude;
	}
	public void setLatitude(Double latitude)
	{
		_latitude = latitude;
	}
	
	public Double getLongitude()
	{
		return _longitude;
	}
	public void setLongitude(Double longitude)
	{
		_longitude = longitude;
	}
}
