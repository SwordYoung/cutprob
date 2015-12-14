var
  i,j,t,k,n:longint;
  strn:string;
  number:array[1..10000] of string;
  cout:array[1..10000] of longint;
  f:boolean;

begin
  readln(n);
  t:=0;
  for i:=1 to n do
    begin
      readln(strn);
      k:=1;
      repeat
        if strn[k]='-' then
           delete(strn,k,1);
        inc(k);
      until k>length(strn);
      for J:=1 to 7 do
        case strn[j] of
          'A'..'C':begin
                     delete(strn,j,1);
                     insert('2',strn,j);
                   end;
          'D'..'F':begin
                     delete(strn,j,1);
                     insert('3',strn,j);
                   end;
          'G'..'I':begin
                     delete(strn,j,1);
                     insert('4',strn,j);
                   end;
          'J'..'L':begin
                     delete(strn,j,1);
                     insert('5',strn,j);
                   end;
          'M'..'O':begin
                     delete(strn,j,1);
                     insert('6',strn,j);
                   end;
          'P','R','S':begin
                     delete(strn,j,1);
                     insert('7',strn,j);
                   end;
          'T'..'V':begin
                     delete(strn,j,1);
                     insert('8',strn,j);
                   end;
          'W'..'Y':begin
                     delete(strn,j,1);
                     insert('9',strn,j);
                   end;
        end;
      f:=true;
      for j:=1 to t do
          if number[j]=strn then
             begin
               inc(cout[j]);
               f:=false;
               break;
             end;
      if f then
         begin
           inc(t);
           number[t]:=strn;
           cout[t]:=1;
         end;
    end;
  for i:=1 to t-1 do
    for j:=i+1 to t do
      if number[i]>number[j] then
         begin
           strn:=number[i];
           number[i]:=number[j];
           number[j]:=strn;
           n:=cout[i];
           cout[i]:=cout[j];
           cout[j]:=n;
         end;
  for i:=1 to t do
    if cout[i]>=2 then
    begin
      for j:=1 to 3 do
        write(number[i,j]);
      write('-');
      for j:=4 to 7 do
        write(number[i,j]);
      write(' ');
      writeln(cout[i]);
    end;
end.