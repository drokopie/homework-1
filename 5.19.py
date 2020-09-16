
   const char services[4][15] = {{"Oil change"},{"Tire rotation"},{"Car wash"},{"Car wax"}};
   const int prices[4] = {35,19,7,12};
   int i=0, j=0;
   printf("Davy's auto shop services\n\n");
   for(i=0; i<4; i++){
       printf("%s -- $%d\n\n",services[i], prices[i]);

   char service[2][15];
   printf("\n");
   printf("Select first service:\n");
   scanf("%[^\n]",service[0]);
   printf("\nSelect second service:\n");
   scanf(" %[^\n]",service[1]);
   printf("\n");
   printf("\nDavy's auto shop invoice");
   printf("\n\n\n");
   int total = 0;
   for(i=0; i<2; i++)
       int index = -1;
       for(j=0; j<4; j++){
           if(strcmp(service[i],services[j]) == 0)
               index = j;
               break;
           }
       }

       if(index == -1){
           printf("Service %d: No service\n\n",(i+1));
       }

       else{
           printf("Service %d: %s, $%d\n\n",(i+1),service[i],prices[index]);
           total = total + prices[index];
   printf("\n");
   printf("Total: $%d\n",total);
   return 0;
}