package pl.kurkiewicz.adam.FunctionalDNA;
import java.util.Collection;
/*
* A lightweight wrapper around the PlusHeap class, implementing a FunctionalDNA
* interface, which allows to compare the performance across implementations.
*/
class SophisticatedDataStructure implements FunctionalDNADataStructure{
	PlusHeap plusHeap = null;
	public void load(Collection<Integer> a_sequence){
		this.plusHeap = new PlusHeap(a_sequence);
	}
	public int getBySum(int value){
		return this.plusHeap.getBySum(value).getValue();
	}
	public void mutate(int toGetBy, int newValue){
		this.plusHeap.mutate(this.plusHeap.getBySum(toGetBy), newValue);
	}
	public int totalSum(){
		return plusHeap.getTotalSum();
	}
	public String toString(){
		PHLeaf current = this.plusHeap.getFirstLeaf();
		String returned = "[";
		while (current != this.plusHeap.getLastLeaf()){
			returned += Integer.toString(current.getValue()) + ", ";
			current = current.next();
		}
		returned += Integer.toString(current.getValue()) + "]";
		return returned;
	}
	@Override
	public void insertSubsequence(int toGetBySum, Collection<Integer> subsequence) {
		PlusHeap pHSubsequence = new PlusHeap(subsequence);
		this.plusHeap.insertSubsequence(toGetBySum, pHSubsequence.getHead());
		
	}
}
