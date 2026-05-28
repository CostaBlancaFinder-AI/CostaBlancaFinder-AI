from opportunity_ai.shared.database.supabase_connection import (
    get_supabase_client
)

client = get_supabase_client()

print("Supabase connection initialized correctly.")
print(client)
