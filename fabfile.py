import json
from fabric.api import local


def update():
    local('rm -rf css/*')
    local('rm -rf fonts/*')
    local('wget https://github.com/FortAwesome/Font-Awesome/archive/master.zip')
    local('unzip master.zip && rm master.zip')
    latest_version = json.loads(open('Font-Awesome-master/bower.json').read())['version']
    print 'latest version: {0}'.format(latest_version)
    local('cp Font-Awesome-master/css/font-awesome.min.css css/')
    local('cp -r Font-Awesome-master/fonts/* fonts/')
    local('rm -rf Font-Awesome-master')
