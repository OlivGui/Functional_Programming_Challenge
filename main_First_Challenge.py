from datetime import datetime
import pandas

# Call records
records = [
          {'source': '48-996355555', 'destination': '48-666666666', 'end': 1564610974, 'start': 1564610674},
          {'source': '41-885633788', 'destination': '41-886383097', 'end': 1564506121, 'start': 1564504821},
          {'source': '48-996383697', 'destination': '41-886383097', 'end': 1564630198, 'start': 1564629838},
          {'source': '48-999999999', 'destination': '41-885633788', 'end': 1564697158, 'start': 1564696258},
          {'source': '41-833333333', 'destination': '41-885633788', 'end': 1564707276, 'start': 1564704317},
          {'source': '41-886383097', 'destination': '48-996384099', 'end': 1564505621, 'start': 1564504821},
          {'source': '48-999999999', 'destination': '48-996383697', 'end': 1564505721, 'start': 1564504821},
          {'source': '41-885633788', 'destination': '48-996384099', 'end': 1564505721, 'start': 1564504821},
          {'source': '48-996355555', 'destination': '48-996383697', 'end': 1564505821, 'start': 1564504821},
          {'source': '48-999999999', 'destination': '41-886383097', 'end': 1564610750, 'start': 1564610150},
          {'source': '48-996383697', 'destination': '41-885633788', 'end': 1564505021, 'start': 1564504821},
          {'source': '48-996383697', 'destination': '41-885633788', 'end': 1564627800, 'start': 1564626000}
          ]

# Fee constants
FIX_TAX = 0.36
DAY_MINUTE_TAX = 0.09
NIGHT_MINUTE_TAX = 0

# Day fee
def dayfee(start, end):
    return FIX_TAX + (((end - start).seconds // 60) * DAY_MINUTE_TAX)

# Night Fee
def nightfee(start, end):
    return FIX_TAX + (((end - start).seconds // 60) * NIGHT_MINUTE_TAX)    

# Call cost
def callfee(start, end):
    # Start and end time
    start = datetime.fromtimestamp(start)
    end = datetime.fromtimestamp(end)
    
    # Day tax
    if (start.hour > 6 and end.hour < 22):
        return dayfee(start, end)
    
    # Night tax
    if ((start.hour > 22 and end.hour > 22) or
       (start.hour < 6 and end.hour < 6)):
        return nightfee(start, end)

    # Mix tax
    else: 
        if (end.hour >= 22, end.minute >= 1):
            end = datetime(end.year, end.month, end.day, hour = 22, 
                           minute = 00, second = 59)
            
        if (start.hour < 6):
            start = datetime(start.year, start.month, start.day, hour = 6)
            
        mix_fee = dayfee(start, end) + nightfee(start, end)
        return mix_fee
    
# Add 'cost' to the recods
def getcosts(records):
    for calls in records:
        calls.update({'cost': callfee(calls['start'], calls['end'])})
    return records

# Classify the phone numbers and costs
def classify_by_phone_number(records):
    # The final result
    results_final = []
    
    # Do the matrix with records
    results_frame = pandas.DataFrame(getcosts(records))
    
    # Let the results sorted by source
    sorted_results = results_frame.groupby('source')['cost'].sum().reset_index().rename(columns = {'cost':'total'}).sort_values(by='total', ascending=False)
    
    # Put source values on the sorted list
    sources = sorted_results['source'].values.tolist()
    
    # Put totals values on the sorted list 
    totals = sorted_results['total'].values.tolist()
    
    # Make the results_final list
    for result in zip(sources, totals):
        results_final.append({'source': result[0], 'total': result[1]})
    
    # Return the final list
    return results_final
