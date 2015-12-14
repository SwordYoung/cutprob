var
  n,i,j,t,k:longint;
  c:char;
  strn:string;
  f:array['A'..'L'] of boolean;
  num:array['A'..'L'] of longint;
  tt,ts:array[1..20] of char;

  procedure add(var a:longint; b:longint);
    begin
      if a<>0 then
         if b=0 then a:=0
            else
              if a=3 then a:=b
                 else
                   if a=b then a:=b
                      else a:=0;
    end;

begin
  readln(n);
  for i:=1 to n do
    begin
      for c:='A' to 'L' do
        num[c]:=3;
      for k:=1 to 3 do
        begin
      read(c);
      t:=0;
      repeat
        inc(t);
        tt[t]:=c;
        read(c);
      until c=' ';
      for j:=1 to t do
        read(ts[j]);
      read(c);
      readln(strn);
      if strn='even' then
         for j:=1 to t do
           begin
             num[tt[j]]:=0;
             num[ts[j]]:=0;
           end
         else
           begin
           fillchar(f,sizeof(f),true);
           for j:=1 to t do
             begin
               f[tt[j]]:=false;
               f[ts[j]]:=false;
             end;
           if strn='up' then
              for j:=1 to t do
                begin
                  add(num[tt[j]],1);
                  add(num[ts[j]],2);
                end
              else
                for j:=1 to t do
                  begin
                    add(num[tt[j]],2);
                    add(num[ts[j]],1);
                  end;
           for c:='A' to 'L' do
             if f[c] then num[c]:=0;
           end;
         end;
      for c:='A' to 'L' do
        if (num[c]<>0)and(num[c]<>3) then
           begin
             write(c,' is the counterfeit coin and it is ');
             if num[c]=2 then
                writeln('light.')
                else writeln('heavy.');
           end;
    end;
end.
