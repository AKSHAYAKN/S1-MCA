#include <stdio.h>
#define MAX 5
int stack[MAX];
int top=-1;

void push(int value)
{
   if(top== MAX-1)
   {
     printf("Stack Overfolw ! cannot pushed %d\n",value);
     }
else{
     stack[++top]=value;
     printf("%d pushed stack \n",value);
     }
  }


void pop()
{
   if(top==-1)
   {
     printf("Stack Overflow!! Cannot pop \n");
     }
   else{
     printf("%d popped from stack \n",stack[top--]);
     }
}

void display()
{
  if(top==-1){
  printf("Stack is empty\n");
  }
  else 
  {
    printf("stack elements:");
    for(int i=top;i>=0;i--)
    {
    printf("%d",stack[i]);
    }
    printf("\n\n");
    }
}
int main()
{
 int choice,value;
 while(1)
 {
   printf("\n-----Stack Menu------\n");
   printf("1.push\n");
    printf("2.pop\n");
     printf("3.Display\n");
      printf("4.Exit\n");
  printf("Enter your choice:");
  scanf("%d",&choice);
  
  switch(choice)
  {
    case 1:
    printf("Enter value to push:");
    scanf("%d",&value);
    push(value);
    break;
    
    case 2:
    pop();
    break;
    
    case 3:
    display();
    break;
    
    case 4:
    return 0;
    
    default:
    printf("Invalid choice!! Try again.\n");
    }
}
}

   
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
