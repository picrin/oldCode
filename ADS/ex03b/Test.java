import java.util.*;
import java.io.* ;

public class Test {      
         
 public static void main(String[] args) throws Exception, FileNotFoundException {

    String commands = "\nBinTree Tester (version 1.3247179) [imperfect]\n" +
                      "preorder, inorder, postorder, bfs, leaves, draw, size, height, quit (q)";

    BinTree t1 = new BinTree(args[0]);

    System.out.println(commands);
    Scanner sc = new Scanner(System.in);

    System.out.print("> ");
    String command = sc.next();
    String s = "";

    while (!command.equals("quit") && !command.equals("q")){
	
	if (command.equals("help")) System.out.println(commands);

	if (command.equals("size")) System.out.println(t1.size());

	if (command.equals("height")) System.out.println(t1.height());
	
	if (command.equals("preorder")) System.out.println(t1.preorder());

	if (command.equals("inorder")) System.out.println(t1.inorder());

	if (command.equals("postorder")) System.out.println(t1.postorder());

	if (command.equals("bfs")) System.out.println(t1.bfs());

	if (command.equals("leaves")) System.out.println(t1.leaves());

	if (command.equals("draw")){
	    StdDraw.clear();
	    t1.draw();
	}

	System.out.print("> ");
	command = sc.next();
      }
    System.exit(0);
  }
}
