buffer_size = 1024
with open('BTS_P2D.mp4', 'rb') as source:
    with open('BTS_P2D2.mp4', 'wb') as copy:
        while True:
            buffer = source.read(buffer_size)
            if not buffer:
                break
            copy.write(buffer)

print('Finish')