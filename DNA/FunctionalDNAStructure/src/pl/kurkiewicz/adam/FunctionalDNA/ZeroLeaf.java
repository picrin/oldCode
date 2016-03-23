package pl.kurkiewicz.adam.FunctionalDNA;
public class ZeroLeaf extends PHLeaf{
	public ZeroLeaf(PHNode father) {
		super(father);
	}
	
	public boolean isZero(){
		return true;
	}

	
	public int getValue(){
		return 0;
	}
}
