package ke;
/*
for循环遇到continue时首先执行循环的增量部分，在while和dowhile中，continue语句时控制直接回到条件测试部分
continue也支持标签功能，使用方法和break一样
 */
public class twenty {
    public static void main(String[] args)
    {
        for(int i=1;i<20;i++)
        {
            if(i%2==0)
            {
                continue;
            }
            System.out.println(i);
        }
    }

}
