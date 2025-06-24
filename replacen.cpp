#include<iostream>
#include<fstream>
#include<string>

int main(int argc, char** argv)
{
    if(argc!=2)
    {
        std::cout<<"使用方法: "<<argv[0]<<" filename"<<std::endl;
        std::cout<<"一般情况下你可能需要使用>或>>重定向符号将输出保存到文件中。"<<std::endl;
        return 1;
    }
    std::ifstream readfile(argv[1], std::ios::in);
    char c;
    while(readfile.get(c))
    {
        if(!(c=='\n'))
        {
            std::putchar(c);
        }
       
    }
}