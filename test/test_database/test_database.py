import pytest
import os
from databases import Database

postgres_url = os.environ.get("DATABASE_URL")

database = Database(postgres_url)


@pytest.mark.asyncio
async def test_database_connection():
    # Connect to the database
    await database.connect()

    # Perform a simple query to ensure the connection works
    query = "SELECT 1"
    result = await database.fetch_one(query=query)

    # Assert the result
    assert result[0] == 1, "The database connection should return 1 for SELECT 1 query"

    # Disconnect from the database
    await database.disconnect()

if __name__ == "__main__":
    pytest.main()
