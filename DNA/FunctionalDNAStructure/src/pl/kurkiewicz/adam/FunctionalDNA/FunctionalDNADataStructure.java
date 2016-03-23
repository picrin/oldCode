package pl.kurkiewicz.adam.FunctionalDNA;
/**
 * This is the interface for all data structures implementing a bayesian
 * functional DNA population genomics model.
 * @author Adam Kurkiewicz
 * @version alpha
 */
import java.util.Collection;
public interface FunctionalDNADataStructure{
	/*
	* Loads an integer sequence we are going to work with.
	*/
	public void load(Collection<Integer> sequence);
	
	/*
	* Gives the sum of all elements in the sequence.
	*/
	public int totalSum();
	
	/**
	 * Returns the value of the first element e in the sequence, such that the
	 * sum of all elements that come before e including e is strictly more than a
	 * given value. This way of accessing the sequence elements is the only
	 * required to be supported. Any other ways of accessing the elements are
	 * optional. 
	 */
	public int getBySum(int value);
	
	/**
	 * Changes value of the element accessed as by getBySum(toGetBySum).
	 * Underlying data structure should adjust accordingly.
	 * @param toGetBySum
	 *     the argument which will be used to access an element of the sequence
	 */
	public void mutate(int toGetBySum, int newValue);
	
	
	/**
	* Inserts a contiguous subsequence into the sequence we work with. The subsequence
	* should be inserted AFTER the element accessed by getBySum(toGetBySum).
	* Unsupported yet
	*/
	void insertSubsequence(int toGetBySum, Collection<Integer> subsequence);
	
	/**
	* Deletes a contiguous subsequence from the sequence. leftBoundary should be
	* <= rightBoundary. Deleted subsequence should only contain elements, whose
	* values would be returned by getBySum(leftBoundary),
	* getBySum(rightBoundary) and all the elements in between these two.
	* Unsupported yet.
	*/
	//DSElement[] deleteSubsequence(int leftBoundary, int rightBoundary);
}
