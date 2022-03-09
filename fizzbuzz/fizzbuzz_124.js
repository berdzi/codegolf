//124
i=0;while(++i<=100){fb={0:i,2:'Fizz',1:'Buzz',3:'FizzBuzz'};a=2;z=0;[3,5].forEach(x=> {z+=+(i%x==0)*a--;});print(fb[z]);}