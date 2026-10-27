def percent_change(old:float,new:float)->float:
    return round(((new-old)/old)*100,2)

def should_alert(old:float | None,new:float,threshold_pct:float)->bool:
    if old is None or old == 0:
        return False
    change=percent_change(old,new)
    return abs(change) >= threshold_pct,change


