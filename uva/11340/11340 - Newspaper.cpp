#include <iostream>
#include <map>
#include <string>


using namespace std;

int main() {
    int t, n, l, price, payment;
    char letter;
    string line;

    scanf("%d\n",&t);
    while (t--) {

        scanf("%d\n",&n);
        map<char, int> letters;
        while (n--) {
            scanf("%c %d\n", &letter, &price);
            letters[letter]= price;
        }

        payment=0;
        scanf("%d\n", &l);
        while(l--){
            getline(cin, line);
            for (int i=0; i< line.length(); i++){
                payment += letters[line[i]];
            }
        }

        printf("%.2f$\n", payment/100.0);
    }

    return 0;

}
