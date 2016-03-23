

import java.io.FileInputStream;
import java.io.FileNotFoundException;
import java.util.Scanner;

public class CheckStudents {

	public static void main(String[] args) {

		final String COURSEFILE = "course.txt";
		Scanner courseScanner = null;
		

		try {
			courseScanner = new Scanner(new FileInputStream(COURSEFILE));
		} catch (FileNotFoundException e) {
			System.out.println("Cannot open file " + COURSEFILE);
			System.exit(0);
		}
		
		

		// set up a Course object to contain the course data
		Course course = new Course(courseScanner);
		System.out.println("The course description is: " + course);

		final String STUDENTFILE = "students.txt";
		Scanner studentScanner = null;
		try {
			studentScanner = new Scanner(new FileInputStream(STUDENTFILE));
		} catch (FileNotFoundException e) {
			System.out.println("Cannot open file " + STUDENTFILE);
			System.exit(0);
		}

		// process the students
		while (studentScanner.hasNextLine()){
			String line = studentScanner.nextLine();
			Scanner lineScanner = new Scanner(line);
			Student student = new Student(lineScanner); 
			//System.out.println("The next student is " + student.initString());
			student.checkEligibility(course);
			student.display();
		}

	}
}