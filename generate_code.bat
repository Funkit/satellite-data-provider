python -m grpc_tools.protoc -I./proto --python_out=./processing --grpc_python_out=./processing ./proto/pointing.proto ./proto/datetime.proto
protoc --proto_path=./proto --go_out=./api-composer/pointing --go_opt=paths=source_relative --go-grpc_out=./api-composer/pointing --go-grpc_opt=paths=source_relative proto/pointing.proto ./proto/datetime.proto
