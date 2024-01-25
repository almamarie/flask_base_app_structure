import uuid
import hashlib


def generate_id():
    id = uuid.uuid4()
    return hash_uuid(id)


def hash_uuid(uuid_str):
    uuid_bytes = str(uuid_str).encode()

    sha256_hash = hashlib.sha256()

    sha256_hash.update(uuid_bytes)

    digest = sha256_hash.hexdigest()

    return digest[:15]
