def percent_change(old:float,new:float)->float:
    return ((new-old)/old)*100

def should_alert(old:float | None,new:float,threshold_pct:float)->bool:
    if old is None or old == 0:
        return False
    return abs(percent_change(old,new)) >= threshold_pct


