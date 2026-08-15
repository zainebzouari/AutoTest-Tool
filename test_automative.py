import pytest
from automative import connect_db, get_vehicle_data
from metadata import metadata, vehicle_id  

@pytest.fixture(scope='module')
def db_connection():
    conn = connect_db()
    yield conn
    conn.close()

@pytest.fixture(scope='module')
def vehicle_id_fixture():  
    return vehicle_id  

@pytest.fixture(scope='module')
def vehicle_data(db_connection, vehicle_id_fixture):
    return get_vehicle_data(db_connection, vehicle_id_fixture)

def check_value(actual, expected, field, vehicle_data):
    if field == 'CO2_Emissions' and 'Fuel_Type' in vehicle_data['vehicleemissions']:
        fuel_type = vehicle_data['vehicleemissions']['Fuel_Type']
        expected = expected.get(fuel_type, None)
        if expected is None:
            return False
    if isinstance(expected, tuple):
        return expected[0] <= actual <= expected[1]
    else:
        return actual == expected

def evaluate_custom_checks(custom_checks, vehicle_data,metadata):
    error_messages = []
    for check_name, check_expr in custom_checks.items():
        try:
            if not eval(check_expr, {'metadata': metadata,'vehicle_data': vehicle_data, 'abs': abs}):
                error_messages.append(f"Custom check failed: {check_name}")
        except Exception as e:
            error_messages.append(f"Error evaluating custom check {check_name}: {e}")
    return error_messages

@pytest.mark.parametrize("attribute", metadata.keys())
def test_vehicle_attributes(vehicle_data, attribute):
    data = vehicle_data.get(attribute)
    expected = metadata[attribute]
    assert data is not None, f"{attribute} data not found in the vehicle data"

    all_error_messages = []

    
    for field, params in expected['fields'].items():
        db_key = field
        expected_value_key = params['expected']
        expected_value = expected.get(expected_value_key, None)  
        if db_key not in data:
            all_error_messages.append(f"Key {db_key} not found in {attribute} data")
        else:
            actual_value = data[db_key]
            if not check_value(actual_value, expected_value, field, vehicle_data):
                all_error_messages.append(f"{db_key} mismatch: expected {expected_value}, got {actual_value}")

   
    if 'custom_checks' in expected:
        all_error_messages.extend(evaluate_custom_checks(expected['custom_checks'], vehicle_data,metadata))

    if all_error_messages:
        raise AssertionError("\n".join(all_error_messages))
