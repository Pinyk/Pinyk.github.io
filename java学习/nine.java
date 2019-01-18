package ke;
//隐式类型转化
public class nine {
    public static void main(String[] args)
    {
        byte mybyte=127;
        int myint=150;
        float myfloat=452.12f;
        char mychar=10;
        double mydouble=45.46546;
        System.out.println("byte型和float型数据进行运算结果为："+(mybyte+myfloat));
        System.out.println("byte型和int型数据进行运算结果为："+mybyte*myint);
        System.out.println("byte型和char型数据进行运算结果为："+mybyte/mychar);
        System.out.println("double型和char型数据进行运算结果为："+(mydouble+mychar));
    }


}
