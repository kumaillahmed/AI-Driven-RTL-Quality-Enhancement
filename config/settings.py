from dataclasses import dataclass

@dataclass
class Settings:
    api_host='0.0.0.0'
    api_port=8000
    log_level='INFO'
