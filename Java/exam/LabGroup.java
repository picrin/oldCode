
import java.util.Scanner;

/** Class to represent a lab group
 */

public class LabGroup  {

	/**
	 * Constructor to set up a lab group by reading from a scanner;
	 */
	public String groupNumber; 
	public TimeSlot timeSlot;
	public LabGroup(Scanner s){
		groupNumber = s.next();
		timeSlot = new TimeSlot(s);
	}


}
