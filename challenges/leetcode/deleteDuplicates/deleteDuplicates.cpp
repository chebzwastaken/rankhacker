class Solution {
    public:
    ListNode* deleteDuplicates(ListNode* head) {
        if (head == NULL) return NULL;
        ListNode* p = head;
        while (p->next != NULL) {
            if (p->val == p->next->val) {
                p->next = p->next->next;
            } else {
                p = p->next;
            }
        }
        return head;
    }
};


int main() {
    Solution s;
    ListNode* head = new ListNode(1);
    ListNode* p = head;
    p->next = new ListNode(1);
    p = p->next;
    p->next = new ListNode(2);
    p = p->next;
    p->next = new ListNode(3);
    p = p->next;
    p->next = new ListNode(3);
    p = p->next;
    p->next = new ListNode(4);
    p = p->next;
    p->next = new ListNode(4);
    p = p->next;
    p->next = new ListNode(5);
    p = p->next;
    p->next = new ListNode(5);
    p = p->next;
    p->next = new ListNode(6);
    p = p->next;
    p->next = new ListNode(6);
    p = p->next;
    p->next = new ListNode(7);
    p = p->next;
    p->next = new ListNode(7);
    p = p->next;
    p->next = new ListNode(8);
    p = p->next;
    p->next = new ListNode(8);
    p = p->next;
    p->next = new ListNode(9);
    p = p->next;
    p->next = new ListNode(9);
    p = p->next;
    p->next = new ListNode(10);
    p = p->next;
    p->next = new ListNode(10);
    p = p->next;
    p->next = new ListNode(11);
    p = p->next;
    p->next = new ListNode(11);
    p = p->next;
    p->next = new ListNode(12);
    p = p->next;
    p->next = new ListNode(12);
    p = p->next;
    p->next = new ListNode(13);
    p = p->next;
    p->next = new ListNode(13);
    p = p->next;
    p->next = new ListNode(14);
    p = p->next;
    p->next = new ListNode(14);
    p = p->next;
    p->next = new ListNode(15);
    p = p->next;
    p->next = new ListNode(15);
    p = p->next;

    