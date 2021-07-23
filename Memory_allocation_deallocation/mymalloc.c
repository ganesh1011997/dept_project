#include<stdio.h>
#include<stddef.h>

char memory[20000];

struct block
{
	size_t size;
	int free;
	struct block *next; 
};

struct block *freeList=(void*)memory;

void initialize();
void split(struct block *fitting_slot,size_t size);
void *MyMalloc(size_t noOfBytes);
void merge();
void MyFree(void* ptr);


void initialize()
{
	freeList->size=20000-sizeof(struct block);
	freeList->free=1;
	freeList->next=NULL;
}

void split(struct block *fitting_slot,size_t size)
{
	struct block *new=(void*)((void*)fitting_slot+size+sizeof(struct block));
	new->size=(fitting_slot->size)-size-sizeof(struct block);
	new->free=1;
	new->next=fitting_slot->next;
	fitting_slot->size=size;
	fitting_slot->free=0;
	fitting_slot->next=new;
}


void *MyMalloc(size_t noOfBytes)
{
	struct block *curr,*prev;
	void *result;
	if(!(freeList->size))
	{
		initialize();
		printf("Memory initialized\n");
	}
	curr=freeList;
	while((((curr->size)<noOfBytes)||((curr->free)==0))&&(curr->next!=NULL))
	{
		//prev=curr;
		curr=curr->next;
		printf("One block checked\n");
	}
	if((curr->size)==noOfBytes)
	{
		curr->free=0;
		result=(void*)(++curr);
		printf("Exact fitting block allocated\n");
		return result;
	}
	else if((curr->size)>(noOfBytes+sizeof(struct block)))
	{
		split(curr,noOfBytes);
		result=(void*)(++curr);
		printf("Fitting block allocated with a split\n");
		return result;
	}
	else
	{
		result=NULL;
		printf("Sorry. No sufficient memory to allocate\n");
		return result;
	}
}

void merge()
{
	struct block *curr,*prev;
	curr=freeList;
		do 
		{
	
			if((curr->free) && (curr->next->free))
				{
					curr->size+=(curr->next->size)+sizeof(struct block);
					curr->next=curr->next->next;
				}
			else                                                                                                //prev=curr;
				curr=curr->next;
	 	}
	while((curr->next)!=NULL&&(curr->next->next)!=NULL);
}

void MyFree(void* ptr)
{
	if(((void*)memory<=ptr)&&(ptr<=(void*)(memory+20000)))
	{
		struct block* curr=ptr;
		--curr;
		curr->free=1;
		merge();
	}
	else printf("Please provide a valid pointer allocated by MyMalloc\n");
}


int main()
{
	int *p=(int*)MyMalloc(10*sizeof(int));
	for(int i=0;i<10;i++)
		p[i]=i;	
	for(int i=0;i<10;i++)
		printf("%x %d\n",&p[i],p[i]);
	MyFree(p);
	for(int i=0;i<10;i++)
		p[i]=i+1;
	for(int i=0;i<10;i++)
		printf("%x %d\n",&p[i],p[i]);

}


