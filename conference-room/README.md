# Conference Room Management System

##### Add Building
    command: add building building_name ?{time_slot default 10:20}

##### Add Floor
    command: add floor building_name floor_name

##### Add Room 
    command: add room building_name floor_name room_name

##### Book a Meeting
    command: book time_slot building_name floor_name
    return: room_name if booked or else failed to book
    example: book 12:13 alpha alpha_1
    output: room booked successfully - room-id is a11

##### Cancel a Meeting
    command: cancel time_slot building_name floor_name room_id

##### List all bookings
    command: list ?{building_name} ?{floor_name}
    ? = optional

##### Check availability 
    command: check time_slot building_name floor_name
    return: list of room available

##### Get availability suggestion
    command: suggest time_slot ?{building_name} ?{floor_name}
    ? = optional
