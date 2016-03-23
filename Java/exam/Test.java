import java.util.Scanner;
public class Test{
	public static void main(String[] args){
		TimeSlot whatever = new TimeSlot(new Scanner("Mon 14:10 14:20"));
		TimeSlot whatever2 = new TimeSlot(new Scanner("Mon 14:10 15:20"));
		System.out.println(whatever.noCollision(whatever2));
		LabGroup labGroup = new LabGroup(new Scanner("A Mon 14:10 15:20"));
		System.out.println(labGroup.groupNumber.toString() + "---" + labGroup.timeSlot.toString());
	}
}
