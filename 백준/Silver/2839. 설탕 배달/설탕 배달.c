#include <stdio.h>

int main(void) {
    int N;
    scanf("%d", &N);
    int cnt = 0;
    while (1) {
        if (N % 5 == 0) {
            cnt += N / 5;
            break;
        }
        N -= 3;
        cnt++;
    }
    if (N < 0) printf("-1");
    else printf("%d", cnt);
    return 0;
}