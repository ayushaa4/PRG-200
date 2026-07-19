def ticket_price(seat_type, count):
   
    if seat_type == 'regular':
        price_per_ticket = 250
    elif seat_type == 'recliner':
        price_per_ticket = 400
    else:
        return 0
    
    total_cost = price_per_ticket * count
    return total_cost

print(ticket_price('regular',2))