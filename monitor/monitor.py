"""
Using a suitable method, design and develop the code to monitor the CPU
in some way. This could be the CPU load, the CPU temperature or similar.
The code for the sensor monitoring should run once every 5 seconds.
To test the developed code works as expected, make the monitor show the
current data on screen, and have the code execute for sixty seconds (repeat
the monitoring process 12 times).
"""
from datetime import datetime
from time import sleep
# import the ORM items
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
# import the Model classes for CPU and Storage
from db import CPU, Storage, Base
# import the methods that will be used from the mypi file
from mypi import \
    get_serial, get_mac, get_host_name, \
    get_cpu_temp, get_gpu_temp, get_maximum_cpu_load
# import sql
import sqlite3

# create connection
conn = sqlite3.connect('data/monitor_data.db')
print("Opened database successfully")

# create table
conn.execute('''CREATE TABLE IF NOT EXISTS CPU_DATA
                (HOST CHAR(10) NOT NULL,
                READING_DATETIME CHAR(80) NOT NULL,
                CPU_LOAD REAL);''')
print("Opened table successfully")

db_filename = './data/monitor_data.db'


def headings():
    print()
    print(f'{"Name":<10}|{"Created at":<28}|{"CPU Load":>8}'
          f'')


def main(_delay):
    engine = create_engine(f'sqlite:///{db_filename}')
    session = sessionmaker(bind=engine)()
    Base.metadata.create_all(engine)
    counter = 0

    while True:
        # Create a CPU object and set the properties
        cpu = CPU()
        cpu.host_name = get_host_name()
        cpu.load = get_maximum_cpu_load()
        cpu.created_at = datetime.now()
        # save the object to the database using SQLAlchemy ORM and
        # commit the action
        session.add(cpu)
        session.commit()

        last_readings = session.query(CPU).order_by(CPU.id.desc()).first()

        if counter % 12 == 0:
            print("Records being created...")
        counter += 1

        host = f'{last_readings.host_name:<10}'
        reading_datetime = last_readings.created_at
        cpu_load = f'{last_readings.load:>8.1f}'

        insert_query = """INSERT INTO CPU_DATA (HOST, READING_DATETIME, CPU_LOAD)
                        VALUES (?, ?, ?)"""

        records_to_insert = (host, reading_datetime, cpu_load)

        conn.execute(insert_query, records_to_insert)
        conn.commit()
        sleep(_delay)

        if counter > 11:
            conn.close()
            exit()


def current_cpu():
    engine = create_engine(f'sqlite:///{db_filename}')
    session = sessionmaker(bind=engine)()
    Base.metadata.create_all(engine)
    cpu = CPU()
    cpu.host_name = get_host_name()
    cpu.load = get_maximum_cpu_load()
    cpu.created_at = datetime.now()
    # cpu.load = get_maximum_cpu_load()
    # currentCpuString = f"The current CPU is: {cpu.load}"
    last_readings = session.query(CPU).order_by(CPU.id.desc()).first()
    host = f'{last_readings.host_name:<10}'
    reading_datetime = last_readings.created_at
    cpu_load = f'{last_readings.load:>8.1f}'

    data = {
        'host_name': host,
        'created_at': reading_datetime,
        'load': cpu_load
    }
    return data


def current_cpu_load():
    engine = create_engine(f'sqlite:///{db_filename}')
    session = sessionmaker(bind=engine)()
    Base.metadata.create_all(engine)
    cpu = CPU()
    cpu.load = get_maximum_cpu_load()
    last_readings = session.query(CPU).order_by(CPU.id.desc()).first()
    cpu_load = f'{last_readings.load:>8.1f}'

    data = {
        'load': cpu_load
    }
    return data


if __name__ == '__main__':
    delay = 5.0
    main(delay)
