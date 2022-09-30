from pathlib import Path
# CREATE FOLDER
# file = Path('myfile.txt')
# folder = Path('myfolder')
# folder.mkdir()


# CREATE FILE
# folder = Path('myfolder')
# folder.mkdir()
# new_file = folder / 'test.py'
# grade = "K"
# template = """\
# grade {1} {0}
# """
# new_file.write_text(template.format(grade, 'UNIT'))


# CREATE MULTIPLE FILES
# template = """\
# grade {number}
# """
#
# for i in range(1,6):
#     file = Path(f'my_py_file{i}.py')
#     file.write_text(template.format(number=i))


# READ FILE
# folder = Path('object_info')
# new_file = folder / 'unit1.object_info'
# content = new_file.read_text()
# print(content)
#
#
# new_file = folder / 'test.py'
#
# template = """\
# words = {}
# """
# new_file.write_text(template.format(content))

# READ FILES IN A GIVEN DIRECTORY

# audio_path = Path(__file__).parent / 'audio'

# print(audio_path)

# READ DIRECTORY
# for path in audio_path.iterdir():
#     print(path.name)

# READ DIRECTORY
# for path in audio_path.glob('**/'):
#     print(path.name)


# CREATE FILES IN NEST FOLDERS THAT DONT EXIST
# BASE_DIR = Path(__file__).parent
# blog_folder = BASE_DIR / 'website' / 'blog'
# blog_folder.mkdir(parents=True, exist_ok=True)
#
# my_post = blog_folder / 'post1.txt'
# my_post.write_text('Juicy Baconator with cheese and fries')

# RENAME FILE
file = Path('jungle.gui')
# file.touch()
file.rename('myfile.txt')
















