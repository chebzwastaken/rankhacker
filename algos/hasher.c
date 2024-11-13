/*making a hash table*/
#include <stdlib.h> 

typedef struct HashNode {
  char *key; 
  int value;
  struct HashNode *next;
} HashNode; 

typedef struct HashTable {
  HashNode **buckets; 
  int size; 
  int count; 
} HashTable; 

unsigned long hash_function(const char *str) {
  unsigned long hash = 5381; 
  int c; 
  while ((c = *str++))
    hash = ((hash << 5) + hash) + c; 
  return hash;
}

HashTable* create_table(int size) {
  HashTable *table = malloc(sizeof(HashTable));
  table->buckets = malloc(sizeof(HashNode*) * size);
  table->size = size; 
  table->count = 0; 

  for (int i = 0; i < size; i++){
    table->buckets[i] = NULL; 
  }

  return table; 
}

void insert(HashTable *table, const char *key, int value) {

}

float load_factor(HashTable *table) {
  return 0.0;
}



