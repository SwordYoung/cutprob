var
  n,l,i,t,j:longint;
  coin:array[1..100] of longint;
  tt,ts:array[1..100] of longint;
  c:char;

  procedure add(var a:longint; b:longint);
    begin
      if a<>0
         then
           if a=3
              then a:=b
              else
                if a<>b then
                   a:=0;
    end;

begin
  readln(n,l);
  for i:=1 to n do
    coin[i]:=3;
  for i:=1 to l do
    begin
      read(t);
      for j:=1 to t do
        read(tt[j]);
      for j:=1 to t do
        read(ts[j]);
      readln;
      read(c);
      case c of
        '=':for j:=1 to t do
              begin
                coin[tt[j]]:=0;
                coin[ts[j]]:=0;
              end;
        '<':for j:=1 to t do
              begin
                add(coin[tt[j]],1);
                add(coin[ts[j]],2);
              end;
        '>':for j:=1 to t do
              begin
                add(coin[tt[j]],2);
                add(coin[ts[j]],1);
              end;
        end;
    end;
  t:=0;
  for i:=1 to n do
    if coin[i]<>0 then
       if t=0 then t:=i
          else
            t:=-1;
  if t=-1 then writeln(0)
     else writeln(t);
end.