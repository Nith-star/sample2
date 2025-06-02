public class DNode {
    int data;
    DNode prev, next;

    DNode(int data) {
        this.data = data;
        this.prev = null;
        this.next = null;
    }
}

class DLL {
    DNode head;

    DLL() {
        head = null;
    }

    void insertAtHead(int value) {
        DNode newNode = new DNode(value);
        if (head != null) {
            newNode.next = head;
            head.prev = newNode;
        }
        head = newNode;
    }

    void insertAtTail(int value) {
        DNode newNode = new DNode(value);
        if (head == null) {
            head = newNode;
            return;
        }
        DNode temp = head;
        while (temp.next != null) {
            temp = temp.next;
        }
        temp.next = newNode;
        newNode.prev = temp;
    }

    void insertAtMiddle(int value, int pos) {
        if (pos < 0) {
            System.out.println("Position out of bounds");
            return;
        }
        if (pos == 0 || head == null) {
            insertAtHead(value);
            return;
        }

        DNode newNode = new DNode(value);
        DNode temp = head;
        while (--pos > 0 && temp.next != null) {
            temp = temp.next;
        }
        if (pos > 0) {
            System.out.println("Position out of bounds");
            return;
        }
        newNode.next = temp.next;
        if (temp.next != null)
            temp.next.prev = newNode;
        newNode.prev = temp;
        temp.next = newNode;
    }

    void deleteAtHead() {
        if (head != null) {
            DNode temp = head;
            head = head.next;
            if (head != null)
                head.prev = null;
            temp = null;
        }
    }

    void deleteAtEnd() {
        if (head == null)
            return;

        if (head.next == null) {
            head = null;
            return;
        }

        DNode temp = head;
        while (temp.next != null) {
            temp = temp.next;
        }
        temp.prev.next = null;
        temp = null;
    }

    void deleteAtPos(int pos) {
        if (pos < 0 || head == null) {
            System.out.println("Position out of bounds");
            return;
        }
        if (pos == 0) {
            deleteAtHead();
            return;
        }

        DNode temp = head;
        while (pos-- > 0 && temp != null) {
            temp = temp.next;
        }

        if (temp == null) {
            System.out.println("Position out of bounds");
            return;
        }

        if (temp.next != null)
            temp.next.prev = temp.prev;
        if (temp.prev != null)
            temp.prev.next = temp.next;
        temp = null;
    }

    void deleteByVal(int val) {
        if (head == null)
            return;

        if (head.data == val) {
            deleteAtHead();
            return;
        }

        DNode temp = head;
        while (temp != null && temp.data != val) {
            temp = temp.next;
        }

        if (temp == null) {
            System.out.println("No such element");
            return;
        }

        if (temp.prev != null)
            temp.prev.next = temp.next;
        if (temp.next != null)
            temp.next.prev = temp.prev;
        temp = null;
    }

    void printDLL() {
        DNode temp = head;
        while (temp != null) {
            System.out.print(temp.data + "->");
            temp = temp.next;
        }
        System.out.println("NULL");
    }
}

class DriverCodeDLL {
    public static void main(String[] args) {
        DLL dll = new DLL();

        dll.insertAtHead(10);
        dll.insertAtHead(20);
        dll.insertAtHead(30);
        dll.insertAtHead(40);
        dll.printDLL();

        dll.insertAtTail(50);
        dll.printDLL();

        dll.insertAtMiddle(500, 2);
        dll.printDLL();

        dll.deleteAtHead();
        dll.printDLL();

        dll.deleteAtEnd();
        dll.printDLL();

        dll.deleteAtPos(1);
        dll.printDLL();

        dll.deleteByVal(20);
        dll.printDLL();
    }
}
