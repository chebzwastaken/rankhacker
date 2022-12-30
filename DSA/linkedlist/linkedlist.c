#include <stdio.h>
#include <stdlib.h>

typedef struct node {
    int data;
    struct node *next;
} node;

// typedef struct linkedList {
//     struct node *head;
//     static node *tail;
// } linkedList

node *createNode(int data) {
    node *newNode = (node *)malloc(sizeof(node));
    newNode->data = data;
    newNode->next = NULL;

    return newNode
}

node *insertNode(node *head, int data){
    if (head == NULL) {
        head = createNode(data);
    } else {
        root->next = insertNode(root->next, data);
    }
    return head
}

node *removeNode(node *head, int data) {
    if (head == NULL) {
        return;
    } else {
        if (head->data == data) {
            head = head->next;
        } else {
            head->next = removeNode(head->next, data);
        }
    }

    return head;
}


int searchNode(node *head, int data) {
    if (head == NULL) {
        return 0;
    } else if (head->data == data) {
        return 1;
    } else {
        return searchNode(head->next, data);
    }
}

void printList(node *head) {
    if (head == NULL) {
        return;
    }

    printf("%d->", head->data);
    printList(head->next);
}

int main() {
    node *head = NULL;
    head = insertNode(head, 5);
    head = insertNode(head, 4);
    head = insertNode(head, 3);
    head = insertNode(head, 2);
    head = insertNode(head, 1);

    printList(head);
}







