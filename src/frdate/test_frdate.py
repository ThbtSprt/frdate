from frdate import frdate

echantillon=[
  ('14071789',False,False,'14 juillet 1789'),
  ('14/07/1789',False,False,'14 juillet 1789')
   ]

def test_fr_conv():
  for t in echantillon:
    assert frdate.conv(t[0],t[1],t[2]) == t[3]
