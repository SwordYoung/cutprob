var
  i:longint;
  t,s:real;
begin
  s:=0;
  for i:=1 to 12 do
    begin
      read(t);
      s:=s+t;
    end;
  writeln('$',s/12:0:2);
end.