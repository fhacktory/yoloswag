package com.example.googlemap;

public class ResumeChecker {
	private static ResumeChecker instance = new ResumeChecker();
	private boolean resumed;
	private boolean background;
	
	private ResumeChecker() {
	}
	
	public static ResumeChecker getInstance() {
		return instance;
	}
	
	public void onActivityStarted() {
		if (background) {
			background = false;
       	}
	}	
	
	public void onActivityResumed() {
		resumed = true;
	}
	
	public void onActivityPaused() {
	    	resumed = false;
	}	
	    
	public void onActivityStopped() {
	 	if (!resumed) {
	 		background = true;
	 	}	
	}	
}
