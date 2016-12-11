import java.util.HashMap;

public class Graph {
	static int problemSize = 500;
	HashMap<String, Node> hm = new HashMap<String, Node>(500);
	Graph(){}
	
	public Node getNode(String nodeString){
		return hm.get(nodeString);
	}
	
	public void connectBoth(String nodeLeft, String nodeRight){
		hm.get(nodeLeft).children.add(hm.get(nodeRight));
		hm.get(nodeRight).children.add(hm.get(nodeLeft));
	}

	public void add(String nodename){
		Node node = new Node(nodename);
		hm.put(nodename, node);
		node.graph = this;
	}
}
