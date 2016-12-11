import java.util.Random;
import java.util.Stack;

/********************************* BORDERS *************************************
 Implements a Stack element.
*******************************************************************************/
class Borders{
    public Borders(int a_lewy, int a_prawy){
        m_lewy = a_lewy;
        m_prawy = a_prawy;
    }
    public void show(){
        System.out.print("{"+m_lewy+", "+m_prawy+"}");
    }
    public int m_lewy, m_prawy;
}

/******************************** QUICK SORT ***********************************
 Implements quicksort in form of in place algorithm using either a Java Stack
 or recurrence. Pivots are chosen randomly.
*******************************************************************************/
class QuickSort{
    
//--------------------------------CONSTRUCTOR(S)------------------------------//
    public QuickSort(int[] a_array){
        array = a_array;
        generator = new Random();
        bordersStack = new Stack<Borders>();
        bordersStack.push(new Borders(0, array.length-1));
    }
    
//--------------------------------INTERFACE METHODS---------------------------//
    public void sortStack(){
        restSort();
        System.out.print("sort(): Sorted!\n");
    }
    
    public void sortRecurrence(){
        sortRecurrence(0,getArrayLength()-1);
        System.out.print("sort(): Sorted!\n");
    }
            
    public void check(){
        for(int i = 1; i<array.length ; i++){
            if(array[i]<array[i-1]) throw new RuntimeException(
                "The check() method was called and detected an unsorted array!");
        }
        System.out.println("check(): Sorted OK!\n");
    }

//----------------------------------FIELDS------------------------------------//
    protected int[] array;
    protected Stack<Borders> bordersStack; 
    protected Random generator;   
    
//--------------------------------LOOKUP TOOLS--------------------------------//
    public void printArray(){
        System.out.print("{");
        for(int i = 0; i< array.length - 1; i ++) System.out.print(array[i]+",");
        System.out.print(array[array.length - 1]);
        System.out.println("}");
    }

    public void printStack(){
        Stack<Borders> b_stack = new Stack<Borders>();
        b_stack = (Stack<Borders>)bordersStack.clone();      
        while(!b_stack.empty()){
            b_stack.pop().show();
        }
    }

//-------------------------------AUXILIARY TOOLS------------------------------//
    public int getArrayLength(){
        return array.length;
    }
    
    protected void swap(int a_leftIndex, int a_rightIndex){
        int aux;
        aux = array[a_leftIndex];
        array[a_leftIndex] = array[a_rightIndex];
        array[a_rightIndex] = aux;
    }
    
    protected int makePartition(int a_index, int a_left, int a_right){
        swap(a_index, a_right);
        int firstGrater = a_left;
        for(int i = a_left; i < a_right; i++){
            if(array[i] < array[a_right]){
                swap(i,firstGrater);
                firstGrater++;
            }
        }
        swap(firstGrater, a_right);
        return firstGrater;
    }

//---------------------------STACK BASED SORTING -----------------------------//
    protected void leftSort(int a_left,int a_right){
        while (a_left <= a_right){
        int index;
        index = generator.nextInt(a_right - a_left + 1) + a_left;
        int pivot = makePartition(index, a_left, a_right);
        Borders unsorted = new Borders(pivot+1, a_right);
        bordersStack.add(unsorted);
        a_right=pivot-1;
        }
    }
    
    protected void restSort(){
        while(!bordersStack.empty()){
            Borders l_borders = bordersStack.pop();
            leftSort(l_borders.m_lewy,l_borders.m_prawy);
        }
    }

//---------------------------RECURRENCE BASED SORTING ------------------------//
    protected void sortRecurrence(int a_left, int a_right){             
        if(a_left >= a_right) return;
        int index;
        index = generator.nextInt(a_right - a_left + 1) + a_left;
        int pivot = makePartition(index, a_left, a_right);
        sortRecurrence(pivot+1, a_right);
        sortRecurrence(a_left, pivot-1);
    }
}

class Medians extends QuickSort{

    public Medians(int[] a_array){
        super(a_array);
    }
    
    public int medianPartitionOfFive(int left){ //(Using five comparisions and five swaps)
        if(array[left+1] > array[left+3]) swap(left+1, left+3);
        if(array[left+2] > array[left+4]) swap(left+2,left+4);
        if(array[left+2] > array[left+1]){
            swap(left+1,left);
            if(array[left+1] > array[left+3]) swap(left+1, left+3);
        }
        else{
            swap(left+2,left);
            if(array[left+2] > array[left+4]) swap(left+2,left+4);
        }
        if(array[left+2]>array[left+3]) swap(left+2,left+3);
        return left + 2;
    }
        
    public int medianOfThree(int left){
        if(array[left] > array[left + 2]){
            swap(left, left + 2);
        }
        if(array[left] > array[left+1]){
            swap(left, left + 1);
        }
        
        if(array[left + 1] > array [left + 2]){
            swap(left + 1, left + 2);
        }
        return left + 1;
    }
    
    public int medianOfMedians(int left, int right){
        if(right - left < 5) return array[left];
        int size = right - left;
        int fives = size/5;
        int rest = size%5;
        int numberOfIterations;
        for(numberOfIterations = 0; numberOfIterations<fives; numberOfIterations++){
            int currentmedian = medianPartitionOfFive(left + 5*numberOfIterations);
            swap(currentmedian, numberOfIterations);
        }
        if(rest > 2){
            int currentmedian = medianOfThree(right - rest+1);
            swap(currentmedian, numberOfIterations);
            numberOfIterations++;
        }
        this.printArray();
        //System.out.println(numberOfIterations+"\n");
        return medianOfMedians(left, left + numberOfIterations);
    }
}

public class Main{
    public static void main(String[] args){
        Random generator = new Random();
        int arraySize = 19;
        int[] strangeArray = {77,8,38,54,85,84,8,76,59,2,23,44,3,81,42,99,20,25,77};
        int[] array = new int[arraySize];
        for(int i = 0; i < arraySize; i++) array[i] = generator.nextInt(100)+1;
        Medians Mymedians = new Medians(array);
        Mymedians.printArray();
        Mymedians.medianOfMedians(0, Mymedians.getArrayLength()-1);
    }
}