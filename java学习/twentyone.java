package ke;
//字符串创建的三种方式
public class twentyone {
    public static void main(String[] args)
    {
        char a[]={'g','o','o','d'};
        String b=new String(a);//等价于String b=new String("good")
        System.out.println(b);
        char c[]={'s','t','u','d','e','n','t'};
        String d=new String(c,2,4);
        System.out.println(d);
        String e;
        e="we are family";
        System.out.println(e);
    }

}
