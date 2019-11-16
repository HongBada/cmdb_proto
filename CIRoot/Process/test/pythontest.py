/*VersionNumber:null*/
var script="";
script+=("cd /Library/tomcat/webapps/ROOT/repo;");
script+=("git init;git remote add origin http://last.dunamisplatform.co.kr:19080/ooranos/cmdb_proto.git;");
script+=("git pull origin master ;");
manager.executeShellCommandBg(script,"WW|Username|ooranos,WW|Password|1qazxsw2".split(","))
out.println(script)