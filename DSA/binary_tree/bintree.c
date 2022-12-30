// implement a binary tree

#include <stdio.h>
#include <stdlib.h>
#include <time.h>

typedef struct node {
    int data;
    struct node *left;
    struct node *right;
} node;

node *createNode(int data) {
    node *newNode = (node *)malloc(sizeof(node));
    newNode->data = data;
    newNode->left = NULL;
    newNode->right = NULL;
    return newNode;
}

node *insertNode(node *root, int data) {
    if (root == NULL) {
        root = createNode(data);
    } else if (data <= root->data) {
        root->left = insertNode(root->left, data);
    } else {
        root->right = insertNode(root->right, data);
    }
    return root;
}

int searchNode(node *root, int data) {
    if (root == NULL) {
        return 0;
    } else if (root->data == data) {
        return 1;
    } else if (data <= root->data) {
        return searchNode(root->left, data);
    } else {
        return searchNode(root->right, data);
    }
}

void Inorder(node *root) {
    if (root == NULL) {
        return;
    }

    Inorder(root->left);
    printf("%d->", root->data);
    Inorder(root->right);
}

void Preorder(node *root){
    if(root == NULL){
        return;
    }
    printf("%d->", root->data);
    Preorder(root->left);
    Preorder(root->right);

}

// populate a tree with random numbers

node *populate_tree(node *root, int n, int max) {
    srand(time(NULL));
    for (int i = 0; i < n; i++) {
        int data = rand() % max;
        root = insertNode(root, data);
    }

    return root;
}


int main() {
    node *root = NULL;

    root = populate_tree(root, 10, 100);

    insertNode(root, 10);
    

    Inorder(root);
}