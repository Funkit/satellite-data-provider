protoc --proto_path=./proto --go_out=./pointing --go_opt=paths=source_relative --go-grpc_out=./pointing --go-grpc_opt=paths=source_relative proto/pointing.proto
python -m grpc_tools.protoc -I ./proto --python_out=./tleprocessing/src/rpc --grpc_python_out=./tleprocessing/src/rpc ./proto/pointing.proto ./proto/datetime.proto
protol --in-place --python-out=./tleprocessing/src/rpc protoc --proto-path=./proto ./proto/pointing.proto ./proto/datetime.proto

