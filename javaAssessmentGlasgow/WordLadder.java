import java.io.*;
import java.util.*;

/**
 program to find word ladder with shortest distance for two words in a dictionary
 distance between elements of the word ladder is the absolute difference in the
 positions of the alphabet of the non-matching letter
 */
public class WordLadder {

	public static void main(String[] args) throws IOException {

		long start = System.currentTimeMillis();

		String inputFileName = args[0]; // dictionary
		String word1 = args[1]; // first word
		String word2 = args[2]; // second word
        word1 = "sheet";
        word2 = "block";
		
		HashMap<String, ArrayList<String>> hm = new HashMap<String, ArrayList<String>>();
		Graph g = new Graph();
		FileReader reader = new FileReader(inputFileName);
		Scanner in = new Scanner(reader);
		
		while(in.hasNext()){
			String next_line = in.nextLine();
			//System.out.println(next_line);
			
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
				//System.out.println(entry);
				if(!hm.containsKey(entry)){
					hm.put(entry, new ArrayList<String>());
				}
				hm.get(entry).add(next_line);
			}
		}
		for(ArrayList<String> al : hm.values()){
			int i = 0;
			for(;i<al.size(); i++){
				for(int ii = i + 1; ii<al.size(); ii++){
					g.connectBoth(al.get(i), al.get(ii));
				}
			}
		}

//		for(Node node: g.hm.get("stark").children){
//			node.printInfo();
//		}
        Node current = null;
		try{
			Node root = g.hm.get(word1);
			//System.out.println(root.name);
			root.visited = true;
	        LinkedList<Node> bfs = new LinkedList<Node>();
	        current = root;
	        mainloop:
	        for(;;){
        		//System.out.println(current.name);
	            for(int i = 0; i < current.children.size(); i++){
	                Node currentChild = current.children.get(i);
	                if(!currentChild.visited){
	                	
	                	bfs.addFirst(currentChild);
	                	currentChild.came_from = current;
	                	currentChild.visited = true;
	                	if (current.name.equals(word2)){

	    	            	break mainloop;
	    	            }
	                }
	            }
	            current = bfs.pollLast();
	            
	            if (current == null){
	            	break;
	            }
	        }
        } catch (Exception e){
        	System.out.println("no chain");
    		in.close();
    		reader.close();
    		System.exit(0);
        }
        
        Node tail = g.hm.get(word2);
        Node currentTail = tail;
        int length = 0;
        
        try{
	        while(!currentTail.name.equals(word1)){
	        	System.out.println(currentTail.name);
	        	currentTail = currentTail.came_from;
	        	length++;
	        }
        }
        
        catch (Exception e){
        	System.out.println("no chain. ");
        	System.exit(0);
        }
        
        System.out.println(currentTail.name);
        //System.out.println(currentTail.came_from.came_from.name);
        System.out.println("\nchain length: " + (length));

		in.close();
		reader.close();
		
		long end = System.currentTimeMillis();
		System.out.println("\nElapsed time: " + (end - start) + " milliseconds");
	}

}
