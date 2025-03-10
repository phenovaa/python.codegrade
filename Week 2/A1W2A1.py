def is_input_valid(inp_date):

    date_1 = inp_date[0:4]
    date_2 = inp_date[5:7]
    date_3 = inp_date[8:10]

    if len(date_1) == 4 and len(date_2) == 2 and len(date_3) == 2 and date_1.isdigit() and date_2.isdigit() and date_3.isdigit() and "-" in inp_date:
        years = int(date_1)
        months = int(date_2)
        days = int(date_3)
    
        if months == 1 and days == 31: # Jan
            months = 2
            days = 1
            years = str(years)
            months = str(months)
            days = str(days)
            return f"{years}-{months.zfill(2)}-{days.zfill(2)}" 
        
        elif months == 2 and days == 28: # Feb
            months = 3
            days = 1
            years = str(years)
            months = str(months)
            days = str(days)
            return f"{years}-{months.zfill(2)}-{days.zfill(2)}" 
        
        elif months == 3 and days == 31: # Mar
            months = 4
            days = 1
            years = str(years)
            months = str(months)
            days = str(days)
            return f"{years}-{months.zfill(2)}-{days.zfill(2)}" 
        
        elif months == 4 and days == 30: # Apr
            months = 5
            days = 1
            years = str(years)
            months = str(months)
            days = str(days)
            return f"{years}-{months.zfill(2)}-{days.zfill(2)}" 
        
        elif months == 5 and days == 31: # May
            months = 6
            days = 1
            years = str(years)
            months = str(months)
            days = str(days)
            return f"{years}-{months.zfill(2)}-{days.zfill(2)}" 
        
        elif months == 6 and days == 30: # Jun
            months = 7
            days = 1
            years = str(years)
            months = str(months)
            days = str(days)
            return f"{years}-{months.zfill(2)}-{days.zfill(2)}" 
        
        elif months == 7 and days == 31: # Jul
            months = 8
            days = 1
            years = str(years)
            months = str(months)
            days = str(days)
            return f"{years}-{months.zfill(2)}-{days.zfill(2)}" 
        
        elif months == 8 and days == 31: # Aug
            months = 9
            days = 1
            years = str(years)
            months = str(months)
            days = str(days)
            return f"{years}-{months.zfill(2)}-{days.zfill(2)}" 
        
        elif months == 9 and days == 30: # Sep
            months = 10
            days = 1
            years = str(years)
            months = str(months)
            days = str(days)
            return f"{years}-{months.zfill(2)}-{days.zfill(2)}" 
        
        elif months == 10 and days == 31: # Oct
            months = 11
            days = 1
            years = str(years)
            months = str(months)
            days = str(days)
            return f"{years}-{months.zfill(2)}-{days.zfill(2)}" 
        
        elif months == 11 and days == 30: # Nov
            months = 12
            days = 1
            years = str(years)
            months = str(months)
            days = str(days)
            return f"{years}-{months.zfill(2)}-{days.zfill(2)}" 
        
        elif months == 12 and days == 31: #Dec
            years += 1
            months = 1
            days = 1
            years = str(years)
            months = str(months)
            days = str(days)
            return f"{years}-{months.zfill(2)}-{days.zfill(2)}" 
        
        elif months < 12 and days < 31: # Rest
            days += 1
            years = str(years)
            months = str(months)
            days = str(days)
            return f"{years}-{months.zfill(2)}-{days.zfill(2)}" 
        else:
            return "Input format ERROR. Correct Format: YYYY-MM-DD"
        
    else:
        print("Input format ERROR. Correct Format: YYYY-MM-DD")


user_input = input("Next Date: ")
print(is_input_valid(user_input))