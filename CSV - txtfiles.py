txtfile = (open('Multiplayer_Results.txt', 'a')) # write or append txt file


txtfile.writelines(f' {winner}') # write a line with the index and winner

txtfile.writelines('\n') # new line

txtfile.close() # close the file