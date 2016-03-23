import java.util.Scanner;

/** Class to represent a time-slot, expressed as a day
 * together with a starting time and finishing time
 */

public class TimeSlot {
	
	/**
	 * Constructor to set up a time slot by reading from a scanner;
	 */
	public String weekDay;
	public Time startTime;
	public Time endTime;
	public TimeSlot(Scanner s){
		weekDay = s.next();
		String[] l_startTime = s.next().split(":");
		String[] l_endTime = s.next().split(":");
		startTime = new Time(new Integer(l_startTime[0]), new Integer(l_startTime[1]));
		endTime = new Time(new Integer(l_endTime[0]), new Integer(l_endTime[1]));		
	}
	
	public boolean noCollision(TimeSlot otherTimeSlot){
		if (!this.weekDay.equals(otherTimeSlot.weekDay)){
			return true;
		}
		else{
			return (this.endTime.precedesOrEquals(otherTimeSlot.startTime) || otherTimeSlot.endTime.precedesOrEquals(this.startTime));
		}
	}
	
	public String toString(){
		return weekDay + " " + startTime.toString() + endTime.toString();
	}

}
