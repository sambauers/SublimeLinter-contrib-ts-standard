from SublimeLinter.lint import NodeLinter


class TSStandard(NodeLinter):
    name = 'ts-standard'
    cmd = 'ts-standard --stdin --stdin-filename ${file}'
    regex = r'^.+:(?P<line>\d+):(?P<col>\d+):\s*(?P<message>.+)'
    multiline = True
    defaults = {
        'selector': 'source.ts, source.tsx',
        'disable_if_not_dependency': False
    }

    def run(self, cmd, code):
        if not self.context.get('file'):
            self.notify_failure()
            return '-:1:1:The file must be saved before it can be linted by ts-standard'
        return super().run(cmd, code)
