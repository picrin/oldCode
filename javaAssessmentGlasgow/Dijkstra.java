import java.io.*;
import java.util.*;

/**
 program to find shortest path using Dijkstra's algorithm
 */
public class Dijkstra {

	public static void main(String[] args) throws IOException {

		long start = System.currentTimeMillis();

		String inputFileName = args[0]; // dictionary
		String word1 = args[1]; // first word
		String word2 = args[2]; // second word
		
		
		HashMap<String, ArrayList<String>> hm = new HashMap<String, ArrayList<String>>();
		WeightedGraph g = new WeightedGraph();
		FileReader reader = new FileReader(inputFileName);
		Scanner in = new Scanner(reader);
		
		while(in.hasNext()){
			String next_line = in.nextLine();
			g.add(next_line);
			//System.out.println(next_line);
			char[] characters = next_line.toCharArray();  
			for(int i = 0; i< characters.length; i++){
				char[] new_characters = new char[characters.length];
				for(int ii = 0; ii< characters.length; ii++){
					new_characters[ii] = new Character(characters[ii]);
				}
				new_characters[i] = "?".toCharArray()[0];
				String entry = new String(new_characters);
				if(!hm.containsKey(entry)){
					hm.put(entry, new ArrayList<String>());
				}
				hm.get(entry).add(next_line);
			}
		}
		for(ArrayList<String> al : hm.values()){
			for(String entryLeft: al){
				for(String entryRight: al){
					if (entryLeft.compareTo(entryRight) > 0){
						g.connectWeighted(entryLeft, entryRight);
					}
				}
			}
		}

		PriorityQueue<WeightedNode> pq = new PriorityQueue<WeightedNode>();
		
		WeightedNode root = g.hm.get(word1);
		
		root.visited = true;
		root.value = 0;
		pq.add(root);
		
		while(!pq.isEmpty()){
			WeightedNode current = pq.poll();
			for(int i = 0; i < current.children.size(); i++){
				WeightedNode child = g.hm.get(current.children.get(i).name);
				//System.out.println(child.name);
				if(!child.visited){
					child.visited = true;
					pq.add(child);
				}
				int potentiallyNew = current.value + current.values.get(i);
				if(potentiallyNew < child.value ){
					child.value = potentiallyNew;
					child.came_from = current;
				}
			}
		}

		WeightedNode tail = g.hm.get(word2);
        WeightedNode currentTail = tail;
        int length = 0;
        
        try{
	        while(!currentTail.name.equals(word1)){
	        	System.out.println(currentTail.name);
	        	currentTail = currentTail.came_from;
	        	length++;
	        }
        } catch (Exception e){
        	System.out.println("no chain");
        	System.exit(0);
        }
        System.out.println(currentTail.name);
        //System.out.println(currentTail.came_from.came_from.name);
        System.out.println("\nchain length in elements: " + (length));
        System.out.println("chain total weight sum: " + g.hm.get(word2).value);
        //root.printInfo();
		in.close();
		reader.close();
		
		long end = System.currentTimeMillis();
		System.out.println("\nElapsed time: " + (end - start) + " milliseconds");
	}

}
