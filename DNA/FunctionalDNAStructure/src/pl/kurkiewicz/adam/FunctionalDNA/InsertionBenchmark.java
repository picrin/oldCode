package pl.kurkiewicz.adam.FunctionalDNA;
import java.util.ArrayList;
public class InsertionBenchmark{
	public static void main(String[] args){
		ArrayList<Integer> toLoad = new ArrayList<Integer>(8);
		ArrayList<Integer> subsequence = new ArrayList<Integer>();
		for(Integer value: new Integer[]{3, 9, 8, 4}){
			subsequence.add(value);
		}
		for(Integer value: new Integer[]{7, 2, 8, 1}){
			toLoad.add(value);
		}
		final int insertTo = 8;
		KISSDataStructure kissDS = new KISSDataStructure();
		SophisticatedDataStructure sophDS = new SophisticatedDataStructure();
		
		kissDS.load(toLoad);
		sophDS.load(toLoad);

		System.out.println(kissDS);
		System.out.println(sophDS);

		

		kissDS.insertSubsequence(insertTo, subsequence);
		sophDS.insertSubsequence(insertTo, subsequence);
		System.out.println(kissDS);
		System.out.println(sophDS);
		System.out.println("tusia");
		//sophDS.plusHeap.printInOrder();
		
		/*for(int i = 0; i < kissDS.totalSum(); i++){
			System.out.println(sophDS.getBySum(i));
		}*/
	}
}
