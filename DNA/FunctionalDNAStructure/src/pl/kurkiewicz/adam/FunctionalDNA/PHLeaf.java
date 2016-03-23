package pl.kurkiewicz.adam.FunctionalDNA;
public class PHLeaf extends AbstractNode{
	public PHLeaf(int value){
		this.value = value;
	}

	public PHLeaf(int value, PHLeaf leftLeaf, PHLeaf rightLeaf){
		this.value = value;
		this.leftLeaf = leftLeaf;
		this.rightLeaf = rightLeaf;
	}

	public PHLeaf(int value, PHNode father){
		this.value = value;
		this.father = father;
	}

	public PHLeaf(PHNode father){
		this.father = father;
	}

	public void updateFather(){
		this.getFather().setValueFromChildren();
	}
	public boolean isLeaf(){
		return true;
	}
	/*
	* getters
	*/

	public int getValue(){
		return this.value;
	}

	public PHNode getFather(){
		return this.father;
	}
	
	public PHLeaf previous(){
		return this.leftLeaf;
	}
	
	public PHLeaf next(){
		return this.rightLeaf;
	}

	/*
	* setters
	*/

	public void setValue(int value){
		this.value = value;
	}

	public void setLeftLeaf(PHLeaf leftLeaf){
		this.leftLeaf = leftLeaf;
	}

	public void setRightLeaf(PHLeaf rightLeaf){
		this.rightLeaf = rightLeaf;
	}

	public void setFather(PHNode father){
		this.father = father;
	}
	
	/*
	* standard methods
	*/
	
	public String toString(){
		return new Integer(this.value).toString() + "L";
	}

	/*
	* attributes
	*/
	protected int value = 0;
	protected PHLeaf leftLeaf = null;
	protected PHLeaf rightLeaf = null;
	protected PHNode father = null;
}
