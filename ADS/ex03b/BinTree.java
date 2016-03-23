import java.util.*;
import java.io.*;

public class BinTree {
    private Node root;
	
    public BinTree(){root = null;}

    public BinTree(String fname) throws IOException {
	Scanner sc = new Scanner(new File(fname));
	Stack<Node>   S1 = new Stack<Node>();
	Stack<String> S2 = new Stack<String>();
	String s = "";
	while (sc.hasNext()){
	    s = sc.next();
	    if (s.equals("(")) S1.push(new Node(null,"!",null));
	    else if (s.equals("+") || s.equals("-") || s.equals("*") || 
		     s.equals("/") || s.equals("^"))
		S2.push(s);
	    else if (s.equals(")")){
		Node r    = S1.pop();
		Node l    = S1.pop();
		Node node = S1.pop();
		String op = S2.pop();
		node.setLeft(l); node.setElement(op); node.setRight(r);
		S1.push(node);
	    }
	    else S1.push(new Node(null,s,null));
	}
	root = S1.pop();
    }

    private void draw(Node node,double x,double xLow,double xHi,double y,double dY){
	StdDraw.filledCircle(x,y,0.001);
	StdDraw.text(x,y-0.02,node.toString());
	double xLeft  = (xLow + x)/2.0;
	double xRight = (x + xHi)/2.0;
	if (node.hasLeft()){
	    StdDraw.line(x,y,xLeft,y+dY);
	    draw(node.getLeft(),xLeft,xLow,x,y+dY,dY);
	}
	if (node.hasRight()){
	    StdDraw.line(x,y,xRight,y+dY);
	    draw(node.getRight(),xRight,x,xHi,y+dY,dY);
	}
    }

    public void draw(){
	if (root != null){
	    int h = height();
	    double dY = -1.0 / (double)h;
	    draw(root,0.5,0.0,1.0,1.0,dY);
	}
    }


    public boolean isEmpty(){return root == null;}

    public int height(){return height(root);}
    //
    // deliver the height of the tree
    // a leaf is at height 1
    // a node has height: 1 + maximum(height(left),height(right))
    //

    private int height(Node node){
	if (node == null) return 0;
	return 1 + Math.max(height(node.getLeft()),height(node.getRight()));
    }

    ////////////////////////////////////////////////////////////////////////////////////


    //
    // IMPLEMENT ME
    //
    public int size(){
    return size(root);
    }
    public static int size(Node node){
	if (node.hasLeft() && node.hasRight()) return 1 + size(node.getLeft()) + size(node.getRight());
	else if (node.hasLeft()) return 1 + size(node.getLeft());
    else if (node.hasRight()) return 1 + size(node.getRight());
    else return 1;
    }
    //
    // deliver the number of nodes in the tree
    //

    //
    // IMPLEMENT ME
    //
    public String preorder(){
    return preorder(root);
    }
    public static String preorder(Node node){
    	if (node.hasLeft() && node.hasRight()) return "(" + node + " " + preorder(node.getLeft()) + " " + preorder(node.getRight()) + ")";
    	else if (node.hasLeft()) return "(" + node + " " + preorder(node.getLeft()) + ")";
    	else if (node.hasRight()) return "(" + node + " " + preorder(node.getRight()) + ")";
    	else return node.toString();
    }
    //
    // The preorder of cats00.txt should produce the string
    // (* (* tiger (* lion liger)) (* siamese (* burmese burmilla)))
    //

    //
    // IMPLEMENT ME
    //
    public String inorder(){
    return inorder(root);
    }
    public static String inorder(Node node){
    	if (node.hasLeft() && node.hasRight()) return "(" + inorder(node.getLeft()) + " " + node + " " + inorder(node.getRight()) + ")";
    	else if (node.hasLeft()) return "(" + inorder(node.getLeft()) + node + " " + ")";
    	else if (node.hasRight()) return "(" + node + " " + inorder(node.getRight()) + ")";
    	else return node.toString();
    }
    //
    // The inorder of cats00.txt should be the string
    // ((tiger * (lion * liger)) * (siamese * (burmese * burmilla)))
    //

    //
    // IMPLEMENT ME
    //
    public String postorder(){
    return postorder(root);
    }
    public static String postorder(Node node){
    	if (node.hasLeft() && node.hasRight()) return "(" + postorder(node.getLeft()) + " " + postorder(node.getRight()) + " " + node + ")";
    	else if (node.hasLeft()) return "(" + postorder(node.getLeft()) + node + " " + ")";
    	else if (node.hasRight()) return "(" + postorder(node.getRight()) + node + " " + ")";
    	else return node.toString();
    }
    //
    // The posorder traversal of cats00.txt is the string
    // ((tiger (lion liger *) *) (siamese (burmese burmilla *) *) *)
    //

    //
    // IMPLEMENT ME
    //
    public String leaves(){
    return leaves(root);
    }
    public static String leaves(Node node){
    	if (node.hasLeft() && node.hasRight()) return leaves(node.getLeft()) + leaves(node.getRight());
    	else if (node.hasLeft()) return leaves(node.getLeft());
    	else if (node.hasRight()) return postorder(node.getRight());
    	else return node.toString() + " ";
    }


    //
    // leaves of cats00.txt is the string
    // tiger lion liger siamese burmese burmilla
    //

    //
    // IMPLEMENT ME
    //
    public String bfs(){return "IMPLEMENT ME";}
    //
    // bfs performs a breadth-first search of the tree
    // bfs visits the root (depth 0), then visits all nodes at depth 1,
    // then all nodes at depth 2, then ...
    // bfs on the data set eqn00.txt delivers the string
    // / ^ + + + 17 Z * * X Y 9 3 2 7
    //
}
