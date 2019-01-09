#include<stdio.h>
#include<stdlib.h>

typedef int ElementType;        //    ������������,�ɸ�����Ҫ�����������Ͷ���
                                //    ����ڵ�Ķ���
typedef struct ListNode {
    ElementType  Element;        //    �����򣬴������
    ListNode* Next;        //    ָ����һ������ڵ�
}Node, *PNode;

//    ��������
PNode CreateList(void);    //    ��������������
void TraverseList(PNode List);    //    ��������������
void InsertList(PNode List, int pos, int val);        //    ����������뺯��
void DeleteTheList(PNode List);    //    ����ɾ������������
void DeleteList(PNode List, int pos);    //    ����ɾ������Ԫ�غ���
PNode FindList(PNode List);    //    ���������ѯ����

//    ������ 
int main() {
    PNode List = CreateList();    //    ����һ��ָ�룬ʹ��ָ���´����������ͷָ��    
    TraverseList(List);        //    ��������
    FindList(List);        //    �����ѯ    
    InsertList(List, 3, 100);    //    ������룬�ڵ�����λ�ò�����ֵ100
    TraverseList(List);
    DeleteList(List, 3);    //    ɾ������������ڵ�
    TraverseList(List);
    DeleteTheList(List);    //    ɾ����������
    TraverseList(List);
    return 0;
}

//    ��������������
PNode CreateList(void) {
    int len ;    //    ���ڶ���������
    int val ;    //    ���ڴ�Žڵ���ֵ
    PNode PHead = (PNode)malloc(sizeof(Node));    //    ��������һ��ͷ�ڵ��ڴ�ռ�
    if (PHead == NULL)    //    �ж��Ƿ����ɹ�
    {
        printf("�ռ����ʧ�� \n");
        exit(-1);
    }

    PNode PTail = PHead;    //    �����ĩβ�ڵ㣬��ʼָ��ͷ�ڵ�
    PTail->Next = NULL;    //    ���һ���ڵ�ָ����Ϊ��
    printf("������ڵ������");
    scanf("%d", &len);        //    ����ڵ����
    for (int i = 0; i < len; i++) {

        PNode PNew = (PNode)malloc(sizeof(Node));    //    ����һ���½ڵ�
        if (PNew == NULL) {
            printf("�����½ڵ�ʧ��\n");
            exit(-1);
        }
        printf("������� %d ���ڵ�����ݣ�", i + 1);
        scanf("%d", &val);    //    ��������ڵ������

        PNew->Element = val;    //    �����ݸ�ֵ���ڵ�������
        PTail->Next = PNew;    //    ĩβ�ڵ�ָ��ָ����һ���½ڵ�
        PNew->Next = NULL;        //    �½ڵ�ָ��ָ��Ϊ��
        PTail = PNew;    //    ���½ڵ㸴�Ƹ�ĩβ�ڵ�        
    }
    printf("��������ɹ�\n");
    return PHead;    //    ����ͷ�ڵ�
}

//    ���������������
void TraverseList(PNode List) {
    PNode P = List->Next;    //    �׽ڵ㸳ֵ����ʱ�ڵ�P
    printf("���������ֵΪ��");
    if (P == NULL)
        printf("����Ϊ��");
    while (P != NULL)        //����ʱ�ڵ�P��Ϊβ�ڵ�ʱ�������ǰ�ڵ�ֵ 
    {
        printf("%d ", P->Element);
        P = P->Next;
    }
    printf("\n");
}

//    ���������ѯ����
PNode FindList(PNode List) {
    PNode P = List->Next;    //    ������ʱָ��Pָ���׽ڵ�ĵ�ַ
    int num = 0;    //    ���ڼ�¼����ڵ�λ��
    int val = 0;    //    ���ڴ��Ҫ��ѯ��ֵ
    printf("������Ҫ��ѯ������");
    scanf("%d", &val);    //    ����Ҫ��ѯ����ֵ
    while (P != NULL&&P->Element != val) {
        P = P->Next;
        ++num;
    }
    if (P != NULL)
        printf("�ҵ��Ľڵ�Ϊ��%d", num + 1);
    else
        printf("�Ҳ����ýڵ�");
    printf("\n");
    return P;
}
//     ����������뺯��
//    ������λ�õ�pos�ڵ�ǰ�����������val�Ľڵ�
void InsertList(PNode List, int pos, int val) {
    int position = 0;
    PNode P = List;    //    ����ڵ�pָ��ͷ�ڵ�
                    //    Ѱ��pos�ڵ��ǰ�����
    while (P != NULL&&position<pos - 1)
    {
        P = P->Next;
        ++position;
    }
    PNode Tmp = (PNode)malloc(sizeof(Node));    //    ����һ����ʱ�ڵ������洢Ҫ���������
    if (Tmp == NULL)
    {
        printf("�ڴ����ʧ�ܣ�");
        exit(-1);
    }
    //    ����ڵ�
    Tmp->Element = val;
    Tmp->Next = P->Next;
    P->Next = Tmp;
}

//����ɾ������������
void DeleteTheList(PNode List) {
    PNode P, Tmp;
    P = List->Next;    //����ָ��Pָ������Ҫɾ��������List�ĵ�һ����ڵ�
    List->Next = NULL;
    while (P != NULL) {
        Tmp = P->Next;        //��ʱTmpָ��Ҫɾ���Ľڵ���¸��ڵ�
        free(P);    //�ͷ�ָ��Pָ��Ľڵ�
        P = Tmp;    //���¸�ֵ
    }
    printf("ɾ������ɹ���\n");
}
//    ����ɾ������Ԫ�غ���
//    ɾ�������еĵ�pos�ڵ�
void DeleteList(PNode List, int pos) {
    int position = 0;
    PNode P = List;    //    ����һ��ָ��pָ������ͷ�ڵ�
                    //    Ѱ��pos�ڵ�λ�õ�ǰ���ڵ�
    while (P != NULL&&position < pos - 1) {
        P = P->Next;
        ++position;
    }

    //    ɾ���ڵ�
    PNode Tmp = P->Next;    //    ������ʱָ��Tmpָ��Ҫɾ���Ľڵ�
    P->Next = Tmp->Next;    //    ʹҪɾ���ڵ��ǰ�����ָ��������ڵ�
    free(Tmp);    //    �ͷ�ɾ���ڵ���ڴ�ռ䣬��ֹ�ڴ�й©
    Tmp = NULL;    //    ʹqָ���ָ�룬��ֹ����Ұָ��
}
