def slices(series, length):
    # pass
    count = 0
    digit_series = []
    
    if len(series) == length:
        digit_series.append(series)
        return digit_series
    elif len(series) < length or length <= 0 :
        raise ValueError("value not good")
    else:
        while True:
            digit_series.append(series[count:count+length])
            count += 1
            if len(series) - count < length:
                break
        return digit_series