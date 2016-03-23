package pl.kurkiewicz.adam.FunctionalDNA;
import java.util.Iterator;
import java.util.ArrayList;
import java.util.Collection;
public class KISSDataStructure implements FunctionalDNADataStructure{

	public ArrayList<Integer> getSequence(){
		return this.sequence;
	}
	public KISSDataStructure(){
	}
	
	public void load(Collection<Integer> a_sequence){
		int sequenceSize = a_sequence.size();
		this.sequence = new ArrayList<Integer>(sequenceSize);
		Iterator<Integer> iterator = a_sequence.iterator();
		int currentValue = 0;
		int incrementedValue = 0;
		while (iterator.hasNext()){
			currentValue = iterator.next();
			incrementedValue += currentValue;
			this.getSequence().add(incrementedValue);
		}
	}
	
	public int getBySum(int searchedValue){
		int index = this.binarySearch(0, this.getSequence().size() - 1, searchedValue);
		return this.getByElement(index);
	}

	public int getByElement(int index){
		if (index == 0) return getSequence().get(0);
		else return (this.getSequence().get(index) - this.getSequence().get(index - 1));
	}

	public int binarySearch(int leftBound, int rightBound, int searchedValue){
		if (leftBound >= rightBound) return leftBound;
		int newBound = (leftBound + rightBound)/2;
		if (searchedValue < this.getSequence().get(newBound)){
			return this.binarySearch(leftBound, newBound, searchedValue);
		}
		else{
			return this.binarySearch(newBound + 1, rightBound, searchedValue);
		}
	}

	public void mutate(int toGetBySum, int newValue){
		int maxIndex = this.getSequence().size() - 1;
		int index = this.binarySearch(0, maxIndex, toGetBySum);
		int oldValue = this.getByElement(index);
		int shiftValue = newValue - oldValue;
		while (index != maxIndex + 1){
			this.getSequence().set(index, this.getSequence().get(index) + shiftValue);
			//System.out.println("nextIndex: " + this.getSequence().get(index));
			index++;
		}
	}

	public int totalSum(){
		return this.getSequence().get(this.getSequence().size() - 1);
	}

	public String toString(){
		String returned = new String("[");
		int i;
		for(i = 0; i < this.getSequence().size() - 1; i++){
			returned += this.getByElement(i) + ", ";
		}
		returned += this.getByElement(i) + "]";
		return returned;
	}

	ArrayList<Integer> sequence = null;

	@Override
	public void insertSubsequence(int toGetBySum, Collection<Integer> subsequence) {
		int indexToInsert = this.binarySearch(0, this.getSequence().size() - 1, toGetBySum);
		int value;
		if (indexToInsert == 0) value = 0;
		else value = this.getSequence().get(indexToInsert - 1);
		KISSDataStructure cumulative = new KISSDataStructure();
		cumulative.load(subsequence);
		ArrayList<Integer> toInsert = cumulative.getSequence();
		int cumulativeSum = cumulative.totalSum();
		
		for(int i = indexToInsert; i < this.getSequence().size(); i++){
			int increment = this.getSequence().get(i);
			increment += cumulativeSum;
			this.getSequence().set(i, increment);
		}
		
		for(int i = 0; i < toInsert.size(); i++){
			int element = toInsert.get(i);
			toInsert.set(i, value + element);
		}

		this.getSequence().addAll(indexToInsert, toInsert);
		
	}

}
