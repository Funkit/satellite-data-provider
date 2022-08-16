from datetime import datetime
import datetime_pb2, pointing_pb2


def datetime_to_grpc_datetime(date: datetime):
    return datetime_pb2.DateTime(year=date.year,
                                 month=date.month,
                                 day=date.day,
                                 hours=date.hour,
                                 minutes=date.minute,
                                 seconds=date.second)


def grpc_datetime_to_datetime(date: pointing_pb2.datetime__pb2):
    return datetime(year=date.year,
                    month=date.month,
                    day=date.day).replace(hour=date.hours,
                                          minute=date.minutes,
                                          second=date.seconds)
