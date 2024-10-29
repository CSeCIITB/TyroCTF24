// The binary from which the challenge was derived
#include <stdio.h>
#include <stdlib.h>

int main() {
  int weights[] = {21, 27, 17, 11, 38, 50, 33, 19, 30, 89, 7,  15, 93, 3,
                   92, 47, 70, 66, 44, 6,  70, 0,  0,  72, 11, 22, 5,  31};
  char encoded[] = "abcdefghijklmnopqrstuvwxyzab";
  char flag[] = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaa";
  for (int i = 0; i < 28; i++) {
    flag[i] = encoded[i];
  }
  for (int i = 0; i < 28; i++) {
    for (int j = 0; j < 1000000000; j++) {
      for (int k = 0; k < 1000000000; k++) {
        flag[i] = flag[i] ^ weights[i];
      }
    }
    for (int j = 0; j < 1000000000; j++) {
      flag[i] = flag[i] ^ weights[i];
    }
    flag[i] = flag[i] ^ weights[i];
    printf("%c", flag[i]);
  }
}
