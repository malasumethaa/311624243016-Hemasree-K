class TableCreationManager:
    def __init__(self, table_file="records_table.json"):
        self.table_file = table_file

    def create_table(self):
        """Milestone 2: Sets up the core database/table schema[cite: 1]."""
        initial_schema = {
            "table_name": "secured_records",
            "columns": ["record_id", "owner_email", "content", "created_at"],
            "records": [
                {
                    "record_id": "REC-101",
                    "owner_email": "admin@domain.com",
                    "content": "Confidential financial projection data.",
                    "created_at": datetime.now().isoformat()
                }
            ]
        }
        
        with open(self.table_file, 'w') as f:
            json.dump(initial_schema, f, indent=4)
            
        print("Milestone 2 (Creation of Table) completed successfully[cite: 1].")