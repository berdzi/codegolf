//135
Array.from({length:100},(_,i)=>i+1).map(x=>{return x%15==0?"FizzBuzz":(x%3==0?"Fizz":(x%5==0?"Buzz":x))}).forEach(z=>{print(z);})