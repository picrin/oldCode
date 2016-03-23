package pl.kurkiewicz.adam.FunctionalDNA;
import java.util.ArrayList;
/*
* A class which generates a random stochastic test for given initial number of
* the elements in the sequence, maximum value of an element in the sequence
* and number of mutations (mutate(int toGetBySum, int newValue) as defined by
* FunctionalDNAStructure interface) that should take place one after another.
* 
* The first argument for every subsequent mutatation -- toGetBySum is uniformly
* drawn from the range [0, current sum of all elements oc the sequence].
* 
* The second argument -- newValue is drawn from 1 to maximum value of an
* element. 
*/
public class SerialisedTestCase{
	ArrayList<Integer> sequenceToLoad;
	public int[] mutationPosition;
	public int[] mutationValue;
	public int maxValue;
	public int numberOfElements;
	
	public SerialisedTestCase(int numberOfElements, int maxValue, int numberOfMutations){
		this.numberOfElements = numberOfElements;
		this.maxValue = maxValue;
		this.mutationValue = new int[numberOfMutations];
		this.mutationPosition = new int[numberOfMutations];
		this.generateTestCase();
	}
	
	public static ArrayList<Integer> randomElements(int numberOfElements, int maxValue){
		int[] data = new int[numberOfElements];
		for(int i = 0; i < numberOfElements; i++){
			data[i] = (int) (Math.random()*maxValue);
		}
		return randomElements(data);
	}
		
	public static ArrayList<Integer> randomElements(int[] data){
		ArrayList<Integer> dataElements = new ArrayList<Integer>(data.length);
		for(int i = 0; i < data.length; i++){
			dataElements.add(data[i]);
		}
		return dataElements;
	}
	
	public void generateTestCase(){
		SophisticatedDataStructure sophisticatedDS = new SophisticatedDataStructure();
		this.sequenceToLoad = randomElements(this.numberOfElements, this.maxValue);
		int i = 0;
		sophisticatedDS.load(this.sequenceToLoad);
		int mutationPosition;
		int mutationValue;
		i = 0;
		while(i < this.mutationPosition.length){
			mutationPosition = (int) (Math.random() * sophisticatedDS.totalSum());
			mutationValue = (int) (Math.random() * (maxValue) + 1);
			sophisticatedDS.mutate(mutationPosition, mutationValue);
			this.mutationPosition[i] = mutationPosition;
			this.mutationValue[i] = mutationValue;
			i++;
		}
	}
}
