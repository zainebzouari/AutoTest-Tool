vehicle_id= 7
metadata={
 'vehicleemissions' : {
    'expected_Air_Filter_Status': True,
    'expected_Oil_Filter_Status': True,
    'expected_co2_limit': {
        'essence': 130,
        'diesel': 120,
        'hybrid': 100
    },
    'fields': {
            'Air_Filter_Status': {'expected': 'expected_Air_Filter_Status'},
            'Oil_Filter_Status': {'expected': 'expected_Oil_Filter_Status'},
            'CO2_Emissions': {'expected': 'expected_co2_limit', 'limit_by': 'Fuel_Type'}
        }
  },
 'tpms':{
  'expected_tpms_pressure_range':(30,35),
  'max_pressure_difference_range_front':(0,2),
  'max_pressure_difference_range_rear':(0,2),

  'fields': {
            'Front_Left_Pressure': {'expected': 'expected_tpms_pressure_range'},
            'Front_Right_Pressure': {'expected': 'expected_tpms_pressure_range'},
            'Rear_Left_Pressure': {'expected': 'expected_tpms_pressure_range'},
            'Rear_Right_Pressure': {'expected': 'expected_tpms_pressure_range'}
        },
      'custom_checks': {
        'max_pressure_difference_range_front':'abs(vehicle_data["tpms"]["Front_Left_Pressure"] - vehicle_data["tpms"]["Front_Right_Pressure"]) <= metadata["tpms"]["max_pressure_difference_range_front"][1]',
        'max_pressure_difference_range_rear': 'abs(vehicle_data["tpms"]["Rear_Left_Pressure"] - vehicle_data["tpms"]["Rear_Right_Pressure"]) <= metadata["tpms"]["max_pressure_difference_range_rear"][1]'
  }
  
    },
  'seatadjustment':{
    'forward_backward_adjustment_range':(0,300),
    'recline_angle_adjustment_range':(0,180),
    'height_adjustment_range':(0,255),
     'fields': {
            'forward_backward_adjustment': {'expected': 'forward_backward_adjustment_range'},
            'recline_angle_adjustment': {'expected': 'recline_angle_adjustment_range'},
            'height_adjustment': {'expected': 'height_adjustment_range'}
        }
  },
  'parkingassistance':{
    'expected_Parking_Sensors_Status':1,
    'expected_Rear_Camera_Status':1,
     'fields': {
            'Parking_Sensors_Status': {'expected': 'expected_Parking_Sensors_Status'},
            'Rear_Camera_Status': {'expected': 'expected_Rear_Camera_Status'}
        }

  },
  'lighting':{
    'expected_Headlights':1,
    'expected_Low_Beams':1,
    'expected_Brake_Lights':1,
    'expected_Light_Intensity':(30,70),
      'fields': {
            'Headlights': {'expected': 'expected_Headlights'},
            'Low_Beams': {'expected': 'expected_Low_Beams'},
            'Brake_Lights': {'expected': 'expected_Brake_Lights'},
            'Interior_Light_Intensity': {'expected': 'expected_Light_Intensity'}
        }
  },
  'climatecontrol':{
    'expected_Fan_Speed_range':(1,5),
    'expected_Temperature':(15,30),
    'fields': {
            'Temperature': {'expected': 'expected_Temperature'},
            'Fan_Speed': {'expected': 'expected_Fan_Speed_range'}
        }
  },
  'adas':{
     'expected_Lane_Assist_Status':1,
     'expected_Adaptive_Cruise_Control_Status':1,
     'expected_Collision_Avoidance_Status':1,
       'fields': {
            'Lane_Assist_Status': {'expected': 'expected_Lane_Assist_Status'},
            'Adaptive_Cruise_Control_Status': {'expected': 'expected_Adaptive_Cruise_Control_Status'},
            'Collision_Avoidance_Status': {'expected': 'expected_Collision_Avoidance_Status'}
        }
  },
  'energyconsumption':{
     'expected_Power_Windows':1,
     'expected_Fuel_Efficiency_range':(6.5,30),
     'expected_Regenerative_Braking':1,
     'fields': {
            'Power_Windows': {'expected': 'expected_Power_Windows'},
            'Fuel_Efficiency': {'expected': 'expected_Fuel_Efficiency_range'},
            'Regenerative_Braking': {'expected': 'expected_Regenerative_Braking'},
        }
  },
     'engine':{
     'expected_Engine_Temperature_Range':(75,120),
     'expected_RPM_Range':(500,2100),
     'expected_Engine_Status':1,
      'fields': {
            'Engine_Temperature': {'expected': 'expected_Engine_Temperature_Range'},
            'RPM': {'expected': 'expected_RPM_Range'},
            'Engine_Status': {'expected': 'expected_Engine_Status'},
        }
  },
    'abs_system': {
    'expected_ABS_Status': 1,
    'expected_Wheel_Slip_Range': (0,5),
    'expected_ABS_Sensor_Status': 1,
    'expected_Brake_Fluid_Level_range': (0.50,1),
    'fields': {
        'ABS_Status': {'expected': 'expected_ABS_Status'},
        'Wheel_Slip': {'expected': 'expected_Wheel_Slip_Range'},
        'ABS_Sensor_Status': {'expected': 'expected_ABS_Sensor_Status'},
        'Brake_Fluid_Level': {'expected': 'expected_Brake_Fluid_Level_range'}
    },
   
  }


}

