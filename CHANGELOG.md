# Changelog

## [1.1.0](https://github.com/googleapis/python-artifact-registry/compare/v1.0.2...v1.1.0) (2022-01-25)


### Features

* add api key support ([#119](https://github.com/googleapis/python-artifact-registry/issues/119)) ([d22f2d9](https://github.com/googleapis/python-artifact-registry/commit/d22f2d93ffcc169540991d224a54c81eb7ca09a4))
* add APIs for importing and uploading Apt and Yum artifacts ([#116](https://github.com/googleapis/python-artifact-registry/issues/116)) ([a86d4f1](https://github.com/googleapis/python-artifact-registry/commit/a86d4f143c401e20052182b7bba3b9178014dace))
* add order_by support for listing versions ([a86d4f1](https://github.com/googleapis/python-artifact-registry/commit/a86d4f143c401e20052182b7bba3b9178014dace))
* add version policy support for Maven repositories ([a86d4f1](https://github.com/googleapis/python-artifact-registry/commit/a86d4f143c401e20052182b7bba3b9178014dace))


### Bug Fixes

* mark a few resource name fields as required ([a86d4f1](https://github.com/googleapis/python-artifact-registry/commit/a86d4f143c401e20052182b7bba3b9178014dace))

### [1.0.2](https://www.github.com/googleapis/python-artifact-registry/compare/v1.0.1...v1.0.2) (2022-01-07)


### Bug Fixes

* fix resource pattern ID segment name ([#107](https://www.github.com/googleapis/python-artifact-registry/issues/107)) ([254dc73](https://www.github.com/googleapis/python-artifact-registry/commit/254dc73dbbc52d41014e0d2db81f3cc6cd864058))

### [1.0.1](https://www.github.com/googleapis/python-artifact-registry/compare/v1.0.0...v1.0.1) (2021-11-01)


### Bug Fixes

* **deps:** drop packaging dependency ([90e3313](https://www.github.com/googleapis/python-artifact-registry/commit/90e3313b50b127d6fc562e7138b12743412fa064))
* **deps:** require google-api-core >= 1.28.0 ([90e3313](https://www.github.com/googleapis/python-artifact-registry/commit/90e3313b50b127d6fc562e7138b12743412fa064))


### Documentation

* list oneofs in docstring ([90e3313](https://www.github.com/googleapis/python-artifact-registry/commit/90e3313b50b127d6fc562e7138b12743412fa064))

## [1.0.0](https://www.github.com/googleapis/python-artifact-registry/compare/v0.5.0...v1.0.0) (2021-10-22)


### Features

* bump release level to production/stable ([#82](https://www.github.com/googleapis/python-artifact-registry/issues/82)) ([d3705c1](https://www.github.com/googleapis/python-artifact-registry/commit/d3705c13605af3e4167c2e86eeb55683a271a3d4))


### Documentation

* fix docstring formatting ([#93](https://www.github.com/googleapis/python-artifact-registry/issues/93)) ([e6c2084](https://www.github.com/googleapis/python-artifact-registry/commit/e6c208427336e8c9d5a5d607c02406c856af6a94))

## [0.5.0](https://www.github.com/googleapis/python-artifact-registry/compare/v0.4.1...v0.5.0) (2021-10-11)


### Features

* add context manager support in client ([#88](https://www.github.com/googleapis/python-artifact-registry/issues/88)) ([0f631cc](https://www.github.com/googleapis/python-artifact-registry/commit/0f631cc8bd8ff0928d5403e756d2206f1842c35c))
* add trove classifier for python 3.10 ([#91](https://www.github.com/googleapis/python-artifact-registry/issues/91)) ([e392f56](https://www.github.com/googleapis/python-artifact-registry/commit/e392f565e5e9252bff8a5f6ede67c11b25438cdd))

### [0.4.1](https://www.github.com/googleapis/python-artifact-registry/compare/v0.4.0...v0.4.1) (2021-09-30)


### Bug Fixes

* improper types in pagers generation ([8a6b687](https://www.github.com/googleapis/python-artifact-registry/commit/8a6b6870f39c34bd1cf2dafd591c58ebd2c48d77))

## [0.4.0](https://www.github.com/googleapis/python-artifact-registry/compare/v0.3.3...v0.4.0) (2021-09-24)


### Features

* add Artifact Registry v1  ([#80](https://www.github.com/googleapis/python-artifact-registry/issues/80)) ([43413eb](https://www.github.com/googleapis/python-artifact-registry/commit/43413ebd0d6823233573ab88c0340e4165ee4487))
* set artifactregistry_v1 as the default import ([43413eb](https://www.github.com/googleapis/python-artifact-registry/commit/43413ebd0d6823233573ab88c0340e4165ee4487))


### Bug Fixes

* add 'dict' annotation type to 'request' ([43413eb](https://www.github.com/googleapis/python-artifact-registry/commit/43413ebd0d6823233573ab88c0340e4165ee4487))

### [0.3.3](https://www.github.com/googleapis/python-artifact-registry/compare/v0.3.2...v0.3.3) (2021-07-27)


### Bug Fixes

* enable self signed jwt for grpc ([#59](https://www.github.com/googleapis/python-artifact-registry/issues/59)) ([bb98a8c](https://www.github.com/googleapis/python-artifact-registry/commit/bb98a8cfcbfadf95ef72499d8bf1fb4ae2e1b599))


### Documentation

* add Samples section to CONTRIBUTING.rst ([#55](https://www.github.com/googleapis/python-artifact-registry/issues/55)) ([55773fe](https://www.github.com/googleapis/python-artifact-registry/commit/55773fe0ab33a8aa5c8b6669eb75e9615f226db0))


### Miscellaneous Chores

* release as 0.3.3 ([#60](https://www.github.com/googleapis/python-artifact-registry/issues/60)) ([b8d7865](https://www.github.com/googleapis/python-artifact-registry/commit/b8d78650cceae268f6616c4eefef3200c7477cc1))

### [0.3.2](https://www.github.com/googleapis/python-artifact-registry/compare/v0.3.1...v0.3.2) (2021-07-20)


### Bug Fixes

* **deps:** pin 'google-{api,cloud}-core', 'google-auth' to allow 2.x versions ([#54](https://www.github.com/googleapis/python-artifact-registry/issues/54)) ([b171295](https://www.github.com/googleapis/python-artifact-registry/commit/b171295c19c0e29025aad08975ceb9a8c9aac66c))

### [0.3.1](https://www.github.com/googleapis/python-artifact-registry/compare/v0.3.0...v0.3.1) (2021-06-30)


### Bug Fixes

* disable always_use_jwt_access ([ce910f4](https://www.github.com/googleapis/python-artifact-registry/commit/ce910f40a365c56a07372664adffe98a628fabe9))
* disable always_use_jwt_access ([#50](https://www.github.com/googleapis/python-artifact-registry/issues/50)) ([ce910f4](https://www.github.com/googleapis/python-artifact-registry/commit/ce910f40a365c56a07372664adffe98a628fabe9))

## [0.3.0](https://www.github.com/googleapis/python-artifact-registry/compare/v0.2.2...v0.3.0) (2021-06-23)


### Features

* add always_use_jwt_access ([#46](https://www.github.com/googleapis/python-artifact-registry/issues/46)) ([247d779](https://www.github.com/googleapis/python-artifact-registry/commit/247d779c881e7fdfc7696adcb3256ca06b3980c3))


### Documentation

* omit mention of Python 2.7 in 'CONTRIBUTING.rst' ([#1127](https://www.github.com/googleapis/python-artifact-registry/issues/1127)) ([#41](https://www.github.com/googleapis/python-artifact-registry/issues/41)) ([7ae05ed](https://www.github.com/googleapis/python-artifact-registry/commit/7ae05eddef4fce0f3f09774e835381f901a6a031)), closes [#1126](https://www.github.com/googleapis/python-artifact-registry/issues/1126)

### [0.2.2](https://www.github.com/googleapis/python-artifact-registry/compare/v0.2.1...v0.2.2) (2021-06-16)


### Bug Fixes

* exclude docs and tests from package ([#38](https://www.github.com/googleapis/python-artifact-registry/issues/38)) ([345496f](https://www.github.com/googleapis/python-artifact-registry/commit/345496fbd96d4c780acdb2ee940e530e7d48ab6c))

### [0.2.1](https://www.github.com/googleapis/python-artifact-registry/compare/v0.2.0...v0.2.1) (2021-06-01)


### Bug Fixes

* **deps:** add packaging requirement ([#33](https://www.github.com/googleapis/python-artifact-registry/issues/33)) ([ca2907e](https://www.github.com/googleapis/python-artifact-registry/commit/ca2907efdcd05a88a63c798a367baa71f2fb78b4))

## [0.2.0](https://www.github.com/googleapis/python-artifact-registry/compare/v0.1.0...v0.2.0) (2021-05-25)


### Features

* support self-signed JWT flow for service accounts ([#25](https://www.github.com/googleapis/python-artifact-registry/issues/25)) ([fade594](https://www.github.com/googleapis/python-artifact-registry/commit/fade594980fa8f389abc0e3f84e34cb1bcda1f1e))

## 0.1.0 (2021-03-15)


### Features

* generate v1beta2 ([87afc6d](https://www.github.com/googleapis/python-artifact-registry/commit/87afc6ddd4966e4c9acb0a88c556cbcd2fb6b566))
