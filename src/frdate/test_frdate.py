from frdate import frdate

echantillon=[
  ('14071789','14 juillet 1789')
   ]

def test_fr_conv():
  for t in echantillon:
    assert frdate.conv(t[0]) == t[1]
