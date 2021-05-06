from SublimeLinter.lint import NodeLinter


class TSStandard(NodeLinter):
    name = 'ts-standard'
    regex = r'^.+:(?P<line>\d+):(?P<col>\d+):\s*(?P<message>.+)'
    multiline=True
    defaults = {
        'selector': 'source.ts, source.tsx',
        'disable_if_not_dependency': False
    }

    def cmd(self):
        if self.context.get('file'):
            return (
                'ts-standard',
                '--stdin',
                '--stdin-filename',
                '${file}'
            )

        self.notify_failure()
        return (
            'echo',
            '<buffer>:1:1:The file must be saved before it can be linted by ts-standard'
        )
