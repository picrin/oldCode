package pl.kurkiewicz.adam.FunctionalDNA;
public abstract class AbstractNode{
	public abstract PHNode getFather();
	public abstract int getValue();
	public abstract void setValue(int value);
	public abstract void setFather(PHNode father);
	public abstract boolean isLeaf();
}
