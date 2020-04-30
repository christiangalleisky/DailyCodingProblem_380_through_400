#include <iostream>

struct Node {
	int data;
	Node *next;
	Node(int data) {
		this->data = data;
		next = NULL;
	}
};

class LinkedList {
private:
	Node *top;
public:
	LinkedList();
	void addNode(int);
	Node* findKth(int);
	void printLL();
};

LinkedList::LinkedList() {
	top = NULL;
}

void LinkedList::addNode(int data) {
	Node *newElement = new Node(data);
	Node *curr = top;
	if (top == NULL) {
		top = newElement;
		newElement->next = NULL;
	}
	else if (top->next == NULL) {
		top->next = newElement;
		newElement->next = NULL;
	}
	else
	{
		while (curr->next != NULL) {
			curr = curr->next;
		}
		curr->next = newElement;
		newElement->next = NULL;
	}
}

void LinkedList::printLL() {
	Node *curr = top;
	while (curr != NULL) {
		std::cout << curr->data << std::endl;
		curr = curr->next;
	}
}

Node* LinkedList::findKth(int k) {
	int i = 0;
	Node* curr = top, *trailer = top, *temp = NULL;
	while (i < k) {
		curr = curr->next;
		i++;
	}
	if (curr == NULL) {
		temp = top;
		top = top->next;
		delete temp;
		return top;
	}
	while (curr->next != NULL) {
		curr = curr->next;
		trailer = trailer->next;
	}
	temp = trailer->next;
	trailer->next = trailer->next->next;
	delete temp;
	
	return top;
}

int main() {
	LinkedList ll;
	ll.addNode(0);
	ll.addNode(1);
	ll.addNode(2);
	ll.addNode(3);
	ll.addNode(4);
	ll.printLL();
	ll.findKth(5);
	std::cout << "LINKED LIST AFTER REMOVE Kth" << std::endl;
	ll.printLL();
	ll.findKth(1);
	std::cout << "LINKED LIST AFTER REMOVE Kth" << std::endl;
	ll.printLL();
	ll.findKth(3);
	std::cout << "LINKED LIST AFTER REMOVE Kth" << std::endl;
	ll.printLL();
	ll.findKth(1);
	std::cout << "LINKED LIST AFTER REMOVE Kth" << std::endl;
	ll.printLL();
	ll.findKth(1);
	std::cout << "LINKED LIST AFTER REMOVE Kth" << std::endl;
	ll.printLL();

	system("PAUSE");
	return 0;
}