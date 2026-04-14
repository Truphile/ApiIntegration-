from datetime import timezone, datetime


def compute_confidence(probability, sample_size):
    return probability >= 0.7 and sample_size >= 100

def get_timestamp():
    return datetime.now(timezone.utc).isoformat().replace('+00:00', 'Z')