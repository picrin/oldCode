

import java.util.Scanner;

/** Class to represent times, expressed in hours and minutes */

public class Time {

	private int hour;

	private int minute;

	/**
	 * standard constructor
	 */
	public Time(int h, int m) {
		if (h >= 0 && h < 24 && m >= 0 && m < 60) {
			hour = h;
			minute = m;
		} else {
			System.out.println("Fatal error in time");
			System.exit(0);
		}
	}

	/**
	 * no-parameter constructor
	 */
	public Time() {
		hour = 0;
		minute = 0;
	}

	/**
	 * copy constructor
	 */
	public Time(Time t) {
		hour = t.hour;
		minute = t.minute;
	}

	/**
	 * Constructor to read time from a scanner;
	 * assumes that time is represented in the form hh:mm
	 */
	public Time(Scanner s) {
		s.useDelimiter(":");
		hour = s.nextInt();
		s.skip(":");
		s.reset();
		minute = s.nextInt();
	}

	/* accessors */

	public int getHour() {
		return hour;
	}

	public int getMinute() {
		return minute;
	}

	/* mutators */

	public void setHour(int h) {
		if (h >= 0 && h < 24)
			hour = h;
		else {
			System.out.println("Fatal error in hour");
			System.exit(0);
		}
	}

	public void setMinute(int m) {
		if (m >= 0 && m < 60)
			minute = m;
		else {
			System.out.println("Fatal error in minute");
			System.exit(0);
		}
	}

	/**
	 * check time for validity
	 */
	public boolean isValid() {
		return 0 <= hour && hour < 24 && 0 <= minute && minute < 60;
	}

	/**
	 * determines whether this time precedes time t
	 */
	public boolean precedes(Time t) {
		if (hour < t.hour)
			return true;
		else if (hour > t.hour)
			return false;
		else
			return minute < t.minute;
	}
	
	@Override
	public boolean equals(Object obj) {
	      if (obj == null)
	         return false;
	      else if (getClass() != obj.getClass())
	         return false;
	      else { 
	         Time t = (Time) obj;        // type cast
	         return hour == t.hour && minute == t.minute;
	      }
	   }

	public boolean precedesOrEquals(Time t) {
		return this.precedes(t) || this.equals(t);
	}

	@Override
	public String toString() {
		String s = "";
		if (hour < 10)
			s += "0";
		s += hour + ":";
		if (minute < 10)
			s += "0";
		return s + minute;
	}
}