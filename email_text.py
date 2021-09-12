def get_text(email):
  msg = []
  for i in email.walk():
    if i.get_content_type() == 'text/plain':
      msg.append(i.get_payload())
  return ''.join(msg)

if not path.exists('/content/drive/My Drive/Data/main_data.csv'):
  df = pd.DataFrame()
  #emails = list(data['message'].apply(email.message_from_string))
  cols = emails[0].keys()
  for col in cols:
    df[col] = [x[col] for x in emails]
  df['content'] = list(map(get_text, emails))
  df.to_csv('/content/drive/My Drive/Data/main_data.csv', index = False)
else:
  print('File Already Present')
  
data = pd.read_csv('/content/drive/My Drive/Data/main_data.csv', nrows = 200000)
data.head(5)
