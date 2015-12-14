const
  haabm:array[1..19] of string=('pop','no','zip','zotz','tzec','xul','yoxkin',
        'mol','chen','yax','zac','ceh','mac','kankin','muan','pax','koyab','cumbu','uayet');
  tzolkind:array[1..20] of string=('imix','ik','akbal','kan','chiccan','cimi',
           'manik','lamat','muluk','ok','chuen','eb','ben','ix','mem','cib',
           'caban','eznab','canac','ahau');

var
  i,j,n,day,hday,month,year:longint;
  c:char;
  strn:string;
  lday,lmonth,lyear:array[1..1000] of longint;

begin
  readln(n);
  for i:=1 to n do
    begin
      if i<>1 then writeln;
      read(c);
      hday:=0;
      repeat
        hday:=hday*10+ord(c)-ord('0');
        read(c);
      until c='.';
      read(c);
      strn:='';
      repeat
        strn:=strn+c;
        read(c);
      until c=' ';
      readln(year);
      for j:=1 to 19 do
        if strn=haabm[j] then
           begin
             month:=j;
             break;
           end;
      day:=hday+(month-1)*20+year*365+1;
      lyear[i]:=day div 260;
      day:=day mod 260;
      lmonth[i]:=(day-1) mod 13+1;
      lday[i]:=day mod 20;
      write(month,' ',tzolkind[day],' ',year);
  end;
  writeln(n);
  for i:=1 to n do
    writeln(lmonth[i],' ',tzolkind[lday[i]],' ',lyear[i]);
end.