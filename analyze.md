# BZ 1869929

## Links
- https://bugs.launchpad.net/oslo.config/+bug/1869929
- https://github.com/tobias-urdin/reproduce-bug-1869929

## Context
Upgrade from rocky to train

## Side notes

- All language packages are ignored.

## Oslo packages

|   Pacakge Name                |     Rocky     |      Train    |
|-------------------------------|:-------------:|--------------:|
|   oslo.upgradecheck           |        ?      |     0.3.2     |
|   oslo.log                    |   3.39.2      |     3.44.1    |
|   oslo.vmware                 |   2.31.0      |     2.34.1    |
|   oslo.utils                  |   3.36.5      |     3.41.5    |
|   oslo.service                |   1.31.8      |     1.40.2    |
|   oslo.concurrency            |   3.27.0      |     3.30.0    |
|   oslo.context                |   2.21.0      |     2.23.0    |
|   oslo.i18n                   |   3.21.0      |     3.24.0    |
|   oslo.middleware             |   3.36.0      |     3.38.1    |
|   oslo.policy                 |   1.38.1      |     2.3.3     |
|   oslo.rootwrap               |   5.14.2      |     5.16.1    |
|   oslo.versionedobjects       |   1.33.3      |     1.36.1    |
|   oslo.serialization          |   2.27.0      |     2.29.2    |
|   oslo.messaging              |   8.1.4       |     10.2.0    |
|   oslo.reports                |   1.28.0      |     1.30.0    |
|   oslo.privsep                |   1.29.2      |     1.33.3    |
|   oslo.db                     |   4.40.2      |     5.0.2     |
|   oslo.config                 |   6.4.2       |     6.11.2    |
|   oslo.cache                  |   1.30.4      |     1.37.0    |

Note:
The oslo.upgradecheck package version for rocky is missing but I don't
think this is necessary for our use case.
