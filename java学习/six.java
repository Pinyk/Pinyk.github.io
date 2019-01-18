package ke;
//成员变量和局部变量名字相同时，成员变量将被隐藏
public class six {
    static int times=3;
    public static void main(String[] args)
    {
        int times=4;
        System.out.println("times值为："+times);
    }


}
