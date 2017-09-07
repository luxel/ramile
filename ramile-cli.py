#! python
import fire

from ramile.project import Project
from ramile.processors import FileProcessor


class ramile_cli(object):

    def extract(self, project_root):
        project = Project(project_root)
        project.run()
        return

    def whatcanido(self):
        processor = FileProcessor()
        print("I can extract source code from files with these extensions: %s" %
              processor.print_processors())
        return

    def test(self):
        print('(%s)' % '   abced    '.strip(' \t'))


def main():
    fire.Fire(ramile_cli(), name='ramile')


if __name__ == '__main__':
    main()
