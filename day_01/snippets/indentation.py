if condition:
    a = 'This is the normal indentation'
else:
  b = 'This is allowed' # but a terrible idea!
  if another_condition:
   c = 'Even this is allowed'
    d = 'This is a syntax error'
   e = "I'm still in the if-statement"
  f = "I'm in the else-statement"

# This is also a syntax error
# Blocks cannot be empty
if condition:
    # TODO: Implement later

