###
KVdir v. 1.0.1
NodeJS script
vetl1489
###

fs = require('fs')
dirs = ['1', '2', '3', '4', '5', '8', '9', '10', 'PDF', 'WEB', 'Реклама']
dirs.forEach (dir)->
	fs.access dir, fs.R_OK | fs.W_OK, (err)->
		if err
			fs.mkdirSync dir
			console.log "Папка '#{dir}' создана."