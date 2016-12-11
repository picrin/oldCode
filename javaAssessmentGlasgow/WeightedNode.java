import java.util.ArrayList;

public class WeightedNode implements Comparable<WeightedNode>{
	ArrayList<WeightedNode> children = new ArrayList<WeightedNode>();
	ArrayList<Integer> values = new ArrayList<Integer>();
	
	WeightedGraph graph;
	WeightedNode came_from = null;
	String name;
	int value = Integer.MAX_VALUE;
	boolean visited = false;
	WeightedNode(String name){
		this.name = name;
	}
	public void printInfo(){
		System.out.println("info for:" + name); 
		for(int i = 0; i < values.size(); i++){
			System.out.println("child:" + children.get(i).name);
			System.out.println("has value:" + values.get(i));			
		}
	}

	@Override
	public int compareTo(WeightedNode other) {
		return Integer.compare(this.value, other.value);
	}
}
