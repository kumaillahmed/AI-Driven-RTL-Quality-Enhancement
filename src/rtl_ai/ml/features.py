def extract_features(record):
    return {
        "severity": record.get("severity",""),
        "message_length": len(record.get("message",""))
    }
