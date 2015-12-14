var
  l,n,i,j,k:longint;
  st:string;
  strn:array[1..100] of string;
  number:array[1..100] of longint;

begin
  readln(l,n);
  for i:=1 to n do
    begin
      readln(strn[i]);
      for j:=1 to l-1 do
        for k:=j+1 to l do
          if strn[i,j]>strn[i,k] then inc(number[i]);
    end;
  for i:=1 to n-1 do
    for j:=i+1 to n do
      if number[i]>number[j] then
         begin
           st:=strn[i];
           strn[i]:=strn[j];
           strn[j]:=st;
           k:=number[i];
           number[i]:=number[j];
           number[j]:=k;
         end;
  for i:=1 to n do
    writeln(strn[i]);
end.
