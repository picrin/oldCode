import java.util.Scanner;
import java.util.HashMap;
public class Courses{

	public static void main(String args[]) {
		alltogether();
	}

	public static void alltogether(){
		while (true){
			try{
				String[] data = input("Feed data: ");
				String output = process(data);
				System.out.println(output);
				alltogether();
			} catch (Exception ex){
				System.out.println("Badly formatted input");
				alltogether();
			}
		}
	}
	
	public static String process(String[] data) throws Exception{
		String studentID = data[0];
		String[] courses = new String[data.length - 1];
		System.arraycopy(data, 1, courses , 0, data.length - 1);
		if (courses.length % 3 != 0){
			throw new Exception("every piece of input consists of 3x + 1 pieces of text separated with spaces");
			
		}
		String[][] separateCourses = new String[3][courses.length/3];
		for(int i = 0; i < courses.length; i++){
			separateCourses[i%3][i/3] = courses[i];
		}
		int[][] grades = new int[2][separateCourses[2].length];
		
		double sumOfCredits = 0.0;
		double accumulatedGPA = 0.0;
		for(int i = 0; i < separateCourses[2].length; i++){
			grades[1][i] = grade(separateCourses[2][i]);
			grades[0][i] = new Integer(separateCourses[1][i]);
			sumOfCredits += (double) (grades[0][i]);
			accumulatedGPA += (double) (grades[1][i]*grades[0][i]);
		}
		Double convertedAcc = new Double(accumulatedGPA/sumOfCredits);
		Double convertedSum = new Double(sumOfCredits);
		String GPA = convertedAcc.toString();
		String summama = convertedSum.toString();
		return studentID + " " + summama  + " " + GPA;
	}

	public static int grade(String grade) throws Exception{
		if (grade == "CW") return 0;
		if (grade == "CR") return 0;
		HashMap<String, Integer> lettersDic = new HashMap<String, Integer>();
		String[] lettersList = {"a","b","c","d","e","f","g","h"};
		String[] capitalLetters = {"A", "B", "C", "D", "E", "F", "G", "H"};
		int[] valuesList = {16, 14, 12, 10, 8, 6, 2, 0};
		for (int i = 0; i < lettersList.length; i++){
			lettersDic.put(lettersList[i], valuesList[i]);
			lettersDic.put(capitalLetters[i], valuesList[i]);
		}
		char[] gradeChar = {grade.charAt(0)};
		String gradeCharString = new String(gradeChar);
		
		if (!lettersDic.containsKey(gradeCharString)){
			throw new Exception("every grade starts with a letter in appropriate range");
		}
		
		return lettersDic.get(gradeCharString);
	}

	public static String[] input(String info){
		System.out.println(info);
		Scanner scanner = new Scanner(System.in);
		String[] data = scanner.nextLine().split(" ");
		return data;
	}

}
