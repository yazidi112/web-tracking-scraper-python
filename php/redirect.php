<?php
setcookie("id", "AZEZAZEZE", time() + (86400 * 30), "/");
setcookie("sid", "45678", time() + (86400 * 30), "/");
header("location: http://localhost:9000/img",true,302);
