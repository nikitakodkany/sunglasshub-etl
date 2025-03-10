from postgres_create_tables import creating_tables_postgres
from synapse_create_tables import creating_tables_synapse
from load_to_postgres import load_to_postgres
from load_to_synapse import load_to_synapse


if __name__ == "__main__":
    config_filename = "configuration.env"

    # Uploading to Postgres    
    print('''
            ------------------------------------------------
            |Upload process initiated for postgres database|
            ------------------------------------------------
    ''')
    creating_tables_postgres(config_filename=config_filename)
    load_to_postgres(config_filename=config_filename)

    print('''
            ------------------------------------------------
            |       Process concluded succesfully!         |
            ------------------------------------------------
    ''')


    # Uploading to Synapse Dedicated SQL Pool
    print('''
            ---------------------------------------------------------
            |Upload process initiated for Synapse Dedicated SQL Pool|
            ---------------------------------------------------------
    ''')
    creating_tables_synapse(config_filename=config_filename)
    load_to_synapse(config_filename=config_filename)

    print('''
            ------------------------------------------------
            |       Process concluded succesfully!         |
            ------------------------------------------------
    ''')