# import sqlite3
# def retrieval():
#        conn = sqlite3.connect('') # name
#        cursor = conn.cursor()
#        cursor.execute("SELECT * FROM flow_table")
#        rows = cursor.fetchall()
#        for row in rows:
#               print(row)
#
#        print("")
#        conn2 = sqlite3.connect('')
#        cursor = conn2.cursor()
#        cursor.execute("SELECT * FROM users")
#        rows = cursor.fetchall()
#        for row in rows:
#               print(row)
# def update():
#        user_input = input("What would you like to update?" "Type 'del' to delete 'add' to add or 'modify' to modify "
#                           "the data")
#        # process user input
#        conn3 = sqlite3.connect('')
#        cursor = conn3.cursor()
#        rows = cursor.fetchall()
#        for row in rows:
#               print(row)
#
#        if user_input == 'del':
#            cursor.execute("DELETE FROM users WHERE id = 6")
#            conn3.commit()  # Commit the changes
#            cursor.execute("SELECT * FROM users")
#            rows = cursor.fetchall()  # Fetch the results
#            for row in rows:
#                print(row)
#
#        elif user_input == 'add':
#            cursor.execute("INSERT INTO users VALUES (6, 'Jonathan', 'johnathan@gmail.com')")
#            conn3.commit()  # Commit the changes
#            cursor.execute("SELECT * FROM users")
#            rows = cursor.fetchall()  # Fetch the results
#            for row in rows:
#                print(row)
#
#        elif user_input == 'modify':
#            cursor.execute("UPDATE users SET name = 'albert' WHERE id = 6")
#            conn3.commit()  # Commit the changes
#            cursor.execute("SELECT * FROM users")
#            rows = cursor.fetchall()  # Fetch the results
#            for row in rows:
#                print(row)

# import sqlite3
# def create_nano_hardware_components():
#     conn = sqlite3.connect('')
#     cursor = conn.cursor()
#
#     # Define the circuit table names
#     circuit_table_names = [
#         "CPU_Enable", "sr_latch_active_high", "sr_latch_active_low",
#         "adder", "OR_ALU_Circuit", "XOR_ALU_Circuit", "AND_ALU_Circuit",
#         "NOT_ALU_Circuit", "ALU", "decoder_2x4", "digitalencoder_ADC",
#         "comparator_ADC"
#     ]
#
#     combined_data = []
#
#     # Iterate through each circuit table
#     for table_name in circuit_table_names:
#         # Build the SQL statement
#         sql_query = f"SELECT circuitname, gate, amtofgate, parent_circuit FROM {table_name};"
#
#         # Execute the query and fetch data
#         cursor.execute(sql_query)
#         circuit_rows = cursor.fetchall()
#
#         # Process the fetched data and update the combined_data list
#         for circuit_row in circuit_rows:
#             parent_circuit = circuit_row[3]
#             gate = circuit_row[1]
#             circuitname = circuit_row[0]
#             amtofgate = circuit_row[2]
#
#             combined_entry = {
#                 "circuitname": circuitname,
#                 "gate": gate,
#                 "amtofgate": amtofgate,
#                 "parent_circuit": parent_circuit
#             }
#             combined_data.append(combined_entry)
#
#         names = ['Carbon nanotubes, graphene, quantum dots', 'Nanowires, quantum dots', 'Field-effect transistors (FETs) using nanoscale materials', 'Quantum dots, nanowires',
#                  'Nanowires, carbon nanotubes']
#
#         # Create a placeholder string for the names
#         placeholders = ', '.join(['?' for _ in names])
#
#         # Process logicgates data
#         # Construct the query with placeholders
#         logicgates_query = f"SELECT id, name, gate, parent_circuit FROM logicgates WHERE name IN ({placeholders});"
#         cursor.execute(logicgates_query, names)
#         logicgates_rows = cursor.fetchall()
#
#         for logicgate_row in logicgates_rows:
#             parent_circuit = logicgate_row[3]
#             gate = logicgate_row[2]
#             name = logicgate_row[1]
#
#             # Find the corresponding entry in combined_data and update it
#             for entry in combined_data:
#                 if entry["parent_circuit"] == parent_circuit and entry["gate"] == gate:
#                     entry["name"] = name
#                     break
#
#     logicgates_query = "SELECT id, name, gate, parent_circuit FROM logicgates;"
#     cursor.execute(logicgates_query)
#     logicgates_rows = cursor.fetchall()
#
#     for logicgate_row in logicgates_rows:
#         parent_circuit = logicgate_row[3]
#         gate = logicgate_row[2]
#         name = logicgate_row[1]
#
#         # Find the corresponding entry in combined_data and update it
#         for entry in combined_data:
#             if entry["parent_circuit"] == parent_circuit and entry["gate"] == gate:
#                 entry["name"] = name
#                 break
#         create_table_query = '''
#             CREATE TABLE IF NOT EXISTS cleaned_nano_table (
#                 circuitname TEXT,
#                 gate TEXT,
#                 amtofgate INTEGER,
#                 parent_circuit INTEGER,
#                 name TEXT
#             );
#         '''
#
#         # Execute the SQL command to create the table
#         cursor.execute(create_table_query)
#
#         # Insert combined data into the newly created table
#         for entry in combined_data:
#             insert_query = "INSERT INTO cleaned_nano_table (circuitname, gate, amtofgate, parent_circuit, name) VALUES (?, ?, ?, ?, ?);"
#             cursor.execute(insert_query, (entry["circuitname"], entry["gate"], entry["amtofgate"], entry["parent_circuit"], entry.get("name", None)))
#
#         # Commit the changes and close the connection
#         conn.commit()
#
#     # print or process the combined data as needed
#     for entry in combined_data:
#         print(entry)
#
#     conn.close()

# import sqlite3
# def create_bio_hardware_components():
#     conn = sqlite3.connect('')
#     cursor = conn.cursor()
#
#     # Define the circuit table names
#     circuit_table_names = [
#         "CPU_Enable", "sr_latch_active_high", "sr_latch_active_low",
#         "adder", "OR_ALU_Circuit", "XOR_ALU_Circuit", "AND_ALU_Circuit",
#         "NOT_ALU_Circuit", "ALU", "decoder_2x4", "digitalencoder_ADC",
#         "comparator_ADC"
#     ]
#
#     combined_data = []
#
#     # Iterate through each circuit table
#     for table_name in circuit_table_names:
#         # Build the SQL statement
#         sql_query = f"SELECT circuitname, gate, amtofgate, parent_circuit FROM {table_name};"
#
#         # Execute the query and fetch data
#         cursor.execute(sql_query)
#         circuit_rows = cursor.fetchall()
#
#         # Process the fetched data and update the combined_data list
#         for circuit_row in circuit_rows:
#             parent_circuit = circuit_row[3]
#             gate = circuit_row[1]
#             circuitname = circuit_row[0]
#             amtofgate = circuit_row[2]
#
#             combined_entry = {
#                 "circuitname": circuitname,
#                 "gate": gate,
#                 "amtofgate": amtofgate,
#                 "parent_circuit": parent_circuit
#             }
#             combined_data.append(combined_entry)
#
#     # List of names to search for
#     names = ['Protein Complex', 'Gene Expression Regulation', 'microRNA (miRNA)', 'Inhibition of Protein Activation',
#              'DNA Damage Response', 'Olfactory Receptor Activation', 'Immune Cell Recognition']
#
#     # Create a placeholder string for the names
#     placeholders = ', '.join(['?' for _ in names])
#
#     # Process logicgates data
#     # Construct the query with placeholders
#     logicgates_query = f"SELECT id, name, gate, parent_circuit FROM logicgates WHERE name IN ({placeholders});"
#     cursor.execute(logicgates_query, names)
#     logicgates_rows = cursor.fetchall()
#
#     for logicgate_row in logicgates_rows:
#         parent_circuit = logicgate_row[3]
#         gate = logicgate_row[2]
#         name = logicgate_row[1]
#
#         # Find the corresponding entry in combined_data and update it
#         for entry in combined_data:
#             if entry["parent_circuit"] == parent_circuit and entry["gate"] == gate:
#                 entry["name"] = name
#                 break
#
#     create_table_query = '''
#         CREATE TABLE IF NOT EXISTS cleaned_bio_table (
#             circuitname TEXT,
#             gate TEXT,
#             amtofgate INTEGER,
#             parent_circuit INTEGER,
#             name TEXT
#         );
#     '''
#
#     # Execute the SQL command to create the table
#     cursor.execute(create_table_query)
#
#     # Insert combined data into the newly created table
#     for entry in combined_data:
#         insert_query = "INSERT INTO cleaned_bio_table (circuitname, gate, amtofgate, parent_circuit, name) VALUES (?, ?, ?, ?, ?);"
#         cursor.execute(insert_query, (entry["circuitname"], entry["gate"], entry["amtofgate"], entry["parent_circuit"], entry.get("name", None)))
#
#     # Commit the changes and close the connection
#     conn.commit()
#
#     # Print or process the combined data as needed
#     for entry in combined_data:
#         print(entry)
#
#     conn.close()


# def create_openflow_controller_hardware_components():
#     conn5 = sqlite3.connect('')
#     cursor = conn5.cursor()
#     cursor.execute( "SELECT circuitname FROM CPU UNION select circuitname FROM RAM")
#     rows = cursor.fetchall()  # Fetch the results
#     for row in rows:
#         print(row)

# def create_CPU_hardware_components():
#     conn6 = sqlite3.connect('')
#     cursor = conn6.cursor()
#     cursor.execute( "SELECT circuitname FROM CPU")
#     rows = cursor.fetchall()  # Fetch the results
#     for row in rows:
#         print(row)


def decode_signal():
    import sqlite3
    from Endoneurobot import Endoneurobot
    from Gliabot import Gliabot
    from Synaptobot import Synaptobot
    from Auxiliary_transport_nanorobot import Auxiliary_transport_nanorobot
    # Connect to the SQLite database
    connection = sqlite3.connect('')
    cursor = connection.cursor()

    # Select only the 'Binary_ID' column from the 'RFID_IP_Nano_Network' table
    cursor.execute('SELECT Binary_ID FROM RFID_IP_Nano_Network')
    binary_ids = cursor.fetchall()

    # Iterate over each Binary_ID and perform conditional checks
    for binary_id in binary_ids:
        if len(binary_id[0]) == 3:
            # Has the endoneurobot been positioned at the Axon Initial Segment?
            endobot1 = Endoneurobot(True, ['ElectroChemical'], -70)
            endostatus = endobot1.auto_position_status(False)
            if endostatus is True:
                print("The endoneurobot been positioned at the Axon Initial Segment")
            if endostatus is False:
                print("The endoneurobot has yet to be positioned at the Axon Initial Segment")

            # Choose Whether ot not to initiate an Action Potential
            endobot2 = Endoneurobot(True, ['Optical'], -55)
            if endobot2.apply_voltage >= -55:
                print("depolarization - action potential initiated")  # In theory bringing the threshold to -55 elicits A.P.

            # Monitoring Status of Neuron - Resting vs Depolarized
                endobot2.reactivity_status()

            # Nanobot signal is on or off
                Nanobot_signaling = endobot2.on_off
                print(Nanobot_signaling)

            # Antenna sensor senses electromagnetic radiation
                electromagnetic_radiation_type = endobot2.sense
                print(electromagnetic_radiation_type)

            # Voltage being applied to Axon Initial Segment
                AIS_Voltage = endobot2.apply_voltage
                print(AIS_Voltage)
        
        if len(binary_id[0]) == 4:
            print("Amplitude 4 - Gliabot Signal")
                gliabot1 = Gliabot(True, ['ElectroChemical'], 1)
        
                # movement
                # gliabot1.movement()
        
                 # Amt of N.T.
                neurotransmitter_amt = gliabot1.neurotransmitter_cargo_amount
                print(neurotransmitter_amt)
        
                 # Payload Release/Reuptake
                gliabot1.reactivity_status()
        
                 # Nanobot signal is on or off
                Nanobot_signaling = gliabot1.on_off
                print(Nanobot_signaling)
        
                # Antenna sensor senses electromagnetic radiation
                electromagnetic_radiation_type = gliabot1.sense
                print(electromagnetic_radiation_type)
        
        if len(binary_id[0]) == 5:
            print('Amplitude 5 - Synaptobot Signal')

        if len(binary_id[0]) == 6:
            print('Amplitude 6 - Auxiliary Transport Nanorobot Signal')
            # Synaptobot cargo must be <= 24
            # nanofiberoptic cargo must be 1
            auxtransbot1 = Auxiliary_transport_nanorobot(True, ['Optical'], 24)
            auxtransbot1.reactivity_status()
            
    Close the database connection
    connection.close()

    # import sqlite3
    # import random
    #
    # # Create/connect to an SQLite database
    # connection = sqlite3.connect('')
    # cursor = connection.cursor()
    #
    # # Create the 'YourTableName' table (replace 'YourTableName' with the actual table name)
    # cursor.execute('''
    #     CREATE TABLE IF NOT EXISTS RFID_IP_Nano_Network (
    #         IPv6 TEXT,
    #         Tag_ID TEXT,
    #         Time_Stamp TEXT,
    #         Reader_ID TEXT,
    #         Antenna TEXT,
    #         Binary_ID INTEGER  -- Remove the comma from here
    #     )
    # ''')
    #
    # # Select data from the 'RFIDbinary' column in the 'signal' table
    # cursor.execute('SELECT RFIDbinary FROM signal')
    #
    # # Fetch all the rows from the result
    # rows = cursor.fetchall()
    #
    # # Generate and insert 401 rows of dummy data
    # for row in rows:
    #     binary_value = row[0]
    #     decoded_identifier = str(int(binary_value, 2))  # Convert binary to decimal and store as string
    #
    #     ipv6 = "IPv6_" + str(random.randint(1, 1000))
    #     tag_id = "Tag_" + str(random.randint(1, 1000))
    #     time_stamp = "TimeStamp_" + str(random.randint(1, 1000))
    #     location = 'Location_' + str(random.randint(1, 1000))
    #     reader_id = "Reader_" + str(random.randint(1, 1000))
    #     antenna = "Antenna_" + str(random.randint(1, 1000))
    #
    #     # Insert the data into the table
    #     cursor.execute('''
    #         INSERT INTO RFID_IP_Nano_Network (IPv6, Tag_ID, TimeStamp, Location, Reader_ID, Antenna, Binary_ID)
    #         VALUES (?, ?, ?, ?, ?, ?, ?)
    #     ''', (ipv6, tag_id, time_stamp, location, reader_id, antenna, decoded_identifier))
    #
    # # Commit changes and close the connection
    # connection.commit()
    # connection.close()









