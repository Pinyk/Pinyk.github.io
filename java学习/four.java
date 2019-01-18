package ke;
//输出某些字符的unicode码
public class four {
    public static void main(String[] args)
    {
        char word = 'd',word2='@';
        int p=23045,p2=45213;
        System.out.println("d在unicode表的顺序位置是："+(int)word);
        System.out.println("@在unicode表的顺序位置是："+(int)word2);
        System.out.println("unicode表中23045位是："+(char)p);
        System.out.println("unicode表中45213位是："+(char)p2);
    }
}
