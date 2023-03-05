"""
This will contain operations to:
    Create
    Read
    Update
    Delete
items in the database.

Author: Alex Wendland
"""

from sqlalchemy.orm import Session

from . import keygen, models, schemas


def create_database_url(database: Session, url: schemas.URL) -> models.URL:
    """
    Creates a URL in the database.

    Args:
        database (Session): The database session.
        url (schemas.URLBase): The URL to create from the API.

    Returns:
        models.URL: The created URL from the database.
    """
    key = keygen.create_unique_random_key(database, length=5)
    secret_key = keygen.create_random_generic_key(length=8)
    database_url = models.URL(
        key=key,
        secret_key=f"{key}_{secret_key}",
        target_url=url.target_url,
    )
    database.add(database_url)
    database.commit()
    database.refresh(database_url)
    return database_url
