import java.util.*;

public class Test {      
         
 public static void main(String[] args) throws Exception {

    String commands = "\nList Tester (version 6.626068 * 10^-34) \n" +
                      "add (+), delete (del/-), max, empty (e), \n" + 
                      "present (p), reverse (r), insert (ins), sort, \n" + 
                      "count, nth, max, append (a), \n"+
                      "equal (=), random (rand), swap, size, \n" +
                      "sum, show, quit (q)";

    System.out.println(commands);
    Scanner sc = new Scanner(System.in);

    System.out.print("> ");
    String command = sc.next();
    int swap = 0;
    List[]LL = new List[2];
    LL[0] = LL[1] = null;
    List L = LL[0];
    int n;
    Random random = new Random();

    while (!command.equals("quit") && !command.equals("q")){
	LL[swap] = L;
	if (command.equals("help")) System.out.println(commands);

	if (command.equals("size")) System.out.println(List.length(L));

	if (command.equals("sum")) System.out.println(List.sum(L));

	if (command.equals("max")) System.out.println(List.max(L));

        if (command.equals("empty") || command.equals("e")) System.out.println(L==null);

	if (command.equals("equal") || command.equals("=")) 
	    System.out.println(List.equal(LL[0],LL[1]));

	if (command.equals("delete") || command.equals("del") || command.equals("-")){
	    System.out.print(">> ");
	    n = sc.nextInt();
	    L = List.delete(n,L);
	    System.out.println(L);
	}

	if (command.equals("add") || command.equals("+")){
	    System.out.print(">> ");
	    n = sc.nextInt();
	    L = new List(n,L);
	    System.out.println(L);
	}

	if (command.equals("insert") || command.equals("ins")){
	    System.out.print(">> ");
	    n = sc.nextInt();
	    L = List.insert(n,L);
	    System.out.println(L);
	}

	if (command.equals("present") || command.equals("p")){
	    System.out.print(">> ");
	    n = sc.nextInt();
	    System.out.println(List.exists(n,L));
	}

	if (command.equals("random") || command.equals("rand")){
	    System.out.print("lengh >> ");
	    n = sc.nextInt(); 
	    L = null;
	    for (int i=0;i<n;i++) L = new List(random.nextInt(10),L);
	    System.out.println(L);
	}

	if (command.equals("reverse") || command.equals("r")){
	    L = List.reverse(L);
	    System.out.println(L);
	}

	if (command.equals("sort")){
	    L = List.sort(L);
	    System.out.println(L);
	}

	if (command.equals("count")){
	    System.out.print(">> ");
	    n = sc.nextInt();
	    System.out.println(List.count(n,L));
	}

	if (command.equals("nth")){
	    System.out.print(">> ");
	    n = sc.nextInt();
	    System.out.println(List.nth(n,L));
	}

	if (command.equals("append")){
	    L = List.append(LL[0],LL[1]);
	    System.out.println(L);
	}

	if (command.equals("show")) System.out.println(L);

	if (command.equals("swap")) {swap = 1 - swap; L = LL[swap]; System.out.println(L);}

	System.out.print("> ");
	command = sc.next();
      }
  }
}
