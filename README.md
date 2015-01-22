For directions on installing Touche, see that installation docs in the
/documentation/ folder of this repository.

Using the Touche repository in a live system.  After cloning the
repository, it should be in a location that is not directly accessible
to the web server you've installed.  The easiest way to use the
repository is to set up symbolic links in the right locations to the
files inside.  Here are the links that need to be done (all
directories are relative to the contest user and assume the repository
is in a directory named src):

    ln -s ~/src/develop develop
    ln -s ~/src/public_html/develop public_html/develop
	ln -s ~/src/public_html/lib/
    ln ~/src/public_html/createcontest.php public_html/createcontest.php
    ln ~/src/public_html/createcontest2.php public_html/createcontest2.php
    ln ~/src/public_html/index.html public_html/index.html
    ln -s ~/src/public_html/dbcreate.sql public_html/dbcreate.sql
    ln -s ~/src/public_html/readme public_html/readme
    ln -s ~/src/public_html/lib public_html/lib
    ln -s ~/src/master-crontab.cron master-crontab.cron
    ln -s ~/src/jails jails

We cannot use symbolic links for the `createcontest` scripts since
they are directly executed by the web server and we use suexec, which
doesn't work over links and so it needs to be hard linked.  This
probably isn't an issue since the two locations are probably on the
same mount point.  Otherwise, you'll have to use a copy instead.  If
you use a copy, be sure that any time those scripts are updated that they
get copied into the web server spot properly and that can be easy to
forget when using version control since it might not explicitly remind
to do so.

More documents should be created and pointed to with this README!!!
