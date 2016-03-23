package pl.kurkiewicz.adam.FunctionalDNA;
import java.util.ArrayList;

public class Test{
	public static <T extends Object> void assertSame(String testName, T o1, T o2){
		if (o1 != o2){
			System.out.println(testName + " fails for " + o1 + ", " + o2);
		}
		return;
	}
	public static <T extends Object> void assertEquals(String testName, T o1, T o2){
		if (o1 == null){
			if (o2 != null){
				System.out.println(testName + " fails for " + o1 + ", " + o2);
			}
		}
		else if (!o1.equals(o2)){
			System.out.println(testName + " fails for " + o1 + ", " + o2);
		}
		return;
	}
	public static PHLeaf getAt(PlusHeap ph, int a_value){
		PHLeaf currentLeaf = ph.getFirstLeaf();
		int value = 0;
		while (value < a_value){
			System.out.println(currentLeaf.toString());
			currentLeaf = currentLeaf.next();
			value += currentLeaf.getValue();
		}
		return currentLeaf;
	}
	public static void main(String[] args){
		PlusHeap ph;
		// Bulk a tree from a leaf and try all operations.
		PHLeaf theLeaf = new PHLeaf(10);
		ArrayList<PHLeaf> gowno = new ArrayList<PHLeaf>();
		gowno.add(theLeaf);
		// TODO -- had to change the constructor... Nothing will work below :(
		/*
		ph = new PlusHeap(gowno);
		assertSame("0 test of assert, first is from constructor", theLeaf, theLeaf);
		assertSame("1 element, first is from constructor", ph.getFirstLeaf(), theLeaf);
		assertSame("1 element, last is from constructor", ph.getLastLeaf(), theLeaf);
		assertSame("1 element, first is last", ph.getFirstLeaf(), ph.getLastLeaf());
		assertSame("1 element, head is from constructor", ph.getHead(), theLeaf);
		assertSame("1 element, get(5) is from constructor", ph.getBySum(5), theLeaf);
		assertSame("1 element, left is null", theLeaf.previous(), null);
		
		
		// Bulk a random tree of thousand elements and try using get. Use a conventional algorithm to compare with
		int heapLeafsSize = 10;
		// int maxSizeOfElement = 100;
		ArrayList<PHLeaf> elements = new ArrayList<PHLeaf>(heapLeafsSize);
		for(int i = 1; i < heapLeafsSize; i++){
			elements.add(new PHLeaf(i));
		}
		ph = new PlusHeap(elements);
		System.out.println(ph.sizeElements());
		
		int dna = 20;// (int) Math.floor(Math.random() * maxSizeOfElement + 1);
		System.out.println(getAt(ph, dna));
		System.out.println(elements);
		System.out.println(ph.getBySum(dna));
		*/
		// Look for common ancestors. Check if every second pair have got a common ancestor one up, every fourth quadrupole a common ancestor two up, etc. Bulk from 2^n leaves!!!
		
		
		/*ArrayList<PHLeaf> al = new ArrayList<PHLeaf>();
		for(int i = 1; i <= 7; i++){
			al.add(new PHLeaf(i));
		}
		PHLeaf left, right;
		AbstractNode yca;
		ph = new PlusHeap(al);
		System.out.println(ph.getHead());
		//left = ph.get(Integer.parseInt(args[0]));
		//right = ph.get(Integer.parseInt(args[1]));
		//System.out.println(left);
		//System.out.println(right);
		//yca = ph.youngestCommonAncestor(left, right);
		//System.out.println(yca);
		System.out.println(ph.getFirstLeaf() + "tusia");
		System.out.println(getAt(ph, dna) + "naive");
		System.out.println(ph.getFirstLeaf() + "tusia");
		System.out.println(ph.get(dna) + "implementation");
		System.out.println(ph.getFirstLeaf() + "tusia");
		*/
	}
}
