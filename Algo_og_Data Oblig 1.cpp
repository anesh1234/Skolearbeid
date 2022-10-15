#include <stack>
#include <iostream>

class Node {
public:
    int val;
    Node* left;
    Node* right;
    Node(int key) : val(key), left(nullptr), right(nullptr) {}
};

void insertNode(Node*& root, int key)
{
    Node* node = new Node(key);

    if (root == 0) {
        root = node;
        return;
    }

    Node* prev = nullptr;
    Node* temp = root;

    while (temp) {
        if (temp->val > key) {
            prev = temp;
            temp = temp->left;
        }
        else if (temp->val < key) {
            prev = temp;
            temp = temp->right;
        }
    }
    if (prev->val > key)
        prev->left = node;
    else
        prev->right = node;
}


void printPreorder(Node* root)
{
    Node* temp = root;

    if (root == nullptr) return;

    std::cout << temp->val << " ";

    printPreorder(temp->left);

    printPreorder(temp->right);
}


Node* search(Node* root, int key)
{
    if (root == nullptr || root->val == key)
        return root;

    if (root->val < key)
        return search(root->right, key);

        return search(root->left, key);
}


int main()
{
    Node* root = nullptr;

    insertNode(root, 8);
    insertNode(root, 3);
    insertNode(root, 1);
    insertNode(root, 6);
    insertNode(root, 4);
    insertNode(root, 7);
    insertNode(root, 10);
    insertNode(root, 14);
    insertNode(root, 13);

    Node* resultat = search(root, 6);

    std::cout << "I searched for int 6 in the tree, I got: " << resultat->val
        << "  At address: " << resultat << std::endl << "Preorder traversal : ";

    printPreorder(root);
    std::cout << std::endl;
}