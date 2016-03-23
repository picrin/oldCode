package pl.kurkiewicz.adam.FunctionalDNA;
import java.util.ArrayList;
import java.util.Collection;
import java.util.Iterator;
public class PlusHeap{
	public PlusHeap(){
		this.head = new PHNode();
	}
	public PlusHeap(Collection<Integer> a_sequence){
		int sequenceSize = a_sequence.size();
		ArrayList<PHLeaf> sequence = new ArrayList<PHLeaf>(sequenceSize);
		Iterator<Integer> iterator = a_sequence.iterator();
		int currentValue = 0;
		while (iterator.hasNext()){
			currentValue = iterator.next();
			sequence.add(new PHLeaf(currentValue));
		}
		this.increaseSizeElements(sequence.size());
		this.increaseTotalSum(sequence);
		this.head = fullBulk(sequence);
		this.linkLeafs(sequence);
		this.setFirstLeaf(sequence.toArray(new PHLeaf[]{})[0]);
		this.setLastLeaf(sequence.toArray(new PHLeaf[]{})[sequence.size() -1]);
	}
	
	public void printPreOrder(){
		printPreOrder(this.getHead());
		System.out.println();
	}
	
	public void printInOrder(){
		printInOrder(this.getHead());
		System.out.println();
	}
	
	public static void printInOrder(AbstractNode node){
		System.out.print("(");
		if (!node.isLeaf()){
			printInOrder(((PHNode) node).getLeftChild());
			System.out.print(node);
			printInOrder(((PHNode) node).getRightChild());
		} else{
			System.out.print(node);
			
		}
		System.out.print(")");
	}

	public static void printPreOrder(AbstractNode node){
		System.out.print("(");
		if (!node.isLeaf()){
			System.out.print(node);
			printPreOrder(((PHNode) node).getLeftChild());
			printPreOrder(((PHNode) node).getRightChild());
		} else{
			System.out.print(node);
		}
		System.out.print(")");
	}

	
	public static AbstractNode getBySum(AbstractNode node, int searchedValue){
	//	return new PHLeaf(0);
		if (node.isLeaf()) return  node;
		else if (( searchedValue < ((PHNode) node).getLeftChild().getValue()))
			return getBySum(((PHNode) node).getLeftChild(), searchedValue);
		else return getBySum(((PHNode) node).getRightChild(),
			searchedValue - ((PHNode) node).getLeftChild().getValue());
	}

	public PHLeaf getBySum(int searchedValue){
		return (PHLeaf) getBySum(this.getHead(), searchedValue);
	}
	
	public ArrayList<? extends AbstractNode> bulkLevelUp(Collection<? extends AbstractNode> dataNodes){
		ArrayList<AbstractNode> returnedAL = new ArrayList<AbstractNode>(dataNodes.size()/2 + 1);
		Iterator<? extends AbstractNode> iterator = dataNodes.iterator();
		while (iterator.hasNext()){
			AbstractNode leftChild = iterator.next();
			if (iterator.hasNext()){
				AbstractNode rightChild = iterator.next();
				PHNode father = new PHNode(leftChild, rightChild);
				leftChild.setFather(father);
				rightChild.setFather(father);
				father.setValueFromChildren();
				returnedAL.add(father);
			}
			else{
				returnedAL.add(leftChild);
			}
		}
		return returnedAL;
	}
	
	public AbstractNode fullBulk(Collection <? extends AbstractNode> dataNodes){
		Collection<? extends AbstractNode> approachingRoot = dataNodes;
		while (approachingRoot.size() > 1){
			//System.out.println(approachingRoot);
			approachingRoot = this.bulkLevelUp(approachingRoot);
		}
		return approachingRoot.iterator().next();
	}
	
	protected void linkLeafs(Collection<PHLeaf> dataNodes){
		this.linkLeafs(dataNodes, null, null);
	}

	public void linkLeafs(Collection<PHLeaf> dataNodes, PHLeaf leftBound, PHLeaf rightBound){
		Iterator<PHLeaf> iterator = dataNodes.iterator();
		PHLeaf left;
		PHLeaf right;
		if (iterator.hasNext()){
			left = iterator.next();
			right = left;
			left.setLeftLeaf(leftBound);
			while (iterator.hasNext()){
				right = iterator.next();
				left.setRightLeaf(right);
				right.setLeftLeaf(left);
				left = right;
			}
			right.setRightLeaf(rightBound);
		}
		
	}
	
	public static boolean updateChildOfParent(AbstractNode oldChild, AbstractNode newChild){
		PHNode parent = oldChild.getFather();
		if (parent == null) return false;
		else{
			if (parent.getLeftChild() == oldChild)
				parent.setLeftChild(newChild);
			else
				parent.setRightChild(newChild);
			newChild.setFather(parent);
			return true;
		}
	}
	
	public void insertSubsequence(int toGetBySum, AbstractNode commonAncestor){
		PHLeaf insertAfter = this.getBySum(toGetBySum);
		boolean existsParentInsertAfter = updateChildOfParent(insertAfter, commonAncestor);
		PHNode parentInsertAfter;
		if (!existsParentInsertAfter){
			this.setHead(commonAncestor);
			commonAncestor.setFather(null);
			parentInsertAfter = null;
		} else {
			parentInsertAfter = insertAfter.getFather(); 
		}
		System.out.println("0");
		PHLeaf leftMost = (PHLeaf) getBySum(commonAncestor, 0);
		PHLeaf rightMost = (PHLeaf) getBySum(commonAncestor, commonAncestor.getValue());
		System.out.println("1");		
		PHNode newNode = new PHNode(insertAfter, leftMost);
		leftMost.setFather(newNode);
		insertAfter.setFather(newNode);
		//newNode.setValueFromChildren();
		System.out.println("2");
		PHNode leftMostFather = leftMost.getFather();
		if (leftMostFather != null) leftMostFather.setLeftChild(newNode);
		//commonAncestor.setFather(parentInsertAfter);
		newNode.setFather(leftMostFather);
		AbstractNode nextNode = insertAfter;
		System.out.println("***********");
		while (nextNode != leftMostFather){
			System.out.println(insertAfter);
			nextNode = nextNode.getFather();
		}
		System.out.println("***********");
		//staticUpdateParents(insertAfter);
		System.out.println("3");
		PHLeaf nextInsertAfter = insertAfter.next();		
		if (nextInsertAfter != null) nextInsertAfter.setLeftLeaf(rightMost);
		rightMost.setRightLeaf(nextInsertAfter);
		leftMost.setLeftLeaf(insertAfter);
		insertAfter.setRightLeaf(leftMost);
		System.out.println("4");
	}
	
	
	public void mutate(PHLeaf pHLeaf, int newValue){
		this.decreaseTotalSum(pHLeaf.getValue());
		this.increaseTotalSum(newValue);
		staticMutate(pHLeaf, newValue);
	}
	
	public static void staticUpdateParents(AbstractNode fromUp){
		PHNode nextNode = fromUp.getFather();
		while (nextNode != null){
			System.out.println(nextNode);
			nextNode.setValueFromChildren();
			nextNode = nextNode.getFather();
		}
	}
	
	public static void staticMutate(AbstractNode pHLeaf, int newValue){
		pHLeaf.setValue(newValue);
		PHNode parent = pHLeaf.getFather();
		while(parent != null){
			parent.setValueFromChildren();
			parent = parent.getFather();
		}
	}
	
	protected ArrayList<AbstractNode> getAncestry(AbstractNode nodeBelongsHeap){
		ArrayList<AbstractNode> ancestry = new ArrayList<AbstractNode>();
		while (nodeBelongsHeap != null){
			ancestry.add(nodeBelongsHeap);
			nodeBelongsHeap = nodeBelongsHeap.getFather();
		}
		return ancestry;
	}

	protected AbstractNode mostRecentCommonAncestor(AbstractNode oneNodeBilongHeap, AbstractNode twoNodeBilongHeap){
		/*
		* This very function does not require oneNodeBilongHeap to be an earlier element than twoNodeBilongHeap. It is not necessarily the case for algorithms using it!
		* TODO Throw an exception in case nodes do not meet up.
		*/
		if (oneNodeBilongHeap == twoNodeBilongHeap){
			return oneNodeBilongHeap;
		}
		ArrayList<AbstractNode> oneAncestry = getAncestry(oneNodeBilongHeap);
		ArrayList<AbstractNode> twoAncestry = getAncestry(twoNodeBilongHeap);
		//System.out.println(oneAncestry);
		//System.out.println(twoAncestry);
		int oneIndex = oneAncestry.size() - 1;
		int twoIndex = twoAncestry.size() - 1;
		int fromEnd = 0;
		if (oneAncestry.get(oneIndex) != twoAncestry.get(twoIndex) && oneAncestry.get(oneIndex) != this.getHead())
			return null; // should be an exception
		while (oneAncestry.get(oneIndex - fromEnd) == twoAncestry.get(twoIndex - fromEnd)){
			fromEnd++;
		}
		return oneAncestry.get(oneIndex - (fromEnd - 1));
	}
	
	/*
	* setters getters and alike
	*/

	public AbstractNode getHead(){
		return this.head;
	}
	
	public void setHead(AbstractNode head){
		this.head = head;
	}
	
	/**
	 * 
	 * @return returns the number of elements. METHOD IS UNRELIABLE. ESPECIALLY 
	 * IF DS EVER WAS CHANGED BY this.insertSubsequence(). Don't use it.
	 */
	public int sizeElements(){
		return this.numberOfElements;
	}
	
	public int getTotalSum(){
		return this.totalSum;
	}
	
	public PHLeaf getLastLeaf(){
		return this.lastLeaf;
	}	

	public PHLeaf getFirstLeaf(){
		return this.firstLeaf;
	}	

	protected void increaseSizeElements(int by){
		this.numberOfElements += by;
	}

	protected void decreaseSizeElements(int by){
		this.numberOfElements -= by;
	}

	protected void increaseTotalSum(int by){
		this.totalSum += by;
	}

	protected void decreaseTotalSum(int by){
		this.totalSum -= by;
	}
	
	protected void increaseTotalSum(Collection<PHLeaf> collection){
		Iterator<PHLeaf> iterator = collection.iterator();
		while (iterator.hasNext()){
			this.increaseTotalSum(iterator.next().getValue());
		}
	}

	protected void decreaseTotalSum(Collection<PHLeaf> collection){
		Iterator<PHLeaf> iterator = collection.iterator();
		while (iterator.hasNext()){
			this.decreaseTotalSum(iterator.next().getValue());
		}
	}
	
	protected void setFirstLeaf(PHLeaf leaf){
		this.firstLeaf = leaf;
	}

	protected void setLastLeaf(PHLeaf leaf){
		this.lastLeaf = leaf;
	}
	


	protected PHLeaf firstLeaf = null;
	protected PHLeaf lastLeaf = null;
	protected AbstractNode head = null;
	protected int numberOfElements = 0;
	protected int totalSum = 0;

}
