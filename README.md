# Simple PV Simulator

## Dependencies

- Python 3.6+
- p4p
- PyYAML

## Installation

```bash
pip install pvsim
```

## Running

To run, invoke `pvsim` passing as argument a YAML file with a list of PVs and their metadata. For an example look into `examples/pvs.yaml`.
Optionally use the `-d` flag to enable debug messages.

```bash
pvsim [-d] pvlist.yaml
```

or

```bash
python -m pvsim [-d] pvlist.yaml
```

## Supported Types

As of now, the small simulator supports the following types:

- Analog In/Out (ai, ao)
- Binary In/Out (bi, bo)

More types will be added in the future.