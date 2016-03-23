package pl.kurkiewicz.adam.FunctionalDNA;
import java.util.ArrayList;
import java.io.BufferedWriter;
import java.io.FileWriter;
import java.io.File;
import java.io.IOException;

public class MutationBenchmark{
	public static void main(String[] args) throws IOException{
		int step;
		int maxNumberOfElements;
		final int maxElementValue = 1000;
		final int numberOfMutations = 100000;
		
		/*int step = 200;
		int maxNumberOfElements = 10000;
		int numberOfMutations = 100000;
		
		int step = 2000;
		int maxNumberOfElements = 800000;*/

		DataSet kdsTest = new DataSet(step = 200, maxNumberOfElements = 1000, numberOfMutations, maxElementValue);
		DataSet sdsTest = new DataSet(step = 2000, maxNumberOfElements = 100000, numberOfMutations, maxElementValue);
		KISSDataStructure kds = new KISSDataStructure();
		SophisticatedDataStructure sds = new SophisticatedDataStructure();
		measureForPlot("LinearWithBinarySearchWorks", kdsTest, kds);
		measureForPlot("PlusHeapWorks", sdsTest, sds);
		SerialisedTestCase assureNoMisbehave = new SerialisedTestCase(123, maxElementValue, 10000000);

		SophisticatedDataStructure potentiallyMisbehaved = new SophisticatedDataStructure();
		measure(assureNoMisbehave, potentiallyMisbehaved);
		System.out.println(potentiallyMisbehaved);


		DataSet test = new DataSet(step = 100, maxNumberOfElements = 1000, numberOfMutations, maxElementValue);
		SerialisedTestCase assureIdentical = new SerialisedTestCase(test.maxNumberOfElements, maxElementValue, numberOfMutations);
		System.out.println(testIfCorrect(assureIdentical));
		
	}

	public static <DS extends FunctionalDNADataStructure> long measure(SerialisedTestCase stc, DS ds){
		ds.load(stc.sequenceToLoad);
		int i = 0;
		final long startTime = System.currentTimeMillis();
		while(i < stc.mutationPosition.length){
			ds.mutate(stc.mutationPosition[i], stc.mutationValue[i]);
			i++;
		}
		final long stopTime = System.currentTimeMillis();
		return stopTime - startTime;

	}
	

	public static boolean testIfCorrect(SerialisedTestCase stc){
		int numberOfMutations = stc.mutationPosition.length;
		KISSDataStructure kissDS = new KISSDataStructure();
		SophisticatedDataStructure sophisticatedDS = new SophisticatedDataStructure();
		kissDS.load(stc.sequenceToLoad);
		sophisticatedDS.load(stc.sequenceToLoad);		
		int i = 0;
		while(i < numberOfMutations){
			kissDS.mutate(stc.mutationPosition[i], stc.mutationValue[i]);
			sophisticatedDS.mutate(stc.mutationPosition[i], stc.mutationValue[i]);
			i++;
		}
		
		//System.out.println(kissDS.toString());
		//System.out.println(sophisticatedDS.toString());
		return kissDS.toString().equals(sophisticatedDS.toString());
	}

	public static void writeTimesToFile(String name, ArrayList<Integer> millis,  ArrayList<Integer> numberOfElements, int numberOfMutations) throws IOException{
		if (millis.size() != numberOfElements.size()){
			throw new ArrayIndexOutOfBoundsException("lengths are not equal");
		}

		File file = new File(Integer.toString(numberOfMutations) + name + ".dat");
		if (!file.exists()) {
			file.createNewFile();
		}
		FileWriter fw = new FileWriter(file.getAbsoluteFile());
		BufferedWriter bw = new BufferedWriter(fw);
		int i = 0;
		while (i < millis.size()){
			bw.write(numberOfElements.get(i) + " " + millis.get(i) + "\n");
			i++;
		}
		bw.close();
	}


	public static <DS extends FunctionalDNADataStructure> void measureForPlot(String name, DataSet dataSet, DS ds) throws IOException{
		SerialisedTestCase testCase;
		ArrayList<Integer> millis = new ArrayList<Integer>();		
		ArrayList<Integer> numberOfElements = new ArrayList<Integer>();		
		for(int i = 1; i <= dataSet.maxNumberOfElements; i += dataSet.step){
			testCase = new SerialisedTestCase(i, dataSet.maxElementValue, dataSet.numberOfMutations);
			System.gc();
			int time = (int) measure(testCase, ds);
			numberOfElements.add(i);
			millis.add(time);
		}	
		writeTimesToFile(name, millis, numberOfElements, dataSet.numberOfMutations);
	}

	private static class DataSet{
		public int step;
		public int maxNumberOfElements;
		public int numberOfMutations;
		public int maxElementValue;
		DataSet(int step, int maxNumberOfElements, int numberOfMutations, int maxElementValue){
			this.step = step;
			this.maxNumberOfElements = maxNumberOfElements;
			this.numberOfMutations = numberOfMutations;
			this.maxElementValue = maxElementValue;
		}
	}

}