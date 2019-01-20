package ke;
//字符串的替换函数
public class twentyeight {
    public static void main(String args[])
    {
        String str="java project";
        String newstr=str.replace("p","P");
        System.out.println(newstr);
        String newstr1=str.replace("j","J");//如果有多个出现全部替换
        System.out.println(newstr1);
    }
}
