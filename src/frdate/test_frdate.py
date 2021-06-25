from frdate import frdate
import datetime

d='14 juillet 1789'
echantillon=[
  ('14071789',False,False),
  ('14/07/1789',False,False),
  ('17890714',False,False),
  ('14 07 1789',False,False),
  ('14 juillet 1789',False,False),
  ('1789-07-14',False,False)
   ]

def test_fr_conv():
  assert frdate.conv('2000-01-01',litteral=True) == 'premier janvier deux mille'
  assert frdate.conv('2000-01-01',True) == datetime.date(2000,1,1)
  for t in echantillon:
    assert frdate.conv(t[0],t[1],t[2]) == d
