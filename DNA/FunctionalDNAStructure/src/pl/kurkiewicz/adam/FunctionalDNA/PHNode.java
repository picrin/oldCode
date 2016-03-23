package pl.kurkiewicz.adam.FunctionalDNA;
public class PHNode extends AbstractNode{

	/*
	* Constructors
	*/

	public PHNode(){}

	public PHNode(int value){
		this.value = value;
	}

	public PHNode(int value, AbstractNode leftChild, AbstractNode rightChild){
		this.value = value;
		this.leftChild = leftChild;
		this.rightChild = rightChild;
	}

	public PHNode(AbstractNode leftChild, AbstractNode rightChild){
		this.leftChild = leftChild;
		this.rightChild = rightChild;
	}

	public PHNode(int value, PHNode father){
		this.value = value;
		this.father = father;
	}

	public PHNode(PHNode father){
		this.father = father;
	}

	/*
	* interesting methods
	*/
	

	public void setValueFromChildren(){
		this.value = this.getLeftChild().getValue() + this.getRightChild().getValue();
	}

	public void updateFather(){
		this.getFather().setValueFromChildren();
	}

	public boolean isRoot(){
		return (this.getFather() == null);
	}
	
	public boolean isLeaf(){
		return false;
	}
	
	public boolean isZero(){
		return false;
	}


	/*
	* getters
	*/

	public int getValue(){
		return this.value;
	}

	public AbstractNode getLeftChild(){
		return this.leftChild;
	}

	public AbstractNode getRightChild(){
		return this.rightChild;
	}

	public PHNode getFather(){
		return this.father;
	}

	/*
	* setters
	*/
	
	public void setValue(int value){
		this.value = value;
	}

	public void setLeftChild(AbstractNode leftChild){
		this.leftChild = leftChild;
	}

	public void setRightChild(AbstractNode rightChild){
		this.rightChild = rightChild;
	}

	public void setFather(PHNode father){
		this.father = father;
	}

	/*
	* standard methods
	*/
	
	public String toString(){
		return (new Integer(this.value)).toString();
	}


	/*
	* attributes
	*/

	protected int value = 0;
	protected AbstractNode leftChild = null;
	protected AbstractNode rightChild = null;
	protected PHNode father = null;	
}
