#include <iostream>
using namespace std;

class Node {
public:
    int data;
    Node* next;
    Node(int val) : data(val), next(nullptr) {}
};

class Stack {
private:
    Node* head;   
    int size;     
    int capacity; 

public:
    Stack(int initialCapacity) {
        head = nullptr;
        size = 0;
        capacity = initialCapacity;
    }

    void push(int x) {
        if (size >= capacity) {
            increaseCapacity();
        }
        Node* newNode = new Node(x);
        newNode->next = head;
        head = newNode;
        size++;
    }

    int pop() {
        if (isEmpty()) {
            cout << "Stack underflow!" << endl;
            return -1;
        }
        int topValue = head->data;
        Node* temp = head;
        head = head->next;
        delete temp;
        size--;
        return topValue;
    }

    int peek() {
        if (isEmpty()) {
            cout << "Stack is empty!" << endl;
            return -1;
        }
        return head->data;
    }

    bool isEmpty() {
        return size == 0;
    }

    void increaseCapacity() {
        capacity *= 2;
        cout << "Stack capacity increased to: " << capacity << endl;
    }

    bool deleteElement(int val) {
        if (isEmpty()) return false;
        Node* temp = head;
        Node* prev = nullptr;

        while (temp != nullptr) {
            if (temp->data == val) {
                if (prev == nullptr) {
                    head = temp->next;
                } else {
                    prev->next = temp->next;
                }
                delete temp;
                size--;
                return true;
            }
            prev = temp;
            temp = temp->next;
        }
        return false;
    }

    void printStack() {
        Node* temp = head;
        while (temp != nullptr) {
            cout << temp->data << " -> ";
            temp = temp->next;
        }
        cout << "NULL" << endl;
    }
};

int main() {
    Stack s(3);
    s.push(10);
    s.push(20);
    s.push(30);
    s.printStack();
    s.push(40);
    s.printStack();
    
    cout << "Top element: " << s.peek() << endl;
    s.pop();
    s.printStack();
    
    s.deleteElement(20);
    s.printStack();
    
    return 0;
}
