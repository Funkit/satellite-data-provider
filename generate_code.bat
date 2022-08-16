python -m grpc_tools.protoc -I./proto --python_out=./tle-processing/generated --grpc_python_out=./tle-processing/generated ./proto/pointing.proto ./proto/datetime.proto
protoc --proto_path=./proto --go_out=./pointing --go_opt=paths=source_relative --go-grpc_out=./pointing --go-grpc_opt=paths=source_relative proto/pointing.proto
