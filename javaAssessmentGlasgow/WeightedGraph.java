import java.util.HashMap;


public class WeightedGraph{
	
		static int problemSize = 1000;
		HashMap<String, WeightedNode> hm = new HashMap<String, WeightedNode>(500);
		WeightedGraph(){}
		public WeightedNode getNode(String nodeString){
			return hm.get(nodeString);
		}
		
		
		public void add(String nodename){
			WeightedNode node = new WeightedNode(nodename);
			hm.put(nodename, node);
			node.graph = this;
		}
		
		public void connectWeighted(String nodeLeft, String nodeRight){
			int compare = Math.abs(nodeLeft.compareTo(nodeRight));
			WeightedNode left = hm.get(nodeLeft);
			WeightedNode right = hm.get(nodeRight);
			left.children.add(right);
			left.values.add(compare);
			right.children.add(left);
			right.values.add(compare);
		}

	
}
