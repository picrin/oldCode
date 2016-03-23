
public class Node  {
    private String element;
    private Node   left;
    private Node   right;
	
    public Node(){this(null,"",null);}
	
    public Node(Node left,String e,Node right){
	this.left    = left;
	this.element = e;
	this.right   = right;
    }

    public Node   getLeft(){return left;}
    public String getElement(){return element;}
    public Node   getRight(){return right;}

    public void setLeft(Node node){left = node;}
    public void setElement(String e){element = e;}
    public void setRight(Node node){right = node;}

    public boolean hasLeft(){return left != null;}
    public boolean hasRight(){return right != null;}
    public boolean isLeaf(){return left == null && right == null;}

    public String toString(){return element;}
}
