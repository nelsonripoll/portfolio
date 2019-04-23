#!/bin/bash
composer create-project --prefer-dist cakephp/app cakephp 

composer --working-dir=cakephp require adldap2/adldap2
composer --working-dir=cakephp require markstory/asset_compress
composer --working-dir=cakephp require --dev cakephp/cakephp-codesniffer
composer --working-dir=cakephp require --dev phpunit/phpunit
composer --working-dir=cakephp require --dev phpunit/php-invoker
