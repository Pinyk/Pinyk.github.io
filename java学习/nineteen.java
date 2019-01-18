package ke;
/*
标签名：循环体{
                 break 标签名；
                }
 */
public class nineteen {
    public static void main(String[] args)
    {
        Loop:for(int i=0;i<3;i++)
        {
            for(int j=0;j<6;j++)
            {
                if(j==4)
                {
                    break Loop;
                }
                System.out.println("i="+i + "j="+j);
            }
        }
    }
}
