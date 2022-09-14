# satellite-data-provider

## Generating code

### Python specific

The `tleprocessing` module must be installed for this project to work. You can run `pip install -e .` to have the module as editable.

To this date, the automated code generation for python using `grpc_tools.protoc` only follows the folder hierarchy of the proto files, which leads to import issues using python 3 which requires relative imports in some instances.
The solution is to install [protoletariat](https://github.com/cpcloud/protoletariat) which is used in the `generate_code` script.

### General

run `generate_code.bat`
