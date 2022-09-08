# Request Api Project

Based on tutorials from Programador Lhama in [YouTube](https://www.youtube.com/watch?v=MtyDUwJTkNE&list=PLAgbpJQADBGLG_ap3sbYefUp8HsiTt6Kf)
### New feature:<br>
- PyLint: need a `.pylint` file to work. Type `$pylint --generate-rcfile > .pylintrc` to generate it<br>
- Pre-commit: need a `.pre-commit.config.yaml`. Create it manually and copy YAML code;<br>
<br>
#### To avoid PYTEST from request on internet every commit, we need to MOCK!<br>

- Install [requests_mock](https://pypi.org/project/requests-mock/): Run `$ pipenv install requests-mock`
- Edit PYTEST FUNCTION you want to mock and add requests_mock as a parameter to activate it: `def test_get_starship(requests_mock)`
- 
