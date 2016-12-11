import java.util.ArrayList;

public class Node {
	ArrayList<Node> children = new ArrayList<Node>();

	Graph graph;
	Node came_from = null;
	String name;
	boolean visited = false;
	Node(String name){
		this.name = name;
	}
	public void printInfo(){
		System.out.println("info for:" + name); 
		for(Node child: children){
			System.out.println("child:" + child.name);
		}
	}
}
