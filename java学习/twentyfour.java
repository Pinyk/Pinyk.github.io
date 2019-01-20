package ke;
//当lastindexof的参数为空字符则返回值为该字符串的长度
public class twentyfour {
    public static void main(String[] args)
    {
        String a="We are students";
        int c=a.indexOf("a");
        int b=a.lastIndexOf("");
        System.out.println("a在字符串中的位置是"+c);
        System.out.println("空字符在字符串中的索引位置是"+b);
        System.out.println("字符串长度为"+a.length());

    }
}
