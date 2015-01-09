<?
#
# Copyright (C) 2002 David Whittington
# Copyright (C) 2005 Victor Replogle
# Copyright (C) 2005 Steve Overton
#
# See the file "COPYING" for further information about the copyright
# and warranty status of this work.
#
# arch-tag: lib/session.inc
#
<?php
    include_once("create.inc");

    session_name("TOUCHE-CREATE");
    session_start();
        header ("expires:Tuesday, 25 Apr 1995 09:30:00 -0700");
    if(   $_SESSION['admin_user'] != $create_user
       || $_SESSION['admin_pass'] != $create_pass)
   {
    header ("Location: index.php?state=2");
	exit(0);
    }
?>
