//
// This is a Pure List, of integers. 
// It does not use a container. It is simple and powerful
// Downside is that we have to preceed calls with List. in a similar way to
// the Math. package.
//

public class List {
    int head;
    List tail;

    public List(int i,List tail){head = i; this.tail = tail;}

    public static int head(List l){return l.head;}
    public static List tail(List l){return l.tail;}

    public static int length(List l){
	if (l == null) return 0;
	else return 1 + length(tail(l));
    }
    //
    // get the length of the list l
    //

    public static int sum(List l){
	if (l == null) return 0;
	else return head(l) + sum(tail(l));
    }
    //
    // give sum total of values in the list
    //

    public static boolean exists(int e,List l){
	return l != null && (head(l) == e || exists(e,tail(l)));
    }
    //
    // does integer e exist in the list?
    //

    public static List reverse(List l){
	if (l == null) return null;
	else return reverse(l,null);
    }
    //
    // deliver a new list, the reversal of l
    //

    private static List reverse(List l1,List l2){
	if (l1 == null) return l2;
	else return reverse(tail(l1),new List(head(l1),l2));
    }				

    public static List delete(int e,List l){
	if (l == null) return null;
	else if (e == head(l)) return delete(e,tail(l));
	else return new List(head(l),delete(e,tail(l)));
    }
    //
    // deliver a new list, the list l with
    // all values e deleted
    //

    //
    // IMPLEMENT ME
    //
    public static int count(int e, List l){
    if (l == null) return 0;
    else if (head(l) == e) return 1 + count(e, tail(l));
    else return count(e, tail(l));
    }
    //
    // deliver an integer result, the number of times e occurs in l
    //

    //
    // IMPLEMENT ME
    //
    public static boolean equal(List l1,List l2){
    if (l1 == null && l2 == null) return true;
    else if (l1 != null && l2 != null && head(l1) == head(l2)) return equal(tail(l1), tail(l2));
    else return false;
    }
    //
    // are lists l1 and l2 equal? That is, do they contain
    // the same data in the same order?
    //

    //
    // IMPLEMENT ME
    //
    public static int nth(int n,List l) throws ListException {
    if(l == null) throw new ListException("indexOutOfBounds");
    if(n == 0) return head(l);
    else return nth(n-1,tail(l));
    }
    //
    // return the nth element of the list, where first element is in
    // position 0. Throw an exception if list is empty or n is beyond length 
    // of the list
    //

    //
    // IMPLEMENT ME
    //
    public static List insert(int e, List l){
    if (l == null) return new List(e, null);
	else return insert(e, l, null);
    }

    public static List insert(int e, List l1, List l2){
    if (e < head(l1) || l1 == null) return insert(l1, new List(e, l2));
    else return insert(e, tail(l1), new List(head(l1), l2));
    }
    
    public static List insert(List l1, List l2){
    if (l1 == null) return reverse(l2);
    else return insert(tail(l1), new List(head(l1), l2));
    }
    //
    // deliver a new list that has e inserted into l in 
    // non-decreasing order
    //

    //
    // IMPLEMENT ME
    //
    public static List sort(List l){
    return sort(l, null);
    }
    
    public static List sort(List l1, List l2){
    if (l1 == null) return l2;
    else return sort(tail(l1), insert(head(l1), l2));
    }
    //
    // Using an insertion sort, deliver a new list
    // corresponding to l sorted in non-decreasing order
    // i.e. use insert above
    // 

    //
    // IMPLEMENT ME
    //
    
    public static List append(List l1, List l2){
    return append(l1, l1, l2);
    }
    
    public static List append(List helper, List l1, List l2){
    if (tail(l1) != null) return append(l1, tail(l1), l2);
    else{
        l1.tail = l2;
        return helper;
    }
    }
    //
    // deliver a new list that contains all the elements
    // of l1 with the current list l2 appended to the end
    // i.e. l2 is not copied, just pointed to
    //

    //
    // IMPLEMENT ME
    //
    public static int max(List l) throws ListException {
    if (tail(l) == null) return head(l);
    else if (head(tail(l)) < head(l)) return max(new List(head(l), tail(tail(l))));
    else return max(new List(head(tail(l)), tail(tail(l))));
    }
    //
    // deliver the largest integer in the list
    // if the list is empty throw an exception
    //

    
    public String toString(){return "(" + toString(this) + ")";}

    private String toString(List l){
	if (l == null) return "";
	else if (tail(l) == null) return "" + head(l);
	else return head(l) +","+ toString(tail(l));
    }
}
