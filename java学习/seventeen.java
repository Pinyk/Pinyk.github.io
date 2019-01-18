package ke;
/*foreach语句的应用
格式为for（元素变量：遍历对象）
      {
        引用元素的语句
       }
 */
public class seventeen {
    public static void main(String[] args)
    {
        int arr[]={7,10,1};
        System.out.println("一维数组中的元素分别为：");
        for(int x:arr)
        {
            System.out.println(x);
        }
    }
}
