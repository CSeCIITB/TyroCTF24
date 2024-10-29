#include <stdarg.h>
#include <stdio.h>

int main(int argc, char const *argv[]) {
  char str[512];
  char garbage[1000];
  char line[256];
  int i;
  int j = 0;
  // Now we take input from the user
  // We want the str to be 71m_4774ck
  // 71m3_53r135_4774ck5_4r3_fun_4nd_7h3y_54v3_l1v35
  // Now to avoid being detected from unix strings we will store the string into
  // the buffer in a random order, charecter by charecter.
  // garbage:
  // "r1bozskn33p81tfnpta0n3jf3_arq7b6h03ykf_iktr1hgp7xksk5h1woyx33q2wm2unhrdjue0ejzgli4qwdu_9_l_y7orqyuql"
  garbage[0] = 'r';
  garbage[1] = '1';
  garbage[2] = 'b';
  garbage[3] = 'o';
  garbage[4] = 'z';
  garbage[5] = 's';
  garbage[6] = 'k';
  garbage[7] = 'n';
  garbage[8] = '3';
  garbage[9] = '3';
  garbage[10] = 'p';
  garbage[11] = '8';
  garbage[12] = '1';
  garbage[13] = 't';
  garbage[14] = 'f';
  garbage[15] = 'n';
  garbage[16] = 'p';
  garbage[17] = 't';
  garbage[18] = 'a';
  garbage[19] = '0';
  garbage[20] = 'n';
  garbage[21] = '3';
  garbage[22] = 'j';
  garbage[23] = 'f';
  garbage[24] = '3';
  garbage[25] = '_';
  garbage[26] = 'a';
  garbage[27] = 'r';
  garbage[28] = 'q';
  garbage[29] = '7';
  garbage[30] = 'b';
  garbage[31] = '6';
  garbage[32] = 'h';
  garbage[33] = '0';
  garbage[34] = '3';
  garbage[35] = 'y';
  str[9] = '3';
  str[2] = 'm';
  str[31] = '_';
  str[10] = '5';
  str[41] = '_';
  str[11] = '_';
  str[35] = 'y';
  str[30] = 'd';
  str[32] = '7';
  str[3] = '3';
  str[1] = '1';
  str[33] = 'h';
  str[43] = '1';
  str[18] = '5';
  str[14] = '7';
  str[13] = '7';
  str[47] = '\0';
  str[25] = 'u';
  str[39] = 'v';
  str[15] = '4';
  str[28] = '4';
  str[27] = '_';
  str[42] = 'l';
  str[19] = '_';
  str[21] = 'r';
  str[24] = 'f';
  str[16] = 'c';
  str[46] = '5';
  str[34] = '3';
  str[8] = '1';
  str[4] = '_';
  str[6] = '3';
  str[20] = '4';
  str[17] = 'k';
  str[38] = '4';
  str[29] = 'n';
  str[7] = 'r';
  str[0] = '7';
  str[36] = '_';
  str[5] = '5';
  str[12] = '4';
  str[40] = '3';
  str[44] = 'v';
  str[37] = '5';
  str[45] = '3';
  str[22] = '3';
  str[26] = 'n';
  str[23] = '_';

  printf("You wil never crack this fortress \n");
  if (fgets(line, sizeof(line), stdin)) {
    /* i can be safely used */
    // Now for each matching charecter we will wait for 1 second.
    int k = 0;
    while (str[k] != '\0' && line[k] != '\0') {
      if (str[k] == line[k]) {
        j = 0;
        while (j < 300000) {
          j++;
        }
      }
      k++;
    }
  }
  return 0;
}
