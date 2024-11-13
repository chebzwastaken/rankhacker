/*making a hash table*/
#include <stdlib.h> 
#include <string.h>

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
  unsigned long index = hash_function(key) % table->size;
  HashNode *new_node = malloc(sizeof(HashNode));
  new_node->key = strdup(key);
  new_node->value = value; 
  new_node->next = table->buckets[index];

  table->buckets[index] = new_node;
  table->count++;
}

float load_factor(HashTable *table) {
  return (float)table->count / table->size; 
}

void rehash(HashTable **table) {
  int old_size = (*table)->size;
  HashTable *new_table = create_table(old_size * 2); 

  for ( int i = 0; i < old_size; i++) {
    HashNode *node = (*table)->buckets[i];
    while (node) {
      insert(new_table, node->key, node->value);
      node = node->next;
    }
  }

  free(*table);
  *table = new_table;
}

int search(HashTable *table, const char *key) {
  unsigned long index = hash_function(key) % table->size; 
  HashNode *node = table->buckets[index];

  while (node) {
    if (strcmp(node->key, key) == 0) {
      return node->value; 
    }
    node = node->next;
  }

  return -1;
}

void delete(HashTable *table, const char *key) {
  unsigned long index = hash_function(key) % table->size;
  HashNode *node = table->buckets[index];
  HashNode *prev = NULL;

  while (node) {
    if (strcmp(node->key, key) == 0) {
      if (prev) {
        prev->next = node->next;
      } else {
        table->buckets[index] = node->next; 
      } 

      free(node->key);
      free(node);

      table->count--;
      return; 
    }
    prev = node; 
    node = node->next; 
  }
}


