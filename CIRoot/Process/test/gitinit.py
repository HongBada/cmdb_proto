/*VersionNumber:null*/
#__python__,__shell__
import os
from os.path import abspath
from git import Repo
to_path = abspath("/Library/tomcat/webapps/ROOT/repo")
Repo.clone_from("http://ooranos:1qazxsw2@last.dunamisplatform.co.kr:19080/ooranos/cmdb_proto.git", to_path)

"""
from git import Repo,remote

rw_dir = 'path/to/your/local/repo'
repo = Repo(rw_dir)

'''Enter code to commit the repository here.
After commit run the following code to push the commit to remote repo.
I am pushing to master branch here'''

origin = repo.remote(name='origin')
origin.push()
"""

