#include <iostream>
#include <string>
#include <algorithm>

using namespace std;

void permutation(string input, int start) {
    int l = input.length();
    
    if (start >= l){
        cout << input << "\n";
    } else {
        permutation(input, start + 1);
    }
    
    for (int i = start + 1; i < l; i++){
	string newinput(input);
        swap(newinput[start], newinput[i]);
        permutation(newinput, start + 1);
    }
}

int main(){
	string input;
	getline(std::cin, input);
	permutation(input, 0);
}
