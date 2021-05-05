from SublimeLinter.lint import NodeLinter

class TSStandard(NodeLinter):
    cmd = 'ts-standard --stdin --stdin-filename ${file}'
    name = 'TS Standard'
    regex = r'^.+:(?P<line>\d+):(?P<col>\d+):\s*(?P<message>.+)'
    defaults = {
        'selector': 'source.ts, source.tsx',
        'disable_if_not_dependency': False
    }
