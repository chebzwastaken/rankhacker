#include <iostream>
#include <sstream>
using namespace std;

/*
Enter code for class Student here.
Read statement for specification.
*/

class Student
{
    private:
        int age, standard;
        string first_name, last_name;
    public:
        void set_age(int a) { age = a; }
        void set_standard(int s) { standard = s; }
        void set_first_name(string fn) { first_name = fn; }
        void set_last_name(string ln) { last_name = ln; }
        int get_age() { return age; }
        int get_standard() { return standard; }
        string get_first_name() { return first_name; }
        string get_last_name() { return last_name; }
        string to_string() {
            stringstream ss;
            ss << age << "," << first_name << "," << last_name << "," << standard;
            return ss.str();
        }
};

class Box
{
    private:
        int l, b, h;
    public:
        Box() {
            l = 0;
            b = 0;
            h = 0;
        }
        Box(int length, int breadth, int height) {
            l = length;
            b = breadth;
            h = height;
        }
        Box(const Box& B) {
            l = B.l;
            b = B.b;
            h = B.h;
        }
        int getLength() { return l; }
        int getBreadth() { return b; }
        int getHeight() { return h; }
        long long CalculateVolume() { return (long long)l * b * h; }
        bool operator<(Box& B) {
            if (l < B.l) {
                return true;
            } else if (b < B.b && l == B.l) {
                return true;
            } else if (h < B.h && b == B.b && l == B.l) {
                return true;
            } else {
                return false;
            }
        }
        friend ostream& operator<<(ostream& out, Box& B) {
            out << B.l << " " << B.b << " " << B.h;
            return out;
        }   
};

int main()
{
    int age, standard;
    string first_name, last_name;

    cin >> age >> first_name >> last_name >> standard;

    Student st;
    st.set_age(age);
    st.set_standard(standard);
    st.set_first_name(first_name);
    st.set_last_name(last_name);

    cout << st.get_age() << "\n";
    cout << st.get_last_name() << ", " << st.get_first_name() << "\n";
    cout << st.get_standard() << "\n";
    cout << "\n";
    cout << st.to_string();

    return 0;
}