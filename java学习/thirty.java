package ke;
//判断字符串是否相等的函数
public class thirty {
    public static void main(String args[])
    {
        String s1=new String("abc");
        String s2=new String("ABC");
        String s3=new String("abc");
        boolean b=s1.equals(s2);//区分大小写
        boolean b3=s1.equals(s3);
        boolean b2=s1.equalsIgnoreCase(s2);//不区分大小写
        System.out.println(s1+"equals"+s2+":"+b);
        System.out.println(s1+"equalsIgnoreCase"+s2+":"+b2);
        System.out.println(s1+"equals"+s3+":"+b3);
    }
}
