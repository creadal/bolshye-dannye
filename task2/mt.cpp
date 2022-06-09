#include <thread>
#include <fstream>
#include <vector>
#include <string>
#include <iostream>
#include <cmath>

#define NUM_THREADS 4

int factorize(long long n) {
    std::vector<int> result;
    long long d = 2;
    while (d * d <= n) {
        if (n % d == 0) {
            result.push_back(d);
            n /= d;
        }
        else d++;
    }
        
    if (n > 1)
        result.push_back(n);

    return result.size();
}

long long mystol(std::string input) {
    long long r = 0;
    for (int i = input.size()-1; i >= 0; i--) {
        r += (input[i] - 48) * std::pow(10, input.size() - i - 1);
    }
    return r;
}

void factorize_mt(long long *numbers, int start, int finish, int *result, int idx) {
    result[idx] = 0;
    for (int i = start; i < finish; i++) {
        result[idx] += factorize(numbers[i]);
    }
}

int main() {
    std::string line;
    std::ifstream ifs;
    ifs.open("numbers.txt", std::ios::in);

    long long numbers[2000];
    int i = 0;

    if (ifs.is_open()) {
        std::string tp;
        while (getline(ifs, tp)) {
            numbers[i] = mystol(tp);
            i++;
        }
        ifs.close();
    }

    std::thread pool[NUM_THREADS];
    int result[NUM_THREADS];
    for (int i=0; i<NUM_THREADS; i++) {
        pool[i] = std::thread(factorize_mt, numbers, i*2000/NUM_THREADS, (i+1)*2000/NUM_THREADS, result, i);
    }

    for (int i=0; i<NUM_THREADS; i++) {
        pool[i].join();
    }

    int sum = 0;
    for (int i=0; i<NUM_THREADS; i++) {
        sum += result[i];
    }

    printf("%d", sum);
}