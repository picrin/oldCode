import java.util.Scanner;

/** Class to represent a course, including information on lab groups of the course
 */
public class Course {

	/**
	 * Constructor to set up a course by reading from a scanner;
	 */
	public ArrayList<TimeSlot> groups;
	
	public Course(Scanner s){
		groups = new ArrayList<TimeSlot>();
		
	}
	

}
