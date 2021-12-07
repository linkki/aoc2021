#include<stdlib.h>
#include<string.h>
#include"lanternfish.h"
#include"../c-utils/arrayutils.h"

long* parse_countdown(int* initial_states, int len_states) {
    long* countdowns = malloc(9 * sizeof(long));
    memset(countdowns, 0, 9*sizeof(long));

    for (int i=0; i<len_states; i++) {
        long current_state = initial_states[i];
        if (current_state != -1) {
            countdowns[current_state] = countdowns[current_state] + 1;
        }
    }
    return countdowns;
}

long count_after_n_days(long* countdowns, int days) {
    int day = 0;
    while (day++<days) {
        advance_day(countdowns);
    }
    return long_sum(countdowns, 9);
}

void advance_day(long* countdowns) {
    long new_fish = countdowns[0];

    // handle fish that do not make babies
    for (int i=0; i<8; i++) {
        countdowns[i] = countdowns[i+1];
    }

    // handle new fish
    countdowns[8] = new_fish;
    countdowns[6] = countdowns[6] + new_fish;
}
