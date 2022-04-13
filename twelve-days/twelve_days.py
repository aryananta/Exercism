def recite(start_verse, end_verse):
  days = (('first', 'A Partridge in a Pear Tree'),
   ('second', 'Two Turtle Doves'),
   ('third', 'Three French Hens'),
   ('fourth', 'Four Calling Birds'),
   ('fifth', 'Five Golden Rings'),
   ('sixth', 'Six Geese a Laying'),
   ('seventh', 'Seven Swans a Swimming'),
   ('eighth', 'Eight Maids a Milking'),
   ('ninth', 'Nine Ladies Dancing'),
   ('tenth', 'Ten Lords a Leaping'),
   ('eleventh', 'Eleven Pipers Piping'),
   ('twelfth', '12 Drummers Drumming'))
   
  text=""
   
  for i in range(start_verse,end_verse):
    text = 'On the {} day of Christmas my true love gave to me:'.format(days[0][i])
    for j in range(start_verse,end_verse):
      text = text
    
  return text
   #pass


