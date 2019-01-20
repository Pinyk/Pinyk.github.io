package ke;
//除去字符串前置和后置空格函数   ps：字符串中间的空格不可以除去
public class twentyseven {
    public static void main(String args[])
    {
        String a="  java  class   ";
        String b=a.trim();
        System.out.println("字符串原来的长度为："+a.length());
        System.out.println("字符串现在的长度为："+b.length());
    }
}
