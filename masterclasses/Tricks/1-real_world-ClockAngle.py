# Clock Angles

import re

def convertMinutesToAngle(minutes):
    # (minutes/60) * 360 = angle
    return minutes * 6

def angles(times):
    total = 0
    pattern = re.compile(r"([0-2][0-9]):([0-5][0-9])")
    for time in times:
        match = pattern.match(time)
        if not match:
            total -= 100
            continue
        hour, minutes = map(int, match.groups())
        if not (0 <= hour < 24):
            total -= 100
            continue
        if not (0 <= minutes < 60):
            total -= 100
            continue

        hour = hour % 12


        # answer = abs(angle of minutes - angle of hours)

        # this value is between 0 and 360
        angle_minutes = convertMinutesToAngle(minutes)
        # if hour is 1, the hand is at least in the 5. For hour=1 the hand can be only between the 5 and the 6
        # if hour is 5, the hand is at least in the 25
        initial_angle = convertMinutesToAngle(hour * 5)
        # the hour hand moves when minute is > 0, for instance: if minute is 30 and hour is 5, the hour hand is in the middle of 5 and 6. 
        # rule of three: 60 is to 1, such as 30 is 1/2
        # Multiply the coeficient between [0,1] per minutes between the hour and the hour + 1 
        offset_angle = convertMinutesToAngle((minutes/60) * 5) 
        angle_hours = (initial_angle + offset_angle) % 360

        if angle_minutes > angle_hours:
            total += angle_minutes - angle_hours 
        else:
            angles_to_begin = (360 - angle_hours) % 360
            total += angles_to_begin + angle_minutes

    return total


import pytest


def test():
    result = angles(["12:00", "17:30", "blabla", "20:21", "26:88"])
    print(result)
    assert result == pytest.approx(50.5)

test()