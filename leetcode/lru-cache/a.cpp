
#include <map>
#include <cassert>

#ifndef NULL
#define NULL 0
#endif

struct Node {
    int key;
    int value;
    struct Node* prev;
    struct Node* next;
    Node(int k, int v) : key(k), value(v), prev(NULL), next(NULL) {}
};

typedef struct Node Node;

class LRUCache{
private:
    Node* mHead;
    Node* mTail;
    typedef std::map<int, Node*> NodeMap;
    NodeMap mDict;
    int mSize;
    int mCap;
    
public:
    LRUCache(int capacity) : mHead(NULL), mTail(NULL), mDict(), mSize(0), mCap(capacity) {
    }
    
    Node* getNode(int key) {
        check();
        NodeMap::iterator mit = mDict.find(key);
        if (mit != mDict.end()) {
            Node* it = mit->second;
            if (it != mTail) {
                if (it == mHead) {
                    mHead = it->next;
                } else {
                it->prev->next = it->next;
                }
                it->next->prev = it->prev;
                mTail->next = it;
                it->prev = mTail;
                it->next = NULL;
            }
            return it;
        }
        return NULL;
    }

    void check() {
        int s = 0;
        Node* it = mHead;
        while (it != NULL) {
            assert (it == mHead || it->prev != NULL);
            assert (it == mTail || it->next != NULL);
            s++;
            it = it->next;
        }
        assert (s == mSize);
    }
    
    int get(int key) {
        Node* node = getNode(key);
        if (node == NULL) {
            return -1;
        }
        return node->value;
    }
    
    void set(int key, int value) {
        Node* node = getNode(key);
        if (node != NULL) {
            if (node->value != value) {
                node->value = value;
            }
        } else {
            Node* new_node = new Node(key, value);
            mDict[key] = new_node;
            if (mHead == NULL) {
                mHead = new_node;
                mTail = mHead;
            } else {
                mTail->next = new_node;
                new_node->prev = mTail;
                mTail = new_node;
            }
            if (mSize >= mCap) {
                // delete
                Node* it = mHead;
                mHead = it->next;
                mHead->prev = NULL;
                mDict.erase(it->key);
                delete it;
            } else {
                mSize++;
            }
        }
    }
};

int main() {
    LRUCache cache(1);
    cache.set(2,1);
    cache.get(2);
    cache.set(3,2);
    cache.get(2);
    cache.get(3);
}
