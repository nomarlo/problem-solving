#include <iostream>
#include <vector>
#include <string>
#include <algorithm>


using namespace std;

int main() {
    int t = 0, n = 0;

    scanf("%d",&t);

    while (t--) {
        scanf("%d",&n);
        vector<string> phoneList;
        while (n--) {
            char sNumber[10];
            scanf("%s",&sNumber);
            phoneList.push_back(sNumber);
        }

        sort(phoneList.begin(), phoneList.end());
        bool prefixFree = true;
        for(int i = 0; i< phoneList.size() - 1; i++){
             if (phoneList[i+1].find(phoneList[i]) == 0){
                 prefixFree = false;
                 break;
             }

        }

        if (prefixFree) {
            printf("YES\n");
        } else {
            printf("NO\n");
        }
    }

    return 0;
}

// Solution using a SET
//
// #include <iostream>
//#include <set>
//#include <string>
//#include <algorithm>
//
//
//using namespace std;
//
//int main() {
//    int t = 0, n = 0;
//
//    scanf("%d",&t);
//
//    while (t--) {
//        scanf("%d",&n);
//        set<string> phoneList;
//        while (n--) {
//            char sNumber[10];
//            scanf("%s",&sNumber);
//            phoneList.insert(sNumber);
//        }
//
//        bool prefixFree = true;
//        for (auto phoneNumber : phoneList) {
//            if (prefixFree) {
//                string prefix = "";
//
//                for (int i = 0; i < phoneNumber.length() - 1; i++) {
//                    prefix += phoneNumber[i];
//                    if (phoneList.find(prefix) != phoneList.end()) {
//                        prefixFree = false;
//                        break;
//                    }
//                }
//            }
//        }
//
//        if (prefixFree) {
//            printf("YES\n");
//        } else {
//            printf("NO\n");
//        }
//    }
//
//    return 0;
//}
