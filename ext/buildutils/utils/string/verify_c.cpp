#include <iostream>
#include <regex>
#include <string>
#include "verify_c.h"
bool email_c(const std::string& str){
    std::regex r("^\\w+([-+.]\\w+)*@\\w+([-.]\\w+)*\\.\\w+([-.]\\w+)*$");
    std::smatch matches;//result
    if (std::regex_search(str, matches, r)) {
        return matches.str() == str;
    }
    else{
        return false;
    }
    
}

bool ipv4_c(const std::string& str){
    std::regex r("((2(5[0-5]|[0-4]\\d))|[0-1]?\\d{1,2})(\\.((2(5[0-5]|[0-4]\\d))|[0-1]?\\d{1,2})){3}");
    std::smatch matches;//result
    if (std::regex_search(str, matches, r)) {
        return matches.str() == str;
    }
    else{
        return false;
    }
    
}
