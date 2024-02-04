//
// Created by KAVOSH on 2/4/2024.
//
#ifndef UNFICATIONALGOL_RESOLMEM_HPP
#define UNFICATIONALGOL_RESOLMEM_HPP
#include <vector>
#include <string>


// the class is a representor of two entries
// variable or a constant.
class EntryCoVar{
public:

    explicit EntryCoVar(std::string& entryName)
    :entryName_p(entryName)
    {}

    explicit EntryCoVar(std::string&& entryName)
    :entryName_p(entryName)
    {}

    const std::string& getName()const{return entryName_p;}

    friend bool operator == (const EntryCoVar& x1, const EntryCoVar& x2){return x1.entryName_p == x2.entryName_p;}
private:
    std::string entryName_p;
};

class EntryFuncList;

struct CompEntryFCV{

    enum TYPE{
        UNI_VARIABLE,
        UNI_CONSTANT,
        UNI_FUNCTION,
        UIN_LIST,
    };

    TYPE tag;
    EntryCoVar* cv{nullptr};
    EntryFuncList* fl{nullptr};
};


// the class is made to represent functions or lists
//  are considered special case of functions with
// name space name " "
class EntryFuncList: EntryCoVar{
public:
    explicit EntryFuncList(std::string& entryName)
            :EntryCoVar(entryName)
    {}

    explicit EntryFuncList(std::string&& entryName = " ")
            :EntryCoVar(entryName)
    {}


    using CompE = std::vector<CompEntryFCV>;

    CompE::const_iterator begin()const{return members_p.begin();}
    CompE::iterator begin(){return members_p.begin();}
    CompE::iterator end(){return members_p.begin();}
    CompE::const_iterator end()const{return members_p.begin();}

    void push_back(CompEntryFCV& x){members_p.push_back(x);}
    void push_back(CompEntryFCV&& x){members_p.push_back(x);}
private:
    CompE members_p;
};
#endif //UNFICATIONALGOL_RESOLMEM_HPP
