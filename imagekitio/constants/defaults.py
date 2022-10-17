import enum


class Default(enum.Enum):
    DEFAULT_TRANSFORMATION_POSITION = "path"
    QUERY_TRANSFORMATION_POSITION = "query"
    VALID_TRANSFORMATION_POSITION = [
        DEFAULT_TRANSFORMATION_POSITION,
        QUERY_TRANSFORMATION_POSITION,
    ]
    DEFAULT_TIMESTAMP = 9999999999
    SDK_VERSION = "python-3.0.1"
    TRANSFORMATION_PARAMETER = "tr"
    CHAIN_TRANSFORM_DELIMITER = ":"
    TRANSFORM_DELIMITER = ","
    TRANSFORM_KEY_VALUE_DELIMITER = "-"
    SIGNATURE_PARAMETER = "ik-s"
    TIMESTAMP_PARAMETER = "ik-t"
