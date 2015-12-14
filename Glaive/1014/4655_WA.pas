var
  f:boolean;
  time,i,j,k,t,s:longint;
  could:array[0..126] of boolean;

begin
  f:=false;
  s:=0;
  time:=1;
  fillchar(could,sizeof(could),false);
  could[0]:=true;
  for i:=1 to 6 do
      begin
        read(t);
        if t<>0 then f:=true;
        for k:=1 to t do
        for j:=126 downto 0 do
            if could[j] and (j+i<=126) then
               could[j+i]:=true;
        inc(s,t*i);
      end;
  while f do
    begin
      writeln('Collection#',time,':');
      if (s mod 2=0) and could[s div 2]
         then writeln('Can be divided.')
         else writeln('Can','''','t be divided.');
      f:=false;
      fillchar(could,sizeof(could),false);
      could[0]:=true;
      inc(time);
      s:=0;
      for i:=1 to 6 do
        begin
          read(t);
          if t<>0 then f:=true;
          for k:=1 to t do
          for j:=126 downto 0 do
              if could[j] and (j+i<=126) then
                 could[j+i]:=true;
          inc(s,t*i);
        end;
    end;
end.
