public class Node
{
    int data;
    Node next;

    Node(int data) {
        this.data = data;
        this.next = null;
    }
}
class SLL
{
    Node head;
    SLL()
    {
        head = null;
    }
    void insertAtHead(int value)
    {
        Node newNode = new Node(value);
        newNode.next = head;
        head = newNode;
    }
    void insertAtTail(int value)
    {
        Node newNode1 = new Node(value);
        if (head == null) {
            head = newNode1;
            return;
        }
        Node temp = head;
        while (temp.next != null) {
            temp = temp.next;
        }
        temp.next = newNode1;
    }

    void insertAtMiddle(int value, int pos)
    {
        Node newNode2 = new Node(value);
        Node temp = head;
        if (pos == 0) {
            insertAtHead(value);
            return;
        }

        else if (pos<0) {
            System.out.println("Position out of bounds");
            return;
        }
        else if (temp == null) {
            System.out.println("Position out of bounds");
            return;
        }

        while (--pos > 0)
        {
            temp = temp.next;
        }
        newNode2.next = temp.next;
        temp.next = newNode2;
    }
    void deleteAtHead()
    {
        if(head != null)
        {
            Node temp = head;
            head = head.next;
            temp = null;
        }
    }
    void deleteByVal(int val)
    {
        if(head == null)
            return;
        if(head.data==val)
        {
            deleteAtHead();
            return;
        }
        Node temp = head;
        while(temp.next!=null && temp.next.data!=val)
        {
            temp = temp.next;
        }
        if(temp.next==null)
        {
            System.out.println("No such element");
            return;
        }
        Node toDelete = temp.next;
        temp.next = temp.next.next;
        toDelete = null;
    }
    void printLL()
    {
        Node temp = head;
        while (temp != null)
        {
            System.out.print(temp.data+ "->");
            temp = temp.next;
        }
        System.out.println("NULL");
    }
}
class DriverCode
{
    public static void main(String[] args)
    {
        SLL sll = new SLL();
        sll.insertAtHead(10);
        sll.insertAtHead(20);
        sll.insertAtHead(30);
        sll.insertAtHead(40);
        sll.printLL();

        sll.insertAtTail(50);
        sll.printLL();

        sll.insertAtMiddle(500,-1);
        sll.printLL();

        sll.deleteAtHead();
        sll.printLL();

        sll.deleteByVal(10);
        sll.printLL();
    }
}
